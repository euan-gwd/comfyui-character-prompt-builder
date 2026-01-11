"""
ComfyUI CharacterPromptBuilder
A standalone, modular portrait prompt generator for ComfyUI

Forked from comfyui-easy-use
Original Portrait Master by AI Wiz Art (Stefano Flore)
"""

__version__ = "1.0.0"
__author__ = "Forked from AI Wiz Art (Stefano Flore)"

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# ComfyUI will look for this to serve web assets if needed
WEB_DIRECTORY = "./web"

print(f"\033[92m[CharacterPromptBuilder] v{__version__} loaded successfully\033[0m")
