import os
import shutil
from pathlib import Path

base_dir = Path(r"c:\Users\Jeremy\Documents\LAB\AI-Content-Automation-Engine-main\flows\image_content_generator\out_short\ideas")

for idea_dir in base_dir.glob("idea_*"):
    if idea_dir.is_dir():
        # 1. Delete videos folder
        videos_dir = idea_dir / "videos"
        if videos_dir.exists():
            shutil.rmtree(videos_dir)
            print(f"Deleted {videos_dir}")
        
        # 2. Rename final video in root to prime_...
        for file in idea_dir.glob("*.mp4"):
            if not file.name.startswith("prime_"):
                new_name = idea_dir / f"prime_{file.name}"
                file.rename(new_name)
                print(f"Renamed {file.name} to {new_name.name}")
