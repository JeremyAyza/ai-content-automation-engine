import csv
import json
from pathlib import Path

PROJECT_ROOT = Path(r"C:\Users\Jeremy\Documents\LAB\AI-Content-Automation-Engine-main")
OUT_SHORT_DIR = PROJECT_ROOT / "flows" / "image_content_generator" / "out_short"
IDEAS_DIR = OUT_SHORT_DIR / "ideas"
TRACKING_CSV = OUT_SHORT_DIR / "ideas_tracking.csv"
OUTPUT_JSON = PROJECT_ROOT / "extracted_scripts.json"

def main():
    extracted = {}
    
    if not TRACKING_CSV.exists():
        print("CSV tracking no encontrado.")
        return
        
    with open(TRACKING_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['state'] == 'SCRIPT_GENERATED':
                idea_id = int(row['id'])
                script_path = IDEAS_DIR / f"idea_{idea_id:06d}" / "script.json"
                
                if script_path.exists():
                    try:
                        with open(script_path, 'r', encoding='utf-8') as sf:
                            script_data = json.load(sf)
                        extracted[str(idea_id)] = script_data
                    except Exception as e:
                        print(f"Error al leer script de idea {idea_id}: {e}")
                else:
                    print(f"script.json no encontrado para idea {idea_id}")
                    
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
        
    print(f"Extracción exitosa: {len(extracted)} scripts guardados en {OUTPUT_JSON.name}")

if __name__ == "__main__":
    main()
