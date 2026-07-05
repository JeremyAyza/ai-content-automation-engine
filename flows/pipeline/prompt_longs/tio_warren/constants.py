# flake8: noqa: E501
IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (MENTALIDAD - CÓDIGO CAPITAL)
**Objetivo:** Generar una propuesta estructurada para un video de 12 minutos sobre la transformación de la mentalidad financiera, utilizando a nuestros personajes de marca.

**Personajes Obligatorios:**
1. **Tío Warren (El Mentor):** Un anciano sabio, de traje formal impecable, cabello blanco y lentes, que representa la riqueza real, la paciencia y las leyes del dinero.
2. **El Aprendiz:** Un joven de 22 años, vestido con una sudadera verde (hoodie), que representa a la audiencia: impulsivo, obsesionado con el dinero rápido (estilo crypto-bro/trading) y atrapado en la carrera de la rata.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto que exponga una verdad incómoda sobre el dinero (ej. "La razón oculta por la que ahorrar en el banco te está empobreciendo hoy").
2. **Estructura en Bloques Analíticos:**
   - Define un mito financiero que el Aprendiz cree fervientemente.
   - Define el error psicológico o trampa de consumo que este mito provoca.
   - Define la regla del Tío Warren que desmonta este mito y la analogía práctica que usará para enseñarlo.
"""

IDEA_PROMPT_ESTRATEGIA: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (ESTRATEGIA - CÓDIGO CAPITAL)
**Objetivo:** Generar una propuesta estructurada para un video de 12 minutos que explique de forma matemática y práctica una estrategia financiera, comparando caminos inteligentes y tontos.

**Personajes Obligatorios:**
1. **Tío Warren (El Mentor):** El experto que devela la lógica detrás de los números de forma calmada y segura.
2. **El Aprendiz:** El joven impulsivo con sudadera verde que comete los errores típicos de cálculo y busca el camino más fácil.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras de alto impacto sobre cómo burlar una trampa del sistema financiero (ej. "La trampa de comprar un auto financiado que las agencias ocultan").
2. **Estructura en Bloques Analíticos:**
   - Define el concepto central (ej. apalancamiento, interés compuesto, escudo fiscal, rentar vs comprar).
   - Define la comparación directa: el método impulsivo del Aprendiz vs el método estratégico del Tío Warren.
   - Define el caso práctico real con números sencillos de entender.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA PREMIUM (BLOQUES ANALÍTICOS - CÓDIGO CAPITAL)
**Objetivo:** Crear un guion denso, educativo e increíblemente entretenido de entre 65 y 80 escenas, estructurado en bloques analíticos para lograr una duración final de aproximadamente 12 minutos de alta retención.

**Estructura del Guion por Bloques (MANDATORIO):**
1. **Bloque 1: El Gancho y el Gran Mito [Escenas 1-10]:** DEBES usar el campo "hook" para la Escena 1 de forma literal. Presenta al Aprendiz presumiendo o cayendo en una trampa financiera común y cómo el Tío Warren lo interrumpe con el gancho inicial.
2. **Bloque 2: El Error del Aprendiz [Escenas 11-30]:** Expone en detalle la tontería financiera del Aprendiz (ej: gastar de más para aparentar, hacer trading con apalancamiento, rentar sin calcular costos). Muestra su frustración al chocar con la pared.
3. **Bloque 3: La Regla del Tío Warren [Escenas 31-50]:** El Tío Warren toma el control y enseña la regla matemática/financiera real. Usa analogías visuales ricas y explicaciones sencillas (ej: comparar el dinero con soldados en batalla o semillas sembradas).
4. **Bloque 4: La Comparativa y el Caso Real [Escenas 51-70]:** Un cara a cara visual detallado. Muestra qué pasa con el dinero del Aprendiz en 5 años vs el dinero del Tío Warren usando la estrategia correcta. Pon números sencillos en pantalla.
5. **Bloque 5: El Payoff y Cierre [Escenas 71-final (Max 80)]:** La transformación del Aprendiz al aplicar el consejo. Finaliza con un consejo accionable inmediato de Código Capital y un llamado a la acción sutil para suscribirse.

## 📜 REGLAS OBLIGATORIAS

### 🟢 NARRACIÓN Y RITMO
- **Gancho:** Uso mandatorio del texto de `hook` literal en la Escena 1.
- **Narración:** Tono documental, magnético y analítico. Evita frases genéricas de motivación. El Tío Warren habla con autoridad calmada; el Aprendiz con confusión, dudas o exclamaciones graciosas y dinámicas.
- **Densidad de Valor:** En cada bloque debe haber información matemática o lógica real. No rellenes con redundancias. Si el tema es Fideicomisos, explica cómo se estructuran y sus ventajas exactas.

### 🔵 REGLAS VISUALES (ESTRICTO)
- **Miniatura (Thumbnail - YT Código Capital):** DEBES generar un `thumbnail_prompt` optimizado para CTR masivo:
  1) **Personajes:** Tío Warren (mentor sabio, traje azul oscuro, lentes, cabello blanco) con expresión seria y apuntando a una pizarra, al lado del Aprendiz (joven, sudadera verde, pelo marrón desordenado) con expresión de absoluta sorpresa o desesperación.
  2) **Texto Gigante (Obligatorio):** Un título de 3 a 7 palabras impactantes dibujado en la imagen (Ej: "ASÍ TE ROBA EL BANCO" o "PIENSA COMO RICO").
  3) **Utilería y Flechas:** Usa flechas rojas o verdes dibujadas a mano apuntando a elementos clave (un saco de billetes, un gráfico colapsando, una trampa de oso).
  4) **Estilo Visual:** `"Premium high-quality 2D vector art style, clean flat background, giant bold typography, thick expressive outlines, high contrast YouTube thumbnail aesthetic."`
- **Consistencia de Personajes (MANDATORIO en todas las escenas):**
  - **Tío Warren:** Siempre debe ser descrito exactamente como: `"wise, distinguished 60-year-old financial mentor, short white hair, elegant glasses, wearing a sharp dark blue suit and a tie, calm and authoritative posture"`.
  - **El Aprendiz:** Siempre debe ser descrito exactamente como: `"22-year-old young man, messy brown hair, wearing a green casual hoodie, looking confused or expressive"`.
- **Estilo de Ilustración Global:** El campo `style` de las escenas DEBE ser estrictamente: `"Premium flat 2D vector art style, minimalist professional background, clean corporate aesthetic, vibrant green highlights, sharp outlines."`
- **Relación Imagen-Texto:** Si la narración habla de "tasas de interés de tarjetas de crédito", el prompt de la imagen debe mostrar una infografía o al Aprendiz siendo aplastado por una tarjeta de crédito gigante con números rojos.

### 🔴 IDIOMAS
- **image_prompt:** Todos los campos de descripción visual (subjects, environment, lighting, composition, style) en **INGLÉS**. Excepción: Los textos que deban aparecer físicamente dibujados en la imagen deben estar en **ESPAÑOL** (Ej: "A folder labeled 'FIDEICOMISO'").
- **video_prompt:** Todos los campos (motion, camera_movement, transition, duration_hint) en **INGLÉS**.
- **narration:** El campo de voz en off en **ESPAÑOL LATINOAMERICANO**.

TU IDEA DE BASE (CONTEXTO EN JSON):
{idea_context_json}

**Formato de Salida Obligatorio (JSON):**
```json
{{
  "thumbnail_prompt": {{
    "subjects": [
      {{
        "description": "Physical description in ENGLISH. Must specify Uncle Warren or the Apprentice matching their visual identity.",
        "action": "Specific action or pose in ENGLISH"
      }}
    ],
    "environment": "Background details in ENGLISH matching the visual style.",
    "lighting": "Lighting mood in ENGLISH",
    "composition": "Framing and angle in ENGLISH",
    "style": "EXACT visual style requested for thumbnails."
  }},
  "scenes": [
    {{
      "scene_number": "Sequential number of the scene (Integer)",
      "image_prompt": {{
        "subjects": [
          {{
            "description": "Physical description in ENGLISH. Ensure exact consistency for Uncle Warren or the Apprentice.",
            "action": "Action in ENGLISH"
          }}
        ],
        "environment": "Background in ENGLISH.",
        "lighting": "Lighting in ENGLISH.",
        "composition": "Framing/angle in ENGLISH.",
        "style": "EXACT visual style requested for scenes."
      }},
      "video_prompt": {{
        "motion": "Movement in ENGLISH.",
        "camera_movement": "Camera motion in ENGLISH.",
        "transition": "Transition in ENGLISH.",
        "duration_hint": "Pacing description in ENGLISH."
      }},
      "narration": "Spoken dialogue or voiceover in SPANISH (LATAM)"
    }}
  ]
}}
```
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
