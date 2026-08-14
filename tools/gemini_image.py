import time
from pathlib import Path
from typing import Any, List, Optional, cast

from google.genai import types
from google.genai.errors import ServerError
from PIL import Image
from pydantic import BaseModel

from tools.gemini_base import GeminiBase
from tools.image_provider import ImageProvider, ImageTask
from tools.messenger import Messenger
from tools.notifications import send_windows_notification
from tools.time_utils import sleep_with_countdown, api_spinner


class GeminiImageGenerator(GeminiBase, ImageProvider):
    image_model: str = "gemini-3.1-flash-image-preview"
    aspect_ratio: str
    style_references: List[Path] = []

    def __init__(
        self,
        aspect_ratio: str,
        reference_dir: Optional[Path] = None,
        **kwargs: Any
    ) -> None:
        style_refs = []
        if reference_dir and reference_dir.exists():
            for ext in ["*.png", "*.jpg", "*.jpeg", "*.webp"]:
                style_refs.extend(reference_dir.glob(ext))
            style_refs = sorted(style_refs)

        super().__init__(
            aspect_ratio=aspect_ratio,
            style_references=style_refs,
            **kwargs
        )

    def generate_image(
        self,
        prompt: str,
        output_path: Path,
        style_references: List[Path] = [],
        sequence_reference: Optional[Path] = None
    ) -> None:
        """Generates an image with Gemini and saves it to disk."""
        sleep_with_countdown(5, "Preparando Gemini API")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        contents = self._prepare_contents(prompt, style_references, sequence_reference)
        config = types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE'],
            image_config=types.ImageConfig(aspect_ratio=self.aspect_ratio, image_size="1K")
        )

        start_time = time.time()
        retries = [180, 360]
        attempt = 0
        while True:
            # Límite de tiempo total de 20 minutos (1200 segundos)
            if time.time() - start_time > 1200:
                msg = "❌ La generación de la imagen tardó más de 20 minutos (incluyendo reintentos) y fue abortada."
                send_windows_notification("Gemini: ERROR CRÍTICO", "Generación abortada por superar los 20 minutos.")
                raise RuntimeError(msg)

            try:
                with api_spinner("Generando imagen (Imagen 3)"):
                    from tools.time_utils import run_with_timeout
                    response = run_with_timeout(
                        self.client.models.generate_content,
                        180, # 3 minutes max wait for an image
                        model=self.image_model,
                        contents=contents,
                        config=config
                    )
                break
            except (ServerError, TimeoutError) as e:
                # Tratar TimeoutError como un 503 (saturación/bloqueo)
                is_503 = getattr(e, 'code', None) == 503 or isinstance(e, TimeoutError)
                
                if is_503 and attempt < len(retries):
                    delay = retries[attempt]
                    attempt += 1
                    warn_msg = f"⚠️ API saturada o bloqueada (503/Timeout). Reintentando en {delay // 60} minutos (Intento {attempt}/2)..."
                    Messenger.info(warn_msg)
                    send_windows_notification("Gemini: API Saturada/Bloqueada", f"Reintento {attempt}/2 en {delay // 60} min.")
                    time.sleep(delay)
                else:
                    err_code = getattr(e, 'code', 'Timeout')
                    send_windows_notification("Gemini: Error de Servidor", f"Fallo definitivo con error {err_code}.")
                    raise e

        if not response or not response.parts:
            raise RuntimeError("❌ Gemini Image no devolvió partes")

        self._extract_usage(response, self.image_model)
        image = self._extract_image(response)
        
        # JPEG no soporta transparencia (RGBA), así que lo convertimos a RGB puro si es necesario
        if output_path.suffix.lower() in ['.jpg', '.jpeg'] and image.mode == 'RGBA':
            image = image.convert('RGB')
            
        image.save(output_path)

        is_ref = style_references or sequence_reference
        msg = f"Imagen generada ({'img2img' if is_ref else 'txt2img'}): {output_path}"
        Messenger.image(msg)

    def generate_images(self, tasks: List[ImageTask]) -> None:
        """
        Generates images in batch for a list of ImageTask objects.
        Processes sequentially (Gemini API is synchronous).
        """
        total = len(tasks)
        Messenger.info(f"Batch Processing: {total} images via Gemini")

        for i, task in enumerate(tasks, start=1):
            Messenger.info(f"Generating image {i}/{total}: {task.output_path.name}")
            self.generate_image(
                prompt=task.prompt,
                output_path=task.output_path,
                style_references=self.style_references,
            )

        Messenger.step_success(f"Batch complete: {total} images generated.")

    def _prepare_contents(
        self,
        prompt: str,
        style_references: List[Path],
        sequence_reference: Optional[Path]
    ) -> List[Any]:
        """Prepares the contents list for the Gemini API call."""
        contents: List[Any] = [f"Primary Prompt: {prompt}"]

        if style_references:
            contents.append("--- STYLE REFERENCES (Maintain this visual aesthetic) ---")
            for ref_path in style_references:
                if ref_path.exists():
                    contents.append(Image.open(ref_path))

        if sequence_reference and sequence_reference.exists():
            contents.append("--- SEQUENCE REFERENCE (Maintain consistency) ---")
            contents.append(Image.open(sequence_reference))

        return contents

    def _extract_image(self, response: Any) -> Image.Image:
        """Extracts the image from the Gemini response."""
        import io
        image: Optional[Image.Image] = None
        for part in response.parts:
            if part.text:
                Messenger.info(f"Gemini thoughts: {part.text}")
            elif getattr(part, 'inline_data', None) and getattr(part.inline_data, 'data', None):
                image = Image.open(io.BytesIO(part.inline_data.data))
                break
            elif getattr(part, 'image', None) and getattr(part.image, 'image_bytes', None):
                image = Image.open(io.BytesIO(part.image.image_bytes))
                break
            elif hasattr(part, 'as_image'):
                obj = part.as_image()
                if hasattr(obj, 'image_bytes'):
                    image = Image.open(io.BytesIO(obj.image_bytes))
                    break

        if image is None:
            raise RuntimeError("❌ No se encontró imagen en la respuesta de Gemini")
        return image
