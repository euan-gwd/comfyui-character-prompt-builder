"""
Character Prompt Builder - Male Fashion Node
"""

from ..utils import load_character_data, combo


class CharacterPromptBuilderMaleFashion:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                "fashion_aesthetic": combo(data, "mens_fashion_aesthetic_list"),
                "tops": combo(data, "mens_tops_list"),
                "tops_color": combo(data, "tops_color_list"),
                "tops_material": combo(data, "tops_material_list"),
                "pants": combo(data, "mens_pants_list"),
                "pants_color": combo(data, "pants_color_list"),
                "pants_material": combo(data, "pants_material_list"),
                "capes": combo(data, "capes_list"),
                "capes_color": combo(data, "capes_color_list"),
                "capes_material": combo(data, "capes_material_list"),
                "hats": combo(data, "mens_hats_list"),
                "hats_color": combo(data, "hats_color_list"),
                "mens_suits": combo(data, "mens_suits_list"),
            },
            "optional": {
                "mens_shoes": combo(data, "mens_shoes_list"),
                "mens_shoe_color": combo(data, "mens_shoe_color_list"),
                "mens_shoe_material": combo(data, "mens_shoe_material_list"),
                "mens_gloves": combo(data, "mens_gloves_list"),
                "mens_gloves_color": combo(data, "mens_gloves_color_list"),
                "mens_gloves_material": combo(data, "mens_gloves_material_list"),
                "mens_belt": combo(data, "mens_belt_list"),
                "mens_belt_color": combo(data, "mens_belt_color_list"),
                "mens_belt_material": combo(data, "mens_belt_material_list"),
                "necklace": combo(data, "mens_necklace_list"),
                "bracelet": combo(data, "mens_bracelet_list"),
                "watches": combo(data, "mens_watches_list"),
                "watches_color": combo(data, "watches_color_list"),
                "ring": combo(data, "mens_ring_list"),
                "settings_in": ("PM_SETTINGS",),
                "mens_glasses": combo(data, "mens_glasses_list"),
                "mens_glasses_color": combo(data, "mens_glasses_color_list"),
                "mens_mask": combo(data, "mens_mask_list"),
                "mens_mask_color": combo(data, "mens_mask_color_list"),
                "mens_mask_material": combo(data, "mens_mask_material_list"),
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
        capes="-",
        capes_color="-",
        capes_material="-",
        hats="-",
        hats_color="-",
        mens_suits="-",
        mens_shoes="-",
        mens_shoe_color="-",
        mens_shoe_material="-",
        mens_gloves="-",
        mens_gloves_color="-",
        mens_gloves_material="-",
        mens_belt="-",
        mens_belt_color="-",
        mens_belt_material="-",
        necklace="-",
        bracelet="-",
        ring="-",
        watches="-",
        watches_color="-",
        settings_in=None,
        mens_glasses="-",
        mens_glasses_color="-",
        mens_mask="-",
        mens_mask_color="-",
        mens_mask_material="-",
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
                "capes": capes,
                "capes_color": capes_color,
                "capes_material": capes_material,
                "hats": hats,
                "hats_color": hats_color,
                "mens_suits": mens_suits,
                "mens_shoes": mens_shoes,
                "mens_shoe_color": mens_shoe_color,
                "mens_shoe_material": mens_shoe_material,
                "mens_gloves": mens_gloves,
                "mens_gloves_color": mens_gloves_color,
                "mens_gloves_material": mens_gloves_material,
                "mens_belt": mens_belt,
                "mens_belt_color": mens_belt_color,
                "mens_belt_material": mens_belt_material,
                "necklace": necklace,
                "bracelet": bracelet,
                "watches": watches,
                "watches_color": watches_color,
                "ring": ring,
                "mens_glasses": mens_glasses,
                "mens_glasses_color": mens_glasses_color,
                "mens_mask": mens_mask,
                "mens_mask_color": mens_mask_color,
                "mens_mask_material": mens_mask_material,
                "custom_clothing": custom_clothing,
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Male Fashion": CharacterPromptBuilderMaleFashion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Male Fashion": "Character Prompt Builder - Male Fashion",
}
