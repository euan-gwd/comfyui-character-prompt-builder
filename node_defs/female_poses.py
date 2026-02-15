"""
Character Prompt Builder - Female Poses Node
"""

from ..utils import load_character_data, combo


class CharacterPromptBuilderFemalePoses:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                "standing_pose": combo(data, "standing_pose_list"),
                "kneeling_pose": combo(data, "kneeling_pose_list"),
                "sitting_pose": combo(data, "sitting_pose_list"),
                "laying_down_pose": combo(data, "laying_down_pose_list"),
                "interaction": combo(data, "interactions_list"),
                "props": combo(data, "props_list"),
                "props_color": combo(data, "props_color_list"),
                "settings_in": ("PM_SETTINGS",),
            },
            "optional": {
                "custom_pose": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Enter custom pose description",
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
        standing_pose="-",
        kneeling_pose="-",
        sitting_pose="-",
        laying_down_pose="-",
        interaction="-",
        props="-",
        props_color="-",
        settings_in=None,
        custom_pose="",
    ):
        settings = settings_in.copy() if settings_in else {}

        # Only one pose can be active at a time: pick the first non-"-"
        pose_fields = [
            ("standing_pose", standing_pose),
            ("kneeling_pose", kneeling_pose),
            ("sitting_pose", sitting_pose),
            ("laying_down_pose", laying_down_pose),
        ]
        selected_pose = "-"
        selected_index = -1
        for idx, (key, val) in enumerate(pose_fields):
            if val != "-":
                selected_pose = val
                selected_index = idx
                break

        # Reset all other poses to "-" except the selected one
        pose_out = {}
        for idx, (key, val) in enumerate(pose_fields):
            if idx == selected_index:
                pose_out[key] = val
            else:
                pose_out[key] = "-"

        settings.update(
            {
                "model_pose": selected_pose,
                **pose_out,
                "props": props,
                "props_color": props_color,
                "interaction": interaction,
                "custom_pose": custom_pose.strip() if custom_pose else "",
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Female Poses": CharacterPromptBuilderFemalePoses,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Female Poses": "Character Prompt Builder - Female Poses",
}
