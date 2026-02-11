"""
Character Prompt Builder - Female Fashion Node
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


class CharacterPromptBuilderFemaleFashion:
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
                "fashion_aesthetic": combo("fashion_aesthetic_list"),
                "tops": combo("tops_list"),
                "tops_color": combo("tops_color_list"),
                "tops_material": combo("tops_material_list"),
                "pants": combo("pants_list"),
                "pants_color": combo("pants_color_list"),
                "pants_material": combo("pants_material_list"),
                "dresses": combo("dresses_list"),
                "dresses_color": combo("dresses_color_list"),
                "dresses_material": combo("dresses_material_list"),
                "legs": combo("legs_list"),
                "legs_color": combo("legs_color_list"),
                "underwear": combo("underwear_list"),
                "underwear_color": combo("underwear_color_list"),
                "underwear_material": combo("underwear_material_list"),
                "capes": combo("capes_list"),
                "capes_color": combo("capes_color_list"),
                "capes_material": combo("capes_material_list"),
                "hats": combo("hats_list"),
                "hats_color": combo("hats_color_list"),
                "womens_suits": combo("womens_suits_list"),
                "womens_suits_primary_color": combo("womens_suits_primary_color_list"),
                "womens_suits_accent_color": combo("womens_suits_accent_color_list")
            },
            "optional": {
                "womens_shoes": combo("womens_shoes_list"),
                "womens_shoe_color": combo("womens_shoe_color_list"),
                "womens_shoe_material": combo("womens_shoe_material_list"),
                "womens_gloves": combo("womens_gloves_list"),
                "womens_gloves_color": combo("womens_gloves_color_list"),
                "womens_gloves_material": combo("womens_gloves_material_list"),
                "womens_belt": combo("womens_belt_list"),
                "womens_belt_color": combo("womens_belt_color_list"),
                "womens_belt_material": combo("womens_belt_material_list"),
                "necklace": combo("necklace_list"),
                "earrings": combo("earrings_list"),
                "bracelet": combo("bracelet_list"),
                "watches": combo("watches_list"),
                "watches_color": combo("watches_color_list"),
                "ring": combo("ring_list"),
                "fingernail_style": combo("fingernail_style_list"),
                "nail_color": combo("nail_color_list"),
                "settings_in": ("PM_SETTINGS",),
                "womens_glasses": combo("womens_glasses_list"),
                "womens_glasses_color": combo("womens_glasses_color_list"),
                "womens_mask": combo("womens_mask_list"),
                "womens_mask_color": combo("womens_mask_color_list"),
                "womens_mask_material": combo("womens_mask_material_list"),
                "stretched_material": (
                    "BOOLEAN",
                    {
                        "default": False,
                        "label": "Show subtle outline"
                    }
                 ),
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
            dresses="-", dresses_color="-", dresses_material="-",
            legs="-", legs_color="-",
            underwear="-", underwear_color="-", underwear_material="-",
            capes="-", capes_color="-", capes_material="-",
            hats="-", hats_color="-",
            womens_suits="-", womens_suits_primary_color="-", womens_suits_accent_color="-",
            womens_shoes="-", womens_shoe_color="-", womens_shoe_material="-",
            womens_gloves="-", womens_gloves_color="-",
            womens_gloves_material="-",
            womens_belt="-",
            womens_belt_color="-",
            womens_belt_material="-",
            necklace="-", earrings="-", bracelet="-", ring="-",
            watches="-", watches_color="-",
            fingernail_style="-", nail_color="-",
            settings_in=None,
            womens_glasses="-", womens_glasses_color="-",
            womens_mask="-", womens_mask_color="-", womens_mask_material="-",
            stretched_material=False,
            custom_clothing="",
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "fashion_aesthetic": fashion_aesthetic,
            "tops": tops, "tops_color": tops_color, "tops_material": tops_material,
            "pants": pants, "pants_color": pants_color, "pants_material": pants_material,
            "dresses": dresses, "dresses_color": dresses_color, "dresses_material": dresses_material,
            "legs": legs, "legs_color": legs_color,
            "underwear": underwear, "underwear_color": underwear_color, "underwear_material": underwear_material,
            "capes": capes, "capes_color": capes_color, "capes_material": capes_material,
            "hats": hats, "hats_color": hats_color,
            "womens_suits": womens_suits,
            "womens_suits_primary_color": womens_suits_primary_color,
            "womens_suits_accent_color": womens_suits_accent_color,
            "womens_shoes": womens_shoes, "womens_shoe_color": womens_shoe_color, "womens_shoe_material": womens_shoe_material,
            "womens_gloves": womens_gloves, "womens_gloves_color": womens_gloves_color,
            "womens_gloves_material": womens_gloves_material,
            "womens_belt": womens_belt,
            "womens_belt_color": womens_belt_color,
            "womens_belt_material": womens_belt_material,
            "necklace": necklace,
            "earrings": earrings,
            "bracelet": bracelet,
            "watches": watches,
            "watches_color": watches_color,
            "ring": ring,
            "fingernail_style": fingernail_style, "nail_color": nail_color,
            "womens_glasses": womens_glasses,
            "womens_glasses_color": womens_glasses_color,
            "womens_mask": womens_mask,
            "womens_mask_color": womens_mask_color,
            "womens_mask_material": womens_mask_material,
            "stretched_material": stretched_material,
            "custom_clothing": custom_clothing,
        })
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Female Fashion": CharacterPromptBuilderFemaleFashion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Female Fashion": "Character Prompt Builder - Female Fashion",
}
