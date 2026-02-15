"""
Shared utilities for Character Prompt Builder nodes.
"""

import json
import os
from functools import lru_cache
from urllib.request import urlopen


RESOURCES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources")


@lru_cache(maxsize=1)
def load_character_data():
    """Load character prompt data from local file or download if missing.

    Uses LRU cache to avoid reloading the JSON file multiple times.
    """
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
            return get_default_character_data()

    with open(prompt_path, "r") as f:
        return json.load(f)


def get_default_character_data():
    """Return minimal default data if download fails."""
    return {
        "gender_list": ["Man", "Woman"],
        "nationality_list": [
            "British",
            "American",
            "French",
            "German",
            "Italian",
            "Spanish",
            "Japanese",
            "Chinese",
            "Korean",
            "Indian",
        ],
        "body_type_list": [
            "Slim",
            "Athletic",
            "Curvy",
            "Petite",
            "Muscular",
            "Average",
        ],
        "breast_size_list": ["Small", "Medium", "Large"],
        "height_list": [
            "4ft10",
            "4ft11",
            "5ft0",
            "5ft1",
            "5ft2",
            "5ft3",
            "5ft4",
            "5ft5",
            "5ft6",
            "5ft7",
            "5ft8",
            "5ft9",
            "5ft10",
            "5ft11",
            "6ft0",
            "6ft1",
            "6ft2",
            "6ft3",
            "6ft4",
            "6ft5",
            "6ft6",
            "6ft7",
            "6ft8",
            "6ft9",
            "6ft10",
            "6ft11",
            "7ft0",
        ],
        "body_weight_list": [
            "80lbs",
            "90lbs",
            "100lbs",
            "110lbs",
            "120lbs",
            "130lbs",
            "140lbs",
            "150lbs",
            "160lbs",
            "170lbs",
            "180lbs",
            "190lbs",
            "200lbs",
            "210lbs",
            "220lbs",
            "230lbs",
            "240lbs",
            "250lbs",
            "260lbs",
            "270lbs",
            "280lbs",
            "290lbs",
            "300lbs",
        ],
        "breast_cup_size_list": [
            "AA",
            "A",
            "B",
            "C",
            "D",
            "DD",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
        ],
        "bust_measurement_list": [
            "28",
            "30",
            "32",
            "34",
            "36",
            "38",
            "40",
            "42",
            "44",
            "46",
            "48",
            "50",
            "52",
            "54",
            "56",
            "58",
            "60",
        ],
        "breast_shape_list": [
            "Round",
            "Teardrop",
            "Asymmetrical",
            "East West",
            "Side Set",
            "Bell Shape",
            "Slender",
            "Relaxed",
            "Athletic",
            "Conical",
        ],
        "bum_size_list": ["Small", "Medium", "Large"],
        "face_shape_list": ["Oval", "Round", "Square", "Heart-shaped", "Long"],
        "eyes_color_list": ["Brown", "Blue", "Green", "Hazel", "Gray"],
        "eye_shape_list": [
            "Almond",
            "Round",
            "Monolid",
            "Hooded",
            "Upturned",
            "Downturned",
        ],
        "nose_shape_list": ["Straight", "Button", "Roman", "Snub", "Hawk"],
        "nose_size_list": ["Small", "Medium", "Large"],
        "face_expression_list": [
            "Happy",
            "Sad",
            "Serious",
            "Surprised",
            "Calm",
            "Confident",
        ],
        "lip_shape_list": ["Full Lips", "Thin Lips", "Medium Lips"],
        "lip_color_list": ["Natural", "Red", "Pink", "Nude"],
        "makeup_list": ["Natural Makeup", "Glam Makeup", "No Makeup"],
        "hair_style_list": [
            "Long straight",
            "Short",
            "Curly",
            "Wavy",
            "Pixie cut",
            "Bob cut",
        ],
        "hair_length_list": ["Short", "Medium", "Long"],
        "hair_color_list": ["Black", "Brown", "Blonde", "Red", "Gray"],
        "fashion_aesthetic_list": [
            "Casual",
            "Formal",
            "Streetwear",
            "Elegant",
            "Bohemian",
        ],
        "outfit_list": [
            "Casual dress",
            "Business suit",
            "Jeans and t-shirt",
            "Evening gown",
        ],
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
        "model_pose_list": ["Standing", "Sitting", "Walking", "Leaning"],
        "camera_horizontal_angle_list": ["camera 0 horizontal angle, straight on view"],
        "camera_vertical_angle_list": ["camera 0 vertical angle, looking straight on"],
        "camera_shot_list": ["Full body (3-5m / 10-16ft)"],
        "camera_model_list": ["Canon EOS 5D Mark IV"],
        "light_type_list": [
            "Natural sunlight",
            "Studio lighting",
            "Soft ambient light",
        ],
        "light_quality_list": [
            "soft diffused",
            "hard dramatic",
            "even balanced",
            "high contrast",
            "low key",
            "high key",
            "chiaroscuro",
            "volumetric",
            "atmospheric",
        ],
        "artistic_style_list": [
            "Photorealistic",
            "Impressionistic",
            "Cubist",
            "Surrealistic",
            "Abstract",
        ],
        "visual_style_list": [
            "Cinematic",
            "Editorial",
            "Fashion Photography",
            "Fine Art",
            "Glamour",
            "High Fashion",
            "Vintage Film",
            "Noir",
            "Neon Noir",
            "Cyberpunk",
            "Vaporwave",
            "Lo-fi",
            "Polaroid",
            "35mm Film",
            "Medium Format",
            "Analog",
            "HDR",
            "Matte",
            "Glossy",
            "Soft Focus",
            "Bokeh",
            "Tilt-shift",
            "Double Exposure",
            "Light Leaks",
            "Grain",
            "Desaturated",
            "High Contrast",
            "Low Key",
            "High Key",
            "Golden Hour",
            "Blue Hour",
            "Moody",
            "Ethereal",
            "Dreamy",
            "Gritty",
            "Raw",
            "Clean",
            "Minimal",
            "Dramatic",
        ],
        "location_list": [
            "New York",
            "London",
            "Paris",
            "Berlin",
            "Tokyo",
            "Beijing",
            "Moscow",
            "Dubai",
            "Rio de Janeiro",
            "Cape Town",
        ],
        "tattoo_list": [
            "-",
            "No tattoos",
            "Small tattoo",
            "Arm tattoo",
            "Leg tattoo",
            "Back tattoo",
            "Sleeve tattoo",
            "Face tattoo",
            "Chest tattoo",
            "Shoulder tattoo",
            "Neck tattoo",
            "Hand tattoo",
            "Finger tattoo",
            "Foot tattoo",
            "Ankle tattoo",
            "Thigh tattoo",
            "Full body tattoo",
        ],
        "props_color_list": [
            "-",
            "Red",
            "Blue",
            "Green",
            "Black",
            "White",
            "Yellow",
            "Pink",
            "Purple",
            "Brown",
            "Gray",
            "Orange",
            "Gold",
            "Silver",
        ],
        "skin_details_list": [
            "subtle skin texture",
            "noticeable skin texture",
            "highly detailed skin texture",
        ],
        "freckles_list": [
            "a few freckles",
            "noticeable freckles",
            "prominent freckles",
        ],
        "dimples_list": ["subtle dimples", "noticeable dimples", "deep dimples"],
        "moles_list": ["a few moles", "several moles", "many moles"],
        "tanned_skin_list": [
            "a hint of a tan",
            "a sun-kissed tan",
            "deeply tanned skin",
        ],
        "skin_acne_list": ["a few blemishes", "some acne", "pronounced acne"],
        "skin_imperfections_list": [
            "minor imperfections",
            "natural imperfections",
            "pronounced imperfections",
        ],
    }


def combo(data, key, default=None, extra_opts=None):
    """Create a combo list with '-' as first option.

    Args:
        data: The character data dictionary
        key: The key to look up in the data
        default: Optional default value
        extra_opts: Optional additional options dictionary

    Returns:
        Tuple of (list, options_dict) for ComfyUI input types
    """
    _list = data.get(key, ["-"]).copy()
    if "-" not in _list:
        _list.insert(0, "-")
    opts = {"default": default} if default else {}
    if extra_opts:
        opts.update(extra_opts)
    return (_list, opts)
