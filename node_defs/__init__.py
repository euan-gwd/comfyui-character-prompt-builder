"""
Character Prompt Builder Node Definitions Package
"""

from .female_person import CharacterPromptBuilderFemalePerson
from .female_person import NODE_CLASS_MAPPINGS as FEMALE_PERSON_CLASS_MAPPINGS
from .female_person import NODE_DISPLAY_NAME_MAPPINGS as FEMALE_PERSON_DISPLAY_NAME_MAPPINGS

from .male_person import CharacterPromptBuilderMalePerson
from .male_person import NODE_CLASS_MAPPINGS as MALE_PERSON_CLASS_MAPPINGS
from .male_person import NODE_DISPLAY_NAME_MAPPINGS as MALE_PERSON_DISPLAY_NAME_MAPPINGS

from .female_fashion import CharacterPromptBuilderFemaleFashion
from .female_fashion import NODE_CLASS_MAPPINGS as FEMALE_FASHION_CLASS_MAPPINGS
from .female_fashion import NODE_DISPLAY_NAME_MAPPINGS as FEMALE_FASHION_DISPLAY_NAME_MAPPINGS

from .male_fashion import CharacterPromptBuilderMaleFashion
from .male_fashion import NODE_CLASS_MAPPINGS as MALE_FASHION_CLASS_MAPPINGS
from .male_fashion import NODE_DISPLAY_NAME_MAPPINGS as MALE_FASHION_DISPLAY_NAME_MAPPINGS

from .female_poses import CharacterPromptBuilderFemalePoses
from .female_poses import NODE_CLASS_MAPPINGS as FEMALE_POSES_CLASS_MAPPINGS
from .female_poses import NODE_DISPLAY_NAME_MAPPINGS as FEMALE_POSES_DISPLAY_NAME_MAPPINGS

from .male_poses import CharacterPromptBuilderMalePoses
from .male_poses import NODE_CLASS_MAPPINGS as MALE_POSES_CLASS_MAPPINGS
from .male_poses import NODE_DISPLAY_NAME_MAPPINGS as MALE_POSES_DISPLAY_NAME_MAPPINGS

__all__ = [
    "CharacterPromptBuilderFemalePerson",
    "CharacterPromptBuilderMalePerson",
    "CharacterPromptBuilderFemaleFashion",
    "CharacterPromptBuilderMaleFashion",
    "CharacterPromptBuilderFemalePoses",
    "CharacterPromptBuilderMalePoses",
    "FEMALE_PERSON_CLASS_MAPPINGS",
    "FEMALE_PERSON_DISPLAY_NAME_MAPPINGS",
    "MALE_PERSON_CLASS_MAPPINGS",
    "MALE_PERSON_DISPLAY_NAME_MAPPINGS",
    "FEMALE_FASHION_CLASS_MAPPINGS",
    "FEMALE_FASHION_DISPLAY_NAME_MAPPINGS",
    "MALE_FASHION_CLASS_MAPPINGS",
    "MALE_FASHION_DISPLAY_NAME_MAPPINGS",
    "FEMALE_POSES_CLASS_MAPPINGS",
    "FEMALE_POSES_DISPLAY_NAME_MAPPINGS",
    "MALE_POSES_CLASS_MAPPINGS",
    "MALE_POSES_DISPLAY_NAME_MAPPINGS",
]
