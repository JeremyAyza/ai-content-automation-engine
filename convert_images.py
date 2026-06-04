import os
from pathlib import Path
from PIL import Image

base_dir = Path(r"c:\Users\Jeremy\Documents\LAB\AI-Content-Automation-Engine-main\flows\image_content_generator\out_short\ideas")

count = 0
for idea_dir in base_dir.glob("idea_*"):
    images_dir = idea_dir / "images"
    if images_dir.exists():
        for png_file in images_dir.glob("*.png"):
            # Open and save as actual JPG to be safe with FFmpeg
            img = Image.open(png_file)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            jpg_file = png_file.with_suffix(".jpg")
            img.save(jpg_file, "JPEG")
            png_file.unlink() # delete the original png
            count += 1

print(f"Successfully converted {count} images to JPG.")
