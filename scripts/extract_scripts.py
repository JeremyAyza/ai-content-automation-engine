import csv
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FLOWS_DIR = PROJECT_ROOT
OUTPUT_JSON = PROJECT_ROOT / "data" / "extracted_scripts.json"

def main():
    extracted = {}
    
    # Process both short and long
    for prefix in ["short", "long"]:
        out_dir = FLOWS_DIR / f"out_{prefix}"
        ideas_dir = out_dir / "ideas"
        tracking_csv = out_dir / "ideas_tracking.csv"
        
        if not tracking_csv.exists():
            print(f"CSV tracking no encontrado para {prefix}: {tracking_csv}")
            continue
            
        with open(tracking_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['state'] == 'SCRIPT_GENERATED':
                    idea_id = int(row['id'])
                    script_path = ideas_dir / f"idea_{idea_id:06d}" / "script.json"
                    
                    # Usa el prefijo para la clave, ej. "short_32" o "long_32"
                    dict_key = f"{prefix}_{idea_id}"
                    
                    if script_path.exists():
                        try:
                            with open(script_path, 'r', encoding='utf-8') as sf:
                                script_data = json.load(sf)
                            extracted[dict_key] = script_data
                        except Exception as e:
                            print(f"Error al leer script de idea {dict_key}: {e}")
                    else:
                        print(f"script.json no encontrado para idea {dict_key}")
                    
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
        
    print(f"Extracción exitosa: {len(extracted)} scripts guardados en {OUTPUT_JSON.name}")

if __name__ == "__main__":
    main()
