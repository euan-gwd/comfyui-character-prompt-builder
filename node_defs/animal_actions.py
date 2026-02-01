"""
Character Prompt Builder - Actions Node
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


class CharacterPromptBuilderActions:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()

        def combo(list_key):
            _list = data.get(list_key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list,)

        # --- Add props_color combo box ---
        def combo_color(list_key):
            _list = data.get(list_key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list,)

        return {
            "required": {
                "standing_pose": combo("standing_pose_list"),
                "kneeling_pose": combo("kneeling_pose_list"),
                "sitting_pose": combo("sitting_pose_list"),
                "laying_down_pose": combo("laying_down_pose_list"),
                # "nsfw_pose": combo("nsfw_pose_list"),
                "props": combo("props_list"),
                "props_color": combo_color("props_color_list"),
                "settings_in": ("PM_SETTINGS",),
            },
            "optional": {
                "custom_action": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Enter custom action or pose description"
                    }
                ),
            }
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self,
            standing_pose="-",
            kneeling_pose="-",
            sitting_pose="-",
            laying_down_pose="-",
            # nsfw_pose="-",
            props="-",
            props_color="-",
            settings_in=None,
            custom_action=""):
        settings = settings_in.copy() if settings_in else {}

        # Only one pose can be active at a time: pick the first non-"-"
        pose_fields = [
            ("standing_pose", standing_pose),
            ("kneeling_pose", kneeling_pose),
            ("sitting_pose", sitting_pose),
            ("laying_down_pose", laying_down_pose),
            # ("nsfw_pose", nsfw_pose),
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

        settings.update({
            "model_pose": selected_pose,
            **pose_out,
            "props": props,
            "props_color": props_color,
            "custom_action": custom_action.strip() if custom_action else "",
        })
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Actions": CharacterPromptBuilderActions,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Actions": "Character Prompt Builder - Actions",
}
