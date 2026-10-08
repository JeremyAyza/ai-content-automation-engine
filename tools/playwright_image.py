import json
import time
import shutil
import glob
from pathlib import Path
from typing import Any, List
import os

from tools.image_provider import ImageProvider
from tools.messenger import Messenger
from tools.time_utils import api_spinner
from pipeline import config

class PlaywrightImageGenerator(ImageProvider):
    extension_path: str = r"C:\Users\Jeremy\Documents\LAB\generate-image-ext\.output\chrome-mv3"

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        # Attempt to find the built extension if not passed
        # WXT builds to .output/chrome-mv3

    def generate_images(self, tasks: List[Any]) -> None:
        """
        Uses Playwright to automate the Flow Image Automator Chrome extension.
        """
        if not tasks:
            return

        try:
            from playwright.sync_api import sync_playwright, expect
        except ImportError:
            raise ImportError("Playwright is not installed. Run: pip install playwright && playwright install chromium")

        # 1. We need the script.json path. In the current architecture, pipeline.py
        # passes tasks but we also need the JSON file itself.
        # Actually, let's just generate a temporary script.json for the extension.
        # Wait, the extension expects a single script.json with a "prompts" array,
        # or we can use the Multi JSON feature. We'll use the single file upload.

        # Determine Idea ID from the first task's output_path
        first_task = tasks[0]
        idea_dir = Path(first_task.output_path).parent.parent # out_short/ideas/idea_XXXXX
        script_json_path = idea_dir / config.SCRIPT_JSON
        script_name = idea_dir.name # e.g. idea_000006

        if not script_json_path.exists():
            raise FileNotFoundError(f"No se encontró el script.json en {script_json_path}")

        Messenger.info(f"Levantando Playwright para procesar {script_name}...")

        # User Data Dir for persistent session
        user_data_dir = str(Path.cwd() / ".browser_profile")

        with sync_playwright() as p:
            browser_context = p.chromium.launch_persistent_context(
                user_data_dir,
                headless=False,
                no_viewport=True, # Permite que el navegador use todo el espacio
                downloads_path=str(idea_dir / "images"), # Fuerza a Chrome a descargar todo en la carpeta de imágenes del proyecto
                args=[
                    f"--disable-extensions-except={self.extension_path}",
                    f"--load-extension={self.extension_path}",
                    "--start-maximized" # Abre la ventana maximizada
                ]
            )

            page = browser_context.new_page()

            with api_spinner("Navegando a la plataforma..."):
                page.goto(config.FLOW_PROJECT_URL)

                # Verify login by checking if "Create with Google Flow" is present
                needs_login = False
                try:
                    # Si no estamos logueados, Flow muestra este botón incluso en la URL del proyecto
                    page.wait_for_selector('text="Create with Google Flow"', timeout=15000)
                    needs_login = True
                except Exception:
                    pass

                if needs_login:
                    error_msg = (
                        "\n⚠️  SESIÓN NO DETECTADA O EXPIRADA ⚠️\n\n"
                        "Para evitar bloqueos de seguridad de Google, el login debe hacerse a través del script dedicado.\n"
                        "Por favor, aborta este comando y ejecuta:\n"
                        "poetry run python scripts/playwright_login.py\n\n"
                        "Una vez que inicies sesión ahí, vuelve a correr tu comando 'generate'."
                    )
                    Messenger.error(error_msg)
                    raise PermissionError("Usuario no logueado en Google Flow.")

                # Ya estamos seguros de estar en el proyecto. Esperamos a la extensión.
                page.wait_for_selector('text="Flow Script Processor"', timeout=30000)

            with api_spinner("Configurando la extensión y subiendo JSON..."):
                # Click "Archivo" tab using data-testid
                page.locator('[data-testid="tab-file"]').click()

                # Set Script Name
                page.locator('[data-testid="input-script-name"]').fill(script_name)

                # Upload JSON
                page.locator('[data-testid="input-file"]').set_input_files(str(script_json_path))

                # Wait for scenes to be detected
                page.wait_for_selector('[data-testid="status-detected"]')

                # Click Add to Queue
                page.locator('[data-testid="btn-add-queue"]').click()

            with api_spinner("Esperando que la extensión genere y descargue las imágenes (puede tardar minutos)..."):
                # Esperamos el badge 'complete' renderizado por la extensión (o 100% como fallback)
                page.wait_for_selector('[data-testid="complete"], [data-testid="progress-text"]:has-text("100%")', timeout=60 * 15 * 1000)

                # Esperamos 45 segundos adicionales para que la extensión termine de mandar
                # a la papelera lo generado y no se sature la UI de Flow.
                Messenger.info("Imágenes generadas. Esperando 45s para la limpieza automática de la UI...")
                time.sleep(45)

            browser_context.close()

        # Now move the images from Downloads to the idea directory
        self._move_downloaded_images(script_name, idea_dir / "images", len(tasks))

    def _move_downloaded_images(self, script_name: str, target_dir: Path, expected_count: int):
        Messenger.info("Revisando imágenes descargadas en la carpeta del proyecto...")
        target_dir.mkdir(parents=True, exist_ok=True)

        # Como forzamos a Chrome a descargar en target_dir, las imágenes pueden estar:
        # 1. En target_dir/Flow_Generations/SCRIPTNAME/scene_X.png (si Chrome respetó la ruta de la extensión)
        # 2. Directamente en target_dir/ como archivos UUID o sin extensión (si Chrome ignoró la ruta)

        moved_count = 0

        # Caso 1: Chrome respetó la ruta de la extensión
        flow_dir = target_dir / "Flow_Generations"
        if flow_dir.exists():
            for d in flow_dir.iterdir():
                if d.is_dir() and d.name.startswith(f"{script_name}"):
                    for file_path in d.glob("*.png"):
                        # Moverlas a la raíz de target_dir como .jpg
                        dest_path = target_dir / (file_path.stem + ".jpg")
                        shutil.copy(file_path, dest_path)
                        moved_count += 1

            # Limpiar la carpeta temporal creada por la extensión dentro de images/
            try:
                shutil.rmtree(flow_dir)
            except Exception:
                pass

        # Caso 2: Chrome las tiró sueltas en la carpeta con nombres raros (UUIDs)
        if moved_count == 0:
            # Buscar archivos recientes sueltos en target_dir (ignorando directorios)
            downloaded_files = [f for f in target_dir.iterdir() if f.is_file() and not f.name.endswith(".jpg")]

            if downloaded_files:
                # Ordenar por fecha de creación/modificación para deducir el orden de las escenas
                downloaded_files.sort(key=lambda x: x.stat().st_mtime)

                for i, file_path in enumerate(downloaded_files):
                    # Renombrar: el primero es el thumbnail, el resto son escenas
                    if i == 0:
                        dest_path = target_dir / "thumbnail.jpg"
                    else:
                        dest_path = target_dir / f"scene_{i}.jpg"

                    shutil.copy(file_path, dest_path)
                    moved_count += 1

                    # Eliminar el archivo original suelto
                    try:
                        file_path.unlink()
                    except Exception:
                        pass

        if moved_count == 0:
            raise FileNotFoundError(f"No se encontraron las imágenes generadas en {target_dir}")

        Messenger.success(f"Se procesaron {moved_count}/{expected_count} imágenes exitosamente.")
