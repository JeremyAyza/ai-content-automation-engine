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
- **Selector Radio "Programar":** `tp-yt-paper-radio-button[name='SCHEDULE']`
- **Acción:** `click()`

### Fecha y Hora
- **Selector Fecha:** `ytcp-date-picker input`
- **Acción:** `clear()` -> `type("28 ago 2026", delay=50)` -> `press("Enter")`
- **Selector Hora:** `input[aria-label*='hora']` (o `ytcp-time-of-day-picker input`)
- **Acción:** `clear()` -> `type("18:30", delay=50)` -> `press("Enter")`

### Extracción de Enlace
- **Selector Link:** `.ytcp-video-info a.style-scope.ytcp-video-info`
- **Acción:** `inner_text()`

## 5. Finalización
El botón para programar definitivamente. No esperamos a que procese antes de hacer clic, lo hacemos directo.
- **Selector Botón Final:** `ytcp-button#done-button:not([disabled])`
- **Acción:** `click()`

### Popup de Advertencia (Opcional)
Si el video no ha subido al 100%, YouTube lanza una advertencia.
- **Selector Botón Forzar:** `ytcp-button:has-text('todas formas')`
- **Acción:** `click()`

### Modal de Éxito y Espera de Subida
Aquí sí esperamos a que el video termine de subir para no cortar el navegador prematuramente.
- **Selector Modal Éxito:** `ytcp-video-share-dialog`
- **Acción:** `wait_for_selector()`
- **Comprobación de Subida:** Extraer `inner_text()` del modal repetidamente. Si dice "Subiendo", "Procesando" o muestra un "%" sin decir "Completado" o "Finalizado", aplicar un delay de 5 segundos y repetir. Al terminar, guardar todo y cerrar.
