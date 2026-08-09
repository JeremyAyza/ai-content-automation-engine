# flake8: noqa: E501
IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (MENTALIDAD & PILARES - CÓDIGO CAPITAL)
**Objetivo:** Generar una propuesta estructurada para un video-ensayo educativo de 12-15 minutos sobre transformación de mentalidad, orden personal o filosofía financiera, listo para ser expandido en un despiece profundo por pilares o pasos.

**Personajes Visuales de Marca:**
1. **Tío Warren (El Mentor Pato):** Pato sabio de plumas blancas, traje azul marino a rayas, lentes en el pico y corbata amarilla. Representa la sabiduría, el rigor financiero y el orden.
2. **El Sobrino (Pato Verde):** Pato joven de plumas verdes, sudadera negra con logo dorado de Bitcoin y gorra negra. Representa a la audiencia: impulsivo, con dudas o buscando atajos.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto directo al espectador (ej. "El secreto que nadie te enseña para construir riqueza sin importar tu salario actual").
2. **Estructura en Bloques Analíticos/Pilares:**
   - Define la tesis central del tema (ej. El orden interior previo a la inversión).
   - Define los pilares, pasos o reglas clave a desglosar en el guion.
   - Define el caso práctico o analogía financiera con números o comparativas reales.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (ESTRATEGIA Y NÚMEROS REALEZ - CÓDIGO CAPITAL)
**Objetivo:** Generar una propuesta estructurada para un video-ensayo de 12-15 minutos que desglose con matemáticas reales y lógica práctica una decisión financiera (ej. Rentar vs Comprar, Ventas, Pagar de contado vs financiado).

**Personajes Visuales de Marca:**
1. **Tío Warren (El Mentor Pato):** Pato sabio de plumas blancas, traje azul marino a rayas, lentes en el pico y corbata amarilla.
2. **El Sobrino (Pato Verde):** Pato joven de plumas verdes, sudadera negra con logo de Bitcoin y gorra negra.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras sobre la trampa oculta de una decisión cotidiana (ej. "Por qué pagar de contado en la agencia te cuesta más caro de lo que crees").
2. **Estructura en Bloques Analíticos:**
   - Define la decisión o trampa del sistema a analizar.
   - Define la comparativa de números reales (Caso A vs Caso B a 5-10 años).
   - Define el método estratégico para maximizar la liquidez y el patrimonio.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA DE VIDEO-ENSAYOS PREMIUM (CÓDIGO CAPITAL)
**Objetivo:** Crear un guion educativo denso, magnético y de altísima retención de entre **62 y 81 escenas**, estructurado como una **Masterclass / Seminario (Estilo Seminario Fénix de Brian Tracy)** de 12 a 15 minutos.

## 📜 NARRACIÓN Y TONO (ESTRICTO Y MAGNÉTICO)
1. **El Tono del Seminario (Estilo Brian Tracy / Don Carlos):** La voz en off (Tío Warren) debe sentirse como un seminario magistral: serio, profundo, directo, lógico y sin rodeos. Habla directamente al espectador en segunda persona ("tú" o "sobrino"). Usa comas y puntos para forzar pausas dramáticas. No hay chistes baratos, hay verdades incómodas dichas con autoridad.
2. **CERO Diálogos de Ficción en el Audio:** Tío Warren es el ÚNICO que habla. Nunca hay diálogos.
3. **Storytelling Matemático (OBLIGATORIO):** Jamás enseñes teoría financiera de forma abstracta. TODO concepto debe ser ilustrado con historias de personajes hipotéticos usando **matemáticas reales**. (Ej: "Imagina a Mateo y a Sofía. Ambos ganan 18,000 dolares al mes... Mateo gasta 17,200..."). Contrasta agresivamente el Caso A vs Caso B a 5 o 10 años para demostrar el impacto del tiempo.
4. **Pacing y Retórica:** Alterna entre explicaciones detalladas (párrafos más largos) y axiomas muy cortos y tajantes que rompen el ritmo. (Ej: "El saldo no cambió, sobrino. El valor sí.").
5. **Autoridad Institucional:** Cita (o inventa con extrema verosimilitud) datos de instituciones reales (Ej: Banco Mundial, OCDE, INEGI, estudios conductuales de universidades) para darle un peso innegable a la premisa.
6. **Axiomas de Cierre (Regla del Tío Warren):** Cada pilar, paso o bloque analítico DEBE cerrar obligatoriamente con una conclusión tajante introducida así: "Regla del Tío Warren: [inserte la verdad incómoda aquí]".
7. **Estructura del Guion:**
   - **Introducción y Tesis (Escenas 1-10):** Arranca con el `hook` literal en la Escena 1 (estableciendo un contraste: "Piensa en alguien que siempre tiene dinero... Ahora piensa en alguien que gana lo mismo pero no le alcanza"). Tío Warren se presenta y plantea la premisa del video.
   - **Desglose de Pilares (Escenas 11-55):** Desarrolla el contenido usando el *Storytelling Matemático*. Cita datos institucionales. Termina cada pilar con su respectiva "Regla del Tío Warren".
   - **Recapitulación y Síntesis (Escenas 56-68):** Conecta todas las reglas demostrando cómo la riqueza opera en silencio.
   - **Cierre Reflexivo y Comunitario (Escenas 69-final):** Da un consejo maduro de implementación (ej. "Aplica solo una regla esta semana"). Pide a los "sobrinos" que comenten qué regla van a automatizar hoy.

## 🔵 REGLAS VISUALES (CADA ESCENA Y THUMBNAIL)
- **Miniatura (Thumbnail - YT Código Capital):** DEBES generar un `thumbnail_prompt` optimizado para CTR masivo (Estilo Minimalista):
  1) **Composición y Fondo:** Fondo BLANCO puro y muy limpio. Cero escenarios complejos, el foco debe ser el texto y una metáfora visual fuerte.
  2) **Texto Gigante (Obligatorio):** Un título de 3 a 6 palabras impactantes en letras ENORMES, NEGRAS, GRUESAS y en MAYÚSCULAS ocupando gran parte del espacio (Ej: "EL TIEMPO ES DINERO" o "APRENDE A VENDER").
  3) **Personajes y Metáfora Central:** El Tío Warren y el Sobrino interactuando con UNA SOLA utilería gigante y simbólica (Ej: un cerebro de engranajes, un reloj de arena enorme, una montaña de dinero, una agenda gigante).
  4) **Detalles (Hand-drawn):** Usa una flecha negras simples dibujadas a mano apuntando a la utilería o a la cara del Sobrino.
  5) **Estilo Visual:** `"Premium 2D cartoon vector style, clean outline, minimalist flat design, huge bold black typography, custom cute duck characters style, pure solid white background, high contrast YouTube thumbnail aesthetic."`
- **Consistencia de Personajes en `image_prompt`:**
  - **Tío Warren:** `"wise, distinguished 60-year-old white duck character, white feathers, wearing glasses on his bill, a sharp navy blue pinstripe suit, a white dress shirt, and a yellow-orange tie, calm and authoritative posture"`.
  - **El Sobrino:** `"22-year-old young green duck character, green feathers, wearing a black casual hoodie with a golden Bitcoin logo on the front, wearing a black baseball cap, looking confused or expressive"`.
- **Estilo de Ilustración Global:** El campo `style` de las escenas DEBE ser estrictamente: `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background."`
- **Rol de los Personajes en la Imagen:** Úsalos como **metáforas e ilustraciones visuales** de lo que dice la voz en off (Ej: si la narración habla de la agenda como presupuesto del tiempo, el Sobrino sostiene una agenda gigante mientras el Tío Warren señala un reloj de arena).

### 🔴 IDIOMAS
- **image_prompt:** Todos los campos de descripción visual (subjects, environment, lighting, composition, style) en **INGLÉS**. Excepción: Los textos que deban aparecer físicamente dibujados en la imagen deben estar en **ESPAÑOL** (Ej: "A folder labeled 'FIDEICOMISO'").
- **video_prompt:** Todos los campos (motion, camera_movement, transition, duration_hint) en **INGLÉS**.
- **narration:** El campo de voz en off en **ESPAÑOL LATINOAMERICANO**.

TU IDEA DE BASE (CONTEXTO EN JSON):
{idea_context_json}

"""

AUDIO_PROMPT: str = """Narra el siguiente guion con una voz **muy carismática, enérgica y profundamente entretenida**. Debe sentirse como un documental dinámico de YouTube que te atrapa desde el primer segundo.

Estilo de actuación:
- Tono: Muy ameno, magnético y conversacional. Eres un experto compartiendo un gran secreto, pero lo haces con chispa, carisma y pasión.
- Ritmo: Dinámico y fluido. Ni muy lento ni muy acelerado. Usa silencios estratégicos SOLO antes de revelar datos impactantes, pero mantén la energía alta y entretenida el resto del tiempo.
- Énfasis: Dale mucho peso emocional a palabras como "trampa", "secreto", "libertad", "error" e "interés compuesto". Juega con las variaciones de volumen para que la narración nunca sea monótona.
- Emoción: Empieza con muchísima fuerza e intriga. Queremos que el espectador no pueda despegarse de la pantalla.
- No agregues sonidos, muletillas ni nada que no esté en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""


from pipeline.schemas import BaseIdea, CategoryHandler


class MindsetTioWarrenIdeaLong(BaseIdea):
    """
    Deep idea model for long-form financial mindset transformation stories featuring Tio Warren.
    """
    IDEA_PROMPT = IDEA_PROMPT_MINDSET
    financial_problem: str
    mindset_shift: str
    key_principle: str


class StrategyTioWarrenIdeaLong(BaseIdea):
    """
    Deep idea model for long-form practical financial strategy videos featuring Tio Warren.
    """
    IDEA_PROMPT = IDEA_PROMPT_ESTRATEGIA
    strategy_name: str
    common_mistake: str
    actionable_tip: str


class TioWarrenHandlerLong(CategoryHandler):
    """
    Specialized handler for Long videos themed around Tio Warren for Código Capital.
    Encapsulates Mindset and Strategy finance variants.
    """

    SCRIPT_PROMPT = SCRIPT_PROMPT
    idea_variants = [
        MindsetTioWarrenIdeaLong,
        StrategyTioWarrenIdeaLong,
    ]
