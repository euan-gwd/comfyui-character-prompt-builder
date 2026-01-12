"""
Character Prompt Builder Nodes
Forked from comfyui-easy-use by AI Wiz Art (Stefano Flore)
"""

import json
import os
from urllib.request import urlopen

# Get the directory where this file is located
RESOURCES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")

# Ensure resources directory exists
os.makedirs(RESOURCES_DIR, exist_ok=True)


def _load_portrait_data():
    """Load portrait prompt data from local file or download if missing."""
    prompt_path = os.path.join(RESOURCES_DIR, 'portrait_prompt.json')
    if not os.path.exists(prompt_path):
        try:
            response = urlopen('https://raw.githubusercontent.com/euan-gwd/comfyui-character-prompt-builder/main/resources/portrait_prompt.json')
            temp_prompt = json.loads(response.read())
            prompt_serialized = json.dumps(temp_prompt, indent=4)
            with open(prompt_path, "w") as f:
                f.write(prompt_serialized)
            del response, temp_prompt
        except Exception as e:
            print(f"[CharacterPromptBuilder] Warning: Could not download portrait data: {e}")
            # Return minimal default data
            return _get_default_portrait_data()

    with open(prompt_path, 'r') as f:
        return json.load(f)


def _get_default_portrait_data():
    """Return minimal default data if download fails."""
    return {
        "gender_list": ["Man", "Woman"],
        "nationality_list": ["British", "American", "French", "German", "Italian", "Spanish", "Japanese", "Chinese", "Korean", "Indian"],
        "body_type_list": ["Slim", "Athletic", "Curvy", "Petite", "Muscular", "Average"],
        "breast_size_list": ["Small", "Medium", "Large"],
        "bum_size_list": ["Small", "Medium", "Large"],
        "face_shape_list": ["Oval", "Round", "Square", "Heart-shaped", "Long"],
        "eyes_color_list": ["Brown", "Blue", "Green", "Hazel", "Gray"],
        "face_expression_list": ["Happy", "Sad", "Serious", "Surprised", "Calm", "Confident"],
        "lip_shape_list": ["Full Lips", "Thin Lips", "Medium Lips"],
        "lip_color_list": ["Natural", "Red", "Pink", "Nude"],
        "makeup_list": ["Natural Makeup", "Glam Makeup", "No Makeup"],
        "hair_style_list": ["Long straight", "Short", "Curly", "Wavy", "Pixie cut", "Bob cut"],
        "hair_length_list": ["Short", "Medium", "Long"],
        "hair_color_list": ["Black", "Brown", "Blonde", "Red", "Gray"],
        "beard_list": ["Clean shaven", "Stubble", "Full Beard", "Goatee"],
        "fashion_aesthetic_list": ["Casual", "Formal", "Streetwear", "Elegant", "Bohemian"],
        "outfit_list": ["Casual dress", "Business suit", "Jeans and t-shirt", "Evening gown"],
        "revealing_outfit_list": ["Bikini", "Lingerie", "Crop top"],
        "womens_shoes_list": ["High heels", "Flats", "Sneakers", "Boots"],
        "womens_shoe_color_list": ["Black", "White", "Red", "Nude"],
        "mens_shoes_list": ["Oxford shoes", "Sneakers", "Boots", "Loafers"],
        "mens_shoe_color_list": ["Black", "Brown", "White"],
        "necklace_list": ["Pearl Necklace", "Gold Chain", "Pendant"],
        "earrings_list": ["Stud Earrings", "Hoop Earrings", "Drop Earrings"],
        "bracelet_list": ["Gold Bracelet", "Silver Bracelet", "Charm Bracelet"],
        "ring_list": ["Diamond Ring", "Gold Band", "Silver Ring"],
        "fingernail_style_list": ["Natural Nails", "French Manicure", "Long Nails"],
        "fingernail_color_list": ["Natural", "Red", "Pink", "Black"],
        "nsfw_appearance_list": ["Topless", "Nude", "Sensual", "Erotic"],
        "model_pose_list": ["Standing", "Sitting", "Walking", "Leaning"],
        "shot_list": ["Portrait", "Full body", "Close-up", "Medium shot"],
        "light_type_list": ["Natural sunlight", "Studio lighting", "Soft ambient light"],
        "light_direction_list": ["front", "left", "right", "top", "back"],
        "artistic_style_list": ["Photorealistic", "Impressionistic", "Cubist", "Surrealistic", "Abstract"],
        "visual_style_list": ["Cinematic", "Editorial", "Fashion Photography", "Fine Art", "Glamour", "High Fashion", "Vintage Film", "Noir", "Neon Noir", "Cyberpunk", "Vaporwave", "Lo-fi", "Polaroid", "35mm Film", "Medium Format", "Analog", "HDR", "Matte", "Glossy", "Soft Focus", "Bokeh", "Tilt-shift", "Double Exposure", "Light Leaks", "Grain", "Desaturated", "High Contrast", "Low Key", "High Key", "Golden Hour", "Blue Hour", "Moody", "Ethereal", "Dreamy", "Gritty", "Raw", "Clean", "Minimal", "Dramatic"],
        "location_list": ["New York", "London", "Paris", "Berlin", "Tokyo", "Beijing", "Moscow", "Dubai", "Rio de Janeiro", "Cape Town"],
        "tattoo_list": ["-", "No tattoos", "Small tattoo", "Arm tattoo", "Leg tattoo", "Back tattoo", "Sleeve tattoo", "Face tattoo", "Chest tattoo", "Shoulder tattoo", "Neck tattoo", "Hand tattoo", "Finger tattoo", "Foot tattoo", "Ankle tattoo", "Thigh tattoo", "Full body tattoo"],
    }


# Character Prompt Builder - Person Node (Subject + Face + Hair + Skin)
class CharacterPromptBuilderPerson:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_portrait_data()
        max_float_value = 1.95

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})

        def weight(default=0):
            return ("FLOAT", {"default": default, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"})

        return {
            "required": {
                # === SUBJECT ===
                "gender": combo("gender_list", "Woman"),
                "age": ("INT", {"default": 30, "min": 18, "max": 90, "step": 1, "display": "slider"}),
                "nationality_1": combo("nationality_list", "British"),
                "nationality_2": combo("nationality_list"),
                "nationality_mix": weight(0.5),
                "body_type": combo("body_type_list"),
                "body_type_weight": weight(),
                "breast_size": combo("breast_size_list"),
                "breast_size_weight": weight(),
                "bum_size": combo("bum_size_list"),
                "bum_size_weight": weight(),
            },
            "optional": {
                # === FACE ===
                "face_shape": combo("face_shape_list"),
                "face_shape_weight": weight(),
                "eyes_color": combo("eyes_color_list"),
                "facial_expression": combo("face_expression_list"),
                "facial_expression_weight": weight(),
                "lip_shape": combo("lip_shape_list"),
                "lip_shape_weight": weight(),
                "lip_color": combo("lip_color_list"),
                "lip_color_weight": weight(),
                "makeup": combo("makeup_list"),
                "makeup_weight": weight(),
                # === HAIR ===
                "hair_style": combo("hair_style_list"),
                "hair_length": combo("hair_length_list"),
                "hair_length_weight": weight(),
                "hair_color": combo("hair_color_list"),
                "disheveled": weight(),
                "beard": combo("beard_list"),
                # === SKIN ===
                "skin_details": weight(),
                "skin_pores": weight(),
                "dimples": weight(),
                "freckles": weight(),
                "moles": weight(),
                "skin_imperfections": weight(),
                "skin_acne": weight(),
                "tanned_skin": weight(),
                "eyes_details": weight(1),
                "iris_details": weight(1),
                "circular_iris": weight(1),
                "circular_pupil": weight(1),
                # === NSFW ===
                "nsfw_appearance": combo("nsfw_appearance_list"),
                "nsfw_appearance_weight": weight(),
                # === NIPPLES & AREOLA ===
                "nipple_appearance": combo("nipple_appearance_list"),
                "nipple_appearance_weight": weight(),
                "areola_appearance": combo("areola_appearance_list"),
                "areola_appearance_weight": weight(),
                # === TATTOOS ===
                "tattoo": combo("tattoo_list"),
                "tattoo_weight": weight(),
                # === CHAIN ===
                "settings_in": ("PM_SETTINGS",),
            }
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self, gender="-", age=30, nationality_1="-", nationality_2="-", nationality_mix=0.5,
            body_type="-", body_type_weight=0, breast_size="-", breast_size_weight=0,
            bum_size="-", bum_size_weight=0,
            face_shape="-", face_shape_weight=0, eyes_color="-",
            facial_expression="-", facial_expression_weight=0,
            lip_shape="-", lip_shape_weight=0, lip_color="-", lip_color_weight=0,
            makeup="-", makeup_weight=0,
            hair_style="-", hair_length="-", hair_length_weight=0, hair_color="-", disheveled=0, beard="-",
            skin_details=0, skin_pores=0, dimples=0, freckles=0, moles=0,
            skin_imperfections=0, skin_acne=0, tanned_skin=0,
            eyes_details=1, iris_details=1, circular_iris=1, circular_pupil=1,
            nipple_appearance="-", nipple_appearance_weight=0,
            areola_appearance="-", areola_appearance_weight=0,
            nsfw_appearance="-", nsfw_appearance_weight=0,
            tattoo="-", tattoo_weight=0,
            settings_in=None):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "gender": gender, "age": age, "nationality_1": nationality_1,
            "nationality_2": nationality_2, "nationality_mix": nationality_mix,
            "body_type": body_type, "body_type_weight": body_type_weight,
            "breast_size": breast_size, "breast_size_weight": breast_size_weight,
            "bum_size": bum_size, "bum_size_weight": bum_size_weight,
            "face_shape": face_shape, "face_shape_weight": face_shape_weight,
            "eyes_color": eyes_color, "facial_expression": facial_expression,
            "facial_expression_weight": facial_expression_weight,
            "lip_shape": lip_shape, "lip_shape_weight": lip_shape_weight,
            "lip_color": lip_color, "lip_color_weight": lip_color_weight,
            "makeup": makeup, "makeup_weight": makeup_weight,
            "hair_style": hair_style,
            "hair_length": hair_length,
            "hair_length_weight": hair_length_weight,  # <-- Add this line
            "hair_color": hair_color, "disheveled": disheveled, "beard": beard,
            "skin_details": skin_details, "skin_pores": skin_pores, "dimples": dimples,
            "freckles": freckles, "moles": moles, "skin_imperfections": skin_imperfections,
            "skin_acne": skin_acne, "tanned_skin": tanned_skin,
            "eyes_details": eyes_details, "iris_details": iris_details,
            "circular_iris": circular_iris, "circular_pupil": circular_pupil,
            "nipple_appearance": nipple_appearance,
            "nipple_appearance_weight": nipple_appearance_weight,
            "areola_appearance": areola_appearance,
            "areola_appearance_weight": areola_appearance_weight,
            "nsfw_appearance": nsfw_appearance,
            "nsfw_appearance_weight": nsfw_appearance_weight,
            "tattoo": tattoo,
            "tattoo_weight": tattoo_weight,
        })
        return (settings,)


# Character Prompt Builder - Female Fashion Node (Style + Outfit + Accessories)
class CharacterPromptBuilderFemaleFashion:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_portrait_data()
        max_float_value = 1.95

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})

        def weight(default=0):
            return ("FLOAT", {"default": default, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"})

        return {
            "required": {
                "fashion_aesthetic": combo("fashion_aesthetic_list"),
                "fashion_aesthetic_weight": weight(),
                "tops": combo("tops_list"),
                "tops_color": combo("tops_color_list"),
                "tops_weight": weight(),
                "dresses": combo("dresses_list"),
                "dresses_color": combo("dresses_color_list"),
                "dresses_weight": weight(),
                "pants": combo("pants_list"),
                "pants_color": combo("pants_color_list"),
                "pants_weight": weight(),
                "legs": combo("legs_list"),
                "legs_color": combo("legs_color_list"),
                "legs_weight": weight(),
                "underwear": combo("underwear_list"),
                "underwear_color": combo("underwear_color_list"),
                "underwear_weight": weight(),
                "capes": combo("capes_list"),
                "capes_color": combo("capes_color_list"),
                "capes_weight": weight(),
                "hats": combo("hats_list"),
                "hats_color": combo("hats_color_list"),
                "hats_weight": weight(),
                "womens_suits": combo("womens_suits_list"),
                "womens_suits_weight": weight(),
                "womens_suits_helmet": combo("womens_suits_helmet_list"),
            },
            "optional": {
                "womens_shoes": combo("womens_shoes_list"),
                "womens_shoe_color": combo("womens_shoe_color_list"),
                "womens_shoes_weight": weight(),
                "womens_gloves": combo("womens_gloves_list"),
                "womens_gloves_color": combo("womens_gloves_color_list"),
                "womens_gloves_weight": weight(),
                "necklace": combo("necklace_list"),
                "necklace_weight": weight(),
                "earrings": combo("earrings_list"),
                "earrings_weight": weight(),
                "bracelet": combo("bracelet_list"),
                "bracelet_weight": weight(),
                "ring": combo("ring_list"),
                "ring_weight": weight(),
                "fingernail_style": combo("fingernail_style_list"),
                "nail_color": combo("nail_color_list"),
                "fingernail_weight": weight(),
                "settings_in": ("PM_SETTINGS",),
                "womens_glasses": combo("womens_glasses_list"),
                "womens_glasses_color": combo("womens_glasses_color_list"),
                "womens_glasses_weight": weight(),
                "custom_clothing": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Enter custom outfit"
                    }
                ),
            }
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self, fashion_aesthetic="-", fashion_aesthetic_weight=0,
            tops="-", tops_color="-", tops_weight=0,
            dresses="-", dresses_color="-", dresses_weight=0,
            pants="-", pants_color="-", pants_weight=0,
            legs="-", legs_color="-", legs_weight=0,
            underwear="-", underwear_color="-", underwear_weight=0,
            capes="-", capes_color="-", capes_weight=0,
            hats="-", hats_color="-", hats_weight=0,
            womens_suits="-", womens_suits_weight=0, womens_suits_helmet="-",
            womens_shoes="-", womens_shoe_color="-", womens_shoes_weight=0,
            womens_gloves="-", womens_gloves_color="-", womens_gloves_weight=0,
            necklace="-", necklace_weight=0, earrings="-", earrings_weight=0,
            bracelet="-", bracelet_weight=0, ring="-", ring_weight=0,
            fingernail_style="-", nail_color="-", fingernail_weight=0,
            settings_in=None,
            womens_glasses="-", womens_glasses_color="-", womens_glasses_weight=0,
            custom_clothing="",
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "fashion_aesthetic": fashion_aesthetic, "fashion_aesthetic_weight": fashion_aesthetic_weight,
            "tops": tops, "tops_color": tops_color, "tops_weight": tops_weight,
            "dresses": dresses, "dresses_color": dresses_color, "dresses_weight": dresses_weight,
            "pants": pants, "pants_color": pants_color, "pants_weight": pants_weight,
            "legs": legs, "legs_color": legs_color, "legs_weight": legs_weight,
            "underwear": underwear, "underwear_color": underwear_color, "underwear_weight": underwear_weight,
            "capes": capes, "capes_color": capes_color, "capes_weight": capes_weight,
            "hats": hats, "hats_color": hats_color, "hats_weight": hats_weight,
            "womens_suits": womens_suits, "womens_suits_weight": womens_suits_weight,
            "womens_suits_helmet": womens_suits_helmet,
            "womens_shoes": womens_shoes, "womens_shoe_color": womens_shoe_color,
            "womens_shoes_weight": womens_shoes_weight,
            "womens_gloves": womens_gloves, "womens_gloves_color": womens_gloves_color,
            "womens_gloves_weight": womens_gloves_weight,
            "necklace": necklace, "necklace_weight": necklace_weight,
            "earrings": earrings, "earrings_weight": earrings_weight,
            "bracelet": bracelet, "bracelet_weight": bracelet_weight,
            "ring": ring, "ring_weight": ring_weight,
            "fingernail_style": fingernail_style, "nail_color": nail_color,
            "fingernail_weight": fingernail_weight,
            "womens_glasses": womens_glasses,
            "womens_glasses_color": womens_glasses_color,
            "womens_glasses_weight": womens_glasses_weight,
            "custom_clothing": custom_clothing,
        })
        return (settings,)


# Character Prompt Builder - Male Fashion Node (Style + Outfit + Accessories)
class CharacterPromptBuilderMaleFashion:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_portrait_data()
        max_float_value = 1.95

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})

        def weight(default=0):
            return ("FLOAT", {"default": default, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"})

        return {
            "required": {
                "fashion_aesthetic": combo("fashion_aesthetic_list"),
                "fashion_aesthetic_weight": weight(),
                "tops": combo("tops_list"),
                "tops_color": combo("tops_color_list"),
                "tops_weight": weight(),
                "pants": combo("pants_list"),
                "pants_color": combo("pants_color_list"),
                "pants_weight": weight(),
                "legs": combo("legs_list"),
                "legs_color": combo("legs_color_list"),
                "legs_weight": weight(),
                "underwear": combo("underwear_list"),
                "underwear_color": combo("underwear_color_list"),
                "underwear_weight": weight(),
                "capes": combo("capes_list"),
                "capes_color": combo("capes_color_list"),
                "capes_weight": weight(),
                "hats": combo("hats_list"),
                "hats_color": combo("hats_color_list"),
                "hats_weight": weight(),
                "mens_suits": combo("mens_suits_list"),
                "mens_suits_helmet": combo("mens_suits_helmet_list"),
            },
            "optional": {
                "mens_shoes": combo("mens_shoes_list"),
                "mens_shoe_color": combo("mens_shoe_color_list"),
                "mens_shoes_weight": weight(),
                "necklace": combo("necklace_list"),
                "necklace_weight": weight(),
                "earrings": combo("earrings_list"),
                "earrings_weight": weight(),
                "bracelet": combo("bracelet_list"),
                "bracelet_weight": weight(),
                "ring": combo("ring_list"),
                "ring_weight": weight(),
                "fingernail_style": combo("fingernail_style_list"),
                "nail_color": combo("nail_color_list"),
                "fingernail_weight": weight(),
                "settings_in": ("PM_SETTINGS",),
                "mens_glasses": combo("mens_glasses_list"),
                "mens_glasses_color": combo("mens_glasses_color_list"),
                "mens_glasses_weight": weight(),
                "custom_clothing": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Enter custom outfit"
                    }
                ),
            }
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self, fashion_aesthetic="-", fashion_aesthetic_weight=0,
            tops="-", tops_color="-", tops_weight=0,
            pants="-", pants_color="-", pants_weight=0,
            legs="-", legs_color="-", legs_weight=0,
            underwear="-", underwear_color="-", underwear_weight=0,
            capes="-", capes_color="-", capes_weight=0,
            hats="-", hats_color="-", hats_weight=0,
            mens_suits="-", mens_suits_helmet="-",
            mens_shoes="-", mens_shoe_color="-", mens_shoes_weight=0,
            necklace="-", necklace_weight=0, earrings="-", earrings_weight=0,
            bracelet="-", bracelet_weight=0, ring="-", ring_weight=0,
            fingernail_style="-", nail_color="-", fingernail_weight=0,
            settings_in=None,
            mens_glasses="-", mens_glasses_color="-", mens_glasses_weight=0,
            custom_clothing="",
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "fashion_aesthetic": fashion_aesthetic, "fashion_aesthetic_weight": fashion_aesthetic_weight,
            "tops": tops, "tops_color": tops_color, "tops_weight": tops_weight,
            "pants": pants, "pants_color": pants_color, "pants_weight": pants_weight,
            "legs": legs, "legs_color": legs_color, "legs_weight": legs_weight,
            "underwear": underwear, "underwear_color": underwear_color, "underwear_weight": underwear_weight,
            "capes": capes, "capes_color": capes_color, "capes_weight": capes_weight,
            "hats": hats, "hats_color": hats_color, "hats_weight": hats_weight,
            "mens_suits": mens_suits, "mens_suits_weight": mens_suits_weight,
            "mens_suits_helmet": mens_suits_helmet,
            "mens_shoes": mens_shoes, "mens_shoe_color": mens_shoe_color,
            "mens_shoes_weight": mens_shoes_weight,
            "necklace": necklace, "necklace_weight": necklace_weight,
            "earrings": earrings, "earrings_weight": earrings_weight,
            "bracelet": bracelet, "bracelet_weight": bracelet_weight,
            "ring": ring, "ring_weight": ring_weight,
            "fingernail_style": fingernail_style, "nail_color": nail_color,
            "fingernail_weight": fingernail_weight,
            "mens_glasses": mens_glasses,
            "mens_glasses_color": mens_glasses_color,
            "mens_glasses_weight": mens_glasses_weight,
            "custom_clothing": custom_clothing,
        })
        return (settings,)


# Character Prompt Builder - Actions Node (Pose/Action)
class CharacterPromptBuilderActions:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_portrait_data()

        def combo(list_key):
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
                "nsfw_pose": combo("nsfw_pose_list"),
                "props": combo("props_list"),  # Add props list to Actions node
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
            nsfw_pose="-",
            props="-",
            settings_in=None,
            custom_action=""):
        settings = settings_in.copy() if settings_in else {}

        # Only one pose can be active at a time: pick the first non-"-"
        pose_fields = [
            ("standing_pose", standing_pose),
            ("kneeling_pose", kneeling_pose),
            ("sitting_pose", sitting_pose),
            ("laying_down_pose", laying_down_pose),
            ("nsfw_pose", nsfw_pose),
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
            "custom_action": custom_action.strip() if custom_action else "",
        })
        return (settings,)


# Character Prompt Builder - Scene Node (Camera + Location + Generate)
class CharacterPromptBuilderScene:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_portrait_data()
        max_float_value = 1.95

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})

        def weight(default=0):
            return ("FLOAT", {"default": default, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"})

        # Add preset_location combo box
        return {
            "required": {
                "num_people": (["1", "2", "3", "4"], {"default": "1"}),
                "settings1": ("PM_SETTINGS",),
                "artistic_style": combo("artistic_style_list", "Photorealistic"),
                "artistic_style_weight": weight(1),
                "shot": combo("shot_list"),
                "shot_weight": weight(1),
                "light_type": combo("light_type_list"),
                "light_direction": combo("light_direction_list"),
                "light_weight": weight(),
                "preset_location": combo("location_list"),
                "location": ("STRING", {"multiline": True, "default": "", "placeholder": "Add a custom location description in here"}),
                "time_of_day": (["-", "Dawn", "Morning", "Midday", "Afternoon", "Golden Hour", "Sunset", "Dusk", "Evening", "Night", "Midnight", "Blue Hour"],),
                "weather": (["-", "Sunny", "Cloudy", "Overcast", "Rainy", "Stormy", "Snowy", "Foggy", "Misty", "Windy", "Clear"],),
                "season": (["-", "Spring", "Summer", "Autumn", "Winter"],),
                "prompt_prefix": ("STRING", {"multiline": True, "default": "", "placeholder": "Added before the generated prompt"}),
                "prompt_suffix": ("STRING", {"multiline": True, "default": "", "placeholder": "Added after the generated prompt"}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""}),
                "photorealism_improvement": (["disable", "enable"],),
            },
            "optional": {
                "settings2": ("PM_SETTINGS",),
                "settings3": ("PM_SETTINGS",),
                "settings4": ("PM_SETTINGS",),
            }
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("positive", "negative",)
    FUNCTION = "generate"
    CATEGORY = "CharacterPromptBuilder"

    def generate(self, num_people, settings1, artistic_style="-", artistic_style_weight=1,
                 shot="-", shot_weight=1,
                 light_type="-", light_direction="-", light_weight=0,
                 preset_location="-", location="", time_of_day="-", weather="-", season="-",
                 prompt_prefix="", prompt_suffix="", negative_prompt="",
                 photorealism_improvement="disable",
                 settings2=None, settings3=None, settings4=None):

        # Collect settings for each person
        settings_list = [settings1]
        if num_people in ("2", "3", "4"):
            if settings2 is not None:
                settings_list.append(settings2)
            else:
                settings_list.append({})
        if num_people in ("3", "4"):
            if settings3 is not None:
                settings_list.append(settings3)
            else:
                settings_list.append({})
        if num_people == "4":
            if settings4 is not None:
                settings_list.append(settings4)
            else:
                settings_list.append({})

        # Compose scene-level settings
        # Use preset_location if not "-" and location text is empty
        scene_location = ""
        if location and location.strip():
            scene_location = location.strip()
        elif preset_location and preset_location != "-":
            scene_location = preset_location

        scene_settings = {
            "artistic_style": artistic_style, "artistic_style_weight": artistic_style_weight,
            "shot": shot, "shot_weight": shot_weight,
            "light_type": light_type, "light_direction": light_direction, "light_weight": light_weight,
            "location": scene_location, "time_of_day": time_of_day, "weather": weather, "season": season,
        }

        # Generate prose for each person
        person_prompts = []
        for idx, person_settings in enumerate(settings_list):
            s = person_settings.copy() if person_settings else {}
            # Merge scene-level settings for each person (for pose, shot, etc.)
            s.update(scene_settings)
            # For clarity, add a label for each person if more than one
            prompt, _ = self._generate_natural_language(s, "", photorealism_improvement)
            if num_people != "1":
                prompt = f"Person {idx+1}: {prompt}"
            person_prompts.append(prompt)

        # Combine all person prompts
        prompt = " ".join(person_prompts)

        # Compose final prompt with prefix/suffix
        parts = []
        if prompt_prefix and prompt_prefix.strip():
            parts.append(prompt_prefix.strip())
        if prompt and prompt.strip():
            parts.append(prompt.strip())
        if prompt_suffix and prompt_suffix.strip():
            parts.append(prompt_suffix.strip())

        final_prompt = " ".join(parts)
        final_prompt = final_prompt.replace(" natural language", "").replace("natural language ", "").replace("natural language", "")
        final_prompt = final_prompt.replace(" prose", "").replace("prose ", "")

        # Negative prompt logic (combine for all people, but only scene-level negative_prompt is used)
        neg = negative_prompt.strip() if negative_prompt else ""

        return (final_prompt.strip(), neg)

    def _generate_natural_language(self, s, negative_prompt, photorealism_improvement):
        def get_eye_mood(expression):
            expression_lower = expression.lower() if expression and expression != "-" else ""
            if expression_lower in ["happy", "excited", "amused", "in love", "surprised and amused", "smiling", "silly"]:
                return ("bright", "sparkling with life", "a warm, lively gleam")
            elif expression_lower in ["angry", "serious", "proud", "prideful", "sarcastic", "contemptuous"]:
                return ("piercing", "intense and focused", "a sharp, penetrating gaze")
            elif expression_lower in ["sad", "disappointed", "fearful", "anxious", "nervous"]:
                return ("glistening", "deep with emotion", "a soft, vulnerable depth")
            elif expression_lower in ["serene", "peaceful", "calm", "content", "relieved", "pensive"]:
                return ("soft", "calm and soulful", "a gentle, peaceful quality")
            elif expression_lower in ["sexually aroused", "ahegao", "in love"]:
                return ("smoldering", "heavy-lidded and alluring", "a sultry, magnetic intensity")
            elif expression_lower in ["curious", "surprised", "confused"]:
                return ("wide", "alert and engaging", "a curious, captivating spark")
            elif expression_lower in ["shy", "cautious", "bored"]:
                return ("guarded", "quietly expressive", "a subtle inner light")
            else:
                return ("expressive", "alive with natural depth", "a genuine, soulful quality")

        def get(key, default="-"):
            return s.get(key, default)

        def getf(key, default=0):
            val = s.get(key, default)
            if isinstance(val, (int, float)):
                return float(val)
            if isinstance(val, str) and val not in ['', '-']:
                try:
                    return float(val)
                except:
                    pass
            return float(default)

        def get_article(word):
            if not word:
                return "a"
            return "an" if word[0].lower() in 'aeiou' else "a"

        # --- Begin natural language prose generation ---
        prose = []

        # Artistic style phrase
        style = s.get("artistic_style", "")
        style_weight = getf("artistic_style_weight")
        style_prefix = ""
        if style and style != "-" and style_weight > 0:
            style_clean = style.strip().lower()
            if not style_clean.endswith("style"):
                style_clean += ""
            style_prefix = f"In {style_clean}"

        # Subject
        gender = get("gender")
        age = int(s.get("age", 30))
        if gender == "Man":
            subj = "He"
            poss = "his"
            obj = "him"
            gender_word = "man"
            if age <= 25:
                gender_word = "boy"
        elif gender == "Woman":
            subj = "She"
            poss = "her"
            obj = "her"
            gender_word = "woman"
            if age <= 25:
                gender_word = "girl"
        else:
            subj = "They"
            poss = "their"
            obj = "them"
            gender_word = "person"

        nationality_str = get("nationality_1", "").strip()
        subject_parts = []
        if nationality_str and nationality_str != "-":
            subject_parts.append(nationality_str)
        if gender_word:
            subject_parts.append(gender_word)
        subject_phrase = " ".join(subject_parts)
        if age and int(age) > 0:
            subject_phrase += f", {age} years old"
        subject_sentence = f"{get_article(subject_phrase)} {subject_phrase}"

        # Body type
        body_type = get("body_type")
        body_type_phrase = ""
        if body_type != "-" and getf("body_type_weight") > 0:
            body_type_phrase = f"with a {body_type.lower()} build"

        # Breasts and bum (for women)
        body_features = []
        if get("breast_size") != "-" and getf("breast_size_weight") > 0 and gender == "Woman":
            breast = get('breast_size').lower()
            if "breast" in breast or "bust" in breast:
                body_features.append(breast)
            else:
                body_features.append(f"{breast} breasts")
        if get("bum_size") != "-" and getf("bum_size_weight") > 0:
            body_features.append(f"{get('bum_size').lower()} bum")
        body_features_phrase = ""
        if body_features:
            body_features_phrase = "with " + " and ".join(body_features)

        # Face features
        face_features = []
        eye_adj, eye_quality, eye_gleam = get_eye_mood(get("facial_expression"))
        if get("eyes_color") != "-":
            face_features.append(f"{eye_adj} {get('eyes_color').lower()} eyes")
        if get("face_shape") != "-" and getf("face_shape_weight") > 0:
            face_shape = get('face_shape').lower().replace(' ', '-')
            article = get_article(face_shape)
            face_features.append(f"{article} {face_shape}-shaped face")
        face_features_phrase = ""
        if face_features:
            face_features_phrase = " and ".join(face_features)

        # Lips
        lips_phrase = ""
        if get("lip_shape") != "-" and getf("lip_shape_weight") > 0:
            lip_desc = get("lip_shape").lower()
            if get("lip_color") != "-" and getf("lip_color_weight") > 0:
                lips_phrase = f"{poss} {lip_desc} are painted {get('lip_color').lower()}"
            else:
                lips_phrase = f"{poss} {lip_desc}"
        elif get("lip_color") != "-" and getf("lip_color_weight") > 0:
            lips_phrase = f"{poss} lips are painted {get('lip_color').lower()}"

        # Makeup
        makeup_phrase = ""
        if get("makeup") != "-" and getf("makeup_weight") > 0 and gender == "Woman":
            makeup_phrase = f"wearing {get('makeup').lower().replace(' makeup', '')} makeup"

        # Hair
        hair_parts = []
        if get("hair_color") != "-":
            hair_parts.append(get("hair_color").lower())
        # Only include hair_length if weight > 0
        if get("hair_length") != "-" and getf("hair_length_weight") > 0:
            hair_parts.append(get("hair_length").lower())
        if get("hair_style") != "-":
            hair_parts.append(get("hair_style").lower())
        hair_phrase = ""
        if hair_parts:
            hair_desc = ", ".join(hair_parts)
            if getf("disheveled") > 0:
                hair_desc += ", slightly disheveled"
            hair_phrase = f"{poss} hair is {hair_desc}"

        beard_phrase = ""
        if get("beard") != "-" and gender == "Man":
            beard_phrase = f"with a {get('beard').lower()} beard"

        # Fashion aesthetic
        fashion_phrase = ""
        if get("fashion_aesthetic") != "-" and getf("fashion_aesthetic_weight") > 0:
            fashion_phrase = f"{poss} style is {get('fashion_aesthetic').lower()}"

        # NSFW or Clothing
        clothing_phrase = ""
        if get("nsfw_appearance") != "-" and getf("nsfw_appearance_weight") > 0:
            clothing_phrase = f"{subj.lower()} is {get('nsfw_appearance').lower()}"
        else:
            clothing = []
            if get("underwear") != "-" and getf("underwear_weight") > 0:
                uw = get('underwear').lower()
                uw_color = get("underwear_color").lower()
                if uw_color != "-" and uw_color != "":
                    uw = f"{uw_color} {uw}"
                clothing.append(uw)
            if get("legs") != "-" and getf("legs_weight") > 0:
                legs = get("legs").lower()
                legs_color = get("legs_color").lower()
                if legs_color != "-" and legs_color != "":
                    legs = f"{legs_color} {legs}"
                clothing.append(legs)
            if get("dresses") != "-" and getf("dresses_weight") > 0:
                dress = get("dresses").lower()
                dress_color = get("dresses_color").lower()
                if dress_color != "-" and dress_color != "":
                    dress = f"{dress_color} {dress}"
                clothing.append(dress)
            if get("tops") != "-" and getf("tops_weight") > 0:
                top = get("tops").lower()
                top_color = get("tops_color").lower()
                if top_color != "-" and top_color != "":
                    top = f"{top_color} {top}"
                clothing.append(top)
            if get("pants") != "-" and getf("pants_weight") > 0:
                pants = get("pants").lower()
                pants_color = get("pants_color").lower()
                if pants_color != "-" and pants_color != "":
                    pants = f"{pants_color} {pants}"
                clothing.append(pants)
            if get("capes") != "-" and getf("capes_weight") > 0:
                cape = get("capes").lower()
                cape_color = get("capes_color").lower()
                if cape_color != "-" and cape_color != "":
                    cape = f"{cape_color} {cape}"
                clothing.append(cape)
            if get("hats") != "-" and getf("hats_weight") > 0:
                hat = get("hats").lower()
                hat_color = get("hats_color").lower()
                if hat_color != "-" and hat_color != "":
                    hat = f"{hat_color} {hat}"
                clothing.append(hat)
            if s.get("womens_gloves", "-") != "-" and float(s.get("womens_gloves_weight", 0)) > 0 and s.get("gender", "-") == "Woman":
                gloves = s.get("womens_gloves").lower()
                gloves_color = s.get("womens_gloves_color", "-").lower()
                if gloves_color != "-" and gloves_color != "":
                    gloves = f"{gloves_color} {gloves}"
                clothing.append(gloves)
            suit = None
            helmet = None
            gender = s.get("gender", "-")
            if gender == "Woman":
                if s.get("womens_suits", "-") != "-":
                    suit = s.get("womens_suits").lower()
                    helmet = s.get("womens_suits_helmet", "-")
            elif gender == "Man":
                if s.get("mens_suits", "-") != "-":
                    suit = s.get("mens_suits").lower()
                    helmet = s.get("mens_suits_helmet", "-")
            if suit:
                if helmet and helmet != "-":
                    suit = f"{suit} ({helmet.lower()})"
                clothing.append(suit)
            custom_clothing = s.get("custom_clothing", "")
            if custom_clothing and custom_clothing.strip():
                clothing.append(custom_clothing.strip())
            if clothing:
                clothing_phrase = "wearing " + " and ".join(clothing)

        # Accessories
        jewelry = []
        if get("necklace") != "-" and getf("necklace_weight") > 0:
            jewelry.append(f"a {get('necklace').lower()}")
        if get("earrings") != "-" and getf("earrings_weight") > 0:
            jewelry.append(get("earrings").lower())
        bracelet_selected = get("bracelet") != "-" and getf("bracelet_weight") > 0
        ring_selected = get("ring") != "-" and getf("ring_weight") > 0
        if bracelet_selected:
            jewelry.append(f"a {get('bracelet').lower()}")
        if ring_selected and (not bracelet_selected or (bracelet_selected and ring_selected)):
            jewelry.append(f"a {get('ring').lower()}")
        if s.get("mens_glasses", "-") != "-" and float(s.get("mens_glasses_weight", 0)) > 0 and s.get("gender", "-") == "Man":
            glasses = s.get("mens_glasses").lower()
            glasses_color = s.get("mens_glasses_color", "-").lower()
            if glasses_color != "-" and glasses_color != "":
                glasses = f"{glasses_color} {glasses}"
            jewelry.append(glasses)
        if s.get("womens_glasses", "-") != "-" and float(s.get("womens_glasses_weight", 0)) > 0 and s.get("gender", "-") == "Woman":
            glasses = s.get("womens_glasses").lower()
            glasses_color = s.get("womens_glasses_color", "-").lower()
            if glasses_color != "-" and glasses_color != "":
                glasses = f"{glasses_color} {glasses}"
            jewelry.append(glasses)
        jewelry_phrase = ""
        if jewelry:
            jewelry_phrase = "accessorized with " + ", ".join(jewelry)

        # Tattoo
        tattoo_phrase = ""
        if get("tattoo") != "-" and getf("tattoo_weight") > 0:
            tattoo_desc = get("tattoo").lower()
            if tattoo_desc not in ["-", "no tattoos"]:
                tattoo_phrase = f"with {tattoo_desc}"

        # Fingernails (for women, if not wearing gloves)
        fingernails_present = (
            get("fingernail_style") != "-" and
            getf("fingernail_weight") > 0 and
            gender == "Woman"
        )
        gloves_type = s.get("womens_gloves", "-").lower()
        gloves_present = (
            gloves_type != "-" and
            float(s.get("womens_gloves_weight", 0)) > 0 and
            s.get("gender", "-") == "Woman"
        )
        show_fingernails = fingernails_present and (
            not gloves_present or "fingerless" in gloves_type
        )
        fingernail_phrase = ""
        if show_fingernails:
            fingernail_style = get("fingernail_style").lower().replace(" nails", "")
            nail_color = get("nail_color").lower() if get("nail_color") != "-" else ""
            if nail_color:
                fingernail_phrase = f"{poss} fingernails are {fingernail_style}, painted {nail_color}"
            else:
                fingernail_phrase = f"{poss} fingernails are {fingernail_style}"
        elif not gloves_present and gender == "Woman":
            fingernail_phrase = f"{poss} hands and fingers are visible"

        # Shoes
        shoes_phrase = ""
        if get("womens_shoes") != "-" and getf("womens_shoes_weight") > 0 and gender == "Woman":
            shoe_desc = get("womens_shoes").lower()
            if get("womens_shoe_color") != "-":
                shoe_desc = f"{get('womens_shoe_color').lower()} {shoe_desc}"
            shoes_phrase = f"wearing {shoe_desc}"
        elif get("mens_shoes") != "-" and getf("mens_shoes_weight") > 0 and gender == "Man":
            shoe_desc = get("mens_shoes").lower()
            if get("mens_shoe_color") != "-":
                shoe_desc = f"{get('mens_shoe_color').lower()} {shoe_desc}"
            shoes_phrase = f"wearing {shoe_desc}"

        # Pose
        pose_fields = [
            ("standing_pose", s.get("standing_pose", "-")),
            ("kneeling_pose", s.get("kneeling_pose", "-")),
            ("sitting_pose", s.get("sitting_pose", "-")),
            ("laying_down_pose", s.get("laying_down_pose", "-")),
            ("nsfw_pose", s.get("nsfw_pose", "-")),
        ]
        selected_pose = next((val for key, val in pose_fields if val and val != "-"), None)
        pose_phrase = ""
        if selected_pose:
            pose_phrase = f"{subj.lower()} is {selected_pose.lower()}"

        # Props
        props = s.get("props", "-")
        props_phrase = ""
        if props and props != "-":
            props_phrase = f"{subj.lower()} is {props.lower()}"

        # Custom action
        custom_action = s.get("custom_action", "")
        custom_action_phrase = ""
        if custom_action and custom_action.strip():
            custom_action_phrase = custom_action.strip()

        # Expression
        expression_phrase = ""
        if get("facial_expression") != "-" and getf("facial_expression_weight") > 0:
            expression_phrase = f"looking {get('facial_expression').lower()}"

        # Shot
        shot_phrase = ""
        if get("shot") != "-" and getf("shot_weight") > 0:
            shot_phrase = f"captured as a {get('shot').lower()}"

        # Location
        location = get("location", "")
        location_phrase = ""
        if location and location.strip() and location.strip() != "-":
            location_phrase = f"{location.strip()}"

        # Environment
        env_parts = []
        if get("time_of_day") != "-":
            env_parts.append(f"during {get('time_of_day').lower()}")
        if get("weather") != "-":
            env_parts.append(f"{get('weather').lower()} weather")
        if get("season") != "-":
            env_parts.append(f"in {get('season').lower()}")
        environment_phrase = ""
        if env_parts:
            environment_phrase = ", ".join(env_parts)

        # Skin
        skin_features = []
        if getf("skin_details") > 0: skin_features.append("detailed texture")
        if getf("skin_pores") > 0: skin_features.append("visible pores")
        if getf("freckles") > 0: skin_features.append("freckles")
        if getf("dimples") > 0: skin_features.append("dimples")
        if getf("moles") > 0: skin_features.append("moles")
        if getf("tanned_skin") > 0: skin_features.append("a sun-kissed tan")
        if getf("skin_acne") > 0: skin_features.append("some acne")
        if getf("skin_imperfections") > 0: skin_features.append("natural imperfections")
        skin_phrase = ""
        if skin_features:
            skin_phrase = f"{poss} skin shows " + ", ".join(skin_features)

        # Eye details
        eye_features = []
        if getf("eyes_details") > 0: eye_features.append("highly detailed")
        if getf("iris_details") > 0: eye_features.append("intricate iris patterns")
        if getf("circular_iris") > 0: eye_features.append("perfectly round irises")
        if getf("circular_pupil") > 0: eye_features.append("realistic pupils")
        eye_detail_phrase = ""
        if eye_features:
            eye_detail_phrase = f"{poss} eyes are " + ", ".join(eye_features) + f", with {eye_gleam} and natural catchlights"

        # Lighting
        lighting_phrase = ""
        if get("light_type") != '-' and getf("light_weight") > 0:
            light_desc = get("light_type").lower()
            if get("light_direction") != '-':
                light_desc += f" from the {get('light_direction').lower()}"
            lighting_phrase = f"the scene is lit by {light_desc}"

        # Compose into a single natural language paragraph
        # Insert style_prefix first if present
        phrases = [
            style_prefix if style_prefix else None,
            subject_sentence,
            body_type_phrase,
            body_features_phrase,
            face_features_phrase,
            lips_phrase,
            makeup_phrase,
            hair_phrase,
            beard_phrase,
            fashion_phrase,
            clothing_phrase,
            jewelry_phrase,
            tattoo_phrase,
            fingernail_phrase,
            shoes_phrase,
        ]
        # Action/pose/location/etc. are better as separate sentences
        tail_phrases = [
            pose_phrase,
            props_phrase,
            custom_action_phrase,
            expression_phrase,
            shot_phrase,
            location_phrase,
            environment_phrase,
            skin_phrase,
            eye_detail_phrase,
            lighting_phrase,
        ]

        # Remove empty phrases and strip
        phrases = [p.strip() for p in phrases if p and p.strip()]
        tail_phrases = [p.strip() for p in tail_phrases if p and p.strip()]

        # Join main description with commas, but avoid double commas after style_prefix
        if phrases:
            if style_prefix and len(phrases) > 1:
                main_desc = phrases[0].rstrip(",") + ", " + ", ".join(phrases[1:])
            else:
                main_desc = ", ".join(phrases)
        else:
            main_desc = ""

        # Join tail phrases with ". "
        tail = ". ".join(tail_phrases)
        if tail:
            prompt = main_desc + ". " + tail
        else:
            prompt = main_desc

        prompt = prompt.strip()
        if prompt and not prompt.endswith("."):
            prompt += "."

        if photorealism_improvement == "enable":
            prompt += " Professional photography with balanced exposure and subtle film grain."
            negative_prompt = negative_prompt + ", shiny skin, reflections on the skin" if negative_prompt else "shiny skin, reflections on the skin"

        return (prompt.strip(), negative_prompt)


# Node mappings
NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Person": CharacterPromptBuilderPerson,
    "Character Prompt Builder Female Fashion": CharacterPromptBuilderFemaleFashion,
    "Character Prompt Builder Male Fashion": CharacterPromptBuilderMaleFashion,
    "Character Prompt Builder Actions": CharacterPromptBuilderActions,
    "Character Prompt Builder Scene": CharacterPromptBuilderScene,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Person": "Character Prompt Builder - Person",
    "Character Prompt Builder Female Fashion": "Character Prompt Builder - Female Fashion",
    "Character Prompt Builder Male Fashion": "Character Prompt Builder - Male Fashion",
    "Character Prompt Builder Actions": "Character Prompt Builder - Actions",
    "Character Prompt Builder Scene": "Character Prompt Builder - Scene & Generate",
}
