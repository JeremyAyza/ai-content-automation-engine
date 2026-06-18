# flake8: noqa: E501
AUDIO_PROMPT: str = """Narra el siguiente guion sobre finanzas personales y educación financiera con una voz cinematográfica, clara, inspiradora y profesional, como el narrador de un documental de alta calidad o una masterclass de finanzas.

Estilo de actuación:
- Tono: Profesional, inspirador y empático. Debes sonar creíble, seguro y motivador.
- Ritmo: Moderado, fluido y natural. Permite que las ideas clave respiren con pausas sutiles y elegantes, manteniendo el interés y la tensión narrativa.
- Énfasis: Subraya con claridad e intención conceptos financieros importantes.
- Emoción: Transmite una evolución emocional desde la seriedad/preocupación del conflicto financiero inicial hasta el entusiasmo e inspiración de la resolución.
- No agregues sonidos, muletillas ni nada que no esté en el texto. Lee exactamente lo que aparece.

Texto a narrar:
{audio_text}"""

IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO MENTALIDAD - LONG)
**Objetivo:** Generar una idea profunda para un video largo (de 5 a 8 minutos) sobre una transformación de mentalidad financiera.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto que exponga un error común, trampa o revelación del sistema (ej: "La verdad incómoda de por qué ahorrar dinero te está haciendo más pobre").
2. **Protagonista:** Una persona común (empleado, joven profesional, padre de familia) que atraviesa una crisis financiera real y llega a una revelación profunda.
3. Arco Narrativo: Desarrollo profundo del conflicto financiero, el proceso de aprendizaje y la transformación antes de la resolución. La historia debe enfocarse en un cambio mental práctico del día a día, evitando la escasez.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS FINANCIERAS (ESTILO ESTRATEGIA - LONG)
**Objetivo:** Generar una idea para un video largo (de 5 a 8 minutos) que explique en profundidad una estrategia financiera poderosa y práctica.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una afirmación o pregunta de 10-15 palabras de alto impacto enfocada en aprender un hack o regla (ej: "El método de la regla del 50/30/20 que los bancos no quieren que uses").
2. **Concepto central:** Una regla, hábito o táctica concreta y fácil de explicar (Ley de Pareto, Bola de nieve vs Avalancha, inflación del estilo de vida).
3. Presenta el concepto con un ejemplo real o analogía cotidiana, demostrando el "cómo hacerlo" paso a paso.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA FINANCIERO (STORYTELLING CINEMATOGRÁFICO - LONG)
**Objetivo:** Crear un guion dinámico y educativo de entre 40 y 60 escenas, estructurado de manera cinematográfica, para lograr una duración final de entre 5 y 8 minutos de alto valor educativo y retención.

**Estructura del Guion (MANDATORIO):**
1. **Acto 1: El Hook y Planteamiento [Primeras 8 escenas]:** DEBES usar el campo "hook" para la Escena 1 de forma literal. Presenta el problema del sistema o crisis financiera cotidiana que enfrenta nuestro protagonista.
2. **Acto 2: El Desarrollo y Aprendizaje [Escenas medias]:** Explica de forma didáctica la regla, hábito o estrategia. Alterna la historia del protagonista con explicaciones conceptuales, analogías sencillas y datos visuales.
3. **Acto 3: El Payoff y Cierre [Últimas 8 escenas]:** Muestra la transformación y el resultado de aplicar el concepto. Termina con un consejo rápido accionable y un Llamado a la Acción (CTA) pidiendo interactuar: suscribirse, comentar su opinión, dar like o guardar el video.

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Narración:** Frases cortas y de alto impacto educativo. El tono debe ser épico, cinematográfico y motivacional — como un documental de alta calidad.
- **Secuencialidad:** La historia debe tener progresión lógica clara: problema cotidiano → revelación/explicación → ejemplo real/analogía → plan de acción.
- **Fluidez y Retención:** Mantén curiosidad constante abriendo preguntas o sembrando datos interesantes que se resuelvan más adelante en el video.

### 🔵 REGLAS VISUALES
- **Protagonista:** Presencia consistente de un personaje principal identificable viviendo la historia o el tutorial en escenas clave.
- **Relación Imagen-Texto:** El `image_prompt` debe ilustrar visualmente el concepto de forma exacta. Lo que el espectador escucha debe verse en pantalla con claridad cinematográfica.
- **Pattern Interrupts:** Cambia con frecuencia de enfoque visual, composición y ángulos de cámara (Wide shot, Close-up, infografías limpias, entornos reales) para reiniciar la atención del espectador.
- **Estilo (Cinematic Documentary):** DEBES usar el campo `style` para generar imágenes hiperrealistas y cinematográficas. La descripción en el campo `style` DEBE ser: `"Detailed cinematic documentary style, high-end commercial photography, soft natural lighting, realistic textures, rich color palette, clean composition, 16:9 aspect ratio."`.
- **Uso del Color:** Utiliza paletas de colores armónicas y profesionales (tonos tierra, azules oscuros, toques de verde para éxito, rojo sutil para errores).

### 🔴 ESTRUCTURA Y SALIDA
- **Extensión:** Entre 40 y 60 escenas, manteniendo suficiente profundidad y ritmo dinámico.
- **Cierre:** Resolución emotiva con un fuerte Llamado a la Acción (CTA).

### 🟠 IDIOMAS (ESTRICTO)
- **image_prompt:** DEBES generar todos los campos de `image_prompt` (subjects, environment, lighting, composition) en **INGLÉS**. EXCEPCIÓN: Si en el prompt pides que haya algún texto escrito o letrero dentro de la imagen, las palabras exactas a escribir DEBEN estar en **ESPAÑOL** (Ejemplo: "A sign that says 'DEUDAS'").
- **narration:** DEBES generar el campo `narration` en **ESPAÑOL LATINOAMERICANO**.
"""
