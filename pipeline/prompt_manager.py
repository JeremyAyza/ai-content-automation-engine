from pathlib import Path
from typing import Sequence, Tuple, Type
import random

from pipeline.schemas import (
    BaseIdea,
    CategoryHandler,
    VideoScript,
    SelectedConfig,
    VideoOrientation,
)
from pipeline.channels import base as base_constants
from tools.messenger import Messenger
from tools.gemini_text import GeminiTextGenerator
from tools.whisper_schemas import WhisperTranscriptionSegment

# Import all channels dynamically
from pipeline.channels.tio_warren_short import TioWarrenHandlerShort
from pipeline.channels.finances_short import FinancesHandler as FinancesHandlerShort
# from pipeline.channels.sprunkis_short import SprunkisHandler
from pipeline.channels.tio_warren_long import TioWarrenHandlerLong
from pipeline.channels.finances_long import FinancesHandlerLong

class PromptManager:
    """
    Unified Prompt Manager for both Shorts and Longs.
    Handles dynamic category routing and common prompt logic.
    """
    def __init__(self, orientation: VideoOrientation):
        self.orientation = orientation
        self.VOICE_NAME = "Charon"
        
        if self.orientation == VideoOrientation.SHORT:
            self.CATEGORIES: Sequence[Type[CategoryHandler]] = [
                TioWarrenHandlerShort,
                # FinancesHandlerShort,
                # SprunkisHandler,
            ]
            # Use short-specific audio prompt logic if needed
            self.AUDIO_PROMPT = base_constants.AUDIO_PROMPT
            
        elif self.orientation == VideoOrientation.LONG:
            self.CATEGORIES: Sequence[Type[CategoryHandler]] = [
                TioWarrenHandlerLong,
                # FinancesHandlerLong,
            ]
            self.AUDIO_PROMPT = base_constants.AUDIO_PROMPT
            
        else:
            raise ValueError(f"Orientation {self.orientation} not supported.")

    def select_random_config(self) -> SelectedConfig:
        """Picks a random handler and idea variant, returning a unified configuration object."""
        selected_category = random.choice(self.CATEGORIES)
        idea_model = selected_category.get_random_idea_variant()

        return SelectedConfig(
            category=f"{selected_category.__name__}_{idea_model.__name__}",
            handler=selected_category,
            idea_prompt=idea_model.get_idea_prompt(),
            idea_model=idea_model,
        )

    def get_audio_prompt(self, audio_text: str) -> str:
        """Formats the audio prompt."""
        return self.AUDIO_PROMPT.format(audio_text=audio_text)

    def get_alignment_prompt(
        self,
        whisper_segments: Sequence[WhisperTranscriptionSegment],
        script_scenes: Sequence[str],
    ) -> str:
        """Formats the alignment prompt."""
        whisper_data = "\n".join([
            f"[{s.start:.3f}s-{s.end:.3f}s] {s.text}"
            for s in whisper_segments
        ])
        scenes_data = "\n".join([
            f"Escena {i+1}: {text}"
            for i, text in enumerate(script_scenes)
        ])
        return base_constants.ALIGNMENT_PROMPT.format(
            whisper_data=whisper_data,
            scenes_data=scenes_data,
            expected_count=len(script_scenes)
        )

    def _get_idea_from_bank(self, bank_path: Path) -> str:
        """Reads the ideas bank (CSV), finds an unused idea, marks it as used, and returns it."""
        import csv
        if not bank_path.exists():
            return ""

        try:
            rows = []
            selected_idea = ""
            updated = False
            
            with open(bank_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or ["idea_base", "used"]
                for row in reader:
                    if not updated and row.get("used", "false").lower() in ("false", "0", ""):
                        selected_idea = row.get("idea_base", "")
                        row["used"] = "true"
                        updated = True
                    rows.append(row)
                    
            if updated:
                with open(bank_path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
                Messenger.info(f"💡 Banco de Ideas: Usando idea base '{selected_idea}'")
                return selected_idea

            Messenger.warning("💡 Banco de Ideas: Todas las ideas han sido usadas. Se generará una idea aleatoria.")
            return ""
        except Exception as e:
            Messenger.error(f"Error reading ideas bank: {e}")
            return ""

    def generate_full_story(
        self, content_gen: GeminiTextGenerator, ideas_bank_path: Path = None
    ) -> Tuple[BaseIdea, VideoScript, str]:
        """
        Executes the generation loop in 3 steps:
        1. Random Selection: Pick a category config.
        2. Idea Generation: Prompt for initial idea (seeded by bank if available).
        3. Script Generation: Build structured script from idea.
        """
        config = self.select_random_config()
        idea_prompt = config.idea_prompt
        
        if ideas_bank_path:
            idea_base = self._get_idea_from_bank(ideas_bank_path)
            if idea_base:
                idea_prompt += f"\n\n**INSPIRACIÓN REFERENCIAL:** Basa tu idea estrictamente en el siguiente concepto central: '{idea_base}'.\n"

        idea_data = content_gen.generate_text(idea_prompt, config.idea_model)

        Messenger.info(f"\n--- Generating script for: {idea_data.title} ---")
        script_prompt = config.handler.get_full_script_prompt(idea_data)
        Messenger.info(script_prompt)
        script = content_gen.generate_text(script_prompt, VideoScript)

        return idea_data, script, config.category
