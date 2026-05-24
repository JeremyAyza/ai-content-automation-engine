# 🗑️ Archivos Eliminados

Registro de todos los archivos y directorios eliminados en la limpieza de dead code del **2026-05-23**.

---

## Resumen

| Archivo / Directorio | Tipo | Justificativo |
|---|---|---|
| `tools/video_generation/` | 📁 Directorio completo | Nunca importado en ningún flow |
| `tools/midjourney/` | 📁 Directorio completo | Solo usado desde `video_generation/` (también eliminado) |
| `tools/chrome/` | 📁 Directorio completo | Solo usado desde `midjourney/base_bot.py` (también eliminado) |
| `tools/discord/` | 📁 Directorio completo | Solo usado desde `midjourney/base_bot.py` (también eliminado) |
| `tools/env_settings/` | 📁 Directorio completo | Solo usado desde `midjourney/` y `discord/` (también eliminados) |
| `tools/image_generation/midjourney.py` | 📄 Archivo | `MidjourneyImageGenerator` nunca se instancia; solo `ImageTask` se reutilizaba |
| `tools/common/style_reference_manager.py` | 📄 Archivo | `StyleReferenceManager` nunca importado fuera de su propio archivo |

---

## Detalle por archivo

### `tools/video_generation/gemini.py`
**Clase**: `GeminiVideoGenerator` (Gemini Veo 3.1)

Herramienta para generar videos con el modelo `veo-3.1-fast-generate-preview`. Soporta text-to-video e image-to-video. Nunca fue registrada ni llamada desde ningún flow ni pipeline. Zero imports entrantes confirmados con `grep`.

---

### `tools/video_generation/midjourney.py`
**Clase**: `MidjourneyVideoGenerator`

Bot de Selenium para generar videos vía Midjourney (usando Discord como interfaz). Incluye lógica de upload de start frame, polling de resultados y descarga. Nunca importado fuera de su directorio. El archivo terminaba con un bloque de prueba comentado (`# MidjourneyVideoGenerator().generate_video(...)`), señal de que fue desarrollado pero nunca integrado.

---

### `tools/midjourney/base_bot.py`
**Clase**: `MidjourneyBot`

Bot base con toda la lógica de Selenium para interactuar con Discord/Midjourney: login, envío de comandos `/imagine`, polling de mensajes y descarga de medios. Solo era importado por `tools/image_generation/midjourney.py` y `tools/video_generation/midjourney.py`, ambos dead code.

---

### `tools/chrome/driver.py`
**Funciones**: `find_element`, `upload_file`, etc.

Wrappers de Selenium WebDriver para Chrome. Solo importado por `tools/midjourney/base_bot.py` (eliminado).

---

### `tools/discord/login.py`
**Clase**: `DiscordBot`

Automatización de login en Discord vía Selenium. Solo importado por `tools/midjourney/base_bot.py` (eliminado).

---

### `tools/env_settings/settings.py`
**Objeto**: `ENV_SETTINGS` (Pydantic Settings)

Configuración de variables de entorno para credenciales de Discord/Midjourney (`DISCORD_EMAIL`, `DISCORD_PASSWORD`, etc.). Solo importado por `tools/midjourney/base_bot.py` y `tools/discord/login.py`, ambos eliminados. El proyecto actualmente gestiona sus secrets directamente con `python-dotenv` en `GeminiBase`.

---

### `tools/image_generation/midjourney.py`
**Clases**: `MidjourneyImageGenerator`, `ActiveJob`, `ImageTask`

`MidjourneyImageGenerator` nunca fue instanciada desde ningún flow (el pipeline usa `GeminiImageGenerator`). `ActiveJob` es interna al archivo. Solo `ImageTask` era reutilizada externamente — se migró a `tools/image_generation/gemini.py` para no perder el contrato de datos.

> **Nota**: El import en `pipeline.py` fue actualizado de:
> ```python
> from tools.image_generation.midjourney import ImageTask
> ```
> a:
> ```python
> from tools.image_generation.gemini import GeminiImageGenerator, ImageTask
> ```

---

### `tools/common/style_reference_manager.py`
**Clase**: `StyleReferenceManager`

Utilidad para cargar imágenes de referencia de estilo desde un directorio. Nunca importada fuera de su propio archivo. La funcionalidad equivalente está integrada directamente en el constructor de `GeminiImageGenerator` (parámetro `reference_dir`).

---

## Árbol de dependencias eliminado

```
tools/video_generation/gemini.py      → sin consumidores
tools/video_generation/midjourney.py  → sin consumidores externos
  └── tools/midjourney/base_bot.py
        ├── tools/chrome/driver.py
        ├── tools/discord/login.py
        └── tools/env_settings/settings.py
tools/image_generation/midjourney.py  → MidjourneyImageGenerator sin consumidores
  └── tools/midjourney/base_bot.py    (ya eliminado arriba)
tools/common/style_reference_manager.py → sin consumidores
```

Todo el árbol parte de dos raíces de dead code aisladas: la integración con **Midjourney/Discord** y la integración con **Gemini Veo** para video — ambas features que existían en el codebase pero nunca fueron conectadas al pipeline activo.
