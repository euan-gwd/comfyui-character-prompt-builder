"""
Character Prompt Builder - Spaceship Modifications Node
"""

from ..utils import load_character_data, combo


class CharacterPromptBuilderSpaceshipMods:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                # === WEAPONS ===
                "weapon_system_1": combo(data, "spaceship_weapons_list"),
                "weapon_system_2": combo(data, "spaceship_weapons_list"),
                "weapon_system_3": combo(data, "spaceship_weapons_list"),
            },
            "optional": {
                # === DEFENSIVE SYSTEMS ===
                "shield_system": combo(data, "spaceship_shields_list"),
                "armor_plating": combo(data, "spaceship_armor_list"),
                "cloaking_device": combo(data, "spaceship_cloaking_list"),
                # === UTILITY SYSTEMS ===
                "cargo_capacity": combo(data, "spaceship_cargo_list"),
                "sensor_array": combo(data, "spaceship_sensors_list"),
                "communication_array": combo(data, "spaceship_comms_list"),
                "tractor_beam": combo(data, "spaceship_tractor_list"),
                # === SPECIAL FEATURES ===
                "special_feature_1": combo(data, "spaceship_special_features_list"),
                "special_feature_2": combo(data, "spaceship_special_features_list"),
                "special_feature_3": combo(data, "spaceship_special_features_list"),
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
        weapon_system_1="-",
        weapon_system_2="-",
        weapon_system_3="-",
        shield_system="-",
        armor_plating="-",
        cloaking_device="-",
        cargo_capacity="-",
        sensor_array="-",
        communication_array="-",
        tractor_beam="-",
        special_feature_1="-",
        special_feature_2="-",
        special_feature_3="-",
        settings_in=None,
    ):
        settings = settings_in.copy() if settings_in else {}

        # Collect weapons
        weapons = []
        for w in [weapon_system_1, weapon_system_2, weapon_system_3]:
            if w and w != "-":
                weapons.append(w)

        # Collect special features
        special_features = []
        for f in [special_feature_1, special_feature_2, special_feature_3]:
            if f and f != "-":
                special_features.append(f)

        settings.update(
            {
                "spaceship_weapons": weapons,
                "shield_system": shield_system,
                "armor_plating": armor_plating,
                "cloaking_device": cloaking_device,
                "cargo_capacity": cargo_capacity,
                "sensor_array": sensor_array,
                "communication_array": communication_array,
                "tractor_beam": tractor_beam,
                "spaceship_special_features": special_features,
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Spaceship Mods": CharacterPromptBuilderSpaceshipMods,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Spaceship Mods": "Character Prompt Builder - Spaceship Modifications",
}
