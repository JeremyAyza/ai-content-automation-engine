from flows.pipeline.prompt_base.models import BaseIdea, CategoryHandler
from flows.pipeline.prompt_shorts.tio_warren import (
    constants as tio_warren_constants,
)


class MindsetTioWarrenIdeaShort(BaseIdea):
    """
    Idea model for financial mindset transformation shorts featuring Tio Warren.
    """
    IDEA_PROMPT = tio_warren_constants.IDEA_PROMPT_MINDSET
    financial_problem: str
    mindset_shift: str
    key_principle: str


class StrategyTioWarrenIdeaShort(BaseIdea):
    """
    Idea model for practical financial strategy shorts featuring Tio Warren.
    """
    IDEA_PROMPT = tio_warren_constants.IDEA_PROMPT_ESTRATEGIA
    strategy_name: str
    common_mistake: str
    actionable_tip: str


class TioWarrenHandlerShort(CategoryHandler):
    """
    Specialized handler for Short videos themed around Tio Warren for Código Capital.
    Encapsulates Mindset and Strategy finance variants.
    """

    SCRIPT_PROMPT = tio_warren_constants.SCRIPT_PROMPT
    idea_variants = [
        MindsetTioWarrenIdeaShort,
        StrategyTioWarrenIdeaShort,
    ]
