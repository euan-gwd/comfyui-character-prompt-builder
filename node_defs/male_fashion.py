"""
Character Prompt Builder - Male Fashion Node
"""

import json
import os
from urllib.request import urlopen

# Get the directory where the main package is located
RESOURCES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "resources")


def _load_character_data():
    """Load character prompt data from local file or download if missing."""
    prompt_path = os.path.join(RESOURCES_DIR, 'character_prompt.json')
    if not os.path.exists(prompt_path):
        try:
            response = urlopen('https://raw.githubusercontent.com/euan-gwd/comfyui-character-prompt-builder/main/resources/character_prompt.json')
            temp_prompt = json.loads(response.read())
            prompt_serialized = json.dumps(temp_prompt, indent=4)
            with open(prompt_path, "w") as f:
                f.write(prompt_serialized)
            del response, temp_prompt
        except Exception as e:
            print(f"[CharacterPromptBuilder] Warning: Could not download character data: {e}")
            return {}

    with open(prompt_path, 'r') as f:
        return json.load(f)


class CharacterPromptBuilderMaleFashion:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})

        return {
            "required": {
                "fashion_aesthetic": combo("mens_fashion_aesthetic_list"),
                "tops": combo("tops_list"),
                "tops_color": combo("tops_color_list"),
                "tops_material": combo("tops_material_list"),
                "pants": combo("pants_list"),
                "pants_color": combo("pants_color_list"),
                "pants_material": combo("pants_material_list"),
                "capes": combo("capes_list"),
                "capes_color": combo("capes_color_list"),
                "capes_material": combo("capes_material_list"),
                "hats": combo("hats_list"),
                "hats_color": combo("hats_color_list"),
                "mens_suits": combo("mens_suits_list"),
            },
            "optional": {
                "mens_shoes": combo("mens_shoes_list"),
                "mens_shoe_color": combo("mens_shoe_color_list"),
                "mens_shoe_material": combo("mens_shoe_material_list"),
                "mens_gloves": combo("mens_gloves_list"),
                "mens_gloves_color": combo("mens_gloves_color_list"),
                "mens_gloves_material": combo("mens_gloves_material_list"),
                "necklace": combo("necklace_list"),
                "bracelet": combo("bracelet_list"),
                "watches": combo("watches_list"),
                "watches_color": combo("watches_color_list"),
                "ring": combo("ring_list"),
                "settings_in": ("PM_SETTINGS",),
                "mens_glasses": combo("mens_glasses_list"),
                "mens_glasses_color": combo("mens_glasses_color_list"),
                "custom_clothing": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Enter custom outfit"
                    }
                ),
            }
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self,
            fashion_aesthetic="-",
            tops="-", tops_color="-", tops_material="-",
            pants="-", pants_color="-", pants_material="-",
            capes="-", capes_color="-", capes_material="-",
            hats="-", hats_color="-",
            mens_suits="-",
            mens_shoes="-", mens_shoe_color="-", mens_shoe_material="-",
            mens_gloves="-", mens_gloves_color="-", mens_gloves_material="-",
            necklace="-", bracelet="-", ring="-",
            watches="-", watches_color="-",
            settings_in=None,
            mens_glasses="-", mens_glasses_color="-",
            custom_clothing="",
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "fashion_aesthetic": fashion_aesthetic,
            "tops": tops, "tops_color": tops_color, "tops_material": tops_material,
            "pants": pants, "pants_color": pants_color, "pants_material": pants_material,
            "capes": capes, "capes_color": capes_color, "capes_material": capes_material,
            "hats": hats, "hats_color": hats_color,
            "mens_suits": mens_suits,
            "mens_shoes": mens_shoes, "mens_shoe_color": mens_shoe_color, "mens_shoe_material": mens_shoe_material,
            "mens_gloves": mens_gloves, "mens_gloves_color": mens_gloves_color,
            "mens_gloves_material": mens_gloves_material,
            "necklace": necklace,
            "bracelet": bracelet,
            "watches": watches,
            "watches_color": watches_color,
            "ring": ring,
            "mens_glasses": mens_glasses,
            "mens_glasses_color": mens_glasses_color,
            "custom_clothing": custom_clothing,
        })
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Male Fashion": CharacterPromptBuilderMaleFashion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Male Fashion": "Character Prompt Builder - Male Fashion",
}
