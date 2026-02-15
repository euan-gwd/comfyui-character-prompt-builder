"""
Character Prompt Builder - Scene Node
"""

import json
import os
import re
from urllib.request import urlopen

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
            return _get_default_character_data()

    with open(prompt_path, "r") as f:
        return json.load(f)


def _get_default_character_data():
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


class CharacterPromptBuilderScene:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()

        def combo(key, default=None, extra_opts=None):
            _list = data.get(key, ["-"]).copy()
            if "-" not in _list:
                _list.insert(0, "-")
            if key == "artistic_style_list":
                default = "professional photography"
            opts = {"default": default} if default else {}
            if extra_opts:
                opts.update(extra_opts)
            return (_list, opts)

        return {
            "required": {
                "num_people": (["1", "2", "3", "4"], {"default": "1"}),
                "settings1": ("PM_SETTINGS",),
                "artistic_style": combo(
                    "artistic_style_list", "professional photography"
                ),
                "character_sheet_render_style": (
                    ["comic", "photorealistic"],
                    {
                        "default": "comic",
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel1_camera_view": combo(
                    "camera_view_list",
                    "front view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel1_camera_shot": combo(
                    "camera_shot_list",
                    "wide",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel2_camera_view": combo(
                    "camera_view_list",
                    "back view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel2_camera_shot": combo(
                    "camera_shot_list",
                    "wide",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel3_camera_view": combo(
                    "camera_view_list",
                    "right side view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel3_camera_shot": combo(
                    "camera_shot_list",
                    "wide",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel4_camera_view": combo(
                    "camera_view_list",
                    "front view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel4_camera_shot": combo(
                    "camera_shot_list",
                    "medium close up",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "camera_model": combo("camera_model_list"),
                "camera_lens": combo("camera_lens_specs"),
                "camera_horizontal_angle": combo("camera_horizontal_angle_list"),
                "camera_vertical_angle": combo("camera_vertical_angle_list"),
                "camera_shot": combo("camera_shot_list"),
                "camera_view": combo("camera_view_list"),
                "preset_location": combo("location_list"),
                "location": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Add a custom location description in here",
                    },
                ),
                "time_of_day": (
                    [
                        "-",
                        "Dawn",
                        "Morning",
                        "Midday",
                        "Afternoon",
                        "Golden Hour",
                        "Sunset",
                        "Dusk",
                        "Evening",
                        "Night",
                        "Midnight",
                        "Blue Hour",
                    ],
                ),
                "weather": (
                    [
                        "-",
                        "Sunny",
                        "Cloudy",
                        "Overcast",
                        "Rainy",
                        "Stormy",
                        "Snowy",
                        "Foggy",
                        "Misty",
                        "Windy",
                        "Clear",
                    ],
                ),
                "season": (["-", "Spring", "Summer", "Autumn", "Winter"],),
                "light_type": combo("light_type_list"),
                "light_quality": combo("light_quality_list"),
                "prompt_prefix": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Added before the generated prompt",
                    },
                ),
                "prompt_suffix": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": "",
                        "placeholder": "Added after the generated prompt",
                    },
                ),
                "enforce_subjects_only": (
                    "BOOLEAN",
                    {"default": False, "label": "Enforce Only Described Subjects"},
                ),
            },
            "optional": {
                "settings2": ("PM_SETTINGS",),
                "settings3": ("PM_SETTINGS",),
                "settings4": ("PM_SETTINGS",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate"
    CATEGORY = "CharacterPromptBuilder"

    def generate(
        self,
        num_people,
        settings1,
        artistic_style="-",
        camera_model="-",
        camera_vertical_angle="-",
        camera_horizontal_angle="-",
        camera_shot="-",
        camera_view="-",
        camera_lens="-",
        light_type="-",
        light_quality="-",
        preset_location="-",
        location="",
        time_of_day="-",
        weather="-",
        season="-",
        prompt_prefix="",
        prompt_suffix="",
        enforce_subjects_only=False,
        settings2=None,
        settings3=None,
        settings4=None,
        character_sheet_render_style="comic",
        panel1_camera_view="front view",
        panel1_camera_shot="wide",
        panel2_camera_view="back view",
        panel2_camera_shot="wide",
        panel3_camera_view="right side view",
        panel3_camera_shot="wide",
        panel4_camera_view="front view",
        panel4_camera_shot="medium close up",
    ):
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

        scene_location = ""
        if location and location.strip():
            scene_location = location.strip()
        elif preset_location and preset_location != "-":
            scene_location = preset_location

        is_multi_person = num_people != "1"
        scene_artistic_style = artistic_style if num_people != "1" else artistic_style
        scene_camera_shot = camera_shot if num_people != "1" else camera_shot
        scene_camera_view = camera_view if num_people != "1" else camera_view

        scene_settings = {
            "camera_horizontal_angle": camera_horizontal_angle,
            "camera_vertical_angle": camera_vertical_angle,
            "camera_lens": camera_lens,
            "camera_model": camera_model,
            "location": scene_location,
            "time_of_day": time_of_day,
            "weather": weather,
            "season": season,
            "light_type": light_type,
            "light_quality": light_quality,
            "panel1_camera_view": panel1_camera_view,
            "panel1_camera_shot": panel1_camera_shot,
            "panel2_camera_view": panel2_camera_view,
            "panel2_camera_shot": panel2_camera_shot,
            "panel3_camera_view": panel3_camera_view,
            "panel3_camera_shot": panel3_camera_shot,
            "panel4_camera_view": panel4_camera_view,
            "panel4_camera_shot": panel4_camera_shot,
        }

        if not is_multi_person:
            scene_settings["artistic_style"] = artistic_style
            scene_settings["camera_shot"] = camera_shot
            scene_settings["camera_view"] = camera_view
        else:
            scene_artistic_style = artistic_style
            scene_camera_shot = camera_shot
            scene_camera_view = camera_view

        person_prompts = []
        is_multi_person = num_people != "1"

        for idx, person_settings in enumerate(settings_list):
            s = person_settings.copy() if person_settings else {}
            s.update(scene_settings)
            prompt = self._generate_natural_language(
                s,
                include_scene_tail=not is_multi_person,
                character_sheet_render_style=character_sheet_render_style,
            )
            if is_multi_person:
                if num_people == "2":
                    position = "on the LEFT" if idx == 0 else "on the RIGHT"
                    prompt = f"{position.upper()}: {prompt}"
                else:
                    prompt = f"Person {idx + 1}: {prompt}"
            person_prompts.append(prompt)

        prompt = "\n\n".join(person_prompts)

        if is_multi_person:
            tail_parts = []
            if scene_location:
                tail_parts.append(f"The scene takes place {scene_location}")
            if time_of_day != "-":
                tail_parts.append(f"It is {time_of_day.lower()}")
            if weather != "-":
                tail_parts.append(f"The weather is {weather.lower()}")
            if season != "-":
                tail_parts.append(f"It is {season.lower()} season")
            if light_type != "-":
                light_desc = ""
                if light_quality != "-":
                    light_desc += light_quality.lower() + " "
                light_desc += light_type.lower()
                tail_parts.append(f"The scene is lit by {light_desc}")

            if tail_parts:
                prompt += "\n\n" + ". ".join(tail_parts)

        parts = []

        camera_shot_view_phrase = ""
        if scene_camera_shot != "-" and scene_camera_view != "-":
            camera_shot_view_phrase = (
                f"{scene_camera_view.lower()}, {scene_camera_shot.lower()} shot"
            )
        elif scene_camera_shot != "-":
            camera_shot_view_phrase = f"{scene_camera_shot.lower()} shot"
        elif scene_camera_view != "-":
            camera_shot_view_phrase = scene_camera_view.lower()

        artistic_style_phrase = ""
        if scene_artistic_style and scene_artistic_style != "-":
            style_clean = scene_artistic_style.strip()
            if not style_clean.lower().endswith("style"):
                style_clean += " style"
            artistic_style_phrase = f"in a {style_clean}"

        if is_multi_person:
            combined_prefix = []
            if camera_shot_view_phrase:
                combined_prefix.append(camera_shot_view_phrase)
            if artistic_style_phrase:
                combined_prefix.append(artistic_style_phrase)
            if prompt_prefix and prompt_prefix.strip():
                combined_prefix.append(prompt_prefix.strip())
            parts.append(", ".join(combined_prefix))
        else:
            if prompt_prefix and prompt_prefix.strip():
                parts.append(prompt_prefix.strip())

        if prompt and prompt.strip():
            parts.append(prompt.strip())
        if prompt_suffix and prompt_suffix.strip():
            parts.append(prompt_suffix.strip())

        final_prompt = "\n\n".join(parts)
        final_prompt = (
            final_prompt.replace(" natural language", "")
            .replace("natural language ", "")
            .replace("natural language", "")
        )
        final_prompt = final_prompt.replace(" prose", "").replace("prose ", "")

        if enforce_subjects_only:
            final_prompt += (
                "\n\nONLY SHOW THE DESCRIBED SUBJECTS, NO EXTRA PEOPLE OR CHARACTERS"
            )

        return (final_prompt.strip(),)

    def _generate_natural_language(
        self, s, include_scene_tail=True, character_sheet_render_style="comic"
    ):
        def get_eye_mood(expression):
            expression_lower = (
                expression.lower() if expression and expression != "-" else ""
            )
            if expression_lower in [
                "happy",
                "excited",
                "amused",
                "in love",
                "surprised and amused",
                "smiling",
                "silly",
            ]:
                return ("bright", "sparkling with life", "a warm, lively gleam")
            elif expression_lower in [
                "angry",
                "serious",
                "proud",
                "prideful",
                "sarcastic",
                "contemptuous",
            ]:
                return ("piercing", "intense and focused", "a sharp, penetrating gaze")
            elif expression_lower in [
                "sad",
                "disappointed",
                "fearful",
                "anxious",
                "nervous",
            ]:
                return ("glistening", "deep with emotion", "a soft, vulnerable depth")
            elif expression_lower in [
                "serene",
                "peaceful",
                "calm",
                "content",
                "relieved",
                "pensive",
            ]:
                return ("soft", "calm and soulful", "a gentle, peaceful quality")
            elif expression_lower in [
                "sexually aroused",
                "ahegao",
                "in love",
                "mischievous",
                "flirty",
                "seductive",
            ]:
                return (
                    "smoldering",
                    "heavy-lidded and alluring",
                    "a sultry, magnetic intensity",
                )
            elif expression_lower in ["curious", "surprised", "confused"]:
                return ("wide", "alert and engaging", "a curious, captivating spark")
            elif expression_lower in ["shy", "cautious", "bored"]:
                return ("guarded", "quietly expressive", "a subtle inner light")
            else:
                return (
                    "expressive",
                    "alive with natural depth",
                    "a genuine, soulful quality",
                )

        def get(key, default="-"):
            return s.get(key, default)

        def getf(key, default=0):
            val = s.get(key, default)
            if isinstance(val, (int, float)):
                return float(val)
            if isinstance(val, str) and val not in ["", "-"]:
                try:
                    return float(val)
                except:
                    pass
            return float(default)

        def get_article(word):
            if not word:
                return "a"
            return "an" if word[0].lower() in "aeiou" else "a"

        def get_verb(subj):
            return "is" if subj in ["She", "He"] else "are"

        prose = []

        style = s.get("artistic_style", "")
        style_prefix = ""
        if style and style != "-":
            style_clean = style.strip()
            if not style_clean.lower().endswith("style"):
                style_clean += " style"
            style_prefix = f"in a {style_clean}"

        gender = get("gender")
        age = max(int(s.get("age", 25)), 18)

        if gender == "Man":
            subj = "He"
            poss = "his"
            obj = "him"
            gender_word = "man"
        elif gender == "Woman":
            subj = "She"
            poss = "her"
            obj = "her"
            gender_word = "woman"
        else:
            subj = "They"
            poss = "their"
            obj = "them"
            gender_word = "person"

        nationality_1 = get("nationality_1", "").strip()
        nationality_2 = get("nationality_2", "").strip()
        nationality_mix = int(getf("nationality_mix", 0))
        nationality_str = ""
        if (
            nationality_1
            and nationality_1 != "-"
            and nationality_2
            and nationality_2 != "-"
            and nationality_1 != nationality_2
        ):
            percent_2 = nationality_mix
            percent_1 = 100 - percent_2
            if 45 <= percent_1 <= 55 and 45 <= percent_2 <= 55:
                nationality_str = f"mixed heritage {nationality_1.lower()} and {nationality_2.lower()}"
            elif nationality_mix >= 100:
                nationality_str = nationality_2
            elif nationality_mix <= 0:
                nationality_str = nationality_1
            else:
                nationality_str = f"of {percent_1}% {nationality_1.lower()} and {percent_2}% {nationality_2.lower()} heritage"
        elif nationality_1 and nationality_1 != "-":
            nationality_str = nationality_1
        elif nationality_2 and nationality_2 != "-":
            nationality_str = nationality_2

        skin_tone = get("skin_tone", "-")
        skin_tone_phrase = ""
        if skin_tone and skin_tone != "-":
            skin_tone_phrase = skin_tone.lower()

        subject_parts = []
        if nationality_str and nationality_str != "-":
            subject_parts.append(nationality_str)
        if gender_word:
            subject_parts.append(gender_word)
        subject_phrase = " ".join(subject_parts)
        if age and int(age) > 0:
            subject_phrase += f", {age} years old"
        if skin_tone_phrase:
            subject_phrase += f", {skin_tone_phrase} skin"
        subject_sentence = f"{get_article(subject_phrase)} {subject_phrase}"

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

        eye_adj, eye_quality, eye_gleam = get_eye_mood(get("facial_expression"))
        face_features = []
        eye_color = get("eyes_color")
        eye_shape = get("eye_shape")
        eye_base = ""
        if eye_color != "-" and eye_shape != "-":
            eye_base = (
                f"{eye_adj} {eye_color.lower()} eyes with {eye_shape.lower()} shape"
            )
        elif eye_color != "-":
            eye_base = f"{eye_adj} {eye_color.lower()} eyes"
        elif eye_shape != "-":
            eye_base = f"{eye_adj} eyes with {eye_shape.lower()} shape"
        else:
            eye_base = f"{eye_adj} eyes"

        eye_features = []
        eyes_details_val = s.get("eyes_details", "-")
        if eyes_details_val and eyes_details_val != "-":
            eye_features.append(eyes_details_val)
        iris_details_val = s.get("iris_details", "-")
        if iris_details_val and iris_details_val != "-":
            eye_features.append(iris_details_val)
        circular_iris_val = s.get("circular_iris", "-")
        if circular_iris_val and circular_iris_val != "-":
            eye_features.append(circular_iris_val)
        circular_pupil_val = s.get("circular_pupil", "-")
        if circular_pupil_val and circular_pupil_val != "-":
            eye_features.append(circular_pupil_val)

        eye_detail_phrase = f"{poss} {eye_base}"
        if eye_features:
            if len(eye_features) == 1:
                details = eye_features[0]
            elif len(eye_features) == 2:
                details = f"{eye_features[0]} and {eye_features[1]}"
            else:
                details = ", ".join(eye_features[:-1]) + f", and {eye_features[-1]}"
            eye_detail_phrase += f" ({details})"
        if eye_gleam and "catchlights" not in eye_detail_phrase:
            eye_detail_phrase += f", with {eye_gleam} and natural catchlights"
        elif eye_gleam:
            eye_detail_phrase += f", with {eye_gleam}"
        elif "catchlights" not in eye_detail_phrase:
            eye_detail_phrase += ", with natural catchlights"

        face_features.append(eye_detail_phrase)

        nose_desc = None
        nose_shape = get("nose_shape")
        nose_size = get("nose_size")
        if nose_shape != "-" and nose_size != "-":
            nose_desc = f"{nose_size.lower()} and {nose_shape.lower()} shaped nose"
        elif nose_shape != "-":
            nose_desc = f"{nose_shape.lower()} shaped nose"
        elif nose_size != "-":
            nose_desc = f"{nose_size.lower()} nose"
        if nose_desc:
            face_features.append(f"{subj} has a {nose_desc}")
        if get("face_shape") != "-":
            face_shape = (
                get("face_shape").lower().replace("-shaped", "").replace(" ", "-")
            )
            article = get_article(face_shape)
            face_features.append(f"{article} {face_shape}-shaped face")
        face_features_phrase = ""
        if face_features:

            def ensure_poss(s):
                return s if s.strip().startswith(poss) else f"{poss} {s}"

            if len(face_features) == 1:
                face_features_phrase = ensure_poss(face_features[0])
            elif len(face_features) == 2:
                face_features_phrase = (
                    f"{ensure_poss(face_features[0])} and {face_features[1]}"
                )
            else:
                face_features_phrase = f"{ensure_poss(face_features[0])}, {', '.join(face_features[1:-1])}, and {face_features[-1]}"

        lips_phrase = ""
        if get("lip_shape") != "-":
            lip_desc = get("lip_shape").lower()
            if get("lip_color") != "-":
                lips_phrase = (
                    f"{poss} {lip_desc} lips are painted {get('lip_color').lower()}"
                )
            else:
                lips_phrase = f"{poss} {lip_desc} lips"
        elif get("lip_color") != "-":
            lips_phrase = f"{poss} lips are painted {get('lip_color').lower()}"

        makeup_phrase = ""
        if get("makeup") != "-" and gender == "Woman":
            makeup_phrase = f"{subj} {get_verb(subj)} wearing {get('makeup').lower().replace(' makeup', '')} makeup"

        hair_parts = []
        vivid_hair_length = ""
        hair_length = get("hair_length")
        if get("hair_color") != "-":
            hair_parts.append(get("hair_color").lower())
        if hair_length != "-":
            hair_parts.append(hair_length.lower())
            if hair_length.lower() in ["waist length", "hip length", "tailbone length"]:
                vivid_hair_length = (
                    f"that reaches down to {hair_length.lower().replace(' length', '')}"
                )
        if get("hair_style") != "-":
            hair_parts.append(get("hair_style").lower())
        hair_phrase = ""
        if hair_parts:
            hair_desc = ", ".join(hair_parts)
            if vivid_hair_length:
                hair_phrase = f"{poss} hair is {hair_desc} {vivid_hair_length}"
            else:
                hair_phrase = f"{poss} hair is {hair_desc}"

        facial_hair_phrase = ""
        facial_hair = s.get("facial_hair", "-")
        if facial_hair and facial_hair != "-" and gender == "Man":
            facial_hair_lower = facial_hair.lower()
            if facial_hair_lower == "clean shaven":
                facial_hair_phrase = f"{subj} is clean shaven"
            else:
                facial_hair_phrase = f"{subj} has a {facial_hair_lower}"

        fashion_phrase = ""
        if get("fashion_aesthetic") != "-":
            fashion_phrase = f"{poss} style is {get('fashion_aesthetic').lower()}"

        core_clothing = []
        accessory_clothing = []
        underwear_phrase = ""
        gender = s.get("gender", "-")

        if gender == "Woman":
            if get("legs") != "-":
                legs = get("legs").lower()
                legs_color = get("legs_color").lower()
                if legs_color != "-" and legs_color != "":
                    legs = f"{legs_color} {legs}"
                accessory_clothing.append(legs)
            if get("dresses") != "-":
                dress = get("dresses").lower()
                dress_color = get("dresses_color").lower()
                dress_material = s.get("dresses_material", "-").lower()
                if dress_color != "-" and dress_color != "":
                    dress = f"{dress_color} {dress}"
                if dress_material and dress_material != "-":
                    dress = f"{dress} made of {dress_material} material"
                core_clothing.append(dress)
                if (
                    dress_material
                    and ("sheer" in dress_material or "see-through" in dress_material)
                    and (get("underwear") == "-")
                ):
                    nipple_desc = (
                        get("nipple_appearance").lower()
                        if get("nipple_appearance") != "-"
                        else ""
                    )
                    areola_desc = (
                        get("areola_appearance").lower()
                        if get("areola_appearance") != "-"
                        else ""
                    )
                    core_clothing.append(
                        f"{poss} {nipple_desc} nipples and {areola_desc} areolae are only slightly visible through the dress"
                    )
            if get("tops") != "-":
                top = get("tops").lower()
                top_color = get("tops_color").lower()
                top_material = s.get("tops_material", "-").lower()
                if top_color != "-" and top_color != "":
                    top = f"{top_color} {top}"
                if top_material and top_material != "-":
                    top = f"{top} made of {top_material} material"
                core_clothing.append(top)
                if (
                    top_material
                    and ("sheer" in top_material or "see-through" in top_material)
                    and (get("underwear") == "-")
                ):
                    nipple_desc = (
                        get("nipple_appearance").lower()
                        if get("nipple_appearance") != "-"
                        else ""
                    )
                    areola_desc = (
                        get("areola_appearance").lower()
                        if get("areola_appearance") != "-"
                        else ""
                    )
                    core_clothing.append(
                        f"{poss} {nipple_desc} nipples and {areola_desc} areolae are only slightly visible through the top"
                    )
            if get("pants") != "-":
                pants = get("pants").lower()
                pants_color = get("pants_color").lower()
                pants_material = s.get("pants_material", "-")
                if pants_color != "-" and pants_color != "":
                    pants = f"{pants_color} {pants}"
                if pants_material and pants_material != "-":
                    pants = f"{pants} made of {pants_material.lower()} material"
                core_clothing.append(pants)
            if get("underwear") != "-":
                uw = get("underwear").lower()
                uw_color = get("underwear_color").lower()
                uw_material = s.get("underwear_material", "-").lower()
                if uw_color != "-" and uw_color != "":
                    uw = f"{uw_color} {uw}"
                if uw_material and uw_material != "-":
                    uw = f"{uw} made of {uw_material} material"
                if (
                    uw_material
                    and ("sheer" in uw_material or "see-through" in uw_material)
                    and (get("dresses") == "-" and get("tops") == "-")
                ):
                    nipple_desc = (
                        get("nipple_appearance").lower()
                        if get("nipple_appearance") != "-"
                        else ""
                    )
                    areola_desc = (
                        get("areola_appearance").lower()
                        if get("areola_appearance") != "-"
                        else ""
                    )
                    details = []
                    if nipple_desc:
                        details.append(f"{nipple_desc} nipples")
                    if areola_desc:
                        details.append(f"{areola_desc} areolae")
                    if details:
                        details_str = ", ".join(details)
                    else:
                        details_str = "breasts and nipples"
                    underwear_phrase = f"{poss} {uw}, visibly conforming to {poss} shape and realistically revealing subtle contours and the natural forms of {poss} {details_str} beneath the sheer material"
                elif get("dresses") != "-" or get("tops") != "-":
                    garment = (
                        "dress"
                        if get("dresses") != "-"
                        else "top"
                        if get("tops") != "-"
                        else None
                    )
                    underwear_phrase = (
                        f"{poss} {uw} is only slightly visible beneath {poss} {garment}"
                    )
                else:
                    underwear_phrase = f"{poss} {uw}"
                core_clothing.append(underwear_phrase)
            if get("capes") != "-":
                cape = get("capes").lower()
                cape_color = get("capes_color").lower()
                cape_material = s.get("capes_material", "-")
                if cape_color != "-" and cape_color != "":
                    cape = f"{cape_color} {cape}"
                if cape_material and cape_material != "-":
                    cape = f"{cape} made of {cape_material.lower()}"
                core_clothing.append(cape)
            if get("hats") != "-":
                hat = get("hats").lower()
                hat_color = get("hats_color").lower()
                if hat_color != "-" and hat_color != "":
                    hat = f"{hat_color} {hat}"
                accessory_clothing.append(hat)
            if s.get("womens_gloves", "-") != "-":
                gloves = s.get("womens_gloves").lower()
                gloves_color = s.get("womens_gloves_color", "-").lower()
                gloves_material = s.get("womens_gloves_material", "-").lower()
                if gloves_color != "-" and gloves_color != "":
                    gloves = f"{gloves_color} {gloves}"
                if gloves_material != "-" and gloves_material != "":
                    gloves = f"{gloves} made of {gloves_material}"
                accessory_clothing.append(gloves)
            if s.get("womens_belt", "-") != "-":
                belt = s.get("womens_belt").lower()
                belt_color = s.get("womens_belt_color", "-").lower()
                belt_material = s.get("womens_belt_material", "-").lower()
                if belt_color != "-" and belt_color != "":
                    belt = f"{belt_color} {belt}"
                if belt_material != "-" and belt_material != "":
                    belt = f"{belt} made of {belt_material}"
                accessory_clothing.append(belt)
            if s.get("womens_suits", "-") != "-":
                suit = s.get("womens_suits").lower()
                primary_color = s.get("womens_suits_primary_color", "-").lower()
                accent_color = s.get("womens_suits_accent_color", "-").lower()

                has_primary_placeholder = "{primary_color}" in suit
                has_accent_placeholder = "{accent_color}" in suit

                if has_primary_placeholder or has_accent_placeholder:
                    primary_value = (
                        primary_color
                        if (primary_color != "-" and primary_color != "")
                        else ""
                    )
                    accent_value = (
                        accent_color
                        if (accent_color != "-" and accent_color != "")
                        else ""
                    )

                    suit = suit.replace("{primary_color}", primary_value)
                    suit = suit.replace("{accent_color}", accent_value)

                    suit = re.sub(r"\s+", " ", suit).strip()
                else:
                    if primary_color != "-" and primary_color != "":
                        if accent_color != "-" and accent_color != "":
                            suit = f"{primary_color} and {accent_color} {suit}"
                        else:
                            suit = f"{primary_color} {suit}"
                    elif accent_color != "-" and accent_color != "":
                        suit = f"{suit} with {accent_color} accents"

                core_clothing.append(suit)

        if gender == "Man":
            if get("tops") != "-":
                top = get("tops").lower()
                top_color = get("tops_color").lower()
                top_material = s.get("tops_material", "-").lower()
                if top_color != "-" and top_color != "":
                    top = f"{top_color} {top}"
                if top_material and top_material != "-":
                    top = f"{top} made of {top_material} material"
                core_clothing.append(top)
            if get("pants") != "-":
                pants = get("pants").lower()
                pants_color = get("pants_color").lower()
                pants_material = s.get("pants_material", "-")
                if pants_color != "-" and pants_color != "":
                    pants = f"{pants_color} {pants}"
                if pants_material and pants_material != "-":
                    pants = f"{pants} made of {pants_material.lower()} material"
                core_clothing.append(pants)
            if get("capes") != "-":
                cape = get("capes").lower()
                cape_color = get("capes_color").lower()
                cape_material = s.get("capes_material", "-")
                if cape_color != "-" and cape_color != "":
                    cape = f"{cape_color} {cape}"
                if cape_material and cape_material != "-":
                    cape = f"{cape} made of {cape_material.lower()}"
                core_clothing.append(cape)
            if get("hats") != "-":
                hat = get("hats").lower()
                hat_color = get("hats_color").lower()
                if hat_color != "-" and hat_color != "":
                    hat = f"{hat_color} {hat}"
                accessory_clothing.append(hat)
            if s.get("mens_gloves", "-") != "-":
                gloves = s.get("mens_gloves").lower()
                gloves_color = s.get("mens_gloves_color", "-").lower()
                gloves_material = s.get("mens_gloves_material", "-").lower()
                if gloves_color != "-" and gloves_color != "":
                    gloves = f"{gloves_color} {gloves}"
                if gloves_material != "-" and gloves_material != "":
                    gloves = f"{gloves} made of {gloves_material}"
                accessory_clothing.append(gloves)
            if s.get("mens_belt", "-") != "-":
                belt = s.get("mens_belt").lower()
                belt_color = s.get("mens_belt_color", "-").lower()
                belt_material = s.get("mens_belt_material", "-").lower()
                if belt_color != "-" and belt_color != "":
                    belt = f"{belt_color} {belt}"
                if belt_material != "-" and belt_material != "":
                    belt = f"{belt} made of {belt_material}"
                accessory_clothing.append(belt)
            if s.get("mens_suits", "-") != "-":
                suit = s.get("mens_suits").lower()
                primary_color = s.get("mens_suits_primary_color", "-").lower()
                accent_color = s.get("mens_suits_accent_color", "-").lower()

                has_primary_placeholder = "{primary_color}" in suit
                has_accent_placeholder = "{accent_color}" in suit

                if has_primary_placeholder or has_accent_placeholder:
                    primary_value = (
                        primary_color
                        if (primary_color != "-" and primary_color != "")
                        else ""
                    )
                    accent_value = (
                        accent_color
                        if (accent_color != "-" and accent_color != "")
                        else ""
                    )

                    suit = suit.replace("{primary_color}", primary_value)
                    suit = suit.replace("{accent_color}", accent_value)

                    suit = re.sub(r"\s+", " ", suit).strip()
                else:
                    if primary_color != "-" and primary_color != "":
                        if accent_color != "-" and accent_color != "":
                            suit = f"{primary_color} and {accent_color} {suit}"
                        else:
                            suit = f"{primary_color} {suit}"
                    elif accent_color != "-" and accent_color != "":
                        suit = f"{suit} with {accent_color} accents"

                core_clothing.append(suit)

        if get("shoes") != "-":
            shoe = get("shoes").lower()
            shoe_color = get("shoes_color").lower()
            if shoe_color != "-" and shoe_color != "":
                shoe = f"{shoe_color} {shoe}"
            accessory_clothing.append(shoe)

        if get("necklace") != "-":
            necklace = get("necklace").lower()
            accessory_clothing.append(necklace)
        if get("earrings") != "-":
            earrings = get("earrings").lower()
            accessory_clothing.append(earrings)
        if get("bracelet") != "-":
            bracelet = get("bracelet").lower()
            accessory_clothing.append(bracelet)
        if get("ring") != "-":
            ring = get("ring").lower()
            accessory_clothing.append(ring)
        if get("fingernail_style") != "-":
            nails = get("fingernail_style").lower()
            nail_color = get("fingernail_color").lower()
            if nail_color != "-" and nail_color != "":
                nails = f"{nails} with {nail_color} polish"
            accessory_clothing.append(nails)

        pose = get("model_pose")
        pose_phrase = ""
        if pose != "-":
            pose_phrase = f"{subj} is {pose.lower()}"

        shot = get("camera_shot")
        view = get("camera_view")
        camera_phrase = ""
        if shot != "-" and view != "-":
            camera_phrase = f"{view.lower()}, {shot.lower()} shot"
        elif shot != "-":
            camera_phrase = f"{shot.lower()} shot"
        elif view != "-":
            camera_phrase = view.lower()

        location_phrase = ""
        loc = get("location")
        if loc and loc != "-":
            location_phrase = f"in {loc.lower()}"

        lighting_phrase = ""
        lt = get("light_type")
        lq = get("light_quality")
        if lt != "-":
            if lq != "-":
                lighting_phrase = f"lit by {lq.lower()} {lt.lower()}"
            else:
                lighting_phrase = f"lit by {lt.lower()}"

        skin_details_phrase = ""
        skin_details = get("skin_details")
        if skin_details and skin_details != "-":
            skin_details_phrase = f"with {skin_details}"

        tattoos = get("tattoo")
        tattoo_phrase = ""
        if tattoos and tattoos != "-" and tattoos != "No tattoos":
            tattoo_phrase = f"{subj} has {tattoos.lower()}"

        props_color = get("props_color")
        props_color_phrase = ""
        if props_color and props_color != "-":
            props_color_phrase = f"with {props_color.lower()} props"

        all_phrase_parts = []
        if subject_sentence:
            all_phrase_parts.append(subject_sentence)
        if body_type_phrase:
            all_phrase_parts.append(body_type_phrase)
        if face_features_phrase:
            all_phrase_parts.append(face_features_phrase)
        if lips_phrase:
            all_phrase_parts.append(lips_phrase)
        if makeup_phrase:
            all_phrase_parts.append(makeup_phrase)
        if hair_phrase:
            all_phrase_parts.append(hair_phrase)
        if facial_hair_phrase:
            all_phrase_parts.append(facial_hair_phrase)
        if fashion_phrase:
            all_phrase_parts.append(fashion_phrase)
        if core_clothing:
            core_clothing_str = ", ".join(core_clothing)
            all_phrase_parts.append(f"wearing {core_clothing_str}")
        if accessory_clothing:
            accessory_clothing_str = ", ".join(accessory_clothing)
            all_phrase_parts.append(f"with {accessory_clothing_str}")
        if pose_phrase:
            all_phrase_parts.append(pose_phrase)
        if camera_phrase:
            all_phrase_parts.append(f"view is {camera_phrase}")
        if location_phrase:
            all_phrase_parts.append(location_phrase)
        if lighting_phrase:
            all_phrase_parts.append(lighting_phrase)
        if skin_details_phrase:
            all_phrase_parts.append(skin_details_phrase)
        if tattoo_phrase:
            all_phrase_parts.append(tattoo_phrase)
        if props_color_phrase:
            all_phrase_parts.append(props_color_phrase)

        main_desc = ", ".join(all_phrase_parts)

        tail = ""
        if style_prefix:
            tail = style_prefix

        if main_desc and tail:
            prompt = main_desc
            if not prompt.endswith("."):
                prompt += "."
            prompt += " " + tail
        elif main_desc:
            prompt = main_desc
            if prompt and not prompt.endswith("."):
                prompt += "."
        else:
            phrases = []
            if style_prefix:
                phrases.append(style_prefix)
            if location_phrase:
                phrases.append(f"in {location_phrase}")
            if lighting_phrase:
                phrases.append(lighting_phrase)
            main_desc = ", ".join(phrases)
            prompt = main_desc
            if prompt and not prompt.endswith("."):
                prompt += "."
        return prompt.strip()


NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Scene": CharacterPromptBuilderScene,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Scene": "Character Prompt Builder - Scene & Generate",
}
