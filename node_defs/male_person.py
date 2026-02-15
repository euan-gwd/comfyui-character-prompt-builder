"""
Character Prompt Builder - Male Person Node
"""

from ..utils import load_character_data, combo


class CharacterPromptBuilderMalePerson:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                # === SUBJECT ===
                "gender": (["Man"], {"default": "Man"}),
                "age": (
                    "INT",
                    {
                        "default": 30,
                        "min": 18,
                        "max": 90,
                        "step": 1,
                        "display": "slider",
                    },
                ),
                "nationality_1": combo(data, "nationality_list", "British"),
                "nationality_2": combo(data, "nationality_list"),
                "nationality_mix": (
                    "INT",
                    {
                        "default": 0,
                        "step": 1,
                        "min": 0,
                        "max": 100,
                        "display": "slider",
                    },
                ),
                "body_type": combo(data, "mens_body_type_list"),
                "height": combo(data, "height_list"),
                "body_weight": combo(data, "body_weight_list"),
                "waist_size": combo(data, "waist_size_list"),
            },
            "optional": {
                # === FACE ===
                "face_shape": combo(data, "face_shape_list"),
                "eyes_color": combo(data, "eyes_color_list"),
                "eye_shape": combo(data, "eye_shape_list"),
                "nose_shape": combo(data, "nose_shape_list"),
                "nose_size": combo(data, "nose_size_list"),
                "lip_shape": combo(data, "lip_shape_list"),
                "facial_expression": combo(data, "face_expression_list"),
                "facial_hair": combo(data, "facial_hair_list"),
                # === HAIR ===
                "hair_style": combo(data, "mens_hair_style_list"),
                "hair_length": combo(data, "hair_length_list"),
                "hair_color": combo(data, "hair_color_list"),
                # === SKIN ===
                "skin_tone": combo(data, "skin_tone_list"),
                "skin_details": combo(data, "skin_details_list"),
                "dimples": combo(data, "dimples_list"),
                "freckles": combo(data, "freckles_list"),
                "moles": combo(data, "moles_list"),
                "skin_imperfections": combo(data, "skin_imperfections_list"),
                "skin_acne": combo(data, "skin_acne_list"),
                "tanned_skin": combo(data, "tanned_skin_list"),
                "eyes_details": combo(data, "eyes_details_list"),
                "iris_details": combo(data, "iris_details_list"),
                "circular_iris": combo(data, "circular_iris_list"),
                "circular_pupil": combo(data, "circular_pupil_list"),
                # === TATTOOS ===
                "tattoo": combo(data, "tattoo_list"),
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
        gender="Man",
        age=30,
        nationality_1="-",
        nationality_2="-",
        nationality_mix=0,
        body_type="-",
        height="-",
        body_weight="-",
        waist_size="-",
        face_shape="-",
        nose_shape="-",
        nose_size="-",
        eyes_color="-",
        eye_shape="-",
        facial_expression="-",
        lip_shape="-",
        facial_hair="-",
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
                "face_shape": face_shape,
                "eyes_color": eyes_color,
                "eye_shape": eye_shape,
                "nose_shape": nose_shape,
                "nose_size": nose_size,
                "lip_shape": lip_shape,
                "facial_expression": facial_expression,
                "facial_hair": facial_hair,
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
                "tattoo": tattoo,
            }
        )
        return (settings,)


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Male Person": CharacterPromptBuilderMalePerson,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Male Person": "Character Prompt Builder - Male Person",
}
