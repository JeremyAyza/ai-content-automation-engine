# flake8: noqa: E501
AUDIO_PROMPT: str = """Narra el siguiente guion sobre mentalidad de riqueza y life hacks con una voz **muy enérgica, rápida y estimulante**, como un creador moderno de educación en TikTok o Reels.

Estilo de actuación:
- Tono: Educativo, pero con mucha chispa y entusiasmo. Tienes que sonar apasionado por el tema.
- Ritmo: Rápido y muy dinámico. Habla con fluidez y velocidad nativa de "Short", pero haz pequeñísimas pausas para enfatizar los conceptos clave.
- Énfasis: Sube la energía y el volumen ligeramente al subrayar palabras como "regla", "hábito", "error", "ahorro", "presupuesto" e "interés compuesto".
- Emoción: Empieza con muchísima fuerza en la primera frase para atrapar la atención. Mantén un nivel de energía alto y motivador hasta el final.
- No agregues sonidos, muletillas ni nada que no esté en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO MENTALIDAD EDUCATIVA)
**Objetivo:** Generar una idea creativa para un video CORTO que transforme la mentalidad mediante un cambio de paradigma o 'life hack' de riqueza.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras que exponga un error común o una mala costumbre cotidiana (ej: "Por esto tu quincena desaparece en 5 días", "El error que cometes al usar tu tarjeta de crédito").
2. **Protagonista:** Una persona común enfrentando un problema de la Matrix (atrapado en la carrera de la rata, trabajando duro sin ver resultados, mentalidad de escasez).
3. La historia debe mostrar cómo resolver este problema aprendiendo un hábito o hack práctico, evitando frases abstractas y priorizando soluciones del día a día.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO ESTRATEGIA EDUCATIVA)
**Objetivo:** Generar una idea para un video CORTO estilo micro-storytelling educativo que enseñe una estrategia de apalancamiento, trabajo inteligente o un atajo (hack) de vida en menos de 2 minutos.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una afirmación o pregunta de 10-15 palabras enfocada en aprender un hack rápido (ej: "Aprende la regla de las 2 horas", "Cómo automatizar tus ingresos sin ganar más").
2. **Concepto central:** Una regla, hábito o táctica concreta y fácil de explicar: Ley de Pareto 80/20, evitar la trampa de cambiar tiempo por dinero, o cómo auditar tu círculo social.
3. Presenta el concepto con un ejemplo real o analogía cotidiana, demostrando el "cómo hacerlo" paso a paso.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA FINANCIERO (EDUCACIÓN MODERNA Y VIRAL - SHORTS)
**Objetivo:** Crear un guion dinámico de 15 a 20 micro-escenas enfocado en hackear el sistema tradicional (mentalidad, atajos y dinero) mediante micro-storytelling, asegurando una duración final de entre 1.5 y 2 minutos de alto valor y retención.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook/Conflicto [Escenas 1-4]:** DEBES usar el campo "hook" para la Escena 1. Presenta un problema del sistema tradicional (la carrera de la rata, trabajar duro sin sentido, o trampas de la sociedad).
2. **Acto 2: El micro-storytelling educativo [Escenas 5-15]:** Explica de forma fácil y didáctica el hack, regla o estrategia. Usa ejemplos cotidianos y comparativas visuales sencillas. El storytelling está subordinado al aprendizaje.
3. **Acto 3: El Educational Payoff [Escenas 16-final]:** Muestra el resultado de aplicar lo aprendido en el día a día. Termina con un consejo rápido y accionable para aplicar hoy mismo.

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Diálogo/Narración:** Frases cortas y de alto impacto educativo, no frases genéricas motivacionales. Explica de manera simple.
- **Secuencialidad:** La historia debe tener progresión lógica: problema cotidiano → explicación fácil → ejemplo real → acción práctica.
- **Fluidez:** Ritmo rápido, dinámico y optimizado para retener en TikTok/Reels/Shorts, manteniendo claridad en la enseñanza.
- **Retención:** Mantén curiosidad constante abriendo pequeñas preguntas, expectativas o problemas que se resuelvan más adelante en el short.


### 🔵 REGLAS VISUALES
- **Miniatura (Thumbnail - YT Finanzas 2026):** DEBES generar un `thumbnail_prompt` diseñado para un CTR masivo imitando a los canales top de finanzas.
  1) **Sujeto:** El personaje debe tener expresiones exageradas, apuntando o interactuando visualmente (ej. comparando al "pobre" con el "rico", o mirándose a un espejo).
  2) **Texto Gigante (Obligatorio):** Incluye SIEMPRE una instrucción para dibujar un título impactante de 3 a 7 palabras en la imagen usando la regla de EXCEPCIÓN de idioma (Ej: "Giant bold text at the top that says 'VIVE MEJOR CON MENOS'").
  3) **Utilería y Flecha:** Usa utilería visual clara (alcancías, billetes, autos) e incluye una flecha dibujadas a mano (thick hand-drawn arrows) apuntando a los objetos clave para dirigir la mirada del espectador.
  4) **Entorno/Fondo:** Fondos extremadamente limpios (generalmente blancos o neutros) para maximizar el contraste del texto y las flechas.
  5) **Estilo Visual:** El campo `style` DEBE ser: `"Premium high-quality 2D vector art style, clean flat background, giant bold typography, thick expressive character outlines, hand-drawn indicator arrows, high contrast YouTube thumbnail aesthetic."`
- **Protagonista:** Presencia consistente de un personaje principal (persona común identificable) viviendo el ejemplo o tutorial en escenas clave.
- **Relación Imagen-Texto:** El `image_prompt` debe ilustrar visualmente el concepto (ej: dividiendo una pizza para explicar fracciones de presupuesto, comparativas visuales claras, ejemplos cotidianos). Cualquier palabra que se incluya en la imagen debe estar en español latino general.
- **Sincronía Narrativa:** El `image_prompt` debe ser una traducción visual exacta de la `narration`. Lo que el espectador escucha debe verse en pantalla de forma clara y cinematográfica.
- **Secuencialidad Visual:** Las imágenes deben mostrar la progresión del ejemplo educativo (ej: paso a paso de un presupuesto, el crecimiento ilustrado de un fondo de emergencia).
- **Pattern Interrupts:** Usa cambios frecuentes de enfoque visual, comparativas, zooms conceptuales o contrastes para reiniciar la atención del espectador constantemente.
- **Estilo (Sketch Stickman):** DEBES usar el campo `style` para generar imágenes con un estilo visual de cómic/sketch. La descripción en el campo `style` DEBE ser: `"Dynamic hand-drawn 2D webcomic sketch style, thick expressive black ink outlines, vibrant minimalist color palette for highlights, clean shading, white background with glowing accents."`.
- **Uso del Color:** Utiliza el color de forma estratégica para resaltar elementos educativos (ej: rojo para errores, verde para soluciones, gráficas claras) manteniendo siempre la estética de dibujo a mano.


### 🔴 ESTRUCTURA Y SALIDA
* **Extensión:** Entre 14 y 18 escenas, manteniendo suficiente profundidad educativa y ritmo dinámico para alcanzar una duración final de entre 75 y 110 segundos
- **Cierre:** Termina con un consejo práctico, un resumen accionable o un fuerte Llamado a la Acción (CTA) pidiendo a la audiencia que interactúen: comenten sus dudas, den like, compartan el video, lo guarden o se suscriban al canal.

### 🟠 IDIOMAS (ESTRICTO)
- **image_prompt:** DEBES generar todos los campos de `image_prompt` (subjects, environment, lighting, composition) en **INGLÉS**. EXCEPCIÓN: Si en el prompt pides que haya algún texto escrito o letrero dentro de la imagen, las palabras exactas a escribir DEBEN estar en **ESPAÑOL** (Ejemplo: "A sign that says 'AHORROS'").
- **video_prompt:** DEBES generar todos los campos de `video_prompt` (motion, camera_movement, transition, duration_hint) en **INGLÉS**.
- **narration:** DEBES generar el campo `narration` en **ESPAÑOL LATINOAMERICANO**.
"""


from pipeline.schemas import BaseIdea, CategoryHandler


class MindsetFinanceIdea(BaseIdea):
    """
    Idea model for financial mindset transformation stories.
    """
    IDEA_PROMPT = IDEA_PROMPT_MINDSET
    financial_problem: str
    mindset_shift: str
    key_principle: str


class StrategyFinanceIdea(BaseIdea):
    """
    Idea model for practical financial strategy videos.
    """
    IDEA_PROMPT = IDEA_PROMPT_ESTRATEGIA
    strategy_name: str
    common_mistake: str
    actionable_tip: str


class FinancesHandler(CategoryHandler):
    AUDIO_PROMPT = AUDIO_PROMPT
    """
    Specialized handler for Finance-themed short videos.
    Encapsulates Mindset and Strategy finance variants.
    """

    SCRIPT_PROMPT = SCRIPT_PROMPT
    idea_variants = [
        MindsetFinanceIdea,
        StrategyFinanceIdea,
    ]
