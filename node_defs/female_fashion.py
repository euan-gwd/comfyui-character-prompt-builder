"""
Character Prompt Builder - Female Fashion Node
"""

from ..utils import load_character_data, combo


class CharacterPromptBuilderFemaleFashion:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                "fashion_aesthetic": combo(data, "fashion_aesthetic_list"),
                "tops": combo(data, "tops_list"),
                "tops_color": combo(data, "tops_color_list"),
                "tops_material": combo(data, "tops_material_list"),
                "pants": combo(data, "pants_list"),
                "pants_color": combo(data, "pants_color_list"),
                "pants_material": combo(data, "pants_material_list"),
                "dresses": combo(data, "dresses_list"),
                "dresses_color": combo(data, "dresses_color_list"),
                "dresses_material": combo(data, "dresses_material_list"),
                "legs": combo(data, "legs_list"),
                "legs_color": combo(data, "legs_color_list"),
                "underwear": combo(data, "underwear_list"),
                "underwear_color": combo(data, "underwear_color_list"),
                "underwear_material": combo(data, "underwear_material_list"),
                "capes": combo(data, "capes_list"),
                "capes_color": combo(data, "capes_color_list"),
                "capes_material": combo(data, "capes_material_list"),
                "hats": combo(data, "hats_list"),
                "hats_color": combo(data, "hats_color_list"),
                "womens_suits": combo(data, "womens_suits_list"),
                "womens_suits_primary_color": combo(
                    data, "womens_suits_primary_color_list"
                ),
                "womens_suits_accent_color": combo(
                    data, "womens_suits_accent_color_list"
                ),
            },
            "optional": {
                "womens_shoes": combo(data, "womens_shoes_list"),
                "womens_shoe_color": combo(data, "womens_shoe_color_list"),
                "womens_shoe_material": combo(data, "womens_shoe_material_list"),
                "womens_gloves": combo(data, "womens_gloves_list"),
                "womens_gloves_color": combo(data, "womens_gloves_color_list"),
                "womens_gloves_material": combo(data, "womens_gloves_material_list"),
                "womens_belt": combo(data, "womens_belt_list"),
                "womens_belt_color": combo(data, "womens_belt_color_list"),
                "womens_belt_material": combo(data, "womens_belt_material_list"),
                "necklace": combo(data, "necklace_list"),
                "earrings": combo(data, "earrings_list"),
                "bracelet": combo(data, "bracelet_list"),
                "watches": combo(data, "watches_list"),
                "watches_color": combo(data, "watches_color_list"),
                "ring": combo(data, "ring_list"),
                "fingernail_style": combo(data, "fingernail_style_list"),
                "nail_color": combo(data, "nail_color_list"),
                "settings_in": ("PM_SETTINGS",),
                "womens_glasses": combo(data, "womens_glasses_list"),
                "womens_glasses_color": combo(data, "womens_glasses_color_list"),
                "womens_mask": combo(data, "womens_mask_list"),
                "womens_mask_color": combo(data, "womens_mask_color_list"),
                "womens_mask_material": combo(data, "womens_mask_material_list"),
                "stretched_material": (
                    "BOOLEAN",
                    {"default": False, "label": "Show subtle outline"},
                ),
                "custom_clothing": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Enter custom outfit",
                    },
                ),
            },
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(
        self,
        fashion_aesthetic="-",
        tops="-",
        tops_color="-",
        tops_material="-",
        pants="-",
        pants_color="-",
        pants_material="-",
        dresses="-",
        dresses_color="-",
        dresses_material="-",
        legs="-",
        legs_color="-",
        underwear="-",
        underwear_color="-",
        underwear_material="-",
        capes="-",
        capes_color="-",
        capes_material="-",
        hats="-",
        hats_color="-",
        womens_suits="-",
        womens_suits_primary_color="-",
        womens_suits_accent_color="-",
        womens_shoes="-",
        womens_shoe_color="-",
        womens_shoe_material="-",
        womens_gloves="-",
        womens_gloves_color="-",
        womens_gloves_material="-",
        womens_belt="-",
        womens_belt_color="-",
        womens_belt_material="-",
        necklace="-",
        earrings="-",
        bracelet="-",
        ring="-",
        watches="-",
        watches_color="-",
        fingernail_style="-",
        nail_color="-",
        settings_in=None,
        womens_glasses="-",
        womens_glasses_color="-",
        womens_mask="-",
        womens_mask_color="-",
        womens_mask_material="-",
        stretched_material=False,
        custom_clothing="",
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update(
            {
                "fashion_aesthetic": fashion_aesthetic,
                "tops": tops,
                "tops_color": tops_color,
                "tops_material": tops_material,
                "pants": pants,
                "pants_color": pants_color,
                "pants_material": pants_material,
                "dresses": dresses,
                "dresses_color": dresses_color,
                "dresses_material": dresses_material,
                "legs": legs,
                "legs_color": legs_color,
                "underwear": underwear,
                "underwear_color": underwear_color,
                "underwear_material": underwear_material,
                "capes": capes,
                "capes_color": capes_color,
                "capes_material": capes_material,
                "hats": hats,
                "hats_color": hats_color,
                "womens_suits": womens_suits,
                "womens_suits_primary_color": womens_suits_primary_color,
                "womens_suits_accent_color": womens_suits_accent_color,
                "womens_shoes": womens_shoes,
                "womens_shoe_color": womens_shoe_color,
                "womens_shoe_material": womens_shoe_material,
                "womens_gloves": womens_gloves,
                "womens_gloves_color": womens_gloves_color,
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
                "fingernail_style": fingernail_style,
                "nail_color": nail_color,
                "womens_glasses": womens_glasses,
                "womens_glasses_color": womens_glasses_color,
                "womens_mask": womens_mask,
                "womens_mask_color": womens_mask_color,
                "womens_mask_material": womens_mask_material,
                "stretched_material": stretched_material,
                "custom_clothing": custom_clothing,
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Female Fashion": CharacterPromptBuilderFemaleFashion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Female Fashion": "Character Prompt Builder - Female Fashion",
}
