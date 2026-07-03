from typing import Sequence, Tuple, Type

from flows.pipeline.prompt_base.manager import BasePromptManager
from flows.pipeline.prompt_base.models import (
    BaseIdea,
    CategoryHandler,
    VideoScript,
)
from flows.pipeline.prompt_shorts.finances import (
    constants as finances_constants,
)
from flows.pipeline.prompt_shorts.finances.models import FinancesHandler
from flows.pipeline.prompt_shorts.sprunkis.models import SprunkisHandler
from tools.common.messenger import Messenger
from tools.text_generation.gemini import GeminiTextGenerator


from flows.pipeline.prompt_shorts.sprunkis import constants as sprunkis_constants

class PromptManagerShorts(BasePromptManager):
    """Manager specific to Short videos (9:16), aggregating modular categories."""

    # Voice & audio style (We use the Sprunkis fast-paced audio prompt)
    AUDIO_PROMPT: str = finances_constants.AUDIO_PROMPT

    CATEGORIES: Sequence[Type[CategoryHandler]] = [
        FinancesHandler,  # Comentado para enfocarnos en Sprunkis
        # SprunkisHandler,
    ]

    def generate_full_story(
        self, content_gen: GeminiTextGenerator, ideas_bank_path: Path = None
    ) -> Tuple[BaseIdea, VideoScript, str]:
        """
        Executes the generation loop in 3 steps:
        1. Random Selection: Pick a category config.
        2. Idea Generation: Prompt for initial idea (seeded by bank if available).
        3. Script Generation: Build structured script from idea.
        """
        # 1. Random Selection
        config = self.select_random_config()

        # 2. Idea Generation
        idea_prompt = config.idea_prompt
        if ideas_bank_path:
            idea_base = self._get_idea_from_bank(ideas_bank_path)
            if idea_base:
                idea_prompt += f"\n\n**INSPIRACIÓN REFERENCIAL:** Basa tu idea estrictamente en el siguiente concepto central: '{idea_base}'.\n"

        import time
        idea_data = content_gen.generate_text(idea_prompt, config.idea_model)


        # 3. Script Generation
        Messenger.info(f"\n--- Generating script for: {idea_data.title} ---")
        script_prompt = config.handler.get_full_script_prompt(idea_data)
        Messenger.info(script_prompt)
        script = content_gen.generate_text(script_prompt, VideoScript)

        return idea_data, script, config.category
