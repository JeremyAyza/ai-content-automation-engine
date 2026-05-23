# 🚀 Guía de Setup — AI Content Automation Engine
> Para devs que vienen de Node.js

---

## 🧠 Equivalencias Node ↔ Python (antes de empezar)

Si sabes Node, ya entiendes el 80%. Aquí el mapa mental:

| Node.js / npm          | Python equivalente        | Para qué sirve                          |
|------------------------|---------------------------|-----------------------------------------|
| `package.json`         | `pyproject.toml`          | Metadata del proyecto + dependencias    |
| `npm install`          | `poetry install`          | Instala dependencias                    |
| `npm run dev`          | `poetry run python ...`   | Ejecuta scripts dentro del entorno      |
| `node_modules/`        | `.venv/`                  | Carpeta de dependencias (no tocar)      |
| `.env`                 | `.env`                    | Variables de entorno (igual)            |
| `npx`                  | `pipx` / `poetry`         | Ejecutar binarios sin instalar global   |
| `npm scripts`          | `Makefile`                | Shortcuts para correr comandos          |

> **`poetry`** es el equivalente a `npm` en este proyecto. Maneja el entorno virtual (`.venv`) y las dependencias automáticamente. **No uses `pip` directamente.**

---

## 📋 Prerrequisitos

### 1. Python 3.11+
Verifica tu versión:
```powershell
python --version
# Necesitas: Python 3.11.x o superior
```

Si no lo tienes → [python.org/downloads](https://www.python.org/downloads/)

> ⚠️ En Windows, asegúrate de marcar **"Add Python to PATH"** durante la instalación.

---

### 2. Poetry (el "npm" de este proyecto)
```powershell
# Instalar Poetry (una sola vez en tu máquina)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Verifica que quedó instalado:
```powershell
poetry --version
```

> Si el comando no se reconoce, reinicia la terminal o agrega Poetry al PATH manualmente:
> `C:\Users\TU_USUARIO\AppData\Roaming\Python\Scripts`

---

### 3. FFmpeg
El proyecto usa FFmpeg para edición de video (como si fuera un codec nativo).

```powershell
# Con winget (recomendado)
winget install ffmpeg

# O con Chocolatey
choco install ffmpeg
```

Verifica:
```powershell
ffmpeg -version
```

---

### 4. Google Gemini API Key
El proyecto usa Gemini para texto, imágenes y audio. Obtén tu key gratis en:
[aistudio.google.com](https://aistudio.google.com/apikey)

---

## ⚙️ Instalación del Proyecto

### Paso 1 — Clonar (si aún no lo tienes)
```powershell
git clone <repo-url>
cd AI-Content-Automation-Engine-main
```

---

### Paso 2 — Instalar dependencias
> Equivalente a `npm install`

```powershell
poetry install
```

Poetry leerá el `pyproject.toml`, creará automáticamente el entorno virtual en `.venv/` e instalará todo. **No necesitas activar el venv manualmente.**

---

### Paso 3 — Configurar variables de entorno
> Igual que en Node: copia el `.env.sample` a `.env`

```powershell
Copy-Item .env.sample .env
```

Luego edita `.env` y pega tu API Key:
```env
GEMINI_API_KEY=tu-api-key-aqui
```

---

## ▶️ Cómo correr el proyecto

### Opción A — Correr todo el pipeline de una vez
> Genera un video completo (Short 9:16) en 7 pasos automáticos

```powershell
poetry run python -m flows.image_content_generator.pipeline.main short all
```

Si tienes `make` instalado (Git Bash / WSL):
```bash
make icg-s-all
```

---

### Opción B — Correr paso por paso
Cada paso equivale a una etapa del pipeline:

```powershell
# Paso 1: Genera el script/idea con Gemini
poetry run python -m flows.image_content_generator.pipeline.main short step1

# Paso 2: Genera imágenes por escena
poetry run python -m flows.image_content_generator.pipeline.main short step2

# Paso 3: Genera audio (TTS narración)
poetry run python -m flows.image_content_generator.pipeline.main short step3

# Paso 4: Ensambla video (imagen + audio por escena)
poetry run python -m flows.image_content_generator.pipeline.main short step4

# Paso 5: Agrega subtítulos (SRT)
poetry run python -m flows.image_content_generator.pipeline.main short step5

# Paso 6: Agrega música de fondo
poetry run python -m flows.image_content_generator.pipeline.main short step6

# Paso 7: Renombra el video final
poetry run python -m flows.image_content_generator.pipeline.main short step7
```

---

## 🗂️ Estructura del proyecto

```
AI-Content-Automation-Engine/
├── flows/                          # "src/" — pipelines de video
│   └── image_content_generator/
│       └── pipeline/
│           ├── main.py             # Entry point (como index.js)
│           ├── pipeline.py         # Orquestador de los 7 pasos
│           ├── schemas.py          # Tipos/enums (como types.ts)
│           └── storage_csv.py      # "Base de datos" en CSV
├── tools/                          # Módulos reutilizables (como utils/)
│   ├── text_generation/            # Gemini → texto/JSON
│   ├── image_generation/           # Gemini → imágenes
│   ├── audio_generation/           # Gemini TTS → WAV
│   └── video_editing/              # FFmpeg + Whisper wrappers
├── .env                            # Variables de entorno (igual que Node)
├── pyproject.toml                  # package.json equivalent
├── poetry.lock                     # package-lock.json equivalent
└── Makefile                        # npm scripts equivalent
```

---

## 🔧 Comandos útiles del día a día

| Quiero...                            | Comando                                      |
|--------------------------------------|----------------------------------------------|
| Instalar deps                        | `poetry install`                             |
| Agregar una nueva dep                | `poetry add nombre-paquete`                  |
| Agregar una dep de desarrollo        | `poetry add --group dev nombre-paquete`      |
| Correr un script puntual             | `poetry run python ruta/al/script.py`        |
| Abrir shell con el entorno activado  | `poetry shell`                               |
| Ver deps instaladas                  | `poetry show`                                |
| Formatear código (como Prettier)     | `poetry run black .`                         |

---

## ❌ Errores comunes

### `poetry: command not found`
Poetry no está en el PATH. Reinicia la terminal o agrégalo manualmente:
```powershell
$env:PATH += ";$env:APPDATA\Python\Scripts"
```

### `pip install -r pyproject.toml` falla
`pyproject.toml` **no es** `requirements.txt`. Usa siempre `poetry install`.

### `.venv\Scripts\activate` falla en PowerShell
No necesitas activar el venv. Usa siempre `poetry run <comando>` en su lugar.
Si de todas formas quieres activarlo manualmente en PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

### `python` no se reconoce
Usa `python3` o reinstala Python marcando "Add to PATH".

---

## 📦 El output del pipeline

Los videos generados se guardan en `out_short/` (para Shorts). Esta carpeta está en `.gitignore`, igual que `node_modules/`.

---

> 💡 **Tip final**: Piensa en `poetry run` como el `npx` de Python. Todo comando que necesite el entorno del proyecto debe ir precedido de `poetry run`.
