Edited untitled:Untitled-2
Edited untitled:Untitled-3
Edited data_don_carlor.json
Viewed data_don_carlor.json:25-67
Listed directory generate-videos-auto
Viewed README.md:1-96

Aquí tienes un resumen estructurado de cómo funciona el código y el flujo de generación de contenido en tu proyecto **AI-Content-Automation-Engine** (`generate-videos-auto`):

### 🧠 Arquitectura General: El Pipeline

El sistema funciona como una **línea de ensamblaje** automatizada. Toma una idea base (en texto) y la pasa de manera secuencial a través de 7 pasos modulares, integrando diferentes IAs en el proceso, hasta entregar un archivo de video (`.mp4`) listo para publicar.

Existen dos flujos principales (formatos):

- **Short (`short`)**: Optimizados para formato vertical (TikTok, Reels, Shorts).
- **Long (`long`)**: Optimizados para formato horizontal (YouTube tradicional).

---

### ⚙️ Los 7 Pasos de Generación (Content Generation Flow)

El motor principal ejecuta estos 7 módulos secuenciales:

1. **📝 Paso 1: Generar Guion (`step1`)**
   - **Cómo funciona:** El código lee un archivo CSV con "ideas" ubicado en `flows/resource/`. Luego le pide a un modelo LLM (como Claude o Gemini) que expanda esa idea hasta convertirla en un guion estructurado.
2. **🎨 Paso 2: Generar Imágenes (`step2`)**
   - **Cómo funciona:** La IA analiza el guion y genera _prompts_ visuales. Luego, solicita a un modelo de generación de imágenes (como Midjourney o DALL-E) los apoyos visuales para cada escena del guion.
3. **🎙️ Paso 3: Generar Audio (`step3`)**
   - **Cómo funciona:** Se usa un modelo Text-to-Speech (TTS) (como ElevenLabs o similar) para convertir el texto del guion en un archivo de voz de alta calidad. _(Nota: En los shorts, el audio se acelera mediante la constante `SHORT_AUDIO_SPEEDUP` que ajustamos a 1.10)._
4. **🎞️ Paso 4: Ensamblar Video Base (`step4`)**
   - **Cómo funciona:** Usando **FFmpeg** a través de Python, se concatenan las imágenes generadas y se ajusta su duración de forma dinámica para sincronizarse con el largo de la pista de voz.
5. **🔤 Paso 5: Generar Subtítulos (`step5`)**
   - **Cómo funciona:** Se realiza una transcripción exacta (con tiempos/marcas) del audio generado, y el sistema superpone texto animado sobre el video para facilitar la retención del espectador.
6. **🎵 Paso 6: Añadir Música (`step6`)**
   - **Cómo funciona:** El código incrusta una pista musical de fondo, balanceando los niveles de volumen entre la música y la locución principal.
7. **✅ Paso 7: Finalizar y Exportar (`step7`)**
   - **Cómo funciona:** El archivo es renombrado y empaquetado en una carpeta definitiva con su propio ID único dentro de `flows/out_short/` o `flows/out_long/`.

---

### 💻 Modos de Ejecución (CLI)

Todo el proyecto está orquestado desde la terminal (`cli.py` o los comandos del `Makefile`), lo que permite 3 formas clave de operar:

- **Modo Manual (Por Paso):** Ejecutar un solo paso (Ej. `make icg-s-step1` para crear solo el guion).
- **Modo Automático (`all`):** Un bucle infinito. El script toma una idea, ejecuta los pasos del 1 al 7 y luego continúa automáticamente con la siguiente idea de la lista. (Ej. `make icg-l-all`).
- **Modo Reparación (`fixed`):** Si un video falló en el Paso 3 por falta de créditos o error de API, este modo (`make icg-s-fixed`) encuentra todos los proyectos incompletos y los retoma exactamente desde donde se quedaron.

### 📂 Gestión de Estado

El código está diseñado de forma robusta. Cada ejecución guarda sus salidas intermedias (texto, mp3, mp4, json) en la subcarpeta del proyecto (dentro de `out_short` u `out_long`). Esto es lo que le permite al sistema saber en qué paso va cada video y retomar trabajos caídos sin tener que regenerar los archivos (y gastar créditos) desde cero.

---

### 🎙️ Configuración de Canales y Prompts

Las personalidades de los videos, estilos de voz y las reglas de redacción no están fijadas en la lógica central, sino que están extraídas en configuraciones de "canales".

Todas las definiciones de los prompts (guiones, ideas y audio) se encuentran centralizadas en el directorio `pipeline/channels/`. Dentro de esta carpeta, hay archivos separados para distintos formatos (cortos o largos) y temáticas (canales), por ejemplo:

- **Finanzas:**
  - `finances_short.py`: Configura los prompts y voces para contenido vertical sobre finanzas (ritmo rápido, dinámico).
  - `finances_long.py`: Configura el estilo para videos horizontales (más pausado, educativo, con mayor profundidad).
- **Tío Warren:**
  - `tio_warren_short.py`: Define el estilo vertical del personaje "Tío Warren" (paternal, autoritario pero accesible).
  - `tio_warren_long.py`: Define el estilo horizontal para el mismo personaje.

**¿Qué contiene cada archivo de canal?**
Dentro de estos archivos se declaran como constantes (cadenas de texto) los prompts maestros que luego se envían a las IAs:
1. `AUDIO_PROMPT`: Le indica al modelo TTS (Text-to-Speech) el tono, el ritmo y la emoción de la voz (ej. hacer pausas, sonar enérgico).
2. `IDEA_PROMPT_*`: Define cómo se deben desarrollar conceptualmente las ideas (ej. "Generar una idea con un gancho fuerte y un problema cotidiano").
3. `SCRIPT_PROMPT`: El prompt guionista. Es extenso e instruye al LLM sobre cómo estructurar el guion completo, dividir la historia en Actos (1, 2, 3), escribir descripciones para las imágenes (prompts visuales) y aplicar reglas de retención de audiencia.

**¿Cómo se orquesta todo?**
El archivo `pipeline/prompt_manager.py` actúa como el administrador central. Determina qué temática y formato se están ejecutando, importa dinámicamente las constantes desde el archivo correspondiente en `pipeline/channels/` e inyecta las variables necesarias (como el texto de la idea base) dentro de los prompts antes de realizar las llamadas a la IA (Gemini, Claude, ElevenLabs, etc.).

---

### 📄 Código de los Archivos de Canal

#### 1. `pipeline/channels/finances_short.py`
```python
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
```

#### 2. `pipeline/channels/finances_long.py`
```python
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
    AUDIO_PROMPT = AUDIO_PROMPT
    """
    Specialized handler for Long Finance-themed videos.
    Encapsulates Mindset and Strategy finance variants for 10-minute content.
    """

    SCRIPT_PROMPT = SCRIPT_PROMPT
    idea_variants = [
        MindsetFinanceIdeaLong,
        StrategyFinanceIdeaLong,
    ]
```

#### 3. `pipeline/channels/tio_warren_short.py`
```python
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
2. **El Sobrino:** El joven impulsivo con sudadera verde obsesionado con dinero fácil.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto que exponga un error cotidiano de dinero (ej. "Esta tontería al pagar con tarjeta de crédito te mantiene pobre").
2. **Historia Rápida:**
   - El Sobrino comete un error financiero típico en un día normal.
   - El Tío Warren lo detiene y le da un 'hack' mental de riqueza rápido para corregirlo.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (ESTRATEGIA - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Generar una propuesta estructurada para un video corto que enseñe un atajo o regla de riqueza práctica con nuestros personajes.

**Personajes Obligatorios:**
1. **Tío Warren (El Mentor):** El experto calmado y calculador.
2. **El Sobrino:** El joven con hoodie verde que busca el camino fácil.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras sobre un life hack financiero rápido (ej. "El truco legal de los ricos para no pagar impuestos que tú no usas").
2. **Concepto central:** Una táctica concreta (Ley de Pareto, inflación de estilo de vida, regla de las 72 horas). El Tío Warren le muestra al Sobrino cómo implementarlo paso a paso con números rápidos.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA PREMIUM (DIVERSIÓN Y VIRALIDAD - CÓDIGO CAPITAL SHORTS)
**Objetivo:** Crear un guion de Shorts ultra-dinámico de 18 a 24 micro-escenas, enfocado en "Código Capital" y la dupla Tío Warren y el Sobrino, garantizando una duración de 1.5 a 2 minutos.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook/Conflicto [Escenas 1-5]:** DEBES usar el campo "hook" para la Escena 1 de forma literal. Muestra al Sobrino cometiendo un grave error o alardeando de su mentalidad de dinero rápido. El Tío Warren aparece para detenerlo.
2. **Acto 2: El Micro-Storytelling [Escenas 6-18]:** El Tío Warren explica de forma simple el truco, la regla o la matemática del hack financiero. Muestra comparativas visuales rápidas (lo que hace la gente común vs lo que hacen los ricos).
3. **Acto 3: El Educational Payoff [Escenas 19-final]:** Muestra al Sobrino aplicando el hack y su cara de satisfacción. Termina con un consejo rápido del Tío Warren y un llamado a la acción (CTA) OMNICANAL. En su lugar, usa llamados como: "Dale like, Síguenos en Código Capital para más", "Guarda este video", "Comparte esto con tu amigo" o "Comenta qué opinas".

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Narración:** Frases cortas, punchy y dinámicas. Considera que la voz del Tío Warren es grave, mayor y autoritaria, por lo que las oraciones deben ser sumamente directas para no perder la velocidad y retención del Short. Tío Warren es el mentor pragmático; el Sobrino es expresivo y cómico.
- **Fluidez:** Ritmo rápido adaptado para la alta retención en Shorts.

### 🔴 TOQUE HUMANO Y NARRADOR ÚNICO
- **Narrador Único:** Tío Warren es el ÚNICO que habla. Nunca hay diálogos entre personajes. Él relata las acciones de su Sobrino como una anécdota (Ej: "Mi sobrino vino a mí pensando que...").
- **Pacto Parasocial:** Llama a la audiencia "Sobrino" de forma directa para generar conexión (Ej: "Escucha bien esto, sobrino...").
- **Punto de Vista Fuerte:** Toma posturas polarizantes. Critica los consejos financieros tradicionales o las "trampas de la Matrix".
- **Datos Reales:** Cita brevemente reglas matemáticas o principios reales para darle autoridad instantánea.

### 🔵 REGLAS VISUALES (ESTRICTO)
- **Miniatura (Thumbnail - YT Código Capital):** DEBES generar un `thumbnail_prompt` optimizado para CTR masivo:
  1) **Personajes:** Tío Warren (pato anciano sabio, traje azul a rayas, lentes en el pico, plumas blancas) con expresión seria y apuntando a una pizarra, al lado del Sobrino (pato joven verde, sudadera negra con logo de Bitcoin, gorra negra) con expresión de absoluta sorpresa o desesperación.
  2) **Texto Gigante (Obligatorio):** Un título de 3 a 7 palabras impactantes dibujado en la imagen (Ej: "EL HACK DEL DINERO").
  3) **Utilería y Flecha:** Usa una flecha dibujadas a mano y utilería (monedas, tarjetas).
  4) **Estilo Visual:** `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background, high contrast YouTube thumbnail aesthetic."`
- **Consistencia de Personajes (MANDATORIO en todas las escenas):**
  - **Tío Warren:** Siempre debe ser descrito exactamente como: `"wise, distinguished 60-year-old white duck character, white feathers, wearing glasses on his bill, a sharp navy blue pinstripe suit, a white dress shirt, and a yellow-orange tie, calm and authoritative posture"`.
  - **El Sobrino:** Siempre debe ser descrito exactamente como: `"22-year-old young green duck character, green feathers, wearing a black casual hoodie with a golden Bitcoin logo on the front, wearing a black baseball cap, looking confused or expressive"`.
- **Estilo de Ilustración Global:** El campo `style` de las escenas DEBE ser estrictamente: `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background."`
- **Relación Imagen-Texto:** Cada escena debe traducir visualmente lo que se escucha (ej: Tío Warren dividiendo un pastel en partes para explicar presupuesto).

### 🔴 IDIOMAS
- **image_prompt:** Todos los campos de descripción visual (subjects, environment, lighting, composition, style) en **INGLÉS**. Excepción: Los textos que deban aparecer físicamente dibujados en la imagen deben estar en **ESPAÑOL** (Ej: "A sign that says 'EMERGENCIA'").
- **video_prompt:** Todos los campos (motion, camera_movement, transition, duration_hint) en **INGLÉS**.
- **narration:** El campo de voz en off en **ESPAÑOL LATINOAMERICANO**.

TU IDEA DE BASE (CONTEXTO EN JSON):
{idea_context_json}

"""


from pipeline.schemas import BaseIdea, CategoryHandler


class MindsetTioWarrenIdeaShort(BaseIdea):
    """
    Idea model for financial mindset transformation shorts featuring Tio Warren.
    """
    IDEA_PROMPT = IDEA_PROMPT_MINDSET
    financial_problem: str
    mindset_shift: str
    key_principle: str


class StrategyTioWarrenIdeaShort(BaseIdea):
    """
    Idea model for practical financial strategy shorts featuring Tio Warren.
    """
    IDEA_PROMPT = IDEA_PROMPT_ESTRATEGIA
    strategy_name: str
    common_mistake: str
    actionable_tip: str


class TioWarrenHandlerShort(CategoryHandler):
    AUDIO_PROMPT = AUDIO_PROMPT
    """
    Specialized handler for Short videos themed around Tio Warren for Código Capital.
    Encapsulates Mindset and Strategy finance variants.
    """

    SCRIPT_PROMPT = SCRIPT_PROMPT
    idea_variants = [
        MindsetTioWarrenIdeaShort,
        StrategyTioWarrenIdeaShort,
    ]
```

#### 4. `pipeline/channels/tio_warren_long.py`
```python
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
    AUDIO_PROMPT = AUDIO_PROMPT
    """
    Specialized handler for Long videos themed around Tio Warren for Código Capital.
    Encapsulates Mindset and Strategy finance variants.
    """

    SCRIPT_PROMPT = SCRIPT_PROMPT
    idea_variants = [
        MindsetTioWarrenIdeaLong,
        StrategyTioWarrenIdeaLong,
    ]
```
