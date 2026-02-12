# AGENTS.md

Coding guidelines for AI agents working on the ComfyUI Character Prompt Builder repository.

## Project Overview

A ComfyUI custom node package for generating detailed character prompts for AI image generation. Uses a modular, chainable architecture where nodes pass `PM_SETTINGS` dictionaries to build comprehensive character descriptions.

## Build/Test/Lint Commands

This project runs in a uv environment. Use `python3` instead of `python`:

```bash
# No formal test suite - manual testing in ComfyUI required
# To verify Python syntax:
python3 -m py_compile node_defs/*.py nodes.py __init__.py

# Check imports work:
python3 -c "from nodes import NODE_CLASS_MAPPINGS; print('OK')"

# Install for development (in ComfyUI/custom_nodes/):
pip install -e ./comfyui-character-prompt-builder
```

## Code Style Guidelines

### Python Style
- Use double quotes for strings consistently
- Indent with 4 spaces
- Maximum line length: follow existing patterns (~100-120 chars)
- Use snake_case for variables, functions, and settings keys
- Use CamelCase for class names

### Imports
```python
# Standard library first
import json
import os
from urllib.request import urlopen

# Local imports use relative paths
from .node_defs.female_person import NODE_CLASS_MAPPINGS as FEMALE_PERSON_CLASS_MAPPINGS
```

### Node Structure Pattern
```python
class CharacterPromptBuilderFeatureName:
    @classmethod
    def INPUT_TYPES(s):
        data = _load_character_data()
        
        def combo(key, default=None):
            _list = data.get(key, ["-"]).copy()
            if '-' not in _list:
                _list.insert(0, '-')
            return (_list, {"default": default} if default else {})
        
        return {
            "required": {},
            "optional": {
                "settings_in": ("PM_SETTINGS",),
            }
        }
    
    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"
    
    def run(self, param="-", settings_in=None):
        settings = settings_in.copy() if settings_in else {}
        settings.update({"param": param})
        return (settings,)

NODE_CLASS_MAPPINGS = {
    "Character Prompt Builder Feature Name": CharacterPromptBuilderFeatureName,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Character Prompt Builder Feature Name": "Character Prompt Builder - Feature Name",
}
```

### Key Conventions

1. **Settings Merging**: Always use `settings_in.copy() if settings_in else {}` to avoid mutation
2. **Dropdown Defaults**: Always include `"-"` as the first/default option in combo lists
3. **Settings Keys**: Use snake_case (e.g., `facial_expression`, `hair_style`)
4. **Optional Inputs**: Include `settings_in` as optional for chaining
5. **Data Loading**: Use `_load_character_data()` helper to access JSON resources
6. **Safe Access**: Use `data.get(key, ["-"])` for dict access with defaults
7. **Node Naming**: Prefix classes with `CharacterPromptBuilder`, use display names with " - " separator

### Data Flow Pattern

Nodes chain together: Person → Fashion → Poses → Actions → Scene
Each node receives `PM_SETTINGS` dict, adds its data, passes it forward.
Scene node converts accumulated settings to natural language prompt.

### Error Handling

```python
try:
    response = urlopen(url)
    data = json.loads(response.read())
except Exception as e:
    print(f"[CharacterPromptBuilder] Warning: {e}")
    return default_data
```

### Resource Management

- JSON data loads from `resources/character_prompt.json`
- Auto-downloads from GitHub if missing
- Package directory resolved via `os.path.dirname(os.path.realpath(__file__))`

### ComfyUI Integration Requirements

- Export `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` in `__init__.py`
- Set `WEB_DIRECTORY = "./web"` for frontend assets
- Return types as tuples: `(settings,)` not `settings`
- Use `"PM_SETTINGS"` as the custom type identifier

## Development Workflow

1. Add new options to `resources/character_prompt.json` first
2. Update node `INPUT_TYPES` to reference new JSON keys
3. Update `run()` method to handle new parameters
4. Test in ComfyUI by connecting to Scene node
5. Update mappings in `nodes.py` if adding new node files

## Copilot Instructions

See `.github/copilot-instructions.md` for additional context on architecture and examples.
