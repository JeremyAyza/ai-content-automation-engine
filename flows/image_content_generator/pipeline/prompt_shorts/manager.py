from typing import Sequence, Tuple, Type

from flows.image_content_generator.pipeline.prompt_base.manager import BasePromptManager
from flows.image_content_generator.pipeline.prompt_base.models import (
    BaseIdea,
    CategoryHandler,
    VideoScript,
)
from flows.image_content_generator.pipeline.prompt_shorts.finances import (
    constants as finances_constants,
)
from flows.image_content_generator.pipeline.prompt_shorts.finances.models import FinancesHandler
from flows.image_content_generator.pipeline.prompt_shorts.sprunkis.models import SprunkisHandler
from tools.common.messenger import Messenger
from tools.text_generation.gemini import GeminiTextGenerator


from flows.image_content_generator.pipeline.prompt_shorts.sprunkis import constants as sprunkis_constants

from pathlib import Path
import json

class PromptManagerShorts(BasePromptManager):
    """Manager specific to Short videos (9:16), aggregating modular categories."""

    # Voice & audio style (We use the Sprunkis fast-paced audio prompt)
    AUDIO_PROMPT: str = finances_constants.AUDIO_PROMPT

    CATEGORIES: Sequence[Type[CategoryHandler]] = [
        FinancesHandler,  # Comentado para enfocarnos en Sprunkis
        # SprunkisHandler,
    ]

    def _get_idea_from_bank(self, bank_path: Path) -> str:
        """Reads the ideas bank, finds an unused idea, marks it as used, and returns it."""
        if not bank_path.exists():
            return ""

        try:
            with open(bank_path, 'r', encoding='utf-8') as f:
                ideas = json.load(f)

            for idea in ideas:
                if not idea.get("used", True):
                    idea["used"] = True
                    # Save back to file
                    with open(bank_path, 'w', encoding='utf-8') as f:
                        json.dump(ideas, f, indent=2, ensure_ascii=False)
                    Messenger.info(f"💡 Banco de Ideas: Usando idea base '{idea['idea_base']}'")
                    return idea.get("idea_base", "")

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
        # 1. Random Selection
        config = self.select_random_config()

        # 2. Idea Generation
        idea_prompt = config.idea_prompt
        if ideas_bank_path:
            idea_base = self._get_idea_from_bank(ideas_bank_path)
            if idea_base:
                idea_prompt += f"\n\n**INSPIRACIÓN REFERENCIAL:** Basa tu idea estrictamente en el siguiente concepto central: '{idea_base}'.\n"

        idea_data = content_gen.generate_text(idea_prompt, config.idea_model)

        # 3. Script Generation
        Messenger.info(f"\n--- Generating script for: {idea_data.title} ---")
        script_prompt = config.handler.get_full_script_prompt(idea_data)
        Messenger.info(script_prompt)
        script = content_gen.generate_text(script_prompt, VideoScript)

        return idea_data, script, config.category
