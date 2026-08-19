from typing import Any, Type, TypeVar

from pydantic import BaseModel

import time
from google.genai.errors import ServerError
from tools.gemini_base import GeminiBase
from tools.messenger import Messenger
from tools.notifications import send_windows_notification
from tools.time_utils import sleep_with_countdown, api_spinner

T = TypeVar("T", bound=BaseModel)



from pipeline.config import GEMINI_TEXT_MODEL

class GeminiTextGenerator(GeminiBase):
    text_model: str = GEMINI_TEXT_MODEL


    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    def generate_text(self, prompt: str, schema: Type[T], *, low: bool = False) -> T:
        """
        Generates content with Gemini and parses it into a Pydantic model.
        Use low=True for lightweight structured tasks (e.g. alignment) to avoid 503 errors.
        On 503 UNAVAILABLE, retries after 180s and 360s (max 3 total attempts).
        """
        sleep_with_countdown(20, "Pausa anti-bloqueo (Texto)")

        model = self.text_model

        retries = [360, 360, 360, 360]
        attempt = 0

        while True:
            try:
                with api_spinner("Generando guión con Gemini"):
                    from tools.time_utils import run_with_timeout
                    response = run_with_timeout(
                        self.client.models.generate_content,
                        600, # 10 minutes max wait for massive long video scripts
                        model=model,
                        contents=prompt,
                        config={
                            'response_mime_type': 'application/json',
                            'response_schema': schema,
                        }
                    )
                break
            except (ServerError, TimeoutError) as e:
                is_503 = getattr(e, 'code', None) == 503 or isinstance(e, TimeoutError)

                if is_503 and attempt < len(retries):
                    delay = retries[attempt]
                    attempt += 1
                    warn_msg = f"⚠️ Gemini Text API saturada o bloqueada (503/Timeout). Reintentando en {delay // 60} minutos (Intento {attempt}/2)..."
                    Messenger.info(warn_msg)
                    send_windows_notification("Gemini Text: API Saturada/Bloqueada", f"Reintento {attempt}/2 en {delay // 60} min.")
                    time.sleep(delay)
                else:
                    err_code = getattr(e, 'code', 'Timeout')
                    send_windows_notification("Gemini Text: Error de Servidor", f"Fallo definitivo con error {err_code}.")
                    raise e

        self._extract_usage(response, model)

        if not response.text:
            raise RuntimeError("❌ No hay respuesta de Gemini")

        return schema.model_validate_json(response.text)
