"""
Character Prompt Builder - Spaceship Character Node
"""

from ..utils import load_character_data, combo


class CharacterPromptBuilderSpaceshipCharacter:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                # === SPACESHIP TYPE ===
                "spaceship_type": combo(data, "spaceship_type_list", "Fighter"),
                "spaceship_size": combo(data, "spaceship_size_list", "Medium"),
                # === COLORS ===
                "primary_color": combo(data, "spaceship_primary_color_list", "Silver"),
                "accent_color": combo(data, "spaceship_accent_color_list", "Blue"),
                # === MATERIAL & DESIGN ===
                "material": combo(data, "spaceship_material_list", "Titanium Alloy"),
                "design_style": combo(data, "spaceship_design_list", "Sleek"),
                "condition": combo(data, "spaceship_condition_list", "Pristine"),
                # === PROPULSION ===
                "propulsion_type": combo(
                    data, "spaceship_propulsion_list", "Ion Engines"
                ),
                "engine_glow_color": combo(data, "spaceship_engine_glow_list", "Blue"),
                # === FACTION ===
                "faction": combo(data, "spaceship_faction_list", "Military"),
            },
            "optional": {
                # === COCKPIT ===
                "cockpit_type": combo(data, "spaceship_cockpit_list"),
                "cockpit_lighting": combo(data, "spaceship_cockpit_lighting_list"),
                # === MARKINGS ===
                "markings": combo(data, "spaceship_markings_list"),
                "decal_style": combo(data, "spaceship_decal_list"),
                # === RUNNING LIGHTS ===
                "running_lights": combo(data, "spaceship_running_lights_list"),
                # === CHAIN ===
                "settings_in": ("PM_SETTINGS",),
            },
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(
        self,
        spaceship_type="Fighter",
        spaceship_size="Medium",
        primary_color="Silver",
        accent_color="Blue",
        material="Titanium Alloy",
        design_style="Sleek",
        condition="Pristine",
        propulsion_type="Ion Engines",
        engine_glow_color="Blue",
        faction="Military",
        cockpit_type="-",
        cockpit_lighting="-",
        markings="-",
        decal_style="-",
        running_lights="-",
        settings_in=None,
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update(
            {
                "character_type": "spaceship",
                "spaceship_type": spaceship_type,
                "spaceship_size": spaceship_size,
                "primary_color": primary_color,
                "accent_color": accent_color,
                "spaceship_material": material,
                "design_style": design_style,
                "condition": condition,
                "propulsion_type": propulsion_type,
                "engine_glow_color": engine_glow_color,
                "faction": faction,
                "cockpit_type": cockpit_type,
                "cockpit_lighting": cockpit_lighting,
                "markings": markings,
                "decal_style": decal_style,
                "running_lights": running_lights,
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Spaceship Character": CharacterPromptBuilderSpaceshipCharacter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Spaceship Character": "Character Prompt Builder - Spaceship Character",
}
