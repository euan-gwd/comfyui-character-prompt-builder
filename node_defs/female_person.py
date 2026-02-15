"""
Character Prompt Builder - Female Person Node
"""

import json
import os
from urllib.request import urlopen

# Get the directory where the main package is located
RESOURCES_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "resources"
)


def _load_character_data():
    """Load character prompt data from local file or download if missing."""
    prompt_path = os.path.join(RESOURCES_DIR, "character_prompt.json")
    if not os.path.exists(prompt_path):
        try:
            response = urlopen(
                "https://raw.githubusercontent.com/euan-gwd/comfyui-character-prompt-builder/main/resources/character_prompt.json"
            )
            temp_prompt = json.loads(response.read())
            prompt_serialized = json.dumps(temp_prompt, indent=4)
            with open(prompt_path, "w") as f:
                f.write(prompt_serialized)
            del response, temp_prompt
        except Exception as e:
            print(
                f"[CharacterPromptBuilder] Warning: Could not download character data: {e}"
            )
            return {}

    with open(prompt_path, "r") as f:
        return json.load(f)


class CharacterPromptBuilderFemalePerson:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()
        max_float_value = 1.95

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if "-" not in _list:
                _list.insert(0, "-")
            return (_list, {"default": default} if default else {})

        def weight(default=0):
            return (
                "INT",
                {
                    "default": int(default * 100)
                    if isinstance(default, float)
                    else default,
                    "step": 1,
                    "min": 0,
                    "max": 100,
                    "display": "slider",
                },
            )

        return {
            "required": {
                # === SUBJECT ===
                "gender": (["Woman"], {"default": "Woman"}),
                "age": (
                    "INT",
                    {
                        "default": 25,
                        "min": 18,
                        "max": 90,
                        "step": 1,
                        "display": "slider",
                    },
                ),
                "nationality_1": combo("nationality_list", "British"),
                "nationality_2": combo("nationality_list"),
                "nationality_mix": weight(0),
                "body_type": combo("body_type_list"),
                "height": combo("height_list"),
                "body_weight": combo("body_weight_list"),
                "waist_size": combo("waist_size_list"),
                "breast_shape": combo("breast_shape_list"),
                "breast_size": combo("breast_size_list"),
                "breast_cup_size": combo("breast_cup_size_list"),
                "bum_size": combo("bum_size_list"),
            },
            "optional": {
                # === FACE ===
                "face_shape": combo("face_shape_list"),
                "eyes_color": combo("eyes_color_list"),
                "eye_shape": combo("eye_shape_list"),
                "nose_shape": combo("nose_shape_list"),
                "nose_size": combo("nose_size_list"),
                "lip_shape": combo("lip_shape_list"),
                "lip_color": combo("lip_color_list"),
                "makeup": combo("makeup_list"),
                "facial_expression": combo("face_expression_list"),
                # === HAIR ===
                "hair_style": combo("hair_style_list"),
                "hair_length": combo("hair_length_list"),
                "hair_color": combo("hair_color_list"),
                # === SKIN ===
                "skin_tone": combo("skin_tone_list"),
                "skin_details": combo("skin_details_list"),
                "dimples": combo("dimples_list"),
                "freckles": combo("freckles_list"),
                "moles": combo("moles_list"),
                "skin_imperfections": combo("skin_imperfections_list"),
                "skin_acne": combo("skin_acne_list"),
                "tanned_skin": combo("tanned_skin_list"),
                "eyes_details": combo("eyes_details_list"),
                "iris_details": combo("iris_details_list"),
                "circular_iris": combo("circular_iris_list"),
                "circular_pupil": combo("circular_pupil_list"),
                # === NIPPLES & AREOLA ===
                "nipple_appearance": combo("nipple_appearance_list"),
                "areola_appearance": combo("areola_appearance_list"),
                # === TATTOOS ===
                "tattoo": combo("tattoo_list"),
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
        gender="Woman",
        age=25,
        nationality_1="-",
        nationality_2="-",
        nationality_mix=0,
        body_type="-",
        height="-",
        body_weight="-",
        waist_size="-",
        breast_shape="-",
        breast_size="-",
        breast_cup_size="-",
        bum_size="-",
        face_shape="-",
        nose_shape="-",
        nose_size="-",
        eyes_color="-",
        eye_shape="-",
        facial_expression="-",
        lip_shape="-",
        lip_color="-",
        makeup="-",
        hair_style="-",
        hair_length="-",
        hair_color="-",
        skin_details="-",
        skin_tone="-",
        dimples="-",
        freckles="-",
        moles="-",
        skin_imperfections="-",
        skin_acne="-",
        tanned_skin="-",
        eyes_details="-",
        iris_details="-",
        circular_iris="-",
        circular_pupil="-",
        nipple_appearance="-",
        areola_appearance="-",
        tattoo="-",
        settings_in=None,
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update(
            {
                "gender": gender,
                "age": age,
                "nationality_1": nationality_1,
                "nationality_2": nationality_2,
                "nationality_mix": nationality_mix,
                "body_type": body_type,
                "height": height,
                "body_weight": body_weight,
                "waist_size": waist_size,
                "breast_shape": breast_shape,
                "breast_size": breast_size,
                "breast_cup_size": breast_cup_size,
                "bum_size": bum_size,
                "face_shape": face_shape,
                "eyes_color": eyes_color,
                "eye_shape": eye_shape,
                "nose_shape": nose_shape,
                "nose_size": nose_size,
                "lip_shape": lip_shape,
                "lip_color": lip_color,
                "makeup": makeup,
                "facial_expression": facial_expression,
                "hair_style": hair_style,
                "hair_length": hair_length,
                "hair_color": hair_color,
                "skin_details": skin_details,
                "skin_tone": skin_tone,
                "dimples": dimples,
                "eyes_details": eyes_details,
                "iris_details": iris_details,
                "freckles": freckles,
                "moles": moles,
                "skin_imperfections": skin_imperfections,
                "skin_acne": skin_acne,
                "tanned_skin": tanned_skin,
                "circular_iris": circular_iris,
                "circular_pupil": circular_pupil,
                "nipple_appearance": nipple_appearance,
                "areola_appearance": areola_appearance,
                "tattoo": tattoo,
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Female Person": CharacterPromptBuilderFemalePerson,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Female Person": "Character Prompt Builder - Female Person",
}
