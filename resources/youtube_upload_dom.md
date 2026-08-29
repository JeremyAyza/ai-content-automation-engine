# Árbol DOM: Subida YouTube Studio

Este documento detalla los selectores (locators) y acciones de Playwright necesarios para navegar el modal de subida de YouTube Studio basado en las capturas proporcionadas.

## 1. Inicio de Subida
- **URL Inicial:** `https://studio.youtube.com/channel/.../videos/short?d=ud`
- **Selector:** `input[type='file']`
- **Acción:** `set_input_files(video_path)` (Sube el `final_video.mp4`)

## 2. Pestaña: Detalles
### Título
- **Selector:** `#textbox` (El primero que aparece corresponde al título).
- **Acción:** `clear()` -> `type(title, delay=50)`

### Miniatura (Nuevo)
- **Selector:** `ytcp-thumbnails-compact-editor-uploader input[type='file']` (Este es el input oculto estándar de YT para thumbnails).
- **Acción:** `set_input_files(thumbnail_path)` (Sube `thumbnail.jpg`).

### Listas de Reproducción
- **Selector Dropdown:** `div.ytcp-text-dropdown-trigger:has-text('Seleccionar')`
- **Acción:** `click()`
- **Selector Checkbox:** `tp-yt-paper-checkbox[aria-label*='Shorts']` (o el primero disponible)
- **Acción:** `click()`
- **Selector Botón Confirmar:** `ytcp-button:has-text('Hecho')`
- **Acción:** `click()`

### Etiquetas (Tags)
- **Selector Botón Expandir:** `ytcp-button#toggle-button` ("Mostrar más")
- **Acción:** `scroll_into_view_if_needed()` -> `click()`
- **Selector Input Etiquetas:** `input[aria-label*='Etiquetas']`
- **Acción:** `scroll_into_view_if_needed()` -> `type(tags, delay=20)` -> `press("Enter")`

## 3. Navegación (Pestañas Intermedias)
El botón "Siguiente" avanza a través de "Elementos del vídeo" y "Comprobación inicial".
- **Selector:** `ytcp-button#next-button`
- **Acción:** Ciclo de 3 clicks, verificando cada vez que `is_visible()` y `not is_disabled()`. Añadir `wait_for_timeout(1000)` entre clicks para animaciones.

## 4. Pestaña: Visibilidad
Esta es la última pestaña del modal.
### Modalidad
- **Selector Radio "Programar":** `#second-container`
- **Acción:** `scroll_into_view_if_needed()` -> `click(force=True)`

### Fecha y Hora
- **Selector Disparador Fecha:** `#datepicker-trigger`
- **Acción:** `click(force=True)`
- **Selector Input Fecha:** `ytcp-date-picker #labelAndInputContainer input`
- **Acción:** `clear()` -> `type("28 ago 2026", delay=50)` -> `press("Enter")`
- **Selector Disparador Hora:** `ytcp-form-input-container#time-of-day-container`
- **Acción:** `click(force=True)`
- **Selector Input Hora:** `ytcp-form-input-container#time-of-day-container input`
- **Acción:** `clear()` -> `type("18:30", delay=50)` -> `press("Enter")` (para activar autocompletado on-blur).

### Extracción de Enlace
- **Selector Link:** `.ytcp-video-info a.style-scope.ytcp-video-info`
- **Acción:** `inner_text()`

## 5. Finalización
### Espera Estratégica (Crucial)
- **Acción:** Esperar 1 minuto (60 segundos) ANTES de hacer clic en el botón de programar final. Esto permite que el video termine de subir o avance lo suficiente para evitar advertencias de procesamiento.

### Confirmación
- **Selector Botón Final:** `ytcp-button#done-button:not([disabled])`
- **Acción:** `scroll_into_view_if_needed()` -> `click(force=True)`

### Popup de Advertencia (Opcional)
Si el video no ha subido al 100%, YouTube lanza una advertencia.
- **Selector Botón Forzar:** `ytcp-button:has-text('todas formas')`
- **Acción:** `click(force=True)`

### Modal de Éxito y Extracción de URL Definitiva
Aquí verificamos si el proceso fue exitoso usando el botón de copiar.
- **Selector Botón Copiar:** `ytcp-icon-button[aria-label*='Copiar']`
- **Selector Link en Modal:** `ytcp-video-share-dialog a.style-scope`
- **Comprobación de Subida:** Extraer `inner_text()` de modales activos (`ytcp-dialog[open]`). Si dice "Subiendo", "Procesando" o muestra un "%" sin decir "Completad", aplicar delay de 5 segundos y repetir. Si detecta el botón de copiar, copiar el link final, la subida es exitosa.
- **Selector Botón Cerrar:** `ytcp-button:has-text('Cerrar')` (.last) para finalizar limpio.
