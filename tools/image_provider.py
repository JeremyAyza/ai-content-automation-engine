from abc import ABC, abstractmethod
from typing import Any, List
from pathlib import Path
from pydantic import BaseModel, ConfigDict

class ImageTask(BaseModel):
    """
    Represents a single image generation task for batch processing.
    """
    prompt: str
    output_path: Path
    scene_number: int = 1 # Used primarily by Playwright to track images

class ImageProvider(BaseModel, ABC):
    """
    Base interface for all Image Generators (API, Playwright extension, etc.)
    """
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="ignore")

    @abstractmethod
    def generate_images(self, tasks: List[Any]) -> None:
        """
        Processes a list of image generation tasks. 
        Each task contains at minimum: prompt, output_path, scene_number
        """
        pass

class ImageProviderFactory:
    @staticmethod
    def get_provider(provider_name: str, **kwargs) -> ImageProvider:
        """
        Instantiates and returns the appropriate ImageProvider based on the config.
        """
        provider_name = provider_name.lower().strip()
        
        if provider_name == "api":
            from tools.gemini_image import GeminiImageGenerator
            return GeminiImageGenerator(**kwargs)
        elif provider_name == "playwright":
            from tools.playwright_image import PlaywrightImageGenerator
            return PlaywrightImageGenerator(**kwargs)
        else:
            raise ValueError(f"Unknown image provider: {provider_name}")
