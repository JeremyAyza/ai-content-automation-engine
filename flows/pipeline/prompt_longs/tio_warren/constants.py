# flake8: noqa: E501
IDEA_PROMPT_MINDSET: str = """# 🧠 PROMPT MAESTRO — AGENTE DE IDEAS (MENTALIDAD & PILARES - CÓDIGO CAPITAL)
**Objetivo:** Generar una propuesta estructurada para un video-ensayo educativo de 12-15 minutos sobre transformación de mentalidad, orden personal o filosofía financiera, listo para ser expandido en un despiece profundo por pilares o pasos.

**Personajes Visuales de Marca:**
1. **Tío Warren (El Mentor Pato):** Pato sabio de plumas blancas, traje azul marino a rayas, lentes en el pico y corbata amarilla. Representa la sabiduría, el rigor financiero y el orden.
2. **El Aprendiz (Pato Verde):** Pato joven de plumas verdes, sudadera negra con logo dorado de Bitcoin y gorra negra. Representa a la audiencia: impulsivo, con dudas o buscando atajos.

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
2. **El Aprendiz (Pato Verde):** Pato joven de plumas verdes, sudadera negra con logo de Bitcoin y gorra negra.

**Instrucciones:**
1. **hook (Gancho de Interrupción):** Una frase de 10-15 palabras sobre la trampa oculta de una decisión cotidiana (ej. "Por qué pagar de contado en la agencia te cuesta más caro de lo que crees").
2. **Estructura en Bloques Analíticos:**
   - Define la decisión o trampa del sistema a analizar.
   - Define la comparativa de números reales (Caso A vs Caso B a 5-10 años).
   - Define el método estratégico para maximizar la liquidez y el patrimonio.
"""

SCRIPT_PROMPT: str = """# 📝 PROMPT MAESTRO — AGENTE GUIONISTA DE VIDEO-ENSAYOS PREMIUM (CÓDIGO CAPITAL)
**Objetivo:** Crear un guion educativo denso, magnético y de altísima retención de entre **62 y 81 escenas**, estructurado como una **Masterclass / Video-Ensayo Educativo de 12 a 15 minutos**.

## 📜 NARRACIÓN Y TONO (ESTRICTO)
1. **Voz en Off (Narración):** Debe hablar **directamente al espectador en segunda persona ("tú")**. Considera que la voz del Tío Warren es grave, mayor y autoritaria. Escribe usando puntuación estratégica (comas y puntos) para forzar pausas dramáticas. Debe sentirse como un documental o clase magistral financiera extremadamente entretenida.
2. **CERO Diálogos de Ficción en el Audio:** Los personajes NO deben actuar una telenovela ni hablarse entre sí en la narración. La voz en off expone los conceptos, matemáticas, hábitos, autores (ej. Marco Aurelio, Warren Buffett) y ejemplos reales de vida.
3. **Alta Densidad de Valor:** Cada escena debe aportar datos duros, lógica clara, pasos concretos o reflexiones profundas. Sin relleno ni redundancias.
4. **Estructura del Guion:**
   - **Introducción y Tesis (Escenas 1-10):** Arranca con el `hook` literal en la Escena 1 y plantea el problema/mito financiero directo al espectador.
   - **Desglose de Pilares / Pasos / Análisis Técnico (Escenas 11-55):** Desarrolla punto por punto o paso a paso el contenido con riqueza de datos, comparativas y ejemplos prácticos.
   - **Recapitulación y Síntesis (Escenas 56-68):** Conecta todos los puntos explicados demostrando cómo construyen patrimonio a largo plazo.
   - **Cierre y Llamado a la Acción (Escenas 69-final):** Conclusión inspiradora y CTA a suscribirse a Código Capital.

## 🔵 REGLAS VISUALES (CADA ESCENA Y THUMBNAIL)
- **Miniatura (Thumbnail - YT Código Capital):** DEBES generar un `thumbnail_prompt` optimizado para CTR masivo:
  1) **Personajes:** Tío Warren (pato anciano sabio, traje azul a rayas, lentes en el pico, plumas blancas) con expresión seria apuntando a un esquema o pizarra, al lado del Aprendiz (pato joven verde, sudadera negra con logo de Bitcoin, gorra negra) con expresión de asombro o análisis.
  2) **Texto Gigante (Obligatorio):** Un título de 3 a 6 palabras impactantes dibujado en la imagen (Ej: "EL ORDEN DE LA RIQUEZA" o "REGLAS DEL DINERO").
  3) **Utilería y Flechas:** Flechas rojas/verdes dibujadas apuntando a elementos clave (gráfico, balanza, bolsas de dinero).
  4) **Estilo Visual:** `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background, high contrast YouTube thumbnail aesthetic."`
- **Consistencia de Personajes en `image_prompt`:**
  - **Tío Warren:** `"wise, distinguished 60-year-old white duck character, white feathers, wearing glasses on his bill, a sharp navy blue pinstripe suit, a white dress shirt, and a yellow-orange tie, calm and authoritative posture"`.
  - **El Aprendiz:** `"22-year-old young green duck character, green feathers, wearing a black casual hoodie with a golden Bitcoin logo on the front, wearing a black baseball cap, looking confused or expressive"`.
- **Estilo de Ilustración Global:** El campo `style` de las escenas DEBE ser estrictamente: `"Premium 2D cartoon vector style, clean outline, vibrant colors, custom cute duck characters style, solid clean white background."`
- **Rol de los Personajes en la Imagen:** Úsalos como **metáforas e ilustraciones visuales** de lo que dice la voz en off (Ej: si la narración habla de la agenda como presupuesto del tiempo, el Aprendiz sostiene una agenda gigante mientras el Tío Warren señala un reloj de arena).

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
