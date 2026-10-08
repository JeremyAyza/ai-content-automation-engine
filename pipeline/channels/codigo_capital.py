# flake8: noqa: E501

# ============================================================================

# NUEVO CANAL: CÓDIGO CAPITAL

# Ubicación: pipeline/channels/codigo_capital.py

#

# Cambios clave respecto a tio*warren*\*.py (que se conserva intacto como legacy):

# 1. Personajes HUMANOS, no patos — resuelve el problema de anatomía

# inconsistente (manos/alas/patas) que baja la calidad visual.

# 2. Regla de "CERO DESVIACIÓN" explícita — evita que el guion se vaya

# de la idea base a temas no relacionados (el bug que describiste

# con "10 consejos tarjeta" -> terminaba hablando de ingresos pasivos).

# 3. Shorts calibrados al ritmo de "Hackea tu Riqueza" (dinámico, rápido,

# un narrador, sin auto-referencias al canal).

# 4. Largos calibrados al ritmo de "Don Carlos Invierte" pero limitados

# a 12-15 min (no 30), formato seminario con storytelling matemático.

# 5. Categorización Mindset/Estrategia ya no es aleatoria "porque sí":

# ver nota en CodigoCapitalHandler más abajo.

#

# Este canal NO reemplaza tio_warren_short.py / tio_warren_long.py.

# Es un archivo nuevo, independiente, que puedes activar en paralelo.

# ============================================================================

# ============================================================================

# SHORTS — CÓDIGO CAPITAL

# ============================================================================

AUDIO_PROMPT_SHORT: str = """Narra el siguiente guion sobre finanzas personales con una voz **muy enérgica, rápida y estimulante**, como un creador moderno de educación financiera en TikTok o Reels.

Estilo de actuación:

- Tono: Educativo pero con chispa y urgencia. Suenas como alguien que te está salvando de un error, no como un profesor.
- Ritmo: Rápido y dinámico, nativo de Shorts. Pausas mínimas, solo para enfatizar el dato clave.
- Énfasis: Sube energía en palabras como "error", "trampa", "regla", "ahorro", "interés compuesto".
- Emoción: Arranca con fuerza total en la primera frase. Mantén la energía alta hasta el cierre.
- No agregues sonidos ni muletillas. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_MINDSET_SHORT: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (MENTALIDAD - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Generar una propuesta para un short que exponga un error de mentalidad financiera cotidiano y lo corrija.

**Contexto del canal:**

- Código Capital: educación financiera dinámica, un mentor (Tío Warren) que habla directo a la audiencia.
- Formato: 60-90 segundos, ritmo veloz.

**Instrucciones:**

1. **hook (Gancho):** Frase de 10-15 palabras que exponga un error cotidiano de forma directa.
   Ej: "Esta tontería al pagar con tarjeta de crédito te mantiene pobre"
2. **Situación:** Describe brevemente el error común (una persona cualquiera, sin necesidad de nombrarla como personaje recurrente).
3. **Corrección:** El cambio de mentalidad o hábito que lo resuelve, explicado en 1 idea clara — no una lista de 5 cosas distintas.
   """

IDEA_PROMPT_ESTRATEGIA_SHORT: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (ESTRATEGIA - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Generar una propuesta para un short que enseñe una táctica financiera concreta y aplicable hoy mismo.

**Contexto del canal:**

- Código Capital: mentor pragmático, números reales, sin rodeos.
- Formato: 60-90 segundos, ritmo veloz.

**Instrucciones:**

1. **hook (Gancho):** Frase de 10-15 palabras sobre una táctica o atajo poco conocido.
   Ej: "El truco legal que usan los que sí ahorran y tú no"
2. **Concepto:** Una regla concreta y accionable (ej: regla del 50/30/20, automatizar el ahorro, la trampa del mínimo de tarjeta).
3. **Pasos:** Cómo aplicarlo hoy, en máximo 3 pasos, con un número o ejemplo real si aplica.
   """

SCRIPT_PROMPT_SHORT: str = """# 📝 PROMPT MAESTRO — GUIONISTA CÓDIGO CAPITAL (SHORTS)
**Objetivo:** Crear un guion de 20 a 25 micro-escenas para un short (aprox 70-90 seg, apuntando a un promedio de 80 segundos / 1min20), enfocado ÚNICAMENTE en la idea base, con el ritmo veloz y dinámico de un short de finanzas viral.

## 🟢 REGLA DE ORO: CERO DESVIACIÓN (la más importante de este prompt)

La idea base es SAGRADA y es la ÚNICA idea que se desarrolla en todo el guion.

- Si la idea es "10 consejos para usar tu tarjeta de crédito", CADA escena debe tratar sobre tarjetas de crédito.
- PROHIBIDO introducir conceptos no solicitados (ingresos pasivos, criptomonedas, inversión en bolsa, etc.) aunque parezcan "relacionados" — si no estaban en la idea base, no entran al guion.
- Antes de generar la escena N, verifica mentalmente: "¿esto sigue hablando exactamente del tema de la idea base?". Si la respuesta es no, corrige.

## 🎬 ESTRUCTURA OBLIGATORIA

**Acto 1 — Hook [Escenas 1-5]**

- Escena 1: usa el campo "hook" de forma literal.
- Presenta el problema/error de forma directa, sin preámbulo.

**Acto 2 — Desarrollo [Escenas 5-22]**

- Explica el concepto central de la idea base, y SOLO ese concepto.
- Si la idea trae varios puntos (ej. "10 consejos"), cada punto es su propia escena corta — no los mezcles ni te extiendas filosofando sobre uno solo.
- Comparaciones visuales rápidas ("esto es lo que hace la mayoría" vs "esto es lo correcto").
- Frases de 8 a 14 palabras por escena (NUNCA menos de 8) — es el rango que, narrado a ritmo enérgico, dura 3-5 segundos y ayuda a cerrar el short cerca de 1min20 con 20-25 escenas. Una escena de 4-6 palabras dura ~2 segundos y rompe el ritmo objetivo.

**Acto 3 — Cierre [Escenas 22-final]**

- Remata con una frase memorable ligada directamente al tema (no una moraleja genérica de "ahorra más").
- CTA estrategico: "Dale like y comparte para que recibas mas ingresos", "Sígueme para no perderte mas consejos financieros", "Comparteselo a tu primer compartido de Whatsapp", "Eviale este video a ese amigo o familiar que siempre le falta dinero" "Guarda esto video", "Compartelo a esa persona que sabes que necesita oirlo", "Cuéntame en comentarios si te pasó esto".

## 🔴 NARRACIÓN

1. **Narrador único:** habla directo a cámara/audiencia, en segunda persona ("tú", o si usas apodo, consistente en todo el canal — ej. "amigo" o el que definas).
2. **Ritmo de short real:** nada de introducciones largas. Al segundo 2 ya debe estar el gancho.
3. **Sin auto-referencias al canal** dentro del short (no digas "en mi canal ya hablé de esto") — rompe la inmersión rápida que necesita un short.

## 🔵 REGLAS VISUALES (CRÍTICO: CONTENIDO > ESTILO)

Estilo calibrado al rendimiento visual de "Hackea tu Riqueza" (personaje expresivo, un color de acento, poses exageradas, cómic) en vez del estilo plano/corporativo anterior. Prioriza el "Qué" (contenido) y dirige el "Cómo" (estilo) hacia un lenguaje de cómic/sketch dinámico.

### 1. El "Qué" (Contenido Súper Detallado, con pose y gesto obligatorios)
- **Mentor (Tío Warren):** `older man with round glasses and grey hair, wearing a navy blue pinstripe suit, thick expressive comic-style outlines, exaggerated body language matching the scene's emotion (pointing, leaning forward, arms wide open, jumping, reacting with shock or triumph)`
- **Aprendiz (Sobrino):** `young man in a black hoodie, blue jeans, and black baseball cap, exaggerated comic-style body language matching the scene's emotion`
- **Pose obligatoria por escena:** describe siempre una pose/gesto específico y exagerado (ej. `pointing directly at the falling price tag`, `covering his face in shock`, `crossing his arms confidently`, `jumping with excitement holding coins`) — nunca una pose neutra tipo "standing" por defecto.
- **Dirección de mirada/gesto:** el personaje mira o señala hacia el elemento clave de la escena (el número, el error, el objeto) para guiar el ojo del espectador.
- **Entorno/Objetos:** Sé extremadamente literal (Ej. `holding a glowing golden coin`, `standing next to a giant rising line chart`). Varía el fondo/escenario entre escenas (oficina, calle, casa, banco, tienda) — evita repetir el mismo fondo o la misma pose en 2+ escenas seguidas.

### 2. El "Cómo" (Estilo Cómic/Sketch Obligatorio)
Usa ÚNICAMENTE esta plantilla exacta en el campo de estilo para todas las escenas:

```
"Dynamic hand-drawn 2D webcomic sketch style, thick expressive black ink outlines, vibrant minimalist color palette for highlights, clean shading, white background with glowing accents."
```

- **Un solo color de acento por escena:** elige UN color dominante con significado (rojo = error/alerta, verde = ahorro/solución, dorado = logro/premio) sobre fondo blanco/neutro — nunca una paleta completa compitiendo por atención.

### 3. Thumbnail (Miniatura) — optimizada para CTR
- Mentor en primer plano con expresión y pose exagerada, comparando o señalando (ej. "antes vs después", "el que ahorra vs el que no").
- Texto GIGANTE en negro (3-7 palabras) integrado como elemento gráfico del diseño, no como etiqueta pegada encima.
- Flechas gruesas dibujadas a mano apuntando al elemento clave.
- Fondo blanco o neutro extremadamente limpio para maximizar contraste (thumbnail-safe: debe leerse a tamaño de miniatura pequeña).
- Style: `"Premium high-quality 2D vector art style, clean flat background, giant bold typography, thick expressive character outlines, hand-drawn indicator arrows, high contrast YouTube thumbnail aesthetic."`

### Sincronía:

- Cada imagen ilustra literalmente lo que se narra en ese momento (no metáforas abstractas difíciles de generar).
- Cambio visual cada 3-5 segundos para mantener el ritmo de short.
- Varía composición, fondo y pose constantemente — nunca 3+ escenas seguidas con el mismo fondo/pose.

## 🟣 AUTO-CHEQUEO DE DURACIÓN (OBLIGATORIO ANTES DE ENTREGAR)

Antes de finalizar el guion, cuenta el total de palabras de todas las narraciones sumadas y divide entre 2.6 (palabras/segundo a ritmo enérgico):

`total_palabras ÷ 2.6 = duración estimada en segundos`

- Debe caer entre 70 y 90 segundos, apuntando a un promedio de 80 segundos (1min20).
- Si da MENOS de 70: **alarga las narraciones existentes** (más detalle, más contexto en cada frase) — NUNCA agregues más escenas para compensar, eso rompe el ritmo y diluye el foco.
- Si da MÁS de 90: recorta palabras por escena, no elimines escenas completas si rompe la progresión lógica.

## 🟠 IDIOMAS (ESTRICTO)

- **image_prompt:** INGLÉS (subjects, environment, lighting, composition, style). Excepción: texto dibujado dentro de la imagen → ESPAÑOL.
- **video_prompt:** INGLÉS (motion, camera_movement, transitions).
- **narration:** ESPAÑOL LATINOAMERICANO.

## 📊 SALIDA

- 20-25 escenas | 70-90 segundos (promedio 80) | 8-14 palabras por escena | ritmo alto | cero relleno | cero desviación del tema.

TU IDEA BASE:
{idea_context_json}
"""

# ============================================================================

# LARGOS — CÓDIGO CAPITAL

# ============================================================================

AUDIO_PROMPT_LONG: str = """Narra el siguiente guion con una voz **carismática, seria pero cercana, y muy magnética**. Debe sentirse como un seminario o video-ensayo de un mentor financiero experimentado que capta la atención desde el primer segundo.

Estilo de actuación:

- Tono: Ameno, reflexivo, con autoridad — no acartonado. Como alguien que ya vivió lo que está enseñando.
- Ritmo: Fluido y pausado donde corresponde, pero sin perder energía. Usa silencios breves antes de revelar un dato importante.
- Énfasis: Peso emocional en palabras como "trampa", "libertad", "error", "tiempo", "interés compuesto".
- Emoción: Arranca con intriga real, no con relleno. El espectador debe querer saber qué sigue.
- No agregues sonidos ni muletillas. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_MINDSET_LONG: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (MENTALIDAD - CÓDIGO CAPITAL LONG)
**Objetivo:** Generar una propuesta para un video largo (10-15 min) sobre una transformación de mentalidad financiera, con profundidad real (no superficial).

**Contexto del canal:**

- Código Capital: seminario educativo, mentor (Tío Warren) enseñando a un aprendiz o directamente a la audiencia.
- Formato: 10-15 minutos, estilo seminario/ensayo (inspirado en Don Carlos Invierte, pero más compacto).

**Instrucciones:**

1. **hook:** Frase de 10-15 palabras que exponga una verdad incómoda o contraintuitiva.
   Ej: "La verdad incómoda de por qué ahorrar dinero no te está haciendo rico"
2. **Pilares:** Define 2-3 pilares/bloques que desarrollarán la idea (no más — con 10-15 min no alcanza para 5 pilares bien explicados).
3. **Caso práctico:** Un ejemplo con números reales o comparativa (Persona A vs Persona B) que ilustre el pilar central.
   """

IDEA_PROMPT_ESTRATEGIA_LONG: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (ESTRATEGIA - CÓDIGO CAPITAL LONG)
**Objetivo:** Generar una propuesta para un video largo (10-15 min) que desglose con números reales una decisión o estrategia financiera concreta.

**Contexto del canal:**

- Código Capital: análisis serio con storytelling matemático.
- Formato: 10-15 minutos.

**Instrucciones:**

1. **hook:** Frase de 10-15 palabras sobre una trampa financiera oculta en una decisión cotidiana.
   Ej: "Por qué pagar de contado te puede costar más caro de lo que crees"
2. **Comparativa central:** Define el Caso A vs Caso B que se va a desarrollar con números a 5-10 años.
3. **Estrategia final:** La conclusión práctica que el espectador puede aplicar esta semana.
   """

SCRIPT_PROMPT_LONG: str = """# 📝 PROMPT MAESTRO — GUIONISTA CÓDIGO CAPITAL (VIDEOS LARGOS)
**Objetivo:** Crear un guion denso y magnético de 55-70 escenas para un video de 10-15 minutos (NO 30 — esto es más compacto que Don Carlos, mismo nivel de profundidad, menos relleno), enfocado ÚNICAMENTE en la idea base.

## 🟢 REGLA DE ORO: CERO DESVIACIÓN

La idea base es SAGRADA. Todo el guion desarrolla exclusivamente esa idea.

- Máximo 2-3 pilares/bloques temáticos — no más. Con 10-15 min, más de 3 pilares obliga a superficialidad.
- Cada vez que introduzcas un dato o ejemplo nuevo, verifica que sirve directamente al pilar que estás desarrollando, no es una tangente interesante pero irrelevante.

## 🎬 ESTRUCTURA OBLIGATORIA

**Acto 1 — Hook + Tesis [Escenas 1-8]**

- Escena 1: usa el campo "hook" literal.
- Plantea la premisa central con un contraste fuerte (Ej: "Piensa en alguien que gana lo mismo que tú pero nunca se preocupa por dinero...").
- Rompe la 4ta pared dirigiéndote directo a quien ve el video — esto SÍ funciona en formato largo (a diferencia del short).

**Acto 2 — Desarrollo por Pilares [Escenas 9-55]**

- Cada pilar: Problema → Por qué pasa (psicología o contexto) → Ejemplo con números reales → Conclusión tajante.
- **Storytelling matemático obligatorio:** usa personas hipotéticas con cifras concretas.
  Ej: "Martín gana $2,000 al mes y gasta $1,900. Sofía gana lo mismo y gasta $1,500. A 10 años, Martín tiene $0 ahorrado. Sofía tiene $60,000."
- Cada pilar cierra con una frase-conclusión corta y memorable (tu "verdad tajante" de cierre de bloque) — dale un formato consistente en todo el canal, por ejemplo: "Y ahí está la diferencia: no es cuánto ganas, es cuánto te quedas."
- Alterna párrafos explicativos más largos con frases cortas de remate para variar el ritmo.
- Rango de palabras por escena: 15-40 palabras (las de remate/conclusión pueden ser más cortas, 8-12 palabras, pero no la mayoría del guion) — evita que el promedio caiga muy bajo, o el video terminará muy por debajo de los 10-15 minutos aunque el número de escenas sea correcto.

**Acto 3 — Síntesis + Cierre [Escenas 56-final]**

- Conecta los pilares en una sola idea final.
- Da un paso concreto y pequeño para aplicar esta semana (no una lista larga).
- CTA natural, no agresivo: invita a comentar qué van a aplicar, o a compartir si les sirvió.

## 🔴 NARRACIÓN

1. **Narrador único**, dirigiéndose en segunda persona a la audiencia. Sin diálogos entre personajes — si aparece un aprendiz, es ilustrativo/visual, no un interlocutor que habla en el audio.
2. **Autoridad + cercanía:** serio pero no acartonado. Es alguien que ya vivió el problema, no un profesor leyendo un libro.
3. **Datos con verosimilitud:** puedes citar cifras de estudios o instituciones conocidas para dar peso, siempre que sea razonable y no inventes fuentes específicas falsas con nombre y apellido.
4. **Auto-referencias permitidas aquí (a diferencia del short):** en formato largo sí puedes mencionar de forma breve que esto es parte de una serie o que hay más contenido relacionado — pero sin que se sienta como publicidad forzada.

## 🔵 REGLAS VISUALES (CRÍTICO: CONTENIDO > ESTILO)

Estilo calibrado al rendimiento visual de "Hackea tu Riqueza" (personaje expresivo, un color de acento, poses exageradas, cómic) en vez del estilo plano/corporativo anterior. Prioriza el "Qué" (contenido) y dirige el "Cómo" (estilo) hacia un lenguaje de cómic/sketch dinámico. En formato largo modera la exageración frente al short (menos "cómic puro", más "ilustración editorial con carácter"), pero mantén siempre pose y gesto específicos, nunca neutros.

### 1. El "Qué" (Contenido Súper Detallado, con pose y gesto obligatorios)
- **Mentor (Tío Warren):** `older man with round glasses and grey hair, wearing a navy blue pinstripe suit, thick expressive comic-style outlines, deliberate body language matching the scene's emotion (gesturing while explaining, leaning forward with authority, reacting with concern or satisfaction)`
- **Aprendiz (Sobrino):** `young man in a black hoodie, blue jeans, and black baseball cap, expressive body language matching the scene's emotion`
- **Pose obligatoria por escena:** describe siempre una pose/gesto específico (ej. `pointing at a rising chart with confidence`, `sitting thoughtfully at a desk with a calculator`, `comparing two piles of coins side by side`) — nunca una pose neutra tipo "standing" por defecto.
- **Dirección de mirada/gesto:** el personaje mira o señala hacia el elemento clave de la escena (el número, la comparativa, el dato) para guiar el ojo del espectador.
- **Entorno/Objetos:** Sé extremadamente literal (Ej. `holding a glowing golden coin`, `standing next to a giant rising line chart`, `a wooden desk`). Varía el fondo/escenario entre escenas (oficina, casa, banco, calle) — evita repetir el mismo fondo o la misma pose en escenas consecutivas.

### 2. El "Cómo" (Estilo Cómic/Sketch Obligatorio)
Usa ÚNICAMENTE esta plantilla exacta en el campo de estilo para todas las escenas:

```
"Dynamic hand-drawn 2D webcomic sketch style, thick expressive black ink outlines, vibrant minimalist color palette for highlights, clean shading, white background with glowing accents."
```

- **Un solo color de acento por escena:** elige UN color dominante con significado (rojo = error/riesgo, verde = ahorro/solución, dorado = logro/resultado) sobre fondo blanco/neutro — nunca una paleta completa compitiendo por atención.

### 3. Thumbnail (Miniatura) — optimizada para CTR
- Mentor en primer plano con expresión y pose marcada, comparando o señalando (ej. "antes vs después", persona A vs persona B).
- Texto GIGANTE en negro (3-7 palabras) integrado como elemento gráfico del diseño, no como etiqueta pegada encima.
- Flechas gruesas dibujadas a mano apuntando al elemento clave.
- Fondo blanco o neutro extremadamente limpio para maximizar contraste (thumbnail-safe: debe leerse a tamaño de miniatura pequeña).
- Style: `"Premium high-quality 2D vector art style, clean flat background, giant bold typography, thick expressive character outlines, hand-drawn indicator arrows, high contrast YouTube thumbnail aesthetic."`

### Sincronía:

- Cada imagen ilustra literalmente el ejemplo o dato que se narra en ese momento.
- Cambios visuales cada 15-20 segundos (más pausado que el short, pero sin escenas estáticas largas ni fondos repetidos).

## 🟣 AUTO-CHEQUEO DE DURACIÓN (OBLIGATORIO ANTES DE ENTREGAR)

Antes de finalizar el guion, cuenta el total de palabras de todas las narraciones sumadas y divide entre 2.3 (palabras/segundo a ritmo pausado-magnético, más lento que el short):

`total_palabras ÷ 2.3 = duración estimada en segundos`

- Debe caer entre 600 y 900 segundos (10-15 min).
- Si da MENOS de 600: **alarga las narraciones existentes** (más desarrollo por pilar, más ejemplos con números) — NUNCA agregues escenas nuevas fuera de los pilares definidos para compensar.
- Si da MÁS de 900: recorta palabras dentro de cada escena, prioriza cortar relleno antes que ejemplos con cifras.

## 🟠 IDIOMAS (ESTRICTO)

- **image_prompt:** INGLÉS. Excepción: texto dibujado dentro de la imagen → ESPAÑOL.
- **video_prompt:** INGLÉS.
- **narration:** ESPAÑOL LATINOAMERICANO.

## 📊 SALIDA

- 55-70 escenas | 10-15 minutos | 15-40 palabras por escena | máximo 2-3 pilares | cero relleno filosófico | cero desviación del tema.

TU IDEA BASE:
{idea_context_json}
"""

# ============================================================================

# HANDLERS

# ============================================================================

#

# NOTA SOBRE LA CATEGORIZACIÓN (Mindset vs Estrategia):

# En el código legacy, el tipo se elegía al azar entre los dos. Funciona para

# variedad, pero puedes hacerlo más intencional sin tocar la lógica central:

# alterna manualmente en tu CSV de ideas una columna "categoria" con valores

# "mindset" o "estrategia" para cada idea, y que tu selector lea esa columna

# en vez de tirar un random — así decides tú qué ideas son de mentalidad

# (más reflexivas) y cuáles son de táctica concreta (más accionables),

# en vez de dejarlo al azar.

from pipeline.schemas import BaseIdea, CategoryHandler

class MindsetCodigoCapitalIdeaShort(BaseIdea):
    """Idea model for financial mindset transformation shorts for Codigo Capital."""
    IDEA_PROMPT = IDEA_PROMPT_MINDSET_SHORT
    financial_problem: str
    mindset_shift: str
    key_principle: str

class StrategyCodigoCapitalIdeaShort(BaseIdea):
    """Idea model for practical financial strategy shorts for Codigo Capital."""
    IDEA_PROMPT = IDEA_PROMPT_ESTRATEGIA_SHORT
    strategy_name: str
    common_mistake: str
    actionable_tip: str

class CodigoCapitalHandlerShort(CategoryHandler):
    """Specialized handler for Short videos themed around Codigo Capital."""
    AUDIO_PROMPT = AUDIO_PROMPT_SHORT
    SCRIPT_PROMPT = SCRIPT_PROMPT_SHORT
    idea_variants = [
        MindsetCodigoCapitalIdeaShort,
        StrategyCodigoCapitalIdeaShort,
    ]

class MindsetCodigoCapitalIdeaLong(BaseIdea):
    """Idea model for long-form financial mindset transformation stories for Codigo Capital."""
    IDEA_PROMPT = IDEA_PROMPT_MINDSET_LONG
    financial_problem: str
    mindset_shift: str
    key_principle: str

class StrategyCodigoCapitalIdeaLong(BaseIdea):
    """Idea model for long-form practical financial strategy videos for Codigo Capital."""
    IDEA_PROMPT = IDEA_PROMPT_ESTRATEGIA_LONG
    strategy_name: str
    common_mistake: str
    actionable_tip: str

class CodigoCapitalHandlerLong(CategoryHandler):
    """Specialized handler for Long videos themed around Codigo Capital."""
    AUDIO_PROMPT = AUDIO_PROMPT_LONG
    SCRIPT_PROMPT = SCRIPT_PROMPT_LONG
    idea_variants = [
        MindsetCodigoCapitalIdeaLong,
        StrategyCodigoCapitalIdeaLong,
    ]
