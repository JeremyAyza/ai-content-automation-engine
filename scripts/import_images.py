import csv
import json
import shutil
from pathlib import Path

# Paths
DOWNLOADS_DIR = Path(r"C:\Users\Jeremy\Downloads\Flow_Generations")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT_SHORT_DIR = PROJECT_ROOT / "flows" / "out_short"
IDEAS_DIR = OUT_SHORT_DIR / "ideas"
TRACKING_CSV = OUT_SHORT_DIR / "ideas_tracking.csv"
REPORT_CSV = PROJECT_ROOT / "import_report.csv"

def update_csv_state(idea_id: int, new_state: str):
    """Updates the state of an idea in the ideas_tracking.csv file."""
    rows = []
    updated = False
    
    with open(TRACKING_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)
        for row in reader:
            if not row:
                continue
            if int(row[0]) == idea_id:
                row[2] = new_state
                updated = True
            rows.append(row)
            
    if updated:
        with open(TRACKING_CSV, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def get_script_generated_ids() -> set[int]:
    """Returns a set of idea IDs that are currently in SCRIPT_GENERATED state."""
    valid_ids = set()
    if not TRACKING_CSV.exists():
        return valid_ids
    with open(TRACKING_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header
        for row in reader:
            if row and row[2] == "SCRIPT_GENERATED":
                valid_ids.add(int(row[0]))
    return valid_ids

def main():
    if not DOWNLOADS_DIR.exists():
        print(f"Directory not found: {DOWNLOADS_DIR}")
        return

    report_data = []
    
    valid_ids = get_script_generated_ids()
    print(f"Found {len(valid_ids)} ideas in SCRIPT_GENERATED state.")
    
    print("Starting image import process...")
    for source_folder in DOWNLOADS_DIR.iterdir():
        if not source_folder.is_dir():
            continue
            
        folder_name = source_folder.name
        parts = folder_name.split("_")
        if len(parts) < 2 or not parts[0].isdigit():
            continue
            
        idea_id = int(parts[0])
        
        # Filtrar desde el inicio: si no está en la lista de válidos, lo ignoramos por completo
        if idea_id not in valid_ids:
            continue
            
        idea_path = IDEAS_DIR / f"idea_{idea_id:06d}"
        
        if not idea_path.exists():
            report_data.append([folder_name, idea_id, "FAILED", "Idea folder does not exist"])
            continue
            
        script_path = idea_path / "script.json"
        if not script_path.exists():
            report_data.append([folder_name, idea_id, "FAILED", "script.json not found"])
            continue
            
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                script_data = json.load(f)
            expected_count = len(script_data.get("scenes", []))
        except Exception as e:
            report_data.append([folder_name, idea_id, "FAILED", f"Error reading script.json: {str(e)}"])
            continue
            
        # Count images in source folder
        images = [img for img in source_folder.glob("*.*") if img.is_file() and img.suffix.lower() in ['.jpg', '.jpeg', '.png']]
        
        if len(images) != expected_count:
            report_data.append([folder_name, idea_id, "FAILED", f"Image count mismatch. Expected: {expected_count}, Found: {len(images)}"])
            continue
            
        # Copy images without renaming
        dest_images_dir = idea_path / "images"
        dest_images_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            for img in images:
                shutil.copy2(img, dest_images_dir / img.name)
        except Exception as e:
            report_data.append([folder_name, idea_id, "FAILED", f"Error copying images: {str(e)}"])
            continue
            
        # Update state
        try:
            update_csv_state(idea_id, "IMAGES_GENERATED")
            report_data.append([folder_name, idea_id, "SUCCESS", f"Imported {len(images)} images"])
            print(f"Successfully imported images for idea {idea_id}")
        except Exception as e:
            report_data.append([folder_name, idea_id, "FAILED", f"Error updating CSV: {str(e)}"])

    # Generate Report
    with open(REPORT_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Source Folder", "Idea ID", "Status", "Reason"])
        writer.writerows(report_data)
        
    print(f"\nImport complete. Report generated at: {REPORT_CSV}")

if __name__ == "__main__":
    main()
