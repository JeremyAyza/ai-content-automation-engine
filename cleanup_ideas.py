import os
import shutil
from pathlib import Path

def cleanup_ideas():
    base_dir = Path(__file__).parent / "flows" / "image_content_generator"
    
    # We have out_long and out_short
    out_dirs = [base_dir / "out_long" / "ideas", base_dir / "out_short" / "ideas"]
    
    total_freed = 0
    
    print("Starting cleanup of intermediate video files...")
    
    for out_dir in out_dirs:
        if not out_dir.exists():
            continue
            
        print(f"\nScanning: {out_dir.relative_to(base_dir.parent.parent)}")
        for idea_dir in out_dir.iterdir():
            if not idea_dir.is_dir():
                continue
                
            # Clean videos/
            videos_dir = idea_dir / "videos"
            if videos_dir.exists():
                size = sum(f.stat().st_size for f in videos_dir.rglob('*') if f.is_file())
                total_freed += size
                shutil.rmtree(videos_dir, ignore_errors=True)
                print(f"  [DELETED] {videos_dir.relative_to(out_dir.parent.parent)} ({size / 1024 / 1024:.2f} MB)")
                
            # Clean intermediate editions
            editions_dir = idea_dir / "editions"
            if editions_dir.exists():
                for temp_file in ["raw_video.mp4", "subtitled_video.mp4", "final_audio.wav"]:
                    target_file = editions_dir / temp_file
                    if target_file.exists():
                        size = target_file.stat().st_size
                        total_freed += size
                        target_file.unlink(missing_ok=True)
                        print(f"  [DELETED] {target_file.relative_to(out_dir.parent.parent)} ({size / 1024 / 1024:.2f} MB)")

    print(f"\n✅ Cleanup Complete!")
    print(f"Total space freed: {total_freed / 1024 / 1024 / 1024:.2f} GB")

if __name__ == "__main__":
    cleanup_ideas()
