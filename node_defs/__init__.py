"""
Character Prompt Builder Node Definitions Package
"""

from .person import CharacterPromptBuilderPerson
from .person import NODE_CLASS_MAPPINGS as PERSON_CLASS_MAPPINGS
from .person import NODE_DISPLAY_NAME_MAPPINGS as PERSON_DISPLAY_NAME_MAPPINGS

__all__ = [
    "CharacterPromptBuilderPerson",
    "PERSON_CLASS_MAPPINGS",
    "PERSON_DISPLAY_NAME_MAPPINGS",
]
