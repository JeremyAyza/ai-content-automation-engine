import sys
from pathlib import Path

def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright no está instalado. Ejecuta: poetry add playwright && poetry run playwright install chromium")
        sys.exit(1)

    # El mismo directorio que usa pipeline.py
    user_data_dir = str(Path.cwd() / ".browser_profile")
    
    # URL de Flow
    from pipeline import config
    target_url = config.FLOW_PROJECT_URL
    if not target_url:
        raise SystemExit("Configura FLOW_PROJECT_URL en .env antes de iniciar sesión.")

    print("=====================================================")
    print("🚀 INICIADOR DE SESIÓN DE PLAYWRIGHT")
    print("=====================================================")
    print("1. Se abrirá una ventana de Chrome.")
    print("2. Inicia sesión en tu cuenta de Google.")
    print("3. Asegúrate de que cargue correctamente la plataforma Flow.")
    print("4. Cierra la ventana del navegador manualmente cuando termines.")
    print("=====================================================\n")

    with sync_playwright() as p:
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir,
            channel="chrome", # Use the installed Chrome so the sign-in page accepts the browser
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
            # No cargamos la extensión aquí para que no interfiera, 
            # solo nos importa guardar las cookies de la sesión de Google.
        )
        page = browser_context.new_page()
        page.goto(target_url)
        
        # Esperar infinitamente hasta que el usuario cierre la página
        try:
            page.wait_for_event("close", timeout=0)
        except Exception:
            pass
            
        browser_context.close()
        print("\n✅ Sesión guardada en .browser_profile. Ya puedes usar 'generate short s2'.")

if __name__ == "__main__":
    main()
