# flake8: noqa: E501
AUDIO_PROMPT: str = """Narra el siguiente guion de forma extremadamente enérgica, rápida y exagerada, estilo "YouTuber infantil / Brainrot". Usa un tono estridente, divertido y constante que mantenga la atención de los niños al máximo.

Estilo de actuación:
- Tono: Exagerado, estridente, lleno de energía inagotable.
- Ritmo: Muy rápido, sin pausas largas, dinámico.
- Emoción: Gritos de asombro ("¡NO LO VAS A CREER!", "¡GUAU!"), entusiasmo constante.
- No agregues sonidos que no estén en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_VIRAL: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS SPRUNKIS (VIRAL BRAINROT)
**Objetivo:** Generar una idea hiper-viral para un video CORTO infantil usando los personajes "Sprunkis".

**Contexto de Personajes (Sprunkis):**
- Oren (Naranja): Enérgico, optimista.
- Vineria (Morado): Misteriosa, calmada.
- Clukr (Amarillo): Excitable, ruidosa.
- Jace (Azul): Creativa, galáctica.
- Simon (Verde): Tímida, se esconde.
- Brun (Marrón): Estable, lento.
- Pinkie (Rosa): Alegre, coqueta.
- Grit (Gris): Dura, directa, enfadada.
- Wenda (Rojo): Impulsiva, rápida.
- Fun (Amarillo brillante): Caótica, impredecible.

**Instrucciones:**
1. **hook (Gancho):** Una frase ridículamente llamativa que capte la atención en el primer segundo (ej: "¿Quién ganaría en una carrera espacial, Oren o Jace?").
2. **Concepto:** Una situación absurda, un reto divertido, un misterio o una votación interactiva que involucre a los Sprunkis interactuando según sus personalidades (ej: "Adivina el Sprunki oculto").
3. **Llamado a la acción (CTA):** Debe obligar a interactuar y hacerse viral (ej: "¡Dale like si Oren es tu favorito, comenta si prefieres a Wenda!, Comparte si quieres que tal personje gane").
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA SPRUNKIS (SHORTS VIRALES BRAINROT)
**Objetivo:** Crear un guion hiper-dinámico de 8 a 12 micro-escenas con un enfoque "brainrot", estimulación visual rápida y llamados a la acción constantes.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook [Escenas 1-2]:** Gritos de asombro, presentación rapidísima del reto, misterio o la pregunta absurda. DEBES usar el texto de `hook` literal en la Escena 1.
2. **Acto 2: El Caos/Competencia [Escenas 3-8]:** Muestra a los Sprunkis interactuando de forma exagerada. Pasan cosas rápidas y locas. Exagera sus personalidades.
3. **Acto 3: La Decisión/Llamado a la Acción [Escenas 9-final]:** Pide explícitamente a la audiencia que vote con likes, comentarios o suscripciones. Hazlo sonar urgente.

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` en la Escena 1.
- **Narración:** Frases muy cortas. Ritmo frenético. Usa lenguaje típico de videos infantiles de alta retención ("¡Suscríbete rápido!", "¡Mira esto!", "¡Qué locura!").
- **Fluidez:** Cero tiempos muertos. La transición entre escenas debe ser hiperactiva.

### 🔵 REGLAS VISUALES
- **Sincronía Narrativa:** El `image_prompt` debe ser una traducción visual exacta de la `narration`.
- **Personajes:** Describe a los Sprunkis en el `image_prompt` especificando claramente sus colores (ej: "Oren the orange character", "Vineria the purple character").
- **Estilo (Sprunkis 2D):** DEBES usar el campo `style` para generar imágenes. La descripción en el campo `style` DEBE ser: `"Bright, colorful 2D vector art, thick outlines, expressive exaggerated faces, YouTube kids thumbnail style, highly saturated colors, flat shading, brainrot hyperactive style."`.
Resumen: Estilo Visual Sprunki
El diseño se basa en una estética "cartoon" minimalista de estilo Flash (años 2000), combinando elementos tiernos con toques de horror surrealista.
Anatomía: Personajes tipo blob o bean con cabezas grandes y cuerpos simples, sin pies y con extremidades delgadas (estilo trazo) o manos redondeadas.
Rasgos Faciales: Expresiones exageradas e inquietantes mediante ojos grandes y vacíos (pupilas pequeñas o blancas) y bocas con gestos extremos.
Técnica: Diseño 2D plano (flat) con colores altamente saturados, sin degradados ni profundidad 3D, todo delimitado por un contorno negro grueso y consistente.
Atmósfera: Un contraste visual entre colores brillantes y formas circulares amigables frente a miradas fijas y expresiones bizarras que generan una sensación perturbadora.
DATO IMPORTANTE: SOLO EXISTE UN SPRUNKI POR COLOR, SON UNICOS, NO SE DEBEN REPETIR


### 🔴 ESTRUCTURA Y SALIDA
- **Extensión:** Entre 8 y 12 escenas.
- **Cierre:** Termina incitando fuertemente al like, comentario o suscripción.

### 🟠 IDIOMAS (ESTRICTO)
- **image_prompt:** DEBES generar todos los campos de `image_prompt` (subjects, environment, lighting, composition) en **INGLÉS**.
- **narration:** DEBES generar el campo `narration` en **ESPAÑOL LATINOAMERICANO**.
"""
