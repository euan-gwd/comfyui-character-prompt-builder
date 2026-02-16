"""
Character Prompt Builder - Scene Node
"""

import re
from ..utils import load_character_data, combo


class CharacterPromptBuilderScene:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()

        return {
            "required": {
                "num_people": (["1", "2", "3", "4"], {"default": "1"}),
                "settings1": ("PM_SETTINGS",),
                "artistic_style": combo(
                    data, "artistic_style_list", "professional photography"
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
                    data,
                    "camera_view_list",
                    "front view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel1_camera_shot": combo(
                    data,
                    "camera_shot_list",
                    "wide",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel2_camera_view": combo(
                    data,
                    "camera_view_list",
                    "back view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel2_camera_shot": combo(
                    data,
                    "camera_shot_list",
                    "wide",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel3_camera_view": combo(
                    data,
                    "camera_view_list",
                    "right side view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel3_camera_shot": combo(
                    data,
                    "camera_shot_list",
                    "wide",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel4_camera_view": combo(
                    data,
                    "camera_view_list",
                    "front view",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "panel4_camera_shot": combo(
                    data,
                    "camera_shot_list",
                    "medium close up",
                    {
                        "display": "dropdown",
                        "visible": "artistic_style == '4-panel character sheet'",
                    },
                ),
                "camera_model": combo(data, "camera_model_list"),
                "camera_lens": combo(data, "camera_lens_specs"),
                "camera_horizontal_angle": combo(data, "camera_horizontal_angle_list"),
                "camera_vertical_angle": combo(data, "camera_vertical_angle_list"),
                "camera_shot": combo(data, "camera_shot_list"),
                "camera_view": combo(data, "camera_view_list"),
                "preset_location": combo(data, "location_list"),
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
                "light_type": combo(data, "light_type_list"),
                "light_quality": combo(data, "light_quality_list"),
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

        # CUSTOM CLOTHING (both genders) - add to core clothing
        custom_clothing = s.get("custom_clothing", "")
        if custom_clothing and custom_clothing.strip():
            core_clothing.append(custom_clothing.strip())

        # Breasts and bum (for women)
        body_features = []

        if (
            get("breast_size") != "-" or get("breast_cup_size") != "-"
        ) and gender == "Woman":
            breast_size = get("breast_size")
            breast_cup_size = get("breast_cup_size")
            breast_shape = get("breast_shape")
            breast_desc = ""
            if breast_size != "-":
                breast_desc += f"{breast_size.lower()} "
            if breast_cup_size != "-":
                breast_desc += f"{breast_cup_size} cup "
            if breast_shape != "-":
                breast_desc += f"{breast_shape.lower()}-shaped "
            breast_desc = breast_desc.strip()
            body_features.append(f"{breast_desc} breasts")

        if get("bum_size") != "-":
            body_features.append(f"{get('bum_size').lower()} bum")
        if get("waist_size") != "-":
            body_features.append(f"{get('waist_size').lower()} waist")
        body_features_phrase = ""
        if body_features:
            body_features_phrase = f"{subj} has " + " and ".join(body_features)

        # --- BEGIN: Subtle nipple outline logic ---
        subtle_nipple_phrase = ""
        extra_clothing_description = None
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
            and ((get("tops") != "-") or (get("dresses") != "-"))
            and garment_material != "-"
            and stretched_material
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
            subtle_nipple_phrase = f"Her {garment}, made of {garment_material}, is tightly stretched and visibly compressing her {details_str}, conforming closely to her shape and realistically revealing the natural contours beneath the fabric, including subtle outlines, the effect is natural and realistic, never explicit or exposed"
            extra_clothing_description = subtle_nipple_phrase
        # --- END: Subtle nipple outline logic ---

        # Generate separate core and accessory clothing phrases (like shoes pattern)
        core_clothing_phrase = ""
        accessory_clothing_phrase = ""

        # Build core_clothing_phrase
        if core_clothing:
            if len(core_clothing) == 1:
                clothing_str = core_clothing[0]
            elif len(core_clothing) == 2:
                clothing_str = f"{core_clothing[0]} and {core_clothing[1]}"
            else:
                clothing_str = (
                    ", ".join(core_clothing[:-1]) + f", and {core_clothing[-1]}"
                )

            if extra_clothing_description:
                core_clothing_phrase = f"{subj} {get_verb(subj)} wearing {clothing_str}, {extra_clothing_description}"
            else:
                core_clothing_phrase = f"{subj} {get_verb(subj)} wearing {clothing_str}"

            # If body features exist, append "covering ..." after core clothing
            if body_features_phrase:
                covering_features = re.sub(
                    f"^{subj} has ",
                    f"{poss} ",
                    body_features_phrase,
                    flags=re.IGNORECASE,
                )
                core_clothing_phrase += f" covering {covering_features}"
                body_features_phrase = ""

        # Build accessory_clothing_phrase
        if accessory_clothing:
            if len(accessory_clothing) == 1:
                accessory_str = accessory_clothing[0]
            elif len(accessory_clothing) == 2:
                accessory_str = f"{accessory_clothing[0]} and {accessory_clothing[1]}"
            else:
                accessory_str = (
                    ", ".join(accessory_clothing[:-1])
                    + f", and {accessory_clothing[-1]}"
                )

            accessory_clothing_phrase = (
                f"{subj} {get_verb(subj)} wearing {accessory_str}"
            )

        # Handle nude/shirtless cases when no core clothing
        if not core_clothing:
            if gender == "Woman":
                nipple_desc = ""
                if get("nipple_appearance") != "-":
                    nipple_desc = get("nipple_appearance").lower()
                areola_desc = ""
                if get("areola_appearance") != "-":
                    areola_desc = get("areola_appearance").lower()
                details = []
                if nipple_desc:
                    details.append(f"{nipple_desc} nipples")
                if areola_desc:
                    details.append(f"and {poss} {areola_desc} areolae")
                if details:
                    details_str = ", ".join(details)
                else:
                    details_str = "breasts and nipples"

                if accessory_clothing:
                    # Has accessory clothing but no core - add nude description
                    accessory_clothing_phrase += f" and {get_verb(subj)} completely nude and {poss} {details_str} are visible"
                else:
                    # Completely nude
                    core_clothing_phrase = f"{subj} {get_verb(subj)} completely nude and {poss} {details_str} are visible"
            elif gender == "Man":
                if accessory_clothing:
                    accessory_clothing_phrase += " and is otherwise shirtless"
                else:
                    core_clothing_phrase = f"{subj} {get_verb(subj)} shirtless"

        # Shoes - gender specific
        shoes_phrase = ""
        if get("womens_shoes") != "-" and gender == "Woman":
            shoe_desc = get("womens_shoes").lower()
            if get("womens_shoe_color") != "-":
                shoe_desc = f"{get('womens_shoe_color').lower()} {shoe_desc}"
            shoe_material = s.get("womens_shoe_material", "-")
            if shoe_material and shoe_material != "-":
                shoe_desc = f"{shoe_desc} made of {shoe_material.lower()}"
            shoes_phrase = f"{subj} {get_verb(subj)} wearing {shoe_desc}"
        # MENS SHOES
        if s.get("mens_shoes", "-") != "-" and gender == "Man":
            shoe_desc = s.get("mens_shoes").lower()
            if s.get("mens_shoe_color", "-") != "-":
                shoe_desc = f"{s.get('mens_shoe_color').lower()} {shoe_desc}"
            shoe_material = s.get("mens_shoe_material", "-")
            if shoe_material and shoe_material != "-":
                shoe_desc = f"{shoe_desc} made of {shoe_material.lower()}"
            shoes_phrase = f"{subj} {get_verb(subj)} wearing {shoe_desc}"

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
        mask = ""
        mask_color = ""
        mask_material = ""
        if s.get("mens_mask", "-") != "-" and s.get("gender", "-") == "Man":
            mask = s.get("mens_mask").lower()
            mask_color = s.get("mens_mask_color", "-").lower()
            mask_material = s.get("mens_mask_material", "-").lower()
        if s.get("womens_mask", "-") != "-" and s.get("gender", "-") == "Woman":
            mask = s.get("womens_mask").lower()
            mask_color = s.get("womens_mask_color", "-").lower()
            mask_material = s.get("womens_mask_material", "-").lower()
        accessory_parts = []
        if necklace != "-":
            accessory_parts.append(f"{get('necklace').lower()} necklace")
        if earrings != "-":
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
            accessory_parts.append(f"{glasses}")
        if mask and mask != "-":
            mask_desc = mask
            if mask_color != "-" and mask_color != "":
                mask_desc = f"{mask_color} {mask_desc}"
            if mask_material != "-" and mask_material != "":
                mask_desc = f"{mask_desc} made of {mask_material}"
            accessory_parts.append(f"{mask_desc}")
        jewelry_phrase = ""
        if accessory_parts:
            # Use Oxford comma for last item
            if len(accessory_parts) == 1:
                jewelry_phrase = f"accessorized with {accessory_parts[0]}"
            else:
                jewelry_phrase = (
                    f"accessorized with "
                    + ", ".join(accessory_parts[:-1])
                    + f", and {accessory_parts[-1]}"
                )

        # Fingernails (for women, if not wearing gloves)
        fingernails_present = get("fingernail_style") != "-" and gender == "Woman"
        gloves_type = s.get("womens_gloves", "-").lower()
        gloves_present = gloves_type != "-" and s.get("gender", "-") == "Woman"
        show_fingernails = fingernails_present and (
            not gloves_present or "fingerless" in gloves_type
        )
        fingernail_phrase = ""
        if show_fingernails:
            fingernail_style = get("fingernail_style").lower().replace(" nails", "")
            nail_color = (
                get("fingernail_color").lower()
                if get("fingernail_color") != "-"
                else ""
            )
            if nail_color:
                fingernail_phrase = (
                    f"{poss} fingernails are {fingernail_style}, painted {nail_color}"
                )
            else:
                fingernail_phrase = f"{poss} fingernails are {fingernail_style}"
        elif not gloves_present and gender == "Woman":
            fingernail_phrase = f"{poss} hands and fingers are visible"

        pose = get("model_pose")
        pose_phrase = ""
        if pose != "-":
            pose_phrase = f"{subj} is {pose.lower()}"

        skin_details_phrase = ""
        skin_details = get("skin_details")
        if skin_details and skin_details != "-":
            skin_details_phrase = f"with {skin_details}"

        tattoos = get("tattoo")
        tattoo_phrase = ""
        if tattoos and tattoos != "-" and tattoos != "No tattoos":
            tattoo_phrase = f"{subj} has {tattoos.lower()}"

        # Props handling with action parsing
        props = s.get("props", "-")
        props_color = s.get("props_color", "-")
        props_phrase = ""
        if props and props != "-":
            # If props starts with a verb (e.g., "holding", "carrying"), insert color before the object
            match = re.match(r"(\w+ing) (a|an|the)? ?(.+)", props.lower())
            if match:
                verb = match.group(1)
                article = match.group(2) or ""
                obj = match.group(3)
                if props_color and props_color != "-":
                    props_phrase = f"{subj.lower()} {get_verb(subj)} {verb} {article} {props_color.lower()} {obj}".replace(
                        "  ", " "
                    )
                else:
                    props_phrase = f"{subj.lower()} {get_verb(subj)} {verb} {article} {obj}".replace(
                        "  ", " "
                    )
            else:
                # fallback: just append color before prop
                if props_color and props_color != "-":
                    props_phrase = f"{subj.lower()} {get_verb(subj)} {props_color.lower()} {props.lower()}"
                else:
                    props_phrase = f"{subj.lower()} {get_verb(subj)} {props.lower()}"

        # Custom action/pose
        custom_action = s.get("custom_action", "") or s.get("custom_pose", "")
        custom_action_phrase = ""
        if custom_action and custom_action.strip():
            custom_action_phrase = custom_action.strip()

        # Expression
        expression_phrase = ""
        if get("facial_expression") != "-":
            expression_phrase = (
                f"{subj} has a {get('facial_expression').lower()} facial expression"
            )

        # Camera shot and view
        camera_shot_view_phrase = ""
        if get("camera_shot") != "-" and get("camera_view") != "-":
            camera_shot_view_phrase = (
                f"{get('camera_view').lower()}, {get('camera_shot').lower()}"
            )
        elif get("camera_shot") != "-":
            camera_shot_view_phrase = f"{get('camera_shot').lower()}"
        elif get("camera_view") != "-":
            camera_shot_view_phrase = get("camera_view").lower()
        if camera_shot_view_phrase:
            camera_shot_view_phrase = f"{camera_shot_view_phrase} shot"

        # Camera angles
        camera_horizontal = get("camera_horizontal_angle")
        camera_vertical = get("camera_vertical_angle")
        camera_horizontal_angle_phrase = ""
        camera_vertical_angle_phrase = ""
        camera_combined_angle_phrase = ""
        if camera_horizontal != "-" and camera_vertical != "-":
            camera_combined_angle_phrase = f"set at a {camera_horizontal.lower()} and is set at a {camera_vertical.lower()}"
        else:
            if camera_horizontal != "-":
                camera_horizontal_angle_phrase = f"set at a {camera_horizontal.lower()}"
            if camera_vertical != "-":
                camera_vertical_angle_phrase = f"set at a {camera_vertical.lower()}"

        camera_lens_phrase = ""
        if get("camera_lens") != "-":
            camera_lens_phrase = f"the camera lens is a {get('camera_lens').lower()}"

        camera_model_phrase = ""
        if get("camera_model") != "-":
            camera_model_phrase = f"the camera is a {get('camera_model').lower()}"

        # Location
        location = get("location", "")
        location_phrase = ""
        if location and location.strip():
            location_phrase = f"The scene takes place {location.strip()}"
        elif s.get("preset_location") and s.get("preset_location") != "-":
            location_phrase = f"The scene takes place {s.get('preset_location')}"

        # Lighting
        lighting_phrase = ""
        if get("light_type") != "-":
            light_desc = ""
            if get("light_quality") != "-":
                light_desc += get("light_quality").lower()
            if get("light_type") != "-":
                if light_desc:
                    light_desc += " "
                light_desc += get("light_type").lower()
            lighting_phrase = f"The scene is lit by {light_desc}"

        # Environment
        env_parts = []
        if get("time_of_day") != "-":
            env_parts.append(f"It is {get('time_of_day').lower()}")
        if get("weather") != "-":
            env_parts.append(f"The weather is {get('weather').lower()}")
        if get("season") != "-":
            env_parts.append(f"It is {get('season').lower()} season")
        environment_phrase = " ".join(env_parts)

        # Skin features
        skin_features = []
        if skin_details and skin_details != "-":
            skin_features.append(skin_details)
        freckles_val = s.get("freckles", "-")
        if freckles_val and freckles_val != "-":
            skin_features.append(freckles_val)
        dimples_val = s.get("dimples", "-")
        if dimples_val and dimples_val != "-":
            skin_features.append(dimples_val)
        moles_val = s.get("moles", "-")
        if moles_val and moles_val != "-":
            skin_features.append(moles_val)
        tanned_skin_val = s.get("tanned_skin", "-")
        if tanned_skin_val and tanned_skin_val != "-":
            skin_features.append(tanned_skin_val)
        skin_acne_val = s.get("skin_acne", "-")
        if skin_acne_val and skin_acne_val != "-":
            skin_features.append(skin_acne_val)
        skin_imperfections_val = s.get("skin_imperfections", "-")
        if skin_imperfections_val and skin_imperfections_val != "-":
            skin_features.append(skin_imperfections_val)
        skin_phrase = ""
        if skin_features:
            skin_phrase = f"{poss} skin shows " + ", ".join(skin_features)

        # Compose into a single natural language paragraph
        phrases = [
            camera_shot_view_phrase,
            style_prefix if style_prefix else None,
            camera_model_phrase,
            camera_lens_phrase,
            camera_combined_angle_phrase
            if camera_combined_angle_phrase
            else camera_horizontal_angle_phrase,
            camera_vertical_angle_phrase if not camera_combined_angle_phrase else "",
            subject_sentence,
            body_type_phrase,
            pose_phrase,
            custom_action_phrase,
            props_phrase,
            face_features_phrase,
            lips_phrase,
            hair_phrase,
            facial_hair_phrase,
            makeup_phrase,
            expression_phrase,
            body_features_phrase,
            core_clothing_phrase,
            accessory_clothing_phrase,
            shoes_phrase,
            jewelry_phrase,
            fingernail_phrase,
            skin_phrase,
            tattoo_phrase,
            fashion_phrase,
        ]

        # For multi-person (include_scene_tail=False), exclude location/environment/lighting
        if include_scene_tail:
            tail_phrases = [
                location_phrase,
                environment_phrase,
                lighting_phrase,
            ]
        else:
            tail_phrases = []

        # Remove empty phrases and strip
        phrases = [p.strip() for p in phrases if p and p.strip()]
        tail_phrases = [p.strip() for p in tail_phrases if p and p.strip()]

        # 4-panel character sheet handling
        if s.get("artistic_style") == "4-panel character sheet":
            panels = [
                (
                    s.get("panel1_camera_view", "front view"),
                    s.get("panel1_camera_shot", "wide"),
                    "Panel 1",
                ),
                (
                    s.get("panel2_camera_view", "back view"),
                    s.get("panel2_camera_shot", "wide"),
                    "Panel 2",
                ),
                (
                    s.get("panel3_camera_view", "right side view"),
                    s.get("panel3_camera_shot", "wide"),
                    "Panel 3",
                ),
                (
                    s.get("panel4_camera_view", "front view"),
                    s.get("panel4_camera_shot", "medium close up"),
                    "Panel 4",
                ),
            ]
            panel_prompts = []
            # Choose style prefix based on character_sheet_render_style
            if character_sheet_render_style == "photorealistic":
                style_prefix = "photorealistic"
            else:
                style_prefix = "Ink drawn comic book illustration"
            for camera_view, camera_shot, panel_name in panels:
                # Build the camera phrase from view and shot
                camera_phrase = ""
                if camera_view != "-" and camera_shot != "-":
                    camera_phrase = f"{camera_view.lower()} {camera_shot.lower()} shot"
                elif camera_view != "-":
                    camera_phrase = f"{camera_view.lower()} shot"
                elif camera_shot != "-":
                    camera_phrase = f"{camera_shot.lower()} shot"

                # Update phrases with the new camera phrase
                panel_phrases = phrases.copy()
                # Remove any phrase containing "4-panel character sheet style"
                panel_phrases = [
                    p
                    for p in panel_phrases
                    if not (p and "4-panel character sheet style" in p)
                ]
                # Remove the original camera_shot_view_phrase if present (first phrase)
                if (
                    panel_phrases
                    and camera_shot_view_phrase
                    and panel_phrases[0] == camera_shot_view_phrase
                ):
                    panel_phrases.pop(0)
                # Insert the camera phrase at the beginning
                if camera_phrase:
                    panel_phrases.insert(0, camera_phrase)
                main_desc_panel = ", ".join(panel_phrases) + "\n"
                panel_prompts.append(f"{panel_name}: {main_desc_panel}")
            prompt = (
                f"Generate a {style_prefix} character model sheet image with 4 evenly spaced vertical column panels: \n\n"
                + "\n".join(panel_prompts)
            )
            return prompt
        else:
            # Add tail if include_scene_tail
            tail_phrases = []
            if include_scene_tail:
                # Location
                location = s.get("location", "")
                if location and location.strip():
                    tail_phrases.append(f"The scene takes place {location.strip()}")
                elif s.get("preset_location") and s.get("preset_location") != "-":
                    tail_phrases.append(
                        f"The scene takes place {s.get('preset_location')}"
                    )
                # Environment
                env_parts = []
                if s.get("time_of_day") != "-":
                    env_parts.append(f"It is {s.get('time_of_day').lower()}")
                if s.get("weather") != "-":
                    env_parts.append(f"The weather is {s.get('weather').lower()}")
                if s.get("season") != "-":
                    env_parts.append(f"It is {s.get('season').lower()} season")
                if env_parts:
                    tail_phrases.append(" ".join(env_parts))
                # Lighting
                if s.get("light_type") != "-":
                    light_desc = ""
                    if s.get("light_quality", "-") != "-":
                        light_desc += s.get("light_quality").lower()
                    if s.get("light_type") != "-":
                        if light_desc:
                            light_desc += " "
                        light_desc += s.get("light_type").lower()
                    tail_phrases.append(f"The scene is lit by {light_desc}")

            tail = ". ".join(tail_phrases)
            if tail:
                main_desc = ", ".join(phrases)
                prompt = main_desc
                if not prompt.endswith("."):
                    prompt += "."
                prompt += " " + tail
            else:
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
