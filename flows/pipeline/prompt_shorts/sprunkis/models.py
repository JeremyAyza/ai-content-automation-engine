from flows.pipeline.prompt_base.models import BaseIdea, CategoryHandler
from flows.pipeline.prompt_shorts.sprunkis import (
    constants as sprunkis_constants,
)


class SprunkiViralIdea(BaseIdea):
    """
    Idea model for viral, hyperactive kids' shorts featuring Sprunkis.
    """
    IDEA_PROMPT = sprunkis_constants.IDEA_PROMPT_VIRAL
    absurd_situation: str
    main_sprunkis_involved: list[str]
    call_to_action: str


class SprunkisHandler(CategoryHandler):
    """
    Specialized handler for Sprunkis-themed viral short videos.
    """

    SCRIPT_PROMPT = sprunkis_constants.SCRIPT_PROMPT
    idea_variants = [
        SprunkiViralIdea,
    ]
