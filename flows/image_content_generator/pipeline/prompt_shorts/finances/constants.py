# flake8: noqa: E501
AUDIO_PROMPT: str = """Narra el siguiente guion de finanzas personales con voz segura, clara y dinámica, como un creador moderno de educación financiera explicando un concepto clave de forma fácil de entender.

Estilo de actuación:
- Tono: educativo, cercano y confiable. Eres alguien que quiere que el espectador entienda y aplique la lección, no un "gurú" inalcanzable.
- Ritmo: dinámico pero didáctico. Acelera en la introducción del problema, pero haz pausas claras al explicar conceptos, reglas o ejemplos para que la audiencia asimile el aprendizaje.
- Énfasis: subraya con energía conceptos prácticos como "regla", "hábito", "error", "ahorro", "presupuesto" e "interés compuesto".
- Emoción: empieza con un gancho directo, mantén energía emocional natural y sensación conversacional durante toda la explicación, y cierra con una invitación clara a aplicar lo aprendido.
- No agregues sonidos, muletillas ni nada que no esté en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO MENTALIDAD EDUCATIVA)
**Objetivo:** Generar una idea creativa para un video CORTO que transforme la mentalidad mediante una lección financiera concreta y aplicable.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras que exponga un error común o una mala costumbre cotidiana (ej: "Por esto tu quincena desaparece en 5 días", "El error que cometes al usar tu tarjeta de crédito").
2. **Protagonista:** Una persona común enfrentando un problema cotidiano real (gastos hormiga, mal manejo de presupuesto, miedo a abrir una cuenta de inversión).
3. La historia debe mostrar cómo resolver este problema aprendiendo un hábito financiero práctico, evitando frases abstractas y priorizando soluciones del día a día.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO ESTRATEGIA EDUCATIVA)
**Objetivo:** Generar una idea para un video CORTO estilo micro-storytelling educativo que enseñe una estrategia financiera accionable en menos de 2 minutos.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una afirmación o pregunta de 10-15 palabras enfocada en aprender algo rápido (ej: "Aprende la regla del 50/30/20 en un minuto", "Cómo crear un fondo de emergencia sin ganar más").
2. **Concepto central:** Una regla, hábito o táctica concreta y fácil de explicar: interés compuesto simple, cómo leer tu estado de cuenta, presupuestos básicos, o cómo evitar deudas malas.
3. Presenta el concepto con un ejemplo real o analogía cotidiana (ej: comparar una inversión con plantar un árbol), demostrando el "cómo hacerlo" paso a paso.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA FINANCIERO (EDUCACIÓN MODERNA Y VIRAL - SHORTS)
**Objetivo:** Crear un guion dinámico de 15 a 20 micro-escenas enfocado en educación financiera práctica y accionable (micro-storytelling educativo), asegurando una duración final de entre 1.5 y 2 minutos de alto valor y retención.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook/Conflicto [Escenas 1-4]:** DEBES usar el campo "hook" para la Escena 1. Presenta un problema financiero cotidiano, error común o mito.
2. **Acto 2: El micro-storytelling educativo [Escenas 5-15]:** Explica de forma fácil y didáctica un concepto, regla o estrategia. Usa ejemplos cotidianos y comparativas visuales sencillas. El storytelling está subordinado al aprendizaje.
3. **Acto 3: El Educational Payoff [Escenas 16-final]:** Muestra el resultado de aplicar lo aprendido en el día a día. Termina con un consejo rápido y accionable para aplicar hoy mismo.

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Diálogo/Narración:** Frases cortas y de alto impacto educativo, no frases genéricas motivacionales. Explica de manera simple.
- **Secuencialidad:** La historia debe tener progresión lógica: problema cotidiano → explicación fácil → ejemplo real → acción práctica.
- **Fluidez:** Ritmo rápido, dinámico y optimizado para retener en TikTok/Reels/Shorts, manteniendo claridad en la enseñanza.
- **Retención:** Mantén curiosidad constante abriendo pequeñas preguntas, expectativas o problemas que se resuelvan más adelante en el short.


### 🔵 REGLAS VISUALES
- **Protagonista:** Presencia consistente de un personaje principal (persona común identificable) viviendo el ejemplo o tutorial en escenas clave.
- **Relación Imagen-Texto:** El `image_prompt` debe ilustrar visualmente el concepto (ej: dividiendo una pizza para explicar fracciones de presupuesto, comparativas visuales claras, ejemplos cotidianos).
- **Sincronía Narrativa:** El `image_prompt` debe ser una traducción visual exacta de la `narration`. Lo que el espectador escucha debe verse en pantalla de forma clara y cinematográfica.
- **Secuencialidad Visual:** Las imágenes deben mostrar la progresión del ejemplo educativo (ej: paso a paso de un presupuesto, el crecimiento ilustrado de un fondo de emergencia).
- **Pattern Interrupts:** Usa cambios frecuentes de enfoque visual, comparativas, zooms conceptuales o contrastes para reiniciar la atención del espectador constantemente.
- **Estilo (Sketch Stickman):** DEBES usar el campo `style` para generar imágenes con un estilo visual de cómic/sketch. La descripción en el campo `style` DEBE ser: `"Dynamic hand-drawn 2D webcomic sketch style, thick expressive black ink outlines, vibrant minimalist color palette for highlights, clean shading, white background with glowing accents."`.
- **Uso del Color:** Utiliza el color de forma estratégica para resaltar elementos educativos (ej: rojo para errores, verde para soluciones, gráficas claras) manteniendo siempre la estética de dibujo a mano.

### 🔴 ESTRUCTURA Y SALIDA
* **Extensión:** Entre 14 y 18 escenas, manteniendo suficiente profundidad educativa y ritmo dinámico para alcanzar una duración final de entre 75 y 110 segundos
- **Cierre:** Termina con un consejo práctico, un resumen accionable o una pregunta que invite a reflexionar y comentar.

### 🟠 IDIOMAS (ESTRICTO)
- **image_prompt:** DEBES generar todos los campos de `image_prompt` (subjects, environment, lighting, composition) en **INGLÉS**.
- **narration:** DEBES generar el campo `narration` en **ESPAÑOL LATINOAMERICANO**.
"""
