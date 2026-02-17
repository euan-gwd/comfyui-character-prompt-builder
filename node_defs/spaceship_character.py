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
                "design_style": combo(
                    data, "spaceship_design_list", "Sleek and Aerodynamic"
                ),
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
                # === PHYSICAL STRUCTURE (Basic Building Blocks) ===
                # Aerodynamics
                "wing_count": combo(data, "spaceship_wing_count_list", "2"),
                "wing_type": combo(data, "spaceship_wing_type_list", "Swept back"),
                "wing_position": combo(
                    data, "spaceship_wing_position_list", "Mid-fuselage"
                ),
                "vertical_stabilizers": combo(
                    data, "spaceship_vertical_stabilizers_list", "2"
                ),
                "canard_wings": combo(data, "spaceship_canard_list", "None"),
                # Propulsion Structure
                "engine_count": combo(data, "spaceship_engine_count_list", "2"),
                "engine_placement": combo(
                    data, "spaceship_engine_placement_list", "Rear cluster"
                ),
                "engine_configuration": combo(
                    data, "spaceship_engine_configuration_list", "Dual nozzles"
                ),
                # Hull & Structure
                "fuselage_shape": combo(
                    data, "spaceship_fuselage_shape_list", "Streamlined"
                ),
                "hull_structure": combo(
                    data, "spaceship_hull_structure_list", "Monocoque"
                ),
                "surface_texture": combo(
                    data, "spaceship_surface_texture_list", "Panel lines"
                ),
                "symmetry": combo(data, "spaceship_symmetry_list", "Bilateral"),
                # Surface Details
                "landing_gear": combo(
                    data, "spaceship_landing_gear_list", "Retractable struts"
                ),
                "canopy_type": combo(
                    data, "spaceship_canopy_type_list", "Bubble canopy"
                ),
                "crew_capacity": combo(
                    data, "spaceship_crew_capacity_list", "Single pilot"
                ),
                "gear_deployment": combo(data, "spaceship_gear_deployment_list"),
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
        design_style="Sleek and Aerodynamic",
        condition="Pristine",
        propulsion_type="Ion Engines",
        engine_glow_color="Blue",
        faction="Military",
        wing_count="2",
        wing_type="Swept back",
        wing_position="Mid-fuselage",
        vertical_stabilizers="2",
        canard_wings="None",
        engine_count="2",
        engine_placement="Rear cluster",
        engine_configuration="Dual nozzles",
        fuselage_shape="Streamlined",
        hull_structure="Monocoque",
        surface_texture="Panel lines",
        symmetry="Bilateral",
        landing_gear="Retractable struts",
        canopy_type="Bubble canopy",
        crew_capacity="Single pilot",
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
