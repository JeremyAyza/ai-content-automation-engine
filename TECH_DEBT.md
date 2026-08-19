# TECH_DEBT.md

> Lista breve de inconsistencias técnicas / deuda técnica detectadas por análisis de código (2026-08-18). No incluye juicios de docs antiguas — solo hechos verificados en código.

1. **Ruta hardcodeada de la extensión Chrome (máquina-específica)**
   `tools/playwright_image.py` — `extension_path` apunta a una ruta local fija (`C:\Users\Jeremy\...\generate-image-ext\...`). El pipeline de imágenes (step2) no corre en otra máquina sin editar código fuente. Debería salir de `.env`.

2. **Canal "Finances" es código muerto**
   `pipeline/prompt_manager.py` importa `FinancesHandler`/`FinancesHandlerLong` de `pipeline/channels/finances_short.py`/`finances_long.py`, pero el routing de canal nunca los referencia. ~200 líneas de prompts huérfanas de un refactor anterior.

3. **`AUDIO_PROVIDER` / Fish Audio: config fantasma**
   `.env` define `FISH_AUDIO_API_KEY` y `config.AUDIO_PROVIDER`, pero `tools/fish_audio.py` fue eliminado (solo queda `.pyc`) y `pipeline.py` siempre instancia `GeminiAudioGenerator` sin leer esa config. Confunde sobre qué provider de audio está realmente activo.

4. **`pyproject.toml` referencia un paquete `flows` inexistente**
   `packages = [{include = "flows"}]` y `include = [...]` en pyright apuntan a un directorio que ya no existe (resabio pre-refactor). Puede romper `poetry build` y da falsos positivos/negativos en pyright. Además `pythonPlatform = "Darwin"` está mal para un proyecto que corre en Windows.

5. **`scripts/cleanup_ideas.py` está roto**
   Usa `Path(__file__).parent.parent / "flows"`, pero la estructura real usa `out_short/`/`out_long/` en la raíz. Falla silenciosamente (no borra nada) dando falsa sensación de limpieza.

6. **`scripts/test.py` es basura versionada**
   Archivo en UTF-16 corrupto, no es un test real, no pertenece a ningún flujo. Eliminar o quitar del control de versiones.

7. **`bin/generate.js` no soporta `--channel`**
   El CLI Node (`generate <short|long> <step>`) no permite pasar canal, a diferencia de `pipeline/main.py` y de los targets `icg-cc-*` del Makefile. Fuerza a usar Poetry/Makefile directamente para canales no-default.

8. **Makefile incompleto para canal `codigo_capital`**
   Solo define `icg-cc-s-all`, `icg-cc-l-all`, `icg-cc-s-step1`, `icg-cc-l-step1`. Faltan `step2`..`step7`/`fixed` para ese canal.

9. **`Dockerfile`/`docker-compose.yml` desalineados y no funcionales**
   Referencian `app/` y `poetry run app` que no existen; no instalan FFmpeg con NVENC, Playwright/Chromium ni whisper.cpp. Boilerplate de plantilla nunca adaptado al proyecto real.

10. **Sin suite de tests**
    No hay `tests/` ni `test_*.py` reales. Lógica frágil (parsing CSV con pandas, alineación de audio, construcción dinámica de JSON schema, heurísticas de `mtime` para mover imágenes descargadas) sin ninguna cobertura automatizada.

11. **`.rules/standards/main.md` desactualizado**
    Documenta rutas `flows/project/out` que ya no reflejan `pipeline/main.py` real (usa `out_short`/`out_long`). Puede inducir a un agente IA a replicar un patrón obsoleto o "corregir" código que en realidad está bien.

12. **`VIDEO_THEME` env var sin uso**
    Documentada en `.env` como si controlara el canal ("TIO_WARREN, FINANCES"), pero no la lee ningún módulo Python. La que realmente aplica es `DEFAULT_CHANNEL`. Elimina confusión al configurar el entorno.

13. **`CsvStore`/`CsvProcessor` sin locking ni backup**
    Reescriben el CSV completo en cada operación sin concurrencia ni journaling. Riesgo de corrupción/pérdida de estado si se interrumpe a mitad de escritura o corre en paralelo.

14. **TODOs de tipado sin resolver**
    `pipeline/storage_csv.py:17` y `tools/csv_processor.py:8` (`# TODO: solve casts`) usan `cast(Any, ...)` para silenciar pandas, reduciendo el valor de `typeCheckingMode = "strict"` en pyright.

15. **`IMAGE_PROVIDER` hardcodeado en código, no en `.env`**
    A diferencia de `AUDIO_PROVIDER` (que sí vive en `.env`, aunque sin efecto real — ver #3), `config.IMAGE_PROVIDER = "playwright"` está fijo en `pipeline/config.py`. Inconsistente: cambiar de provider de imágenes requiere editar código en vez de configuración.
