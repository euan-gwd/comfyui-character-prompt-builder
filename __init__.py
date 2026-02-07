"""
ComfyUI CharacterPromptBuilder
A standalone, modular portrait prompt generator for ComfyUI

Inspired by the original Portrait Master by AI Wiz Art (Stefano Flore)
"""

__version__ = "2.1.0"
__author__ = "Euan Greenwood"

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

# ComfyUI will look for this to serve web assets if needed
WEB_DIRECTORY = "./web"

print(f"\033[92m[CharacterPromptBuilder] v{__version__} loaded successfully\033[0m")
