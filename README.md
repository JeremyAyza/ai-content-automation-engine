# 🎬 AI Video Automation Pipeline

¡Bienvenido al motor de automatización de creación de videos! Este proyecto es un **Pipeline (Tubería de procesos)** diseñado para generar videos automatizados (tanto cortos verticales como largos horizontales) desde cero, utilizando IA para escribir el guion, generar imágenes, locución, subtítulos y edición de video.

Este documento está diseñado para ser la guía definitiva. No importa si eres un Product Owner, un Project Manager o un desarrollador Junior: aquí entenderás exactamente **cómo funciona la magia** y **cómo usarla**.

---

## 🧠 ¿Cómo funciona el flujo? (El Pipeline)

El proyecto funciona como una línea de ensamblaje de una fábrica. Toma una idea básica y la pasa por **7 pasos** secuenciales hasta tener un video finalizado. 

Estos son los 7 pasos mágicos:

1. **📝 Paso 1: Generar Historia/Guion (`step1`)**
   Toma una idea de nuestra base de datos (un archivo CSV) y genera un guion completo usando IA.
2. **🎨 Paso 2: Generar Imágenes (`step2`)**
   Lee el guion generado y crea las imágenes o escenas visuales necesarias para el video.
3. **🎙️ Paso 3: Generar Audio (`step3`)**
   Convierte el texto del guion en voz (Text-to-Speech) para la narración del video.
4. **🎞️ Paso 4: Ensamblar Video (`step4`)**
   Junta las imágenes generadas con la narración de audio para crear un primer corte del video.
5. **🔤 Paso 5: Generar Subtítulos (`step5`)**
   Analiza el audio y crea subtítulos sincronizados, superponiéndolos en el video.
6. **🎵 Paso 6: Añadir Música de Fondo (`step6`)**
   Agrega una pista de música de fondo para darle el toque final y equilibrar los volúmenes.
7. **✅ Paso 7: Finalizar Video (`step7`)**
   Renombra y empaqueta el video final para que esté listo para publicarse.

---

## 🚀 ¿Cómo usarlo?

Tienes dos formas principales de interactuar con el proyecto: usando el archivo **`cli.py` (Línea de Comandos)** o usando los atajos de **`Makefile`**. 

El flujo requiere que especifiques dos cosas siempre:
- **Formato**: `short` (Video vertical, ideal para TikTok/Reels) o `long` (Video horizontal, ideal para YouTube).
- **Paso a ejecutar**: Puede ser un paso específico (`step1`, `step2`, etc.), o modos automáticos como `all` o `fixed`.

### Modos Automáticos (Los más útiles)

- **Modo `all` (Bucle Infinito):** Ejecuta todo el proceso desde el paso 1 hasta el 7 y luego vuelve a empezar con una nueva idea. Nunca se detiene. Ideal para dejarlo trabajando toda la noche.
- **Modo `fixed` (Terminar Pendientes):** Busca ideas en la base de datos que se quedaron a medias (por ejemplo, tienen guion pero falló el audio) y continúa el proceso desde donde se quedó hasta terminarlas todas.

---

### 💻 Opción 1: Usando el CLI (Python)

Abre tu terminal en la carpeta del proyecto y usa el siguiente comando:

```bash
python cli.py run [formato] [paso]
```

**Ejemplos:**
- Generar un guion para un video corto: `python cli.py run short step1`
- Ejecutar el pipeline completo para videos cortos sin parar: `python cli.py run short all`
- Retomar todos los videos largos incompletos y terminarlos: `python cli.py run long fixed`

---

### 🛠️ Opción 2: Usando Makefile (Atajos rápidos)

Si tienes `make` instalado, es mucho más rápido. Los comandos siguen esta estructura: `make icg-[s o l]-[paso]`.
- `s` = short
- `l` = long

**Ejemplos de comandos rápidos:**
- `make icg-s-step1` (Paso 1 para Short)
- `make icg-l-all` (Loop infinito para Long)
- `make icg-s-fixed` (Terminar pendientes de Shorts)

---

## 📂 ¿Dónde se guarda todo?

- **Tus Ideas Base:** Se encuentran en `flows/resource/`. Aquí hay archivos `.csv` (como `bank_ideas_shorts.csv`) donde puedes alimentar al sistema con nuevas ideas.
- **Tus Videos Terminados:** Los resultados y los archivos intermedios se guardan en dos carpetas:
  - `flows/out_short/` (Para formato vertical)
  - `flows/out_long/` (Para formato horizontal)

Cada video tendrá su propia subcarpeta con su ID, donde podrás ver el guion generado, las imágenes, el audio y el archivo de video final `.mp4`.

---

## ⚙️ Requisitos previos para el equipo Técnico (Setup)

Si eres el desarrollador que va a configurar esto por primera vez, asegúrate de tener:

1. **Python 3.10+**
2. **Poetry** (Manejador de dependencias): Ejecuta `poetry install` para instalar todo.
3. **FFmpeg** instalado en tu sistema operativo (Esencial para la edición de video).
4. Configurar tus **Variables de Entorno** (API Keys de IA, etc.). Copia el archivo `.env.sample` a `.env` y llénalo.

¡Y eso es todo! Ya estás listo para generar videos en automático. 🍿
