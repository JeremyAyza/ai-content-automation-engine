# Historial de Cambios del Proyecto (Evolución Práctica)

A continuación, se detalla la evolución del código fuente desde el inicio del proyecto, agrupando los cambios por áreas funcionales tras haber analizado las modificaciones directas en los archivos (y no solo los mensajes).

## 1. Arquitectura y Estructura Base (Pipelines)
- **Implementación del Core Pipeline:** Se estructuró el flujo principal de generación en `flows/pipeline/pipeline.py`, el cual orquesta la creación del video.
- **Manejadores Base:** Se crearon manejadores genéricos y específicos (`prompt_base/manager.py`, `prompt_longs/manager.py`, `prompt_shorts/manager.py`) para administrar y despachar las instrucciones a las APIs dependiendo del formato (Shorts vs Videos Largos).
- **Integraciones con IA y Edición:**
  - **Gemini:** Conexiones en `tools/text_generation/gemini.py` y `tools/audio_generation/gemini.py` para la generación de guiones y la síntesis de voz (TTS).
  - **FFmpeg:** Configuración de utilidades de renderizado en `tools/video_editing/ffmpeg.py` (recientemente se simplificó eliminando la transición de *zoom blur*).

## 2. Especialización de Contenido (Persona: Tío Warren)
- **Modelos y Constantes:** Se introdujo fuertemente el perfil "Tío Warren". Se crearon constantes especializadas de prompts (`constants.py`) y definiciones de modelos Pydantic (`models.py`) en sus respectivos directorios tanto para `shorts` como para `longs`.
- **Refinamiento de Prompts:** 
  - Se eliminaron los esquemas JSON incrustados crudos dentro de los archivos `constants.py` para depender más de la validación estructural externa.
  - Se hicieron ajustes iterativos a los prompts para mejorar la naturalidad ("toque humano") y la proporcionalidad visual ("aumentar escenas proporcionalmente").
- **Assets de Referencia:** Se introdujeron imágenes semilla/referencia (ej. `tio_warren_reference.png`, `tio_warren_aprendiz.jpeg`) para estandarizar la línea visual.

## 3. Migración y Optimización de Datos (Bancos de Ideas)
- **De JSON a CSV:** El proyecto comenzó utilizando extensos diccionarios JSON para almacenar el banco de ideas (`bank_ideas_longs.json`, `bank_ideas_shorts.json`). En las etapas más recientes, se realizó una migración masiva de estos datos hacia formato CSV (`bank_ideas_base.csv`, `bank_ideas_longs.csv`, `bank_ideas_shorts.csv`).
- **Impacto:** Esto redujo drásticamente el peso de los archivos de configuración (eliminando más de 1200 líneas de código JSON), haciendo que la lectura y seguimiento de ideas sea más manejable como tabla.

## 4. Herramientas de Automatización y CLI
- **Scripts de Soporte:** Se implementaron herramientas en la carpeta `scripts/`:
  - `extract_scripts.py`: Para sacar y procesar la data de los guiones generados.
  - `import_images.py`: Para facilitar la ingesta y manipulación de imágenes al directorio del proyecto.
- **Interfaz de Usuario (CLI) y Comandos:**
  - Se introdujo `cli.py`, sentando las bases para interactuar con los pipelines y los scripts desde la terminal sin tocar código.
  - Se agregó un `Makefile` para registrar comandos rápidos (ej. ejecutar CLI, correr importaciones, etc.).

---
*Nota: Este análisis está basado en la lectura directa del histórico de diferencias (diffs) y la adición/eliminación de archivos en los 36 commits del repositorio.*
