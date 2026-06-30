# 📘 Guía de Contenido: Cómo Cambiar la Temática del Automatizador

El **AI Content Automation Engine** está diseñado con una arquitectura modular basada en **Prompt Managers** y **Handlers**. Esto significa que puedes cambiar completamente el tipo de contenido que genera el bot (de Finanzas a "Sprunkis", Historias de Terror, Curiosidades, etc.) *sin tocar el código base del pipeline de video*.

Aquí te explico cómo funciona y cómo agregar tus propias temáticas.

---

## 🏗️ La Arquitectura de Temáticas (Niches)

El contenido se divide por orientación (Shorts o Longs). Dentro de cada uno, existen "handlers" para diferentes temáticas.

```text
flows/image_content_generator/pipeline/
├── prompt_shorts/                # 📱 Para videos 9:16 (Shorts/Reels)
│   ├── manager.py                # <- Aquí registras tu temática
│   ├── finances/                 # Temática 1 (Ejemplo: Finanzas)
│   └── sprunkis/                 # Temática 2 (Ejemplo: Sprunkis Viral)
│       ├── __init__.py
│       ├── constants.py          # <- Tus prompts (Instrucciones al bot)
│       └── models.py             # <- Tus esquemas de datos (Pydantic)
```

---

## 🚀 Pasos para crear una nueva temática

Si quieres agregar una temática nueva (ej. `misterio`), sigue estos 3 pasos:

### Paso 1: Crea la carpeta y los archivos
Crea una carpeta llamada `misterio` dentro de `prompt_shorts/` con tres archivos:
1. `__init__.py` (vacío)
2. `constants.py`
3. `models.py`

### Paso 2: Define tus Prompts en `constants.py`
Aquí es donde le dices a la IA cómo comportarse. Necesitas definir al menos:
- `AUDIO_PROMPT`: Cómo debe sonar la voz (tono, velocidad, emoción).
- `IDEA_PROMPT`: Cómo idear el concepto del video (ej. "Genera un misterio sin resolver...").
- `SCRIPT_PROMPT`: Las reglas de dirección y guionaje (ritmo, estilo visual, estructura de actos).

> 💡 **Tip Visual:** En el `SCRIPT_PROMPT`, en la sección de reglas visuales, especifica exactamente cómo quieres que se vean las imágenes. El bot usará esto en cada `image_prompt`.

### Paso 3: Define tus Modelos en `models.py`
Define qué variables quieres que la IA te devuelva en la fase de "Ideación" usando Pydantic, y crea el Handler.

```python
from flows.image_content_generator.pipeline.prompt_base.models import BaseIdea, CategoryHandler
from . import constants

class MisterioIdea(BaseIdea):
    IDEA_PROMPT = constants.IDEA_PROMPT_MISTERIO
    # Variables personalizadas:
    asesino_oculto: str
    pista_clave: str

class MisterioHandler(CategoryHandler):
    SCRIPT_PROMPT = constants.SCRIPT_PROMPT
    idea_variants = [MisterioIdea]
```

### Paso 4: Registra tu temática en `manager.py`
Ve a `flows/image_content_generator/pipeline/prompt_shorts/manager.py` y agrega tu Handler a la lista `CATEGORIES`.

```python
from flows.image_content_generator.pipeline.prompt_shorts.misterio.models import MisterioHandler

class PromptManagerShorts(BasePromptManager):
    CATEGORIES = [
        # FinancesHandler,  <-- Puedes comentar los que no quieras usar
        MisterioHandler,    <-- Agregas el tuyo
    ]
```

---

## 🖼️ Referencias de Imagen (Style References)

Si tienes imágenes de referencia para tu temática (por ejemplo, cómo se ven los Sprunkis), colócalas en la carpeta:
`resource/reference/`

El pipeline automáticamente leerá todos los `.png` de esa carpeta y se los enviará a Gemini como anclaje de estilo para que todos los frames que genere se parezcan a tus referencias.

---

> 🎉 **¡Listo!** Ya actualicé el código para incluir la temática **"Sprunkis"** como la temática activa para Shorts. Revisa la carpeta `prompt_shorts/sprunkis` para ver cómo quedó implementado.
