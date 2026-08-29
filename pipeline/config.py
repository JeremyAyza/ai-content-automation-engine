from pathlib import Path
import os

# Standard Output Directories
IDEAS_DIR = "ideas"
IMAGES_DIR = "images"
AUDIOS_DIR = "audios"
VIDEOS_DIR = "videos"
EDITIONS_DIR = "editions"

# Standard Output Files
IDEA_JSON = "idea.json"
SCRIPT_JSON = "script.json"
RAW_VIDEO = "raw_video.mp4"
SUBTITLED_VIDEO = "subtitled_video.mp4"
FINAL_AUDIO = "final_audio.wav"
FINAL_SUBS = "final_subs.srt"
FINAL_VIDEO = "final_video.mp4"

# --- Audio & Image Configuration ---
AUDIO_PROVIDER: str = os.getenv("AUDIO_PROVIDER", "gemini") # "gemini" or "fish"
IMAGE_PROVIDER = "playwright" # "api" or "playwright"
FLOW_PROJECT_URL: str = os.getenv("FLOW_PROJECT_URL", "https://labs.google/fx/es/tools/flow/project/a4c59561-19b9-4709-92a6-5e2c76789fb1")

# --- Gemini Configuration ---
GEMINI_TEXT_MODEL = "gemini-3.1-pro-preview"
# En prueba: gemini-3.1-flash-tts-preview (más costoso: $1.00/$20.00 por M
# tokens vs $0.50/$10.00 del anterior "gemini-2.5-flash-preview-tts").
# Revertir a la línea anterior si la voz/consistencia no convence.
GEMINI_TTS_MODEL = "gemini-2.5-flash-preview-tts"
SHORT_AUDIO_SPEEDUP = 1.02
LONG_AUDIO_SPEEDUP = 1.065
# Escenas por batch de audio TTS. Elegido para minimizar "costuras" de tono
# entre llamadas (cada llamada al TTS es stateless, ver TECH_DEBT/notas de
# investigación) sin arriesgar el techo real del modelo (~16k tokens de
# salida =~ 10 min de audio continuo):
#   - Shorts (20-25 escenas, 8-14 palabras/escena): caben SIEMPRE en 1 solo
#     batch (25 escenas x 14 palabras = 350 palabras =~ 2.5 min, muy por
#     debajo del techo).
#   - Longs (55-70 escenas, 15-40 palabras/escena): peor caso 25 escenas x
#     40 palabras = 1000 palabras =~ 7.2 min por batch, con margen de
#     seguridad bajo el techo de ~10 min.
AUDIO_BATCH_SIZE = 25
MIN_AUDIO_DURATION = 0.5
MIN_AUDIO_SIZE_BYTES = 1024
BG_MUSIC_VOLUME = 0.18

# Video Dimension Configurations
SHORT_WIDTH = 1080
SHORT_HEIGHT = 1920
LONG_WIDTH = 1920
LONG_HEIGHT = 1080

# Subtitle Font Sizes
SHORT_FONT_SIZE = 80
LONG_FONT_SIZE = 55

# Zoom and Rotation (Swing) Configurations
SHORT_ZOOM_MAX = 1.05
SHORT_ROTATE_ANGLE = 1.0
LONG_ZOOM_MAX = 1.02
LONG_ROTATE_ANGLE = 0.3

# Standard Scene Patterns
SCENE_IMAGE_PATTERN = "scene_{}.jpg"
SCENE_AUDIO_PATTERN = "scene_{}.wav"
SCENE_VIDEO_PATTERN = "scene_{}.mp4"
BATCH_AUDIO_PATTERN = "batch_{}.wav"

# Standard Resource Directories
BG_MUSIC_DIR = "bg-music"
REFERENCES_DIR = "reference"

# Standard Tracking Files
IDEAS_TRACKING_CSV = "ideas_tracking.csv"
SHORTS_IDEAS_BANK = "bank_ideas_shorts.csv"
LONGS_IDEAS_BANK = "bank_ideas_longs.csv"
