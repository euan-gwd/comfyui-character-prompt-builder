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
            # Return minimal default data
            return _get_default_character_data()

    with open(prompt_path, 'r') as f:
        return json.load(f)


def _get_default_character_data():
    """Return minimal default data if download fails."""
    return {
        "gender_list": ["Man", "Woman"],
        "nationality_list": ["British", "American", "French", "German", "Italian", "Spanish", "Japanese", "Chinese", "Korean", "Indian"],
        "body_type_list": ["Slim", "Athletic", "Curvy", "Petite", "Muscular", "Average"],
        "breast_size_list": ["Small", "Medium", "Large"],
        # --- Height and weight fields ---
        "height_list": [
            "4ft10", "4ft11", "5ft0", "5ft1", "5ft2", "5ft3", "5ft4", "5ft5", "5ft6", "5ft7", "5ft8", "5ft9", "5ft10", "5ft11", "6ft0", "6ft1", "6ft2", "6ft3", "6ft4", "6ft5", "6ft6", "6ft7", "6ft8", "6ft9", "6ft10", "6ft11", "7ft0"
        ],
        "body_weight_list": [
            "80lbs", "90lbs", "100lbs", "110lbs", "120lbs", "130lbs", "140lbs", "150lbs", "160lbs", "170lbs", "180lbs", "190lbs", "200lbs", "210lbs", "220lbs", "230lbs", "240lbs", "250lbs", "260lbs", "270lbs", "280lbs", "290lbs", "300lbs"
        ],
        "breast_cup_size_list": ["AA", "A", "B", "C", "D", "DD", "E", "F", "G", "H", "I", "J", "K"],
        "bust_measurement_list": ["28", "30", "32", "34", "36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56", "58", "60"],
        "breast_shape_list": ["Round", "Teardrop", "Asymmetrical", "East West", "Side Set", "Bell Shape", "Slender", "Relaxed", "Athletic", "Conical"],
        "bum_size_list": ["Small", "Medium", "Large"],
        "face_shape_list": ["Oval", "Round", "Square", "Heart-shaped", "Long"],
        "eyes_color_list": ["Brown", "Blue", "Green", "Hazel", "Gray"],
        "eye_shape_list": ["Almond", "Round", "Monolid", "Hooded", "Upturned", "Downturned"],
        "nose_shape_list": ["Straight", "Button", "Roman", "Snub", "Hawk"],
        "nose_size_list": ["Small", "Medium", "Large"],
        "face_expression_list": ["Happy", "Sad", "Serious", "Surprised", "Calm", "Confident"],
        "lip_shape_list": ["Full Lips", "Thin Lips", "Medium Lips"],
        "lip_color_list": ["Natural", "Red", "Pink", "Nude"],
        "makeup_list": ["Natural Makeup", "Glam Makeup", "No Makeup"],
        "hair_style_list": ["Long straight", "Short", "Curly", "Wavy", "Pixie cut", "Bob cut"],
        "hair_length_list": ["Short", "Medium", "Long"],
        "hair_color_list": ["Black", "Brown", "Blonde", "Red", "Gray"],
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
        "camera_angle_list": ["Medium shot (camera 4–8 feet from subject, waist up visible)"],
        "field_of_view_list": ["Normal (40°–50°)"],
        "light_type_list": ["Natural sunlight", "Studio lighting", "Soft ambient light"],
        "light_quality_list": ["soft diffused", "hard dramatic", "even balanced", "high contrast", "low key", "high key", "chiaroscuro", "volumetric", "atmospheric"],
        "artistic_style_list": ["Photorealistic", "Impressionistic", "Cubist", "Surrealistic", "Abstract"],
        "visual_style_list": ["Cinematic", "Editorial", "Fashion Photography", "Fine Art", "Glamour", "High Fashion", "Vintage Film", "Noir", "Neon Noir", "Cyberpunk", "Vaporwave", "Lo-fi", "Polaroid", "35mm Film", "Medium Format", "Analog", "HDR", "Matte", "Glossy", "Soft Focus", "Bokeh", "Tilt-shift", "Double Exposure", "Light Leaks", "Grain", "Desaturated", "High Contrast", "Low Key", "High Key", "Golden Hour", "Blue Hour", "Moody", "Ethereal", "Dreamy", "Gritty", "Raw", "Clean", "Minimal", "Dramatic"],
        "location_list": ["New York", "London", "Paris", "Berlin", "Tokyo", "Beijing", "Moscow", "Dubai", "Rio de Janeiro", "Cape Town"],
        "tattoo_list": ["-", "No tattoos", "Small tattoo", "Arm tattoo", "Leg tattoo", "Back tattoo", "Sleeve tattoo", "Face tattoo", "Chest tattoo", "Shoulder tattoo", "Neck tattoo", "Hand tattoo", "Finger tattoo", "Foot tattoo", "Ankle tattoo", "Thigh tattoo", "Full body tattoo"],
        # --- Add props_color_list ---
        "props_color_list": ["-", "Red", "Blue", "Green", "Black", "White", "Yellow", "Pink", "Purple", "Brown", "Gray", "Orange", "Gold", "Silver"],
        # --- Breast fields ---
        "breast_cup_size_list": ["AA", "A", "B", "C", "D", "DD", "E", "F", "G", "H", "I", "J", "K"],
        "breast_shape_list": ["Round", "Teardrop", "Asymmetrical", "East West", "Side Set", "Bell Shape", "Slender", "Relaxed", "Athletic", "Conical"],
        "bust_measurement_list": ["28", "30", "32", "34", "36", "38", "40", "42", "44", "46", "48", "50", "52", "54", "56", "58", "60"],
    }


# Character Prompt Builder - Person Node (Subject + Face + Hair + Skin)
class CharacterPromptBuilderPerson:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()
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
                "age": ("INT", {"default": 25, "min": 18, "max": 90, "step": 1, "display": "slider"}),
                "nationality_1": combo("nationality_list", "British"),
                "nationality_2": combo("nationality_list"),
                "nationality_mix": weight(0.0),
                "body_type": combo("body_type_list"),
                "height": combo("height_list"),
                "body_weight": combo("body_weight_list"),
                # "breast_cup_size": combo("breast_cup_size_list"),
                # "bust_measurement": combo("bust_measurement_list"),
                "breast_shape": combo("breast_shape_list"),
                "breast_size": combo("breast_size_list"),
                "breast_size_weight": weight(),
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
                # === NIPPLES & AREOLA & VULVA ===
                "nipple_appearance": combo("nipple_appearance_list"),
                "areola_appearance": combo("areola_appearance_list"),
                "vulva_appearance": combo("vulva_appearance_list"),
                # === TATTOOS ===
                "tattoo": combo("tattoo_list"),
                # === CHAIN ===
                "settings_in": ("PM_SETTINGS",),
            }
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self, gender="-", age=20, nationality_1="-", nationality_2="-", nationality_mix=0.5,
            body_type="-", height="-", body_weight="-", breast_cup_size="-", bust_measurement="-", breast_shape="-",
            breast_size="-", breast_size_weight=0,
            bum_size="-",
            face_shape="-", nose_shape="-", nose_size="-", eyes_color="-", eye_shape="-",
            facial_expression="-",
            lip_shape="-",
            lip_color="-",
            makeup="-",
            hair_style="-", hair_length="-",
            hair_color="-",
            skin_details=0, skin_tone="-", skin_pores=0, dimples=0, freckles=0, moles=0,
            skin_imperfections=0, skin_acne=0, tanned_skin=0,
            eyes_details=1, iris_details=1, circular_iris=1, circular_pupil=1,
            nipple_appearance="-",
            areola_appearance="-",
            vulva_appearance="-",
            nsfw_appearance="-",
            tattoo="-",
            settings_in=None):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "gender": gender, "age": age, "nationality_1": nationality_1,
            "nationality_2": nationality_2, "nationality_mix": nationality_mix,
            "body_type": body_type,
            "height": height, "body_weight": body_weight,
            # "breast_cup_size": breast_cup_size, "bust_measurement": bust_measurement,
            "breast_shape": breast_shape,
            "breast_size": breast_size, "breast_size_weight": breast_size_weight,
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
            "skin_details": skin_details, "skin_tone": skin_tone, "skin_pores": skin_pores, "dimples": dimples,
            "freckles": freckles, "moles": moles, "skin_imperfections": skin_imperfections,
            "skin_acne": skin_acne, "tanned_skin": tanned_skin,
            "eyes_details": eyes_details, "iris_details": iris_details,
            "circular_iris": circular_iris, "circular_pupil": circular_pupil,
            "nipple_appearance": nipple_appearance,
            "areola_appearance": areola_appearance,
            "vulva_appearance": vulva_appearance,
            "nsfw_appearance": nsfw_appearance,
            "tattoo": tattoo,
        })
        return (settings,)


# Character Prompt Builder - Female Fashion Node (Style + Outfit + Accessories)
class CharacterPromptBuilderFemaleFashion:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()

        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})

        return {
            "required": {
                "fashion_aesthetic": combo("fashion_aesthetic_list"),
                "tops": combo("tops_list"),
                "tops_color": combo("tops_color_list"),
                "tops_material": combo("tops_material_list"),
                "pants": combo("pants_list"),
                "pants_color": combo("pants_color_list"),
                "pants_material": combo("pants_material_list"),
                "dresses": combo("dresses_list"),
                "dresses_color": combo("dresses_color_list"),
                "dresses_material": combo("dresses_material_list"),
                "legs": combo("legs_list"),
                "legs_color": combo("legs_color_list"),
                "underwear": combo("underwear_list"),
                "underwear_color": combo("underwear_color_list"),
                "underwear_material": combo("underwear_material_list"),
                "capes": combo("capes_list"),
                "capes_color": combo("capes_color_list"),
                "capes_material": combo("capes_material_list"),
                "hats": combo("hats_list"),
                "hats_color": combo("hats_color_list"),
                "womens_suits": combo("womens_suits_list"),
                "womens_suits_helmet": combo("womens_suits_helmet_list"),
            },
            "optional": {
                "womens_shoes": combo("womens_shoes_list"),
                "womens_shoe_color": combo("womens_shoe_color_list"),
                "womens_shoe_material": combo("womens_shoe_material_list"),
                "womens_gloves": combo("womens_gloves_list"),
                "womens_gloves_color": combo("womens_gloves_color_list"),
                "womens_gloves_material": combo("womens_gloves_material_list"),
                "necklace": combo("necklace_list"),
                "earrings": combo("earrings_list"),
                "bracelet": combo("bracelet_list"),
                "watches": combo("watches_list"),
                "watches_color": combo("watches_color_list"),
                "ring": combo("ring_list"),
                "fingernail_style": combo("fingernail_style_list"),
                "nail_color": combo("nail_color_list"),
                "settings_in": ("PM_SETTINGS",),
                "womens_glasses": combo("womens_glasses_list"),
                "womens_glasses_color": combo("womens_glasses_color_list"),
                "stretched_material": (
                    "BOOLEAN",
                    {
                        "default": False,
                        "label": "Show subtle outline"
                    }
                 ),
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

    def run(self,
            fashion_aesthetic="-",
            tops="-", tops_color="-", tops_material="-",
            pants="-", pants_color="-", pants_material="-",
            dresses="-", dresses_color="-", dresses_material="-",
            legs="-", legs_color="-",
            underwear="-", underwear_color="-", underwear_material="-",
            capes="-", capes_color="-", capes_material="-",
            hats="-", hats_color="-",
            womens_suits="-", womens_suits_helmet="-",
            womens_shoes="-", womens_shoe_color="-", womens_shoe_material="-",
            womens_gloves="-", womens_gloves_color="-",
            womens_gloves_material="-",
            necklace="-", earrings="-", bracelet="-", ring="-",
            watches="-", watches_color="-",
            fingernail_style="-", nail_color="-",
            settings_in=None,
            womens_glasses="-", womens_glasses_color="-",
            stretched_material=False,
            custom_clothing="",
    ):
        settings = settings_in.copy() if settings_in else {}
        settings.update({
            "fashion_aesthetic": fashion_aesthetic,
            "tops": tops, "tops_color": tops_color, "tops_material": tops_material,
            "pants": pants, "pants_color": pants_color, "pants_material": pants_material,
            "dresses": dresses, "dresses_color": dresses_color, "dresses_material": dresses_material,
            "legs": legs, "legs_color": legs_color,
            "underwear": underwear, "underwear_color": underwear_color, "underwear_material": underwear_material,
            "capes": capes, "capes_color": capes_color, "capes_material": capes_material,
            "hats": hats, "hats_color": hats_color,
            "womens_suits": womens_suits,
            "womens_suits_helmet": womens_suits_helmet,
            "womens_shoes": womens_shoes, "womens_shoe_color": womens_shoe_color, "womens_shoe_material": womens_shoe_material,
            "womens_gloves": womens_gloves, "womens_gloves_color": womens_gloves_color,
            "womens_gloves_material": womens_gloves_material,
            "necklace": necklace,
            "earrings": earrings,
            "bracelet": bracelet,
            "watches": watches,
            "watches_color": watches_color,
            "ring": ring,
            "fingernail_style": fingernail_style, "nail_color": nail_color,
            "womens_glasses": womens_glasses,
            "womens_glasses_color": womens_glasses_color,
            "stretched_material": stretched_material,
            "custom_clothing": custom_clothing,
        })
        return (settings,)


# Character Prompt Builder - Actions Node (Pose/Action)
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
                "nsfw_pose": combo("nsfw_pose_list"),
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
            nsfw_pose="-",
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
            "props_color": props_color,
            "custom_action": custom_action.strip() if custom_action else "",
        })
        return (settings,)


# Character Prompt Builder - Scene Node (Camera + Location + Generate)
class CharacterPromptBuilderScene:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()
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
                "camera_lens": combo("camera_lens_specs"),
                "field_of_view": combo("field_of_view_list"),
                "camera_angle": combo("camera_angle_list"),
                "preset_location": combo("location_list"),
                "location": ("STRING", {"multiline": True, "default": "", "placeholder": "Add a custom location description in here"}),
                "time_of_day": (["-", "Dawn", "Morning", "Midday", "Afternoon", "Golden Hour", "Sunset", "Dusk", "Evening", "Night", "Midnight", "Blue Hour"],),
                "weather": (["-", "Sunny", "Cloudy", "Overcast", "Rainy", "Stormy", "Snowy", "Foggy", "Misty", "Windy", "Clear"],),
                "season": (["-", "Spring", "Summer", "Autumn", "Winter"],),
                "light_type": combo("light_type_list"),
                "light_quality": combo("light_quality_list"),
                "light_weight": weight(),
                "prompt_prefix": ("STRING", {"multiline": True, "default": "", "placeholder": "Added before the generated prompt"}),
                "prompt_suffix": ("STRING", {"multiline": True, "default": "", "placeholder": "Added after the generated prompt"}),
                "negative_prompt": ("STRING", {"multiline": True, "default": "","placeholder": "Negative prompt"})
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

    def generate(self, num_people, settings1, artistic_style="-",
                 field_of_view="-", camera_angle="-", camera_lens="-",
                 light_type="-", light_quality="-", light_weight=0,
                 preset_location="-", location="", time_of_day="-", weather="-", season="-",
                 prompt_prefix="", prompt_suffix="", negative_prompt="",
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
            "artistic_style": artistic_style,
            "field_of_view": field_of_view,
            "camera_angle": camera_angle,
            "camera_lens": camera_lens,
            "location": scene_location, "time_of_day": time_of_day, "weather": weather, "season": season,
            "light_type": light_type, "light_quality": light_quality, "light_weight": light_weight,
        }

        # Generate prose for each person
        person_prompts = []
        for idx, person_settings in enumerate(settings_list):
            s = person_settings.copy() if person_settings else {}
            # Merge scene-level settings for each person (for pose, shot, etc.)
            s.update(scene_settings)
            # For clarity, add a label for each person if more than one
            prompt, _ = self._generate_natural_language(s, "")
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

    def _generate_natural_language(self, s, negative_prompt):
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
        style_prefix = ""
        if style and style != "-":
            style_clean = style.strip()
            # Use the style directly, optionally add "style" if not present
            if not style_clean.lower().endswith("style"):
                style_clean += " style"
            style_prefix = f"In a {style_clean}"

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

        # --- Nationality mix logic ---
        nationality_1 = get("nationality_1", "").strip()
        nationality_2 = get("nationality_2", "").strip()
        nationality_mix = getf("nationality_mix", 0.0)
        nationality_str = ""
        if nationality_1 and nationality_1 != "-" and nationality_2 and nationality_2 != "-" and nationality_1 != nationality_2:
            if nationality_mix >= 0.95:
                nationality_str = nationality_2
            elif nationality_mix <= 0.05:
                nationality_str = nationality_1
            else:
                percent_2 = int(nationality_mix * 100)
                percent_1 = 100 - percent_2
                nationality_str = f"{percent_1}% {nationality_1} and {percent_2}% {nationality_2}"
        elif nationality_1 and nationality_1 != "-":
            nationality_str = nationality_1
        elif nationality_2 and nationality_2 != "-":
            nationality_str = nationality_2

        # --- skin tone addition ---
        skin_tone = get("skin_tone", "-")
        skin_tone_phrase = ""
        if skin_tone and skin_tone != "-":
            skin_tone_phrase = skin_tone.lower()
        # --- end skin tone addition ---

        # Compose subject phrase in a more natural way
        subject_parts = []
        if nationality_str and nationality_str != "-":
            subject_parts.append(nationality_str)
        if gender_word:
            subject_parts.append(gender_word)
        subject_phrase = " ".join(subject_parts)
        # Add age if present
        if age and int(age) > 0:
            subject_phrase += f", {age} years old"
        # Add skin tone as "(skin tone)" if present
        if skin_tone_phrase:
            subject_phrase += f", {skin_tone_phrase} skin"
        subject_sentence = f"{get_article(subject_phrase)} {subject_phrase}"

        # Body type, height, and weight
        body_type = get("body_type")
        height = get("height")
        body_weight = get("body_weight")
        body_type_phrase = ""
        body_parts = []
        if body_type != "-":
            body_parts.append(body_type.lower())
        if height != "-":
            body_parts.append(f"{height}")
        if body_weight != "-":
            body_parts.append(f"{body_weight}")
        if body_parts:
            body_type_phrase = f"{subj} is {' '.join(body_parts)}"

        # Breasts and bum (for women)
        body_features = []
        if gender == "Woman":
            # cup = get("breast_cup_size")
            shape = get("breast_shape")
            # bust = get("bust_measurement")
            breast_parts = []
            # if cup != "-":
            #     breast_parts.append(f"{cup} cup")
            # if bust != "-":
            #     breast_parts.append(f"{bust} inch bust")
            if shape != "-":
                breast_parts.append(f"{shape.lower()} shaped")
            if breast_parts and get("breast_size") != "-" and getf("breast_size_weight") > 0:
                body_features.append("/".join(breast_parts))
            else :
                body_features.append("/".join(breast_parts) + " breasts")

        breast_size_weight_val = getf("breast_size_weight")
        if get("breast_size") != "-" and getf("breast_size_weight") > 0 and gender == "Woman" :
                breast = get('breast_size').lower()
                # Emphasize breast size based on weight
                if breast_size_weight_val >= 1.5:

                    breast_desc = f"strikingly {breast}"
                elif breast_size_weight_val >= 1.0:
                    breast_desc = f"noticeably {breast}"
                elif breast_size_weight_val >= 0.5:
                    breast_desc = f"slightly {breast}"
                else:
                    breast_desc = f"{breast}"
                if "breast" in breast or "bust" in breast:
                    body_features.append(breast_desc)
                else:
                    body_features.append(f"{breast_desc} breasts")


        if get("bum_size") != "-":
            body_features.append(f"{get('bum_size').lower()} bum")
        body_features_phrase = ""
        if body_features:
            body_features_phrase = f"{subj} has " + " and ".join(body_features)



        # Face features
        eye_adj, eye_quality, eye_gleam = get_eye_mood(get("facial_expression"))
        face_features = []
        # Eyes
        eye_desc = None
        if get("eyes_color") != "-":
            eye_desc = f"{eye_adj} {get('eyes_color').lower()} eyes"
            # Add extra color nuance if present in eyes_color (e.g., "gray (often appears blue or greenish in some lights)")
        if get("eye_shape") != "-":
            if eye_desc:
                eye_desc += f" with {get('eye_shape').lower()} shape"
            else:
                eye_desc = f"{get('eye_shape').lower()} eye shape"
        if eye_desc:
            face_features.append(eye_desc)
        # Nose
        nose_desc = None
        if get("nose_shape") != "-":
            nose_desc = f"{get('nose_shape').lower()} nose"
        if get("nose_size") != "-":
            if nose_desc:
                nose_desc += f" and {get('nose_size').lower()} size"
            else:
                nose_desc = f"{get('nose_size').lower()} nose size"
        if nose_desc:
            face_features.append(nose_desc)
        # Face shape
        if get("face_shape") != "-":
            face_shape = get('face_shape').lower().replace('-shaped', '').replace(' ', '-')
            article = get_article(face_shape)
            face_features.append(f"{article} {face_shape}-shaped face")
        # Join features naturally
        face_features_phrase = ""
        if face_features:
            if len(face_features) == 1:
                face_features_phrase = f"{poss} {face_features[0]}"
            elif len(face_features) == 2:
                face_features_phrase = f"{poss} {face_features[0]} and {face_features[1]}"
            else:
                face_features_phrase = f"{poss} {face_features[0]}, {', '.join(face_features[1:-1])}, and {face_features[-1]}"

        # Lips
        lips_phrase = ""
        if get("lip_shape") != "-":
            lip_desc = get("lip_shape").lower()
            if get("lip_color") != "-":
                lips_phrase = f"{poss} {lip_desc} lips are painted {get('lip_color').lower()}"
            else:
                lips_phrase = f"{poss} {lip_desc} lips"
        elif get("lip_color") != "-":
            lips_phrase = f"{poss} lips are painted {get('lip_color').lower()}"

        # Makeup
        makeup_phrase = ""
        if get("makeup") != "-" and gender == "Woman":
            makeup_phrase = f"{subj} is wearing {get('makeup').lower().replace(' makeup', '')} makeup"

        # Hair
        hair_parts = []
        vivid_hair_length = ""
        hair_length = get("hair_length")
        if get("hair_color") != "-":
            hair_parts.append(get("hair_color").lower())
        if hair_length != "-":
            hair_parts.append(hair_length.lower())
            if hair_length.lower() in ["waist length", "hip length", "tailbone length"]:
                vivid_hair_length = f"that reaches down to {hair_length.lower().replace(' length', '')}"
        if get("hair_style") != "-":
            hair_parts.append(get("hair_style").lower())
        hair_phrase = ""
        if hair_parts:
            hair_desc = ", ".join(hair_parts)
            if vivid_hair_length:
                hair_phrase = f"{poss} hair is {hair_desc} {vivid_hair_length}"
            else:
                hair_phrase = f"{poss} hair is {hair_desc}"

        # Fashion aesthetic
        fashion_phrase = ""
        # Only check for not "-" (no weight)
        if get("fashion_aesthetic") != "-":
            fashion_phrase = f"{poss} style is {get('fashion_aesthetic').lower()}"

        # NSFW or Clothing
        clothing_phrase = ""
        nsfw_appearance = get("nsfw_appearance")
        if get("nsfw_appearance") != "-" :
            clothing_phrase = f"{subj} is {get('nsfw_appearance').lower()}"
            if get("nipple_appearance") != "-" :
                clothing_phrase += f", {poss} nipples are {get('nipple_appearance').lower()}"
            if get("areola_appearance") != "-" :
                clothing_phrase += f", {poss} areolae are {get('areola_appearance').lower()}"
            if get("vulva_appearance") != "-":
                clothing_phrase += f", {poss} vulva appears {get('vulva_appearance').lower()}"
        else:
            clothing = []
            # UNDERWEAR (always first, and only mention if visible)
            underwear_phrase = ""
            if get("underwear") != "-" :
                uw = get('underwear').lower()
                uw_color = get("underwear_color").lower()
                uw_material = s.get("underwear_material", "-")
                if uw_color != "-" and uw_color != "":
                    uw = f"{uw_color} {uw}"
                if uw_material and uw_material != "-":
                    uw = f"{uw} made of {uw_material.lower()}"
                # If a dress or top is present, underwear is only slightly visible
                if (get("dresses") != "-" or get("tops") != "-"):
                    garment = "dress" if get("dresses") != "-" else "top" if get("tops") != "-" else None
                    underwear_phrase = f"{poss} {uw} is slightly visible beneath {poss}"
                else:
                    underwear_phrase = f"{poss} {uw}"
                clothing.append(underwear_phrase)
            # LEGS
            if get("legs") != "-":
                legs = get("legs").lower()
                legs_color = get("legs_color").lower()
                if legs_color != "-" and legs_color != "":
                    legs = f"{legs_color} {legs}"
                clothing.append(legs)
            # DRESSES
            if get("dresses") != "-" :
                dress = get("dresses").lower()
                dress_color = get("dresses_color").lower()
                dress_material = s.get("dresses_material", "-")
                if dress_color != "-" and dress_color != "":
                    dress = f"{dress_color} {dress}"
                if dress_material and dress_material != "-":
                    dress = f"{dress} made of {dress_material.lower()}"
                clothing.append(dress)
            # TOPS
            if get("tops") != "-" :
                top = get("tops").lower()
                top_color = get("tops_color").lower()
                top_material = s.get("tops_material", "-")
                if top_color != "-" and top_color != "":
                    top = f"{top_color} {top}"
                if top_material and top_material != "-":
                    top = f"{top} made of {top_material.lower()}"
                clothing.append(top)
            # PANTS
            if get("pants") != "-":
                pants = get("pants").lower()
                pants_color = get("pants_color").lower()
                pants_material = s.get("pants_material", "-")
                if pants_color != "-" and pants_color != "":
                    pants = f"{pants_color} {pants}"
                if pants_material and pants_material != "-":
                    pants = f"{pants} made of {pants_material.lower()}"
                clothing.append(pants)
            # CAPES
            if get("capes") != "-":
                cape = get("capes").lower()
                cape_color = get("capes_color").lower()
                cape_material = s.get("capes_material", "-")
                if cape_color != "-" and cape_color != "":
                    cape = f"{cape_color} {cape}"
                if cape_material and cape_material != "-":
                    cape = f"{cape} made of {cape_material.lower()}"
                clothing.append(cape)
            if get("hats") != "-":
                hat = get("hats").lower()
                hat_color = get("hats_color").lower()
                if hat_color != "-" and hat_color != "":
                    hat = f"{hat_color} {hat}"
                clothing.append(hat)
            if s.get("womens_gloves", "-") != "-" and s.get("gender", "-") == "Woman" :
                gloves = s.get("womens_gloves").lower()
                gloves_color = s.get("womens_gloves_color", "-").lower()
                # --- Add gloves material ---
                gloves_material = s.get("womens_gloves_material", "-").lower()
                if gloves_color != "-" and gloves_color != "":
                    gloves = f"{gloves_color} {gloves}"
                if gloves_material != "-" and gloves_material != "":
                    gloves = f"{gloves} made of {gloves_material}"
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
            if custom_clothing and custom_clothing.strip() :
                clothing.append(custom_clothing.strip())
            # --- BEGIN: Subtle nipple outline logic ---
            subtle_nipple_phrase = ""
            stretched_material = s.get("stretched_material", False)
            # Get material for top or dress
            garment = None
            garment_material = None
            if get("dresses") != "-":
                garment = "dress"
                garment_material = s.get("dresses_material", "-").lower()
            else:
                garment = "top"
                garment_material = s.get("tops_material", "-").lower()
            if (
                gender == "Woman"
                and (get("underwear") == "-")
                and ((get("tops") != "-") or (get("dresses") != "-"))
                and (not nsfw_appearance or nsfw_appearance == "-")
                and garment_material != "-" and stretched_material
            ):
                # Use selected nipple/areola appearance if set, otherwise default to "nipples"
                breast_size_desc = ""
                if get("breast_size") != "-":
                    breast_size_desc = get("breast_size").lower()
                nipple_desc = ""
                if get("nipple_appearance") != "-":
                    nipple_desc = get("nipple_appearance").lower()
                areola_desc = ""
                if get("areola_appearance") != "-":
                    areola_desc = get("areola_appearance").lower()
                # --- Improved, always safe-for-work phrasing ---
                details = []
                if breast_size_desc:
                    details.append(f"{breast_size_desc} breasts")
                if nipple_desc:
                    details.append(f"{nipple_desc} nipples")
                if areola_desc:
                    details.append(f"{areola_desc} areolae")
                if details:
                    details_str = ", ".join(details)
                else:
                    details_str = "breasts and nipples"
                subtle_nipple_phrase = (
                    f"Her {garment}, made of {garment_material}, is tightly stretched and visibly compressing her {details_str}, conforming closely to her shape and realistically revealing the natural contours beneath the fabric, including subtle outlines; the effect is natural and realistic, never explicit or exposed"
                )
                extra_clothing_description = subtle_nipple_phrase
            # --- END: Subtle nipple outline logic ---
        if clothing:
            # Use commas and 'and' for the last item
            if len(clothing) == 1:
                clothing_str = clothing[0]
            elif len(clothing) == 2:
                clothing_str = f"{clothing[0]} and {clothing[1]}"
            else:
                clothing_str = ", ".join(clothing[:-1]) + f", and {clothing[-1]}"
            if 'extra_clothing_description' in locals():
                clothing_phrase = f"{subj} is wearing {clothing_str}, {extra_clothing_description}"
            else:
                clothing_phrase = f"{subj} is wearing {clothing_str}"
        # Accessories
        # Only check for not "-" (no weight) for all female fashion fields
        jewelry = []
        necklace = get("necklace")
        earrings = get("earrings")
        bracelet = get("bracelet")
        ring = get("ring")
        watches = get("watches")
        watches_color = get("watches_color")
        glasses = ""
        glasses_color = ""
        if s.get("mens_glasses", "-") != "-" and s.get("gender", "-") == "Man":
            glasses = s.get("mens_glasses").lower()
            glasses_color = s.get("mens_glasses_color", "-").lower()
        if s.get("womens_glasses", "-") != "-" and s.get("gender", "-") == "Woman":
            glasses = s.get("womens_glasses").lower()
            glasses_color = s.get("womens_glasses_color", "-").lower()
        accessory_parts = []
        if necklace != "-" :
            accessory_parts.append(f"{get('necklace').lower()} necklace")
        if earrings != "-" :
            accessory_parts.append(f"{get('earrings').lower()} earrings")
        if bracelet != "-":
            accessory_parts.append(f"{get('bracelet').lower()} bracelet")
        if ring != "-":
            accessory_parts.append(f"{get('ring').lower()} ring")
        if watches != "-":
            watch = watches.lower()
            if watches_color != "-" and watches_color != "":
                watch = f"{watches_color.lower()} {watch}"
            accessory_parts.append(f"{watch} watch")
        if glasses and glasses != "-":
            if glasses_color != "-" and glasses_color != "":
                glasses = f"{glasses_color} {glasses}"
            accessory_parts.append(f"{glasses} glasses")
        jewelry_phrase = ""
        if accessory_parts:
            # Use Oxford comma for last item
            if len(accessory_parts) == 1:
                jewelry_phrase = f"accessorized with {accessory_parts[0]}"
            else:
                jewelry_phrase = f"accessorized with " + ", ".join(accessory_parts[:-1]) + f", and {accessory_parts[-1]}"

        # Tattoo
        tattoo_phrase = ""
        if get("tattoo") != "-" :
            tattoo_desc = get("tattoo").lower()
            if tattoo_desc not in ["-", "no tattoos"]:
                tattoo_phrase = f"with {tattoo_desc}"

        # Fingernails (for women, if not wearing gloves)
        fingernails_present = (
            get("fingernail_style") != "-" and
            gender == "Woman"
        )
        gloves_type = s.get("womens_gloves", "-").lower()
        gloves_present = (
            gloves_type != "-" and
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
        if get("womens_shoes") != "-" and gender == "Woman":
            shoe_desc = get("womens_shoes").lower()
            if get("womens_shoe_color") != "-":
                shoe_desc = f"{get('womens_shoe_color').lower()} {shoe_desc}"
            shoe_material = s.get("womens_shoe_material", "-")
            if shoe_material and shoe_material != "-":
                shoe_desc = f"{shoe_desc} made of {shoe_material.lower()}"
            shoes_phrase = f"wearing {shoe_desc}"
        elif get("mens_shoes") != "-" and gender == "Man":
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
        props_color = s.get("props_color", "-")
        props_phrase = ""
        if props and props != "-":
            # If props starts with a verb (e.g., "holding", "carrying"), insert color before the object
            import re
            match = re.match(r"(\w+ing) (a|an|the)? ?(.+)", props.lower())
            if match:
                verb = match.group(1)
                article = match.group(2) or ""
                obj = match.group(3)
                if props_color and props_color != "-":
                    props_phrase = f"{subj.lower()} is {verb} {article} {props_color.lower()} {obj}".replace("  ", " ")
                else:
                    props_phrase = f"{subj.lower()} is {verb} {article} {obj}".replace("  ", " ")
            else:
                # fallback: just append color before prop
                if props_color and props_color != "-":
                    props_phrase = f"{subj.lower()} is {props_color.lower()} {props.lower()}"
                else:
                    props_phrase = f"{subj.lower()} is {props.lower()}"

        # Custom action
        custom_action = s.get("custom_action", "")
        custom_action_phrase = ""
        if custom_action and custom_action.strip():
            custom_action_phrase = custom_action.strip()

        # Expression
        expression_phrase = ""
        if get("facial_expression") != "-":
            expression_phrase = f"looking {get('facial_expression').lower()}"

        # Field of view
        field_of_view_phrase = ""
        if get("field_of_view") != "-":
            field_of_view_phrase = f"Field of view is {get('field_of_view').lower()}"
        # Camera distance
        camera_angle_phrase = ""
        if get("camera_angle") != "-":
            camera_angle_phrase = f"The Camera distance is {get('camera_angle').lower()}"
        camera_lens_phrase = ""
        if get("camera_lens") != "-":
            camera_lens_phrase = f"The Camera lens is a {get('camera_lens').lower()}"

        # Location
        location = get("location", "")
        location_phrase = ""
        # Always include location if preset_location or custom location is set
        if location and location.strip():
            location_phrase = f"The scene takes place {location.strip()}"
        elif s.get("preset_location") and s.get("preset_location") != "-":
            location_phrase = f"The scene takes place {s.get('preset_location')}"

        # Environment
        env_parts = []
        if get("time_of_day") != "-":
            env_parts.append(f"It is {get('time_of_day').lower()}")
        if get("weather") != "-":
            env_parts.append(f"The weather is {get('weather').lower()}")
        if get("season") != "-":
            env_parts.append(f"It is {get('season').lower()} season")
        environment_phrase = " ".join(env_parts)

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
            light_desc = ""
            if s.get("light_quality", '-') != '-':
                light_desc += s.get("light_quality").lower()
            if get("light_type") != '-':
                if light_desc:
                    light_desc += " "
                light_desc += get("light_type").lower()
            lighting_phrase = f"The scene is lit by {light_desc}"


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
            fashion_phrase,
            clothing_phrase,
            shoes_phrase,
            jewelry_phrase,
            fingernail_phrase,
            skin_phrase,
            tattoo_phrase,
        ]
        # Action/pose/location/etc. are better as separate sentences
        tail_phrases = [
            pose_phrase,
            props_phrase,
            expression_phrase,
            eye_detail_phrase,
            custom_action_phrase,
            location_phrase,
            environment_phrase,
            lighting_phrase,
            field_of_view_phrase,
            camera_angle_phrase,
            camera_lens_phrase
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
            prompt = main_desc
            if not prompt.endswith("."):
                prompt += "."
            prompt += " " + tail
        else:
            prompt = main_desc
            if prompt and not prompt.endswith("."):
                prompt += "."

        return (prompt.strip(), negative_prompt)


# Node mappings
NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Person": CharacterPromptBuilderPerson,
    "Character Prompt Builder Female Fashion": CharacterPromptBuilderFemaleFashion,
    "Character Prompt Builder Actions": CharacterPromptBuilderActions,
    "Character Prompt Builder Scene": CharacterPromptBuilderScene,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Person": "Character Prompt Builder - Person",
    "Character Prompt Builder Female Fashion": "Character Prompt Builder - Female Fashion",
    "Character Prompt Builder Actions": "Character Prompt Builder - Actions",
    "Character Prompt Builder Scene": "Character Prompt Builder - Scene & Generate",
}
