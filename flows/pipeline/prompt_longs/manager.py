import random
from pathlib import Path
from typing import List, Sequence, Tuple, Type

from flows.pipeline.prompt_base.manager import BasePromptManager
from flows.pipeline.prompt_base.models import (
    BaseIdea,
    CategoryHandler,
    Scene,
    VideoScript,
)
from flows.pipeline.prompt_longs.finances import (
    constants as finances_long_constants,
)
from flows.pipeline.prompt_longs.finances.models import FinancesHandlerLong
from tools.common.messenger import Messenger
from tools.text_generation.gemini import GeminiTextGenerator


class PromptManagerLongs(BasePromptManager):
    """Manager specific to Long videos (16:9), aggregating modular categories."""

    AUDIO_PROMPT: str = finances_long_constants.AUDIO_PROMPT

    CATEGORIES: Sequence[Type[CategoryHandler]] = [
        FinancesHandlerLong,
    ]

    def generate_full_story(
        self, text_gen: GeminiTextGenerator, ideas_bank_path: Path = None
    ) -> Tuple[BaseIdea, VideoScript, str]:
        """
        Executes the generation loop in 3 steps:
        1. Random Selection: Pick a category config.
        2. Idea Generation: Prompt for initial idea (seeded by bank if available).
        3. Script Generation: Build multi-chunk script from idea.
        """
        # 1. Random Selection
        config = self.select_random_config()

        # 2. Idea Generation
        idea_prompt = config.idea_prompt
        if ideas_bank_path:
            idea_base = self._get_idea_from_bank(ideas_bank_path)
            if idea_base:
                idea_prompt += f"\n\n**INSPIRACIÓN REFERENCIAL:** Basa tu idea estrictamente en el siguiente concepto central: '{idea_base}'.\n"

        idea_data = text_gen.generate_text(idea_prompt, config.idea_model)

        # 3. Script Generation
        Messenger.info(f"\n--- Generating script for: {idea_data.title} ---")
        script_prompt = config.handler.get_full_script_prompt(idea_data)
        Messenger.info(script_prompt)
        script = text_gen.generate_text(script_prompt, VideoScript)

        return idea_data, script, config.category
