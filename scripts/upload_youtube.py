import json
import random
from datetime import datetime, timedelta
from pathlib import Path
import os
import time

from pipeline.schemas import State
from pipeline.storage_csv import CsvStore, Column
from tools.messenger import Messenger
from tools.time_utils import api_spinner

def get_next_schedule(csv_store: CsvStore) -> datetime:
    df = csv_store.read_all()
    scheduled_dates = df[Column.SCHEDULED_DATE.value].dropna().tolist()
    
    today = datetime.now().date()
    valid_dates = []
    
    for date_str in scheduled_dates:
        if date_str:
            try:
                # Assuming format "YYYY-MM-DD" in CSV
                dt = datetime.strptime(date_str, "%Y-%m-%d").date()
                valid_dates.append(dt)
            except ValueError:
                pass
                
    if not valid_dates:
        target_date = today
        count_target = 0
    else:
        max_date = max(valid_dates)
        if max_date < today:
            target_date = today
        else:
            target_date = max_date
            
        count_target = valid_dates.count(target_date)
        
    if count_target >= 3:
        target_date = target_date + timedelta(days=1)
        
    # Determine time based on day of week
    def get_time_for_date(d: datetime.date):
        day_of_week = d.weekday() # 0 = Mon, 6 = Sun
        if day_of_week < 5: # M-F
            return 18, random.randint(0, 45)
        elif day_of_week == 5: # Sat
            return 10, random.randint(0, 30)
        else: # Sun
            m = random.randint(30, 59)
            return (11, 0) if m == 60 else (10, m)
            
    hour, minute = get_time_for_date(target_date)
    target_dt = datetime(target_date.year, target_date.month, target_date.day, hour, minute)
    
    # Garantizar que la fecha esté en el futuro (mínimo 1 hora de margen)
    now = datetime.now()
    while target_dt < now + timedelta(hours=1):
        target_date += timedelta(days=1)
        hour, minute = get_time_for_date(target_date)
        target_dt = datetime(target_date.year, target_date.month, target_date.day, hour, minute)
        
    return target_dt


def format_youtube_date(dt: datetime) -> str:
    # YouTube date format in Spanish: "28 ago 2026"
    months = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    day = dt.day
    month_name = months[dt.month - 1]
    year = dt.year
    return f"{day} {month_name} {year}"

def format_youtube_time(dt: datetime) -> str:
    return dt.strftime("%H:%M")


def upload_video():
    csv_path = Path("out_short") / "ideas_tracking.csv"
    if not csv_path.exists():
        csv_path = Path("resources") / "ideas_tracking.csv"
        
    store = CsvStore(csv_path)
    
    idea_to_upload = store.get_first_by_state(State.COMPLETED)
    if not idea_to_upload:
        Messenger.info("No hay videos en estado COMPLETED listos para subir.")
        return
        
    # Parse idea.json
    idea_dir = Path("out_short") / "ideas" / f"idea_{idea_to_upload.id:06d}"
    video_files = list(idea_dir.glob("*.mp4"))
    idea_json_path = idea_dir / "idea.json"
    
    if not video_files or not idea_json_path.exists():
        Messenger.error(f"Faltan archivos para la idea {idea_to_upload.id}")
        return
        
    video_path = video_files[0]
        
    with open(idea_json_path, "r", encoding="utf-8") as f:
        idea_data = json.load(f)
        
    title = f"💰 {idea_data.get('title', idea_to_upload.title)}"
    tags = idea_data.get("tags", "")
    
    # Calculate date
    next_schedule = get_next_schedule(store)
    date_str_yt = format_youtube_date(next_schedule)
    time_str_yt = format_youtube_time(next_schedule)
    db_date_str = next_schedule.strftime("%Y-%m-%d")
    
    Messenger.info(f"Subiendo idea {idea_to_upload.id}: '{title}'")
    Messenger.info(f"Se programará para: {date_str_yt} a las {time_str_yt}")
    
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        Messenger.error("Playwright no instalado.")
        return
        
    user_data_dir = str(Path.cwd() / ".browser_profile")
    
    # Preparar directorio de debug
    debug_dir = idea_dir / "debug_screenshots"
    debug_dir.mkdir(exist_ok=True, parents=True)
    step_count = 1
    
    def capture(p_page, name: str):
        nonlocal step_count
        try:
            path = str(debug_dir / f"{step_count:02d}_{name}.png")
            p_page.screenshot(path=path)
            step_count += 1
        except Exception as e:
            Messenger.error(f"[DEBUG] Falló la captura '{name}': {e}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir, 
            headless=False,
            args=["--start-maximized"],
            no_viewport=True
        )
        page = browser.new_page()
        
        with api_spinner("Abriendo YouTube Studio..."):
            Messenger.info("[DEBUG] Navegando a YouTube Studio...")
            page.goto("https://studio.youtube.com/channel/UCz5iw1S4C9BOYeYF5LPovpw/videos/short?d=ud")
            page.wait_for_timeout(5000) # Wait for modal to load properly
            capture(page, "inicio_modal")
            
            # Select file
            Messenger.info("[DEBUG] Subiendo archivo mp4...")
            file_input = page.locator("input[type='file']").first
            file_input.set_input_files(str(video_path))
            
        with api_spinner("Subiendo video y configurando detalles..."):
            # Wait for details screen
            Messenger.info("[DEBUG] Esperando pantalla de Detalles (Buscando textbox del título)...")
            page.wait_for_selector("#textbox", timeout=60000)
            capture(page, "pantalla_detalles")
            
            # Title
            Messenger.info("[DEBUG] Escribiendo título...")
            title_box = page.locator("#textbox").first
            title_box.clear()
            title_box.type(title, delay=50) # Type slowly to trigger React events
            page.wait_for_timeout(1000)
            capture(page, "titulo_escrito")
            
            # Thumbnail
            thumbnail_path = idea_dir / "images" / "thumbnail.jpg"
            if thumbnail_path.exists():
                Messenger.info("[DEBUG] Subiendo miniatura...")
                # El input de miniatura suele tener el ID file-loader o ser el segundo input file de la página
                thumb_input = page.locator("input#file-loader")
                if thumb_input.count() == 0:
                    # Fallback al uploader
                    thumb_input = page.locator("ytcp-thumbnails-compact-editor-uploader input[type='file']")
                
                if thumb_input.count() > 0:
                    thumb_input.set_input_files(str(thumbnail_path))
                    Messenger.info("[DEBUG] Esperando 3 segundos a que cargue la miniatura...")
                    page.wait_for_timeout(3000)
                    capture(page, "miniatura_subida")
                else:
                    Messenger.error("[DEBUG] No se encontró el botón de miniatura.")
            else:
                Messenger.info("[DEBUG] No se encontró miniatura, se omitirá este paso.")
            
            # Playlists (Listas)
            try:
                Messenger.info("[DEBUG] Buscando Listas de Reproducción...")
                # The playlist dropdown usually has an ID or class.
                dropdown = page.locator("div.ytcp-text-dropdown-trigger:has-text('Seleccionar')")
                if dropdown.count() > 0:
                    dropdown.scroll_into_view_if_needed()
                    dropdown.click()
                    page.wait_for_timeout(1000)
                    
                    Messenger.info("[DEBUG] Seleccionando lista 'Shorts'...")
                    # Try to find "Shorts" playlist
                    shorts_list = page.locator("tp-yt-paper-checkbox[aria-label*='Shorts']")
                    if shorts_list.count() > 0:
                        shorts_list.click()
                    else:
                        # Click the first one available
                        first_list = page.locator("tp-yt-paper-checkbox").first
                        if first_list.count() > 0:
                            first_list.click()
                            
                    # Click "Hecho"
                    Messenger.info("[DEBUG] Clic en 'Hecho' (Listas)...")
                    capture(page, "lista_seleccionada")
                    done_btn = page.locator("ytcp-button:has-text('Hecho')")
                    if done_btn.count() > 0:
                        done_btn.click()
            except Exception as e:
                Messenger.error(f"No se pudo seleccionar lista: {e}")
            
            # Tags
            Messenger.info("[DEBUG] Expandiendo 'Mostrar más' para Tags...")
            page.wait_for_timeout(1000)
            
            more_btn = page.locator("ytcp-button#toggle-button") # 'Mostrar más'
            if more_btn.count() > 0:
                more_btn.scroll_into_view_if_needed()
                if more_btn.is_visible():
                    more_btn.click()
                    page.wait_for_timeout(1000)
                
            Messenger.info("[DEBUG] Escribiendo Tags...")
            tags_input = page.locator("input[aria-label*='Etiquetas']")
            if tags_input.count() > 0:
                tags_input.scroll_into_view_if_needed()
                tags_input.type(tags, delay=20)
                tags_input.press("Enter")
                capture(page, "tags_escritos")
                
            # Go to Visibility
            Messenger.info("[DEBUG] Avanzando a la pestaña 'Visibilidad'...")
            # Click Siguiente multiple times until Visibility is active
            for _ in range(3):
                next_btn = page.locator("ytcp-button#next-button")
                if next_btn.is_visible() and not next_btn.is_disabled():
                    next_btn.click()
                    page.wait_for_timeout(1500)
            capture(page, "pestana_visibilidad")
                    
            # Programar
            Messenger.info("[DEBUG] Seleccionando opción 'Programar'...")
            
            # Click #second-container
            programar_container = page.locator("#second-container")
            if programar_container.count() > 0:
                programar_container.scroll_into_view_if_needed()
                programar_container.click(force=True)
                page.wait_for_timeout(1000)
                
                # Date
                Messenger.info("[DEBUG] Estableciendo fecha de programación...")
                datepicker_trigger = page.locator("#datepicker-trigger")
                if datepicker_trigger.count() > 0:
                    datepicker_trigger.click(force=True)
                    page.wait_for_timeout(500)
                    
                    # El input dentro de datepicker
                    date_input = page.locator("ytcp-date-picker #labelAndInputContainer input").last
                    if date_input.count() > 0 and date_input.is_visible():
                        date_input.clear()
                        date_input.type(date_str_yt, delay=50)
                        date_input.press("Enter")
                        page.wait_for_timeout(500)
                        
                # Time
                Messenger.info("[DEBUG] Estableciendo hora de programación...")
                time_container = page.locator("ytcp-form-input-container#time-of-day-container")
                if time_container.count() > 0:
                    time_container.click(force=True)
                    page.wait_for_timeout(500)
                    
                    time_input = time_container.locator("input").last
                    if time_input.count() > 0 and time_input.is_visible():
                        time_input.clear()
                        time_input.type(time_str_yt, delay=50)
                        # Blur to format automatically
                        time_input.press("Enter")
                        page.wait_for_timeout(500)
                        
            capture(page, "fecha_hora_programadas")
            
            # Extract link
            Messenger.info("[DEBUG] Extrayendo enlace del video...")
            link_locator = page.locator(".ytcp-video-info a.style-scope.ytcp-video-info")
            video_url = ""
            if link_locator.count() > 0:
                video_url = link_locator.inner_text()
                    
        # Wait for video upload to finish before saving
        with api_spinner("Finalizando y esperando subida en modal final..."):
            
            # Esperar 1 minuto antes de programar para asegurar avance de subida
            Messenger.info("[DEBUG] Esperando 1 minuto antes de darle a Programar...")
            page.wait_for_timeout(60000)
            
            Messenger.info("[DEBUG] Haciendo clic en botón 'Programar' final...")
            page.wait_for_selector("ytcp-button#done-button:not([disabled])", timeout=60000)
            done_btn = page.locator("ytcp-button#done-button")
            done_btn.scroll_into_view_if_needed()
            done_btn.click(force=True)
            capture(page, "click_programar")
            
            # Si sale el popup "Publicar de todas formas" o "Programar de todas formas"
            page.wait_for_timeout(3000)
            warning_btn = page.locator("ytcp-button", has_text="todas formas")
            if warning_btn.count() > 0 and warning_btn.is_visible():
                Messenger.info("[DEBUG] Apareció popup de advertencia, forzando...")
                warning_btn.click(force=True)
                capture(page, "popup_todas_formas_click")
            
            # Wait for success dialog (o dialog de procesando)
            Messenger.info("[DEBUG] Esperando modal de éxito o progreso...")
            try:
                page.wait_for_selector("ytcp-video-share-dialog, ytcp-dialog[open]", timeout=60000)
            except Exception:
                pass
            capture(page, "modal_exito")
            
            Messenger.info("[DEBUG] Verificando progreso de subida en el modal...")
            for _ in range(120): # Max 10 minutes
                # Verificar si ya está el botón de copiar vínculo (éxito total)
                copy_btn = page.locator("ytcp-icon-button[aria-label*='Copiar']")
                if copy_btn.count() > 0 and copy_btn.first.is_visible():
                    Messenger.info("[DEBUG] Se detectó botón de copiar. Subida y programación exitosa.")
                    # Extraer el enlace final desde el modal por si acaso
                    share_link = page.locator("ytcp-video-share-dialog a.style-scope").first
                    if share_link.count() > 0:
                        video_url = share_link.inner_text()
                    break
                    
                # Si no está el botón, verificar si hay un modal activo con progreso
                dialog_loc = page.locator("ytcp-dialog[open]").last
                if dialog_loc.count() > 0:
                    text = dialog_loc.inner_text().lower()
                    if "subiendo" in text or "procesando" in text or "verificando" in text or "%" in text:
                        if "completad" in text or "finalizad" in text or "se completaron las verificaciones" in text:
                            break
                        page.wait_for_timeout(5000)
                    else:
                        break
                else:
                    break
            
            capture(page, "subida_completada_modal_final")
            
            # Si el botón "Cerrar" está en el modal, cerrarlo de forma segura
            close_btn = page.locator("ytcp-button:has-text('Cerrar')").last
            if close_btn.count() > 0 and close_btn.is_visible():
                close_btn.click(force=True)
            
        Messenger.success("¡Video programado y subido a YouTube exitosamente!")
        
        # Guardar todo
        idea_data["scheduled_date"] = db_date_str
        idea_data["youtube_url"] = video_url
        with open(idea_json_path, "w", encoding="utf-8") as f:
            json.dump(idea_data, f, indent=2, ensure_ascii=False)
            
        idea_to_upload.state = State.UPLOADED
        idea_to_upload.scheduled_date = db_date_str
        store.save(idea_to_upload)
        
        browser.close()

if __name__ == "__main__":
    upload_video()
