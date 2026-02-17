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
                # === STYLE & IDENTITY ===
                "style_reference": combo(data, "spaceship_style_list"),
                "spaceship_type": combo(data, "spaceship_type_list"),
                "spaceship_size": combo(data, "spaceship_size_list"),
                "faction": combo(data, "spaceship_faction_list"),
                # === APPEARANCE ===
                "design_style": combo(data, "spaceship_design_list"),
                "condition": combo(data, "spaceship_condition_list"),
                "primary_color": combo(data, "spaceship_primary_color_list"),
                "accent_color": combo(data, "spaceship_accent_color_list"),
                # === PROPULSION ===
                "propulsion_type": combo(data, "spaceship_propulsion_list"),
                "engine_glow_color": combo(data, "spaceship_engine_glow_list"),
            },
            "optional": {
                # === MATERIAL ===
                "material": combo(data, "spaceship_material_list"),
                # === COCKPIT ===
                "cockpit_type": combo(data, "spaceship_cockpit_list"),
                "cockpit_lighting": combo(data, "spaceship_cockpit_lighting_list"),
                # === MARKINGS ===
                "markings": combo(data, "spaceship_markings_list"),
                "decal_style": combo(data, "spaceship_decal_list"),
                # === LIGHTING ===
                "running_lights": combo(data, "spaceship_running_lights_list"),
                # === WINGS ===
                "wing_count": combo(data, "spaceship_wing_count_list"),
                "wing_type": combo(data, "spaceship_wing_type_list"),
                "wing_position": combo(data, "spaceship_wing_position_list"),
                "vertical_stabilizers": combo(
                    data, "spaceship_vertical_stabilizers_list"
                ),
                "canard_wings": combo(data, "spaceship_canard_list"),
                # === ENGINES ===
                "engine_count": combo(data, "spaceship_engine_count_list"),
                "engine_placement": combo(data, "spaceship_engine_placement_list"),
                "engine_configuration": combo(
                    data, "spaceship_engine_configuration_list"
                ),
                # === HULL & STRUCTURE ===
                "fuselage_shape": combo(data, "spaceship_fuselage_shape_list"),
                "hull_structure": combo(data, "spaceship_hull_structure_list"),
                "surface_texture": combo(data, "spaceship_surface_texture_list"),
                "symmetry": combo(data, "spaceship_symmetry_list"),
                # === OPERATIONS ===
                "landing_gear": combo(data, "spaceship_landing_gear_list"),
                "canopy_type": combo(data, "spaceship_canopy_type_list"),
                "crew_capacity": combo(data, "spaceship_crew_capacity_list"),
                "gear_deployment": combo(data, "spaceship_gear_deployment_list"),
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
        spaceship_type="-",
        spaceship_size="-",
        primary_color="-",
        accent_color="-",
        material="-",
        design_style="-",
        condition="-",
        propulsion_type="-",
        engine_glow_color="-",
        faction="-",
        style_reference="-",
        wing_count="-",
        wing_type="-",
        wing_position="-",
        vertical_stabilizers="-",
        canard_wings="-",
        engine_count="-",
        engine_placement="-",
        engine_configuration="-",
        fuselage_shape="-",
        hull_structure="-",
        surface_texture="-",
        symmetry="-",
        landing_gear="-",
        canopy_type="-",
        crew_capacity="-",
        gear_deployment="-",
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
                "style_reference": style_reference,
                "wing_count": wing_count,
                "wing_type": wing_type,
                "wing_position": wing_position,
                "vertical_stabilizers": vertical_stabilizers,
                "canard_wings": canard_wings,
                "engine_count": engine_count,
                "engine_placement": engine_placement,
                "engine_configuration": engine_configuration,
                "fuselage_shape": fuselage_shape,
                "hull_structure": hull_structure,
                "surface_texture": surface_texture,
                "symmetry": symmetry,
                "landing_gear": landing_gear,
                "canopy_type": canopy_type,
                "crew_capacity": crew_capacity,
                "gear_deployment": gear_deployment,
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
