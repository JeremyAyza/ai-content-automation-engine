# flake8: noqa: E501
AUDIO_PROMPT: str = """Narra el siguiente guion sobre mentalidad de riqueza y consejos financieros con una voz **muy enérgica, rápida y estimulante**, como un creador moderno de educación en TikTok o Reels (Código Capital).

Estilo de actuación:
- Tono: Educativo, pero con mucha chispa y entusiasmo. Tienes que sonar apasionado por el tema.
- Ritmo: Rápido y muy dinámico. Habla con fluidez y velocidad nativa de "Short", pero haz pequeñísimas pausas para enfatizar los conceptos clave.
- Énfasis: Sube la energía y el volumen ligeramente al subrayar palabras como "regla", "hábito", "error", "ahorro", "presupuesto" e "interés compuesto".
- Emoción: Empieza con muchísima fuerza en la primera frase para atrapar la atención. Mantén un nivel de energía alto y motivador hasta el final.
- No agregues sonidos, muletillas ni nada que no esté en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (MENTALIDAD - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Generar una propuesta estructurada para un video corto (Short/TikTok) que exponga un error común de mentalidad usando a nuestros personajes.

**Personajes Obligatorios:**
1. **Tío Warren (El Mentor):** El anciano sabio de traje formal y lentes que devela los trucos financieros.
2. **El Aprendiz:** El joven impulsivo con sudadera verde obsesionado con dinero fácil.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto que exponga un error cotidiano de dinero (ej. "Esta tontería al pagar con tarjeta de crédito te mantiene pobre").
2. **Historia Rápida:**
   - El Aprendiz comete un error financiero típico en un día normal.
   - El Tío Warren lo detiene y le da un 'hack' mental de riqueza rápido para corregirlo.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (ESTRATEGIA - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Generar una propuesta estructurada para un video corto que enseñe un atajo o regla de riqueza práctica con nuestros personajes.

**Personajes Obligatorios:**
1. **Tío Warren (El Mentor):** El experto calmado y calculador.
2. **El Aprendiz:** El joven con hoodie verde que busca el camino fácil.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras sobre un life hack financiero rápido (ej. "El truco legal de los ricos para no pagar impuestos que tú no usas").
2. **Concepto central:** Una táctica concreta (Ley de Pareto, inflación de estilo de vida, regla de las 72 horas). El Tío Warren le muestra al Aprendiz cómo implementarlo paso a paso con números rápidos.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA PREMIUM (DIVERSIÓN Y VIRALIDAD - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Crear un guion de Shorts ultra-dinámico de 15 a 20 micro-escenas, enfocado en "Código Capital" y la dupla Tío Warren y el Aprendiz, garantizando una duración de 1.5 a 2 minutos.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook/Conflicto [Escenas 1-4]:** DEBES usar el campo "hook" para la Escena 1 de forma literal. Muestra al Aprendiz cometiendo un grave error o alardeando de su mentalidad de dinero rápido. El Tío Warren aparece para detenerlo.
2. **Acto 2: El Micro-Storytelling [Escenas 5-15]:** El Tío Warren explica de forma simple el truco, la regla o la matemática del hack financiero. Muestra comparativas visuales rápidas (lo que hace la gente común vs lo que hacen los ricos).
3. **Acto 3: El Educational Payoff [Escenas 16-final]:** Muestra al Aprendiz aplicando el hack y su cara de satisfacción. Termina con un consejo rápido del Tío Warren y un llamado a la acción (CTA) OMNICANAL. En su lugar, usa llamados como: "Dale like, Síguenos en Código Capital para más", "Guarda este video", "Comparte esto con tu amigo" o "Comenta qué opinas".

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Narración:** Frases cortas, punchy y dinámicas. Considera que la voz del Tío Warren es grave, mayor y autoritaria, por lo que las oraciones deben ser sumamente directas para no perder la velocidad y retención del Short. Tío Warren es el mentor pragmático; el Aprendiz es expresivo y cómico.
- **Fluidez:** Ritmo rápido adaptado para la alta retención en Shorts.

### 🔵 REGLAS VISUALES (ESTRICTO)
- **Miniatura (Thumbnail - YT Código Capital):** DEBES generar un `thumbnail_prompt` optimizado para CTR masivo:
  1) **Personajes:** Tío Warren (pato anciano sabio, traje azul a rayas, lentes en el pico, plumas blancas) con expresión seria y apuntando a una pizarra, al lado del Aprendiz (pato joven verde, sudadera negra con logo de Bitcoin, gorra negra) con expresión de absoluta sorpresa o desesperación.
  2) **Texto Gigante (Obligatorio):** Un título de 3 a 7 palabras impactantes dibujado en la imagen (Ej: "EL HACK DEL DINERO").
  3) **Utilería y Flechas:** Usa flechas dibujadas a mano y utilería (monedas, tarjetas).
  4) **Estilo Visual:** `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background, high contrast YouTube thumbnail aesthetic."`
- **Consistencia de Personajes (MANDATORIO en todas las escenas):**
  - **Tío Warren:** Siempre debe ser descrito exactamente como: `"wise, distinguished 60-year-old white duck character, white feathers, wearing glasses on his bill, a sharp navy blue pinstripe suit, a white dress shirt, and a yellow-orange tie, calm and authoritative posture"`.
  - **El Aprendiz:** Siempre debe ser descrito exactamente como: `"22-year-old young green duck character, green feathers, wearing a black casual hoodie with a golden Bitcoin logo on the front, wearing a black baseball cap, looking confused or expressive"`.
- **Estilo de Ilustración Global:** El campo `style` de las escenas DEBE ser estrictamente: `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background."`
- **Relación Imagen-Texto:** Cada escena debe traducir visualmente lo que se escucha (ej: Tío Warren dividiendo un pastel en partes para explicar presupuesto).

### 🔴 IDIOMAS
- **image_prompt:** Todos los campos de descripción visual (subjects, environment, lighting, composition, style) en **INGLÉS**. Excepción: Los textos que deban aparecer físicamente dibujados en la imagen deben estar en **ESPAÑOL** (Ej: "A sign that says 'EMERGENCIA'").
- **video_prompt:** Todos los campos (motion, camera_movement, transition, duration_hint) en **INGLÉS**.
- **narration:** El campo de voz en off en **ESPAÑOL LATINOAMERICANO**.

TU IDEA DE BASE (CONTEXTO EN JSON):
{idea_context_json}

"""
