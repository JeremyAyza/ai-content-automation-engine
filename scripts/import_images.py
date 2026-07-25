import csv
import json
import shutil
from pathlib import Path

# Paths
DOWNLOADS_DIR = Path(r"C:\Users\Jeremy\Downloads\Flow_Generations")
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FLOWS_DIR = PROJECT_ROOT / "flows"
REPORT_CSV = PROJECT_ROOT / "data" / "import_report.csv"

def get_tracking_csv(prefix: str) -> Path:
    return FLOWS_DIR / f"out_{prefix}" / "ideas_tracking.csv"

def update_csv_state(prefix: str, idea_id: int, new_state: str):
    """Updates the state of an idea in the corresponding ideas_tracking.csv file."""
    tracking_csv = get_tracking_csv(prefix)
    rows = []
    updated = False
    
    with open(tracking_csv, 'r', encoding='utf-8') as f:
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
        with open(tracking_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def get_script_generated_ids(prefix: str) -> set[int]:
    """Returns a set of idea IDs that are currently in SCRIPT_GENERATED state for a prefix."""
    valid_ids = set()
    tracking_csv = get_tracking_csv(prefix)
    if not tracking_csv.exists():
        return valid_ids
    with open(tracking_csv, 'r', encoding='utf-8') as f:
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
    
    valid_ids_short = get_script_generated_ids("short")
    valid_ids_long = get_script_generated_ids("long")
    
    print(f"Found {len(valid_ids_short)} short ideas and {len(valid_ids_long)} long ideas in SCRIPT_GENERATED state.")
    print("Starting image import process...")
    
    for source_folder in DOWNLOADS_DIR.iterdir():
        if not source_folder.is_dir():
            continue
            
        folder_name = source_folder.name
        parts = folder_name.split("_")
        
        # Parse prefix and ID, format expected: short_32_title or long_10_title
        if len(parts) < 2 or parts[0] not in ["short", "long"] or not parts[1].isdigit():
            report_data.append([folder_name, "N/A", "IGNORED", "Folder name format invalid (expected short_ID_... or long_ID_...)"])
            continue
            
        prefix = parts[0]
        idea_id = int(parts[1])
        dict_key = f"{prefix}_{idea_id}"
        
        valid_ids = valid_ids_short if prefix == "short" else valid_ids_long
        
        # Filter: if not in the valid list, ignore
        if idea_id not in valid_ids:
            continue
            
        idea_path = FLOWS_DIR / f"out_{prefix}" / "ideas" / f"idea_{idea_id:06d}"
        
        if not idea_path.exists():
            report_data.append([folder_name, dict_key, "FAILED", "Idea folder does not exist"])
            continue
            
        script_path = idea_path / "script.json"
        if not script_path.exists():
            report_data.append([folder_name, dict_key, "FAILED", "script.json not found"])
            continue
            
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                script_data = json.load(f)
            expected_count = len(script_data.get("scenes", []))
            if script_data.get("thumbnail_prompt"):
                expected_count += 1
        except Exception as e:
            report_data.append([folder_name, dict_key, "FAILED", f"Error reading script.json: {str(e)}"])
            continue
            
        # Count images in source folder
        images = [img for img in source_folder.glob("*.*") if img.is_file() and img.suffix.lower() in ['.jpg', '.jpeg', '.png']]
        
        if len(images) != expected_count:
            report_data.append([folder_name, dict_key, "FAILED", f"Image count mismatch. Expected: {expected_count}, Found: {len(images)}"])
            continue
            
        # Copy images without renaming
        dest_images_dir = idea_path / "images"
        dest_images_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            for img in images:
                shutil.copy2(img, dest_images_dir / img.name)
        except Exception as e:
            report_data.append([folder_name, dict_key, "FAILED", f"Error copying images: {str(e)}"])
            continue
            
        # Update state
        try:
            update_csv_state(prefix, idea_id, "IMAGES_GENERATED")
            report_data.append([folder_name, dict_key, "SUCCESS", f"Imported {len(images)} images"])
            print(f"Successfully imported images for idea {dict_key}")
        except Exception as e:
            report_data.append([folder_name, dict_key, "FAILED", f"Error updating CSV: {str(e)}"])

    # Generate Report
    with open(REPORT_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Source Folder", "Idea ID", "Status", "Reason"])
        writer.writerows(report_data)
        
    print(f"\nImport complete. Report generated at: {REPORT_CSV}")

if __name__ == "__main__":
    main()
