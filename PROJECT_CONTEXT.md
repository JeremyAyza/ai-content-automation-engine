# PROJECT_CONTEXT.md

> Documento de contexto técnico para agentes IA. Generado a partir del código real (no de docs antiguos) el 2026-08-18, rama `add-playwrite`. Si algo aquí contradice el código, confía en el código y actualiza este archivo.

## 1. Qué hace el proyecto

Pipeline CLI en **Python** que genera videos verticales (shorts) u horizontales (long) 100% con IA, de principio a fin: guion → imágenes por escena → narración TTS → alineación audio/texto → ensamblado de video → subtítulos quemados → música de fondo → renombrado final. Soporta múltiples "canales" de contenido (persona/temática distinta cada uno) mediante un sistema de prompts modulares. El canal activo y más maduro es **`codigo_capital`** (contenido financiero, personaje "Tío Warren"). El estado de cada video ("idea") se persiste en CSV y el pipeline es reanudable paso a paso.

No es un servicio web ni tiene API HTTP: es una herramienta de línea de comandos operada por una sola persona en Windows.

## 2. Stack tecnológico

- **Python 3.11+** con **Poetry** (`pyproject.toml` / `poetry.lock`).
- **Pydantic v2** para casi todos los modelos de datos (incluso wrappers de herramientas no-datos, ej. `FFmpegTool`).
- **Pandas** para persistencia en CSV (estado de ideas).
- **google-genai** (Gemini): texto, imágenes (provider alternativo), TTS.
- **Playwright**: controla Chrome con perfil persistente para automatizar una extensión Chrome externa ("Flow Script Processor", proyecto separado fuera de este repo) que interactúa con Google Labs Flow para generar imágenes. Este es el provider de imágenes **por defecto**.
- **Whisper.cpp** (binarios locales en `bin/whisper/`, incluye build CUDA) para transcripción/alineación.
- **FFmpeg/ffprobe** vía `subprocess` (no como librería) — usa `h264_nvenc`, **requiere GPU NVIDIA**.
- **winotify**: notificaciones nativas de Windows (acopla el proyecto a Windows).
- Wrapper **Node.js** (`bin/generate.js` + `package.json`) que solo invoca `poetry run python -m pipeline.main` — atajo de shell, no runtime propio.
- Dev tools: `black`, `isort`, `flake8`, `pyright` (strict, pero mal configurado, ver deuda técnica).
- `selenium` está declarado como dependencia pero **sin uso real** en el código.

## 3. Arquitectura de carpetas

```
pipeline/                  Núcleo del pipeline (paquete Python)
  main.py                  Entry point CLI (argparse): orientation + step + --channel
  pipeline.py              Clase Pipeline (Pydantic BaseModel): orquesta steps 1-7
  config.py                Constantes globales (dirs, patrones de archivo, dimensiones, providers)
  paths.py                 PipelinePaths: resolución de rutas por idea/subcarpeta
  schemas.py               Modelos Pydantic: State, VideoOrientation, BaseIdea, ImagePrompt,
                            VideoPrompt, Scene, VideoScript, CategoryHandler, SelectedConfig
  prompt_manager.py        PromptManager: selecciona canal/categoría, arma prompts, banco de ideas CSV
  storage_csv.py           CsvStore: CRUD de ideas_tracking.csv (estado de cada idea)
  channels/
    base.py                  Prompts genéricos compartidos (chunking, alineación, audio genérico)
    codigo_capital.py         Canal ACTIVO: prompts short/long, handlers e idea-variants
    tio_warren_short.py/long.py  Canal legacy, usado como fallback cuando channel no matchea
    finances_short.py/long.py    Importados pero NUNCA usados en el routing — código muerto

tools/                     Utilidades reusables entre canales
  gemini_base.py            Cliente Gemini compartido + reintentos + tracking de uso de tokens
  gemini_text.py             Generación de texto estructurado (guion/idea)
  gemini_image.py            Generación de imágenes vía Gemini API (provider alternativo)
  gemini_audio.py             TTS vía Gemini
  image_provider.py           Interfaz ImageProvider + Factory ("api" -> Gemini, "playwright" -> Playwright)
  playwright_image.py         Generador de imágenes vía Chrome/extensión Flow (ruta hardcodeada, ver deuda)
  ffmpeg.py                    Wrapper de comandos ffmpeg/ffprobe
  whisper_tool.py               Transcripción con whisper-cli.exe, genera SRT
  whisper_schemas.py             Modelos Pydantic para JSON de whisper.cpp
  audio_tool.py                  Selección de música de fondo aleatoria
  csv_processor.py                Base genérica lectura/escritura CSV con pandas
  messenger.py                     Logger de consola estandarizado (emojis por tipo)
  terminal.py                       Deshabilita QuickEdit mode en consola Windows
  notifications.py                   Notificaciones nativas de Windows
  time_utils.py                       retry decorator, spinners, sleep_with_countdown, run_with_timeout
  text_utils.py                        slugify()

scripts/                   Scripts sueltos, no integrados al pipeline principal
  playwright_login.py       Login manual persistente en Google Flow (guarda sesión en .browser_profile)
  import_images.py           Importa imágenes descargadas manualmente desde Downloads/Flow_Generations
  extract_scripts.py          Extrae script.json en estado SCRIPT_GENERATED a un JSON consolidado
  cleanup_ideas.py             ROTO: usa ruta "flows/" que ya no existe
  test.py                       Archivo basura en UTF-16 corrupto, no versionar

resources/                 Assets estáticos de entrada: bancos de ideas CSV, música, imágenes de referencia
out_short/ out_long/       Salidas por idea (ideas_tracking.csv + carpetas idea_XXXXXX/{images,audios,videos,editions})
data/, example/, temp/, trash/   Artefactos sueltos de pruebas manuales, sin estructura clara
models/whisper/            Modelo ggml-small.bin
bin/whisper/                Binarios whisper.cpp/parakeet (Windows, con soporte CUDA)
bin/generate.js              Wrapper Node.js del CLI Python
.rules/, .agents/            Reglas para agentes IA (algunas DESACTUALIZADAS, ver deuda técnica)
.browser_profile/            Perfil persistente de Chrome (local, correctamente en .gitignore, no trackeado)
Dockerfile, docker-compose.yml   Boilerplate genérico desalineado del proyecto real (no funcional)
Makefile                       Atajos `make icg-*` para correr steps por orientación/canal
```

## 4. Flujo principal del pipeline

Se ejecuta con `python -m pipeline.main <short|long> <step> [--channel X]` (o `make icg-*`, o `node bin/generate.js` sin soporte de `--channel`).

1. **step1_generate_story**: `PromptManager.generate_full_story()` elige un handler de categoría (aleatorio o forzado por canal), opcionalmente toma una idea base sin usar del banco CSV (`resources/bank_ideas_*.csv`, marca `used=true`), genera `BaseIdea` con Gemini, luego el `VideoScript` (escenas con `image_prompt`, `video_prompt`, `narration`). Registra la idea en `ideas_tracking.csv` (estado `SCRIPT_GENERATED`), guarda `idea.json`/`script.json`.
2. **step2_generate_images**: arma `ImageTask` por cada escena/thumbnail faltante y delega a `ImageProvider` (default `IMAGE_PROVIDER = "playwright"`, hardcodeado en `config.py`, no configurable por `.env`). Abre Chrome con la extensión externa "Flow Script Processor" cargada, sube `script.json`, espera que la extensión genere/descargue imágenes desde Google Flow, las mueve a `images/`. Estado → `IMAGES_GENERATED`.
3. **step3_generate_audios** (con `@retry(max_attempts=3)`): procesa escenas en lotes de 15 (`AUDIO_BATCH_SIZE`), sintetiza con Gemini TTS, aplica speedup con ffmpeg, transcribe con Whisper, alinea tiempos por escena con Gemini (`AudioAlignment`), valida duración mínima, separa audio por escena. Estado → `AUDIO_GENERATED`.
4. **step4_generate_videos**: combina imagen+audio por escena con zoom/rotación vía ffmpeg (`h264_nvenc`, requiere GPU NVIDIA), concatena en `raw_video.mp4`. Estado → `VIDEO_GENERATED`.
5. **step5_generate_subtitles**: extrae audio del video, genera `.srt` con Whisper, quema subtítulos (ASS/ffmpeg). Estado → `VIDEO_SUBTITLED`.
6. **step6_add_background_music**: selecciona pista aleatoria de `resources/bg-music`, mezcla con ffmpeg `amix`. Estado → `VIDEO_MUSIC_GENERATED`.
7. **step7_rename_final_video**: renombra al slug del título, limpia archivos intermedios pesados. Estado → `COMPLETED`.

Modos especiales en `main.py`:
- `all`: bucle infinito ejecutando steps 1-7 sobre ideas nuevas.
- `fixed`: retoma una idea incompleta según su `State` hasta completarla, sin generar ideas nuevas.

## 5. Módulos clave

- **`PromptManager`** (`pipeline/prompt_manager.py`): punto central de generación de contenido. Según `orientation` (short/long) y `channel` (string; `codigo_capital`, `tio_warren`, o cualquier otro valor cae en fallback `tio_warren`), selecciona `CategoryHandler`s disponibles, elige aleatoriamente uno y una variante de idea, arma el prompt (+ formato JSON derivado dinámicamente de los campos Pydantic), y expone `get_audio_prompt`/`get_alignment_prompt`. Lee/marca usadas las ideas del banco CSV.
- **Canales** (`pipeline/channels/*`): cada uno define `AUDIO_PROMPT`, `IDEA_PROMPT_*`, `SCRIPT_PROMPT` (bloques largos en español con instrucciones de tono/estructura) y clases `BaseIdea`/`CategoryHandler` vinculando esos prompts a un schema Pydantic. `codigo_capital.py` es el canal activo/maduro. `finances_short.py`/`finances_long.py` están importados pero inalcanzables (código muerto, ver deuda técnica).
- **Generación de imágenes vía Playwright** (`tools/playwright_image.py`): no llama a una API de imágenes directamente; automatiza la extensión Chrome externa que interactúa con Google Labs Flow. Usa perfil de navegador persistente (`.browser_profile`, requiere login manual previo con `scripts/playwright_login.py`). **La ruta a la extensión está hardcodeada a una máquina específica** (ver deuda técnica).
- **`ImageProviderFactory`** (`tools/image_provider.py`): abstrae dos providers intercambiables — `"api"` (Gemini Image) y `"playwright"` (extensión Flow) — seleccionado por `config.IMAGE_PROVIDER` (hardcodeado en código, no por env var).
- **`CsvStore` / `CsvProcessor`**: persistencia simple pandas+CSV del estado de las ideas. Sin locking/concurrencia — asume ejecución single-process.
- **`schemas.py`**: modelos Pydantic centrales, incluye generación dinámica de instrucciones de formato JSON a partir de los propios campos del modelo (para instruir a Gemini el schema de salida esperado).

## 6. Configuración y variables de entorno

`.env.sample` solo documenta `GEMINI_API_KEY`, pero el `.env` real usado incluye más variables:

| Variable | Uso real | Notas |
|---|---|---|
| `GEMINI_API_KEY` | Obligatoria (`tools/gemini_base.py`), lanza `RuntimeError` si falta | — |
| `DEFAULT_CHANNEL` | Usada en `pipeline/main.py`, default `"codigo_capital"` | — |
| `FLOW_PROJECT_URL` | URL del proyecto Google Flow usada por Playwright | — |
| `VIDEO_THEME` | **Sin uso real** en el código | Confuso, documentado como si controlara el canal |
| `AUDIO_PROVIDER` | Leída en `config.py` pero **sin efecto real** | `pipeline.py` siempre instancia `GeminiAudioGenerator` |
| `FISH_AUDIO_API_KEY` | Referenciada en `.env` pero el módulo `tools/fish_audio.py` **ya no existe** | Solo queda un `.pyc` residual |

Requisitos externos NO capturados en `.env`/dependencias declaradas:
- FFmpeg/ffprobe en el PATH del sistema.
- Binarios de whisper.cpp en `bin/whisper/` (ya incluidos en el repo).
- Extensión Chrome "Flow Script Processor" compilada en una ruta externa hardcodeada (proyecto separado, fuera de este repo y de control de versiones).
- GPU NVIDIA para `h264_nvenc` (usado en todos los comandos ffmpeg de video).

## 7. Scripts disponibles

**Makefile** (usa `poetry run python -m pipeline.main ...`):
- `icg-s-step1..7`, `icg-s-all`, `icg-s-fixed` (shorts, canal por defecto)
- `icg-l-step1..7`, `icg-l-all`, `icg-l-fixed` (longs, canal por defecto)
- `icg-import-images`, `icg-extract-scripts`
- `icg-cc-s-all`, `icg-cc-l-all`, `icg-cc-s-step1`, `icg-cc-l-step1` (canal `codigo_capital` explícito) — **incompleto**: faltan `step2`..`step7`/`fixed` para este canal.

**`package.json`** (Node): `install-global` instala `bin/generate.js` como CLI global `generate`. Soporta `generate <short|long> <step|s1..s7|fixed|all>` pero **no expone `--channel`**.

**`scripts/` sueltos** (sin entrada en Makefile salvo los dos ya mencionados): `playwright_login.py`, `cleanup_ideas.py` (roto), `import_images.py`, `extract_scripts.py`, `test.py` (basura, no funcional).

## 8. Convenciones observadas

- **Idioma mixto intencional**: código (nombres, docstrings) en **inglés**; prompts de contenido, mensajes al usuario (`Messenger`) y comentarios de negocio en **español**. Es consistente y deliberado (el contenido final es en español LATAM) — no "corregir" a un único idioma.
- **Pydantic BaseModel** extensivo incluso para herramientas no-datos (`FFmpegTool`, `WhisperTool`, `AudioTool` son `BaseModel` con `arbitrary_types_allowed=True`).
- **Steps de pipeline** como métodos numerados `stepN_verbo_objeto` en `Pipeline`, cada uno con docstring de pasos numerados.
- **Constantes centralizadas** en `pipeline/config.py` — se evita hardcode disperso dentro de `pipeline.py`.
- **Reintentos manuales** con notificaciones Windows para llamadas a Gemini (503/timeout); en cambio `PlaywrightImageGenerator` y los `scripts/` sueltos tienen manejo de errores mínimo.
- **Logging vía `Messenger`** (emoji por tipo de mensaje), no `logging` estándar — sin niveles configurables ni logs a archivo.

## 9. Para el próximo agente

- Antes de tocar `pipeline/channels/`, revisa el routing en `PromptManager` — hay canales importados que no están conectados (`finances_*`).
- El paso más frágil/dependiente del entorno es **step2 (imágenes vía Playwright)**: requiere sesión de Google logueada, extensión externa compilada, y ruta hardcodeada. No asumas que funciona "out of the box" en otra máquina.
- No confíes en `Dockerfile`/`docker-compose.yml` ni en `.rules/standards/main.md` — están desalineados con el código real (ver `TECH_DEBT.md`).
- Ver `TECH_DEBT.md` para la lista de deuda técnica antes de decidir si "arreglar" algo que en realidad es deuda conocida.
