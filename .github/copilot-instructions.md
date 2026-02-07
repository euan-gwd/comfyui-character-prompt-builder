# ComfyUI Character Prompt Builder - AI Coding Guidelines

## Project Overview

This is a ComfyUI custom node package that generates detailed character prompts for AI image generation. It uses a modular, chainable architecture where nodes pass `PM_SETTINGS` dictionaries to build comprehensive character descriptions.

## Architecture

- **Node Structure**: Each node in `node_defs/` defines INPUT_TYPES with dropdowns populated from `resources/character_prompt.json`
- **Data Flow**: Nodes accumulate settings in a shared dict, merged in the Scene node for natural language generation
- **Settings Type**: `PM_SETTINGS` is a Python dict with string keys/values; use `settings_in.copy()` to merge

## Key Patterns

- **Node Definition**: Class with `INPUT_TYPES()`, `RETURN_TYPES = ("PM_SETTINGS",)`, `run()` method updating settings dict
- **Combo Inputs**: Use `combo(key)` helper to create dropdowns from JSON data; always include `"-"` as default
- **Settings Merging**: `settings = settings_in.copy() if settings_in else {}; settings.update({...})`
- **JSON Data**: Loaded via `_load_character_data()`; downloads from GitHub if missing

## Development Workflow

- Add new options to `character_prompt.json` first, then update node INPUT_TYPES
- Test nodes individually in ComfyUI by connecting to Scene node
- Maintain gender-specific nodes (Female/Male) for tailored options
- Use natural language generation in Scene node for flowing prompts

## Examples

- **Adding a new eye color**: Add to `eyes_color_list` in JSON, no code changes needed
- **New node**: Create `node_defs/new_feature.py`, import in `nodes.py`, add to mappings
- **Settings key**: Use snake_case, e.g., `"facial_expression"` → `"happy"`

## Conventions

- Nodes return single `PM_SETTINGS` dict, not multiple outputs
- Scene node handles prompt generation; other nodes focus on data collection
- Use `get(key, default="-")` in generation for safe dict access
- Chain: Person → Fashion → Actions → Scene

## Integration

- ComfyUI expects `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` in `__init__.py`
- No external dependencies; pure Python with stdlib only
- Resources auto-download on first use

dont summarize conversation history, just provide the code changes in the recent edits.
