# flake8: noqa: E501
IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO MENTALIDAD - LONG)
**Objetivo:** Generar una idea profunda para un video largo (de 12 a 15 minutos) sobre una transformación de mentalidad financiera.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto que exponga un error común, trampa o revelación del sistema (ej: "La verdad incómoda de por qué ahorrar dinero te está haciendo más pobre").
2. **Protagonista:** Un personaje stickman común y corriente (dibujo de palitos) que atraviesa una crisis financiera real y llega a una revelación profunda.
3. Arco Narrativo: Desarrollo profundo del conflicto. Dedica tiempo a explorar la psicología detrás del error o la trampa del sistema antes de dar la solución. Genera empatía detallando por qué es tan fácil caer en la trampa antes de mostrar la transformación.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO ESTRATEGIA - LONG)
**Objetivo:** Generar una idea para un video largo (de 12 a 15 minutos) que explique en profundidad una estrategia financiera poderosa y práctica.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una afirmación o pregunta de 10-15 palabras de alto impacto enfocada en aprender un hack o regla (ej: "El método de la regla del 50/30/20 que los bancos no quieren que uses").
2. **Concepto central:** Una regla, hábito o táctica concreta y fácil de explicar (Ley de Pareto, Bola de nieve vs Avalancha, inflación del estilo de vida).
3. Presenta el concepto con un ejemplo real o analogía cotidiana. Explora a profundidad el 'por qué' funciona a nivel psicológico o matemático antes de demostrar el "cómo hacerlo" paso a paso.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA FINANCIERO (STORYTELLING DE DIBUJOS - LONG)
**Objetivo:** Crear un guion profundo, inmersivo y educativo de entre 70 y 95 escenas, estructurado de manera secuencial, para lograr una duración final de entre 12 y 15 minutos de alto valor y retención al estilo documental de YouTube.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook y Planteamiento [Primeras 12-15 escenas]:** DEBES usar el campo "hook" para la Escena 1 de forma literal. Presenta el problema del sistema o crisis financiera con gran empatía y contexto.
2. **Acto 2: El Desarrollo Psicológico y Solución [Escenas medias]:** Analiza el 'por qué' detrás del problema antes de dar la regla o estrategia. Usa storytelling inmersivo. Alterna la historia con explicaciones conceptuales y analogías ricas en detalle.
3. **Acto 3: El Payoff y Cierre [Últimas 12-15 escenas]:** Muestra la transformación de forma realista. Termina con un consejo rápido accionable y un CTA sutil: suscribirse, comentar su opinión o dar like.

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Narración:** Párrafos ricos, conversacionales y explicativos. Permite que cada escena desarrolle una idea completa y respire. Usa un tono analítico, magnético y reflexivo, propio de un ensayo en video. Evita saltar frenéticamente entre ideas cortas.
- **Secuencialidad:** Progresión lógica profunda: problema → empatía/psicología del error → revelación → ejemplo real/analogía profunda → plan de acción.
- **Fluidez y Retención:** Usa storytelling inmersivo abriendo preguntas conceptuales que inviten a la reflexión a lo largo del video.

### 🔵 REGLAS VISUALES
- **Miniatura (Thumbnail - YT Finanzas 2026):** DEBES generar un `thumbnail_prompt` diseñado para un CTR masivo imitando a los canales top de finanzas.
  1) **Sujeto:** El personaje debe tener expresiones exageradas, apuntando o interactuando visualmente (ej. comparando al "pobre" con el "rico", o mirándose a un espejo).
  2) **Texto Gigante (Obligatorio):** Incluye SIEMPRE una instrucción para dibujar un título impactante de 3 a 7 palabras en la imagen usando la regla de EXCEPCIÓN de idioma (Ej: "Giant bold text at the top that says 'VIVE MEJOR CON MENOS'").
  3) **Utilería y Flechas:** Usa utilería visual clara (alcancías, billetes, autos) e incluye flechas dibujadas a mano (thick hand-drawn arrows) apuntando a los objetos clave para dirigir la mirada del espectador.
  4) **Entorno/Fondo:** Fondos extremadamente limpios (generalmente blancos o neutros) para maximizar el contraste del texto y las flechas.
  5) **Estilo Visual:** El campo `style` DEBE ser: `"Premium high-quality 2D vector art style, clean flat background, giant bold typography, thick expressive character outlines, hand-drawn indicator arrows, high contrast YouTube thumbnail aesthetic."`
- **Protagonista:** Presencia consistente de un personaje principal stickman (dibujo de palitos) viviendo la historia o el tutorial en escenas clave.
- **Relación Imagen-Texto:** El `image_prompt` debe ilustrar visualmente el concepto de forma exacta. Lo que el espectador escucha debe verse en pantalla con claridad conceptual.
- **Pattern Interrupts:** Cambia con frecuencia de enfoque visual, composición y planos visuales (plano general, plano medio, infografías de stickmans, etc.) para reiniciar la atención del espectador de forma elegante.
- **Estilo (Sketch Stickman):** DEBES usar el campo `style` para generar imágenes con un estilo visual de cómic/sketch. La descripción en el campo `style` DEBE ser: `"Dynamic hand-drawn 2D webcomic sketch style, thick expressive black ink outlines, vibrant minimalist color palette for highlights, clean shading, white background with glowing accents."`.
- **Uso del Color:** Utiliza el color de forma estratégica para resaltar elementos educativos (ej: rojo para errores, verde para soluciones, gráficas claras) manteniendo siempre la estética de dibujo a mano.

### 🔴 ESTRUCTURA Y SALIDA
- **Extensión:** Entre 70 y 95 escenas de narración sustancial, manteniendo profundidad analítica.
- **Cierre:** Resolución reflexiva con un Llamado a la Acción (CTA) natural y poco agresivo.

### 🟠 IDIOMAS (ESTRICTO)
- **image_prompt:** DEBES generar todos los campos de `image_prompt` (subjects, environment, lighting, composition) en **INGLÉS**. EXCEPCIÓN: Si en el prompt pides que haya algún texto escrito o letrero dentro de la imagen, las palabras exactas a escribir DEBEN estar en **ESPAÑOL** (Ejemplo: "A sign that says 'DEUDAS'").
- **video_prompt:** DEBES generar todos los campos de `video_prompt` (motion, camera_movement, transition, duration_hint) en **INGLÉS**.
- **narration:** DEBES generar el campo `narration` en **ESPAÑOL LATINOAMERICANO**.
"""

AUDIO_PROMPT: str = """Narra el siguiente guion con una voz **muy carismática, enérgica y profundamente entretenida**. Debe sentirse como un video-ensayo dinámico y moderno de YouTube que te atrapa desde el primer segundo.

Estilo de actuación:
- Tono: Muy ameno, magnético y conversacional. Eres un experto compartiendo un gran secreto, pero lo haces con chispa, carisma y pasión.
- Ritmo: Dinámico y fluido. Ni muy lento ni muy acelerado. Usa silencios estratégicos SOLO antes de revelar datos impactantes, pero mantén la energía alta y entretenida el resto del tiempo.
- Énfasis: Dale mucho peso emocional a palabras como "trampa", "secreto", "libertad", "error" e "interés compuesto". Juega con las variaciones de volumen para que la narración nunca sea monótona.
- Emoción: Empieza con muchísima fuerza e intriga. Queremos que el espectador no pueda despegarse de la pantalla.
- No agregues sonidos, muletillas ni nada que no esté en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""


from pipeline.schemas import BaseIdea, CategoryHandler


class MindsetFinanceIdeaLong(BaseIdea):
    """
    Deep idea model for long-form financial mindset transformation stories.
    """
    IDEA_PROMPT = IDEA_PROMPT_MINDSET
    financial_problem: str
    mindset_shift: str
    key_principle: str


class StrategyFinanceIdeaLong(BaseIdea):
    """
    Deep idea model for long-form practical financial strategy videos.
    """
    IDEA_PROMPT = IDEA_PROMPT_ESTRATEGIA
    strategy_name: str
    common_mistake: str
    actionable_tip: str


class FinancesHandlerLong(CategoryHandler):
    """
    Specialized handler for Long Finance-themed videos.
    Encapsulates Mindset and Strategy finance variants for 10-minute content.
    """

    SCRIPT_PROMPT = SCRIPT_PROMPT
    idea_variants = [
        MindsetFinanceIdeaLong,
        StrategyFinanceIdeaLong,
    ]
