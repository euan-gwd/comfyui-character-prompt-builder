# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] - 2026-02-15

### Changed

- **Refactored Data Loading Architecture**
  - Extracted shared utility functions into new `utils.py` module
  - `load_character_data()` - now cached with `@lru_cache(maxsize=1)` for better performance
  - `get_default_character_data()` - centralized fallback data
  - `combo()` - standardized helper for dropdown list creation
- **Eliminated Code Duplication**
  - Removed duplicate `_load_character_data()` functions from all 7 node files (~210 lines eliminated)
  - Removed duplicate `combo()` helper functions from node files
  - Removed duplicate import statements and constants
  - Standardized function signatures across all nodes
- **Improved Maintainability**
  - Single source of truth for data loading logic
  - Consistent quote style and formatting across all files
  - Better separation of concerns with dedicated utilities module

## [2.0.0] - 2026-02-01

### Added

- **Separate Male and Female Person Nodes**
  - `Character Prompt Builder - Female Person` with gender options: Woman, Girl
  - `Character Prompt Builder - Male Person` with gender options: Man, Boy
- **Male-Specific Lists**
  - `mens_body_type_list` - 32 masculine body types (Athletic, Muscular, Buff, Dad bod, etc.)
  - `mens_fashion_aesthetic_list` - 45+ masculine aesthetics (Gentleman, Military, Biker, Knight, etc.)
  - `mens_hair_style_list` - 36 male hairstyles (Buzz cut, Fade, Pompadour, Man bun, etc.)
  - `facial_hair_list` - 23 beard and mustache styles
  - `mens_tops_list` - 26 male tops (T-shirt, Polo, Dress shirt, Hoodie, etc.)
  - `mens_pants_list` - 18 male pants styles
  - `mens_hats_list` - 27 masculine hat styles
  - `mens_necklace_list` - 13 masculine necklace options
  - `mens_bracelet_list` - 11 masculine bracelet styles
  - `mens_ring_list` - 12 masculine ring types
  - `mens_watches_list` - 13 masculine watch styles
  - `mens_suits_list` - 43 suit and superhero costume options
  - `mens_standing_pose_list` - 25 masculine standing poses
  - `mens_kneeling_pose_list` - 10 masculine kneeling poses
  - `mens_sitting_pose_list` - 15 masculine sitting poses
  - `mens_laying_down_pose_list` - 10 masculine lying poses
  - `mens_props_list` - 35 masculine props (sword, gun, briefcase, sports equipment, etc.)
- **Separate Male and Female Actions Nodes**
  - `Character Prompt Builder - Female Actions` for female poses and props
  - `Character Prompt Builder - Male Actions` for male poses and props
- **Refactored Node Architecture**
  - Nodes split into separate files under `node_defs/` folder
  - Improved code organization and maintainability
- **Enforce Only Described Subjects** option in Scene & Generate node
  - Boolean toggle to prevent model hallucination of extra characters

### Changed

- Renamed `person.py` to `female_person.py` for clarity
- Renamed `actions.py` to `female_actions.py` for clarity
- Male Fashion node now uses all male-specific lists
- Female Fashion node retains original female-focused lists
- Superhero suits now have gender-specific versions

### Removed

- Generic `Character Prompt Builder - Person` node (replaced by gender-specific nodes)
- Generic `Character Prompt Builder - Actions` node (replaced by gender-specific nodes)
- Feminine items from male lists (Buxom, Curvy, Voluptuous, etc.)

## [2.2.0] - 2026-02-10

### Added

- **Render Prompt Node**
  - New `Character Prompt Builder - Render Prompt` node for displaying and editing generated prompts.
  - Integrates `simpleShowText` functionality with persistence for manual edits.
  - Automatically syncs with input changes while preserving user modifications when appropriate.
  - Added frontend extension for interactive text editing on the node.

## [2.1.0] - 2026-02-07

### Added

- New node for advanced facial expressions (e.g., "ecstatic", "melancholic") in `node_defs/facial_expression.py`
- Updated `character_prompt.json` with additional eye colors and hair styles
- Improved settings merging logic in Scene node for better prompt flow

### Changed

- Refactored combo inputs to use updated JSON data loading
- Enhanced natural language generation in Scene node to handle new settings keys

### Fixed

- Resolved issue with default values in dropdowns not resetting properly
- Fixed typo in "facial_expression" key usage

## [1.1.0] - 2026-01-XX

### Added

- Initial release
- **Character Prompt Builder - Person** node
  - Gender, age, nationality options
  - Body type and features
  - Face shape, eyes, lips, makeup
  - Hair style, length, color
  - Skin details (pores, freckles, etc.)
  - Eye detail options
- **Character Prompt Builder - Female Fashion** node
  - Fashion aesthetic styles
  - Regular and revealing outfits
  - Women's and men's shoes with colors
  - Jewelry (necklaces, earrings, bracelets, rings)
  - Fingernail styles and colors
- **Character Prompt Builder - Male Fashion** node
  - Fashion aesthetic styles
  - Regular and revealing outfits
  - Women's and men's shoes with colors
  - Jewelry (necklaces, earrings, bracelets, rings)
  - Fingernail styles and colors
- **Character Prompt Builder - Actions** node
  - Model poses
  - Regular and revealing outfits
  - Women's and men's shoes with colors
  - Jewelry (necklaces, earrings, bracelets, rings)
  - Fingernail styles and colors
- **Character Prompt Builder - Scene & Generate** node
  - Camera shot types
  - Lighting type and direction
  - Free-text location description
  - Time of day, weather, season
  - Prompt prefix and suffix
  - Natural language output mode
  - Weighted prompt output mode
  - Photorealism improvement option
- Chainable node architecture via PM_SETTINGS type
- Auto-download of portrait_prompt.json data
- Fallback default data if download fails

### Credits

- Forked from [comfyui-easy-use](https://github.com/yolain/ComfyUI-Easy-Use)
- Original Portrait Master by AI Wiz Art (Stefano Flore)
