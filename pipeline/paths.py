from pathlib import Path
from tools.text_utils import slugify
from pipeline import config

class PipelinePaths:
    """
    Handles all path resolution logic for the Pipeline.
    """
    def __init__(self, out_base: Path):
        self.out_base = out_base

    def get_out_dir(self) -> Path:
        """Returns the absolute path to the base output directory."""
        self.out_base.mkdir(parents=True, exist_ok=True)
        return self.out_base

    def get_ideas_dir(self) -> Path:
        """Returns the absolute path to the global ideas folder."""
        path = self.get_out_dir() / config.IDEAS_DIR
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_idea_path(self, idea_id: int) -> Path:
        """Returns the absolute path to an idea's folder."""
        folder_name = f"idea_{idea_id:06d}"
        path = self.get_ideas_dir() / folder_name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_idea_subdir(self, idea_id: int, subdir: str) -> Path:
        """Returns the absolute path to a subdirectory within an idea's folder"""
        path = self.get_idea_path(idea_id) / subdir
        path.mkdir(parents=True, exist_ok=True)
        return path

    def get_idea_asset_path(self, idea_id: int, subdir: str, filename: str) -> Path:
        """Returns the absolute path to a file within an idea's subdirectory."""
        if not subdir:
            return self.get_idea_path(idea_id) / filename
        return self.get_idea_subdir(idea_id, subdir) / filename

    def get_named_video_path(self, idea_id: int, title: str) -> Path:
        """Derives the path for the final named video based on the idea title."""
        title_slug = slugify(title)
        return self.get_idea_path(idea_id) / f"{title_slug}.mp4"
