# AGENTS.md - Character Prompt Builder

## Project Overview

ComfyUI custom node package for generating detailed character prompts. Uses a modular, chainable architecture where nodes pass `PM_SETTINGS` dictionaries to build comprehensive character descriptions.

**Python**: 3.10+ | **Dependencies**: None (stdlib only)

---

## Build/Lint/Test Commands

This project has no formal test suite or linting infrastructure. Manual testing via ComfyUI is the primary validation method.

### Python Validation
```bash
# Check syntax on a specific file
python -m py_compile nodes.py

# Validate all Python files
python -m py_compile node_defs/*.py utils.py render_prompt.py
```

### Installation
```bash
# Install in development mode (optional)
cd ComfyUI/custom_nodes
git clone https://github.com/euan-gwd/comfyui-character-prompt-builder.git
# Restart ComfyUI to load nodes
```

---

## Code Style Guidelines

### General Principles
- **Zero dependencies**: Use only Python standard library (`json`, `os`, `urllib`, etc.)
- **PEP 8 compliant**: Follow standard Python conventions
- **No external type checking**: No mypy, ruff, or other linting tools configured

### File Structure
```
├── __init__.py           # Package entry point, exports NODE_CLASS_MAPPINGS
├── nodes.py              # Aggregates all node mappings
├── utils.py              # Shared utilities (load_character_data, combo helper)
├── render_prompt.py      # Prompt rendering/output node
├── node_defs/            # Individual node definitions
│   ├── female_person.py
│   ├── male_person.py
│   ├── female_fashion.py
│   ├── male_fashion.py
│   ├── female_poses.py
│   ├── male_poses.py
│   ├── scene.py
│   ├── spaceship_character.py
│   └── spaceship_mods.py
└── resources/            # JSON data files (auto-downloaded if missing)
```

### Node Definition Pattern

```python
class CharacterPromptBuilderNodeName:
    @classmethod
    def INPUT_TYPES(s):
        data = load_character_data()
        return {
            "required": {
                # required inputs
            },
            "optional": {
                "settings_in": ("PM_SETTINGS",),  # Chain input
            },
        }

    RETURN_TYPES = ("PM_SETTINGS",)
    RETURN_NAMES = ("settings",)
    FUNCTION = "run"
    CATEGORY = "CharacterPromptBuilder"

    def run(self, ..., settings_in=None):
        settings = settings_in.copy() if settings_in else {}
        settings.update({...})
        return (settings,)


NODE_CLASS_MAPPINGS = {"Node Display Name": CharacterPromptBuilderNodeName}
NODE_DISPLAY_NAME_MAPPINGS = {"Node Display Name": "Display Name"}
```

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Classes | PascalCase | `CharacterPromptBuilderFemalePerson` |
| Functions | snake_case | `load_character_data`, `combo` |
| Settings keys | snake_case | `facial_expression`, `breast_size` |
| Node names | PascalCase | `Character Prompt Builder Female Person` |
| Display names | Title Case | `Character Prompt Builder - Female Person` |
| JSON lists | snake_case + `_list` | `eyes_color_list`, `hair_style_list` |

### Imports
- Use relative imports within the package: `from ..utils import load_character_data`
- Aggregate node mappings in `nodes.py` using dictionary unpacking
- Import pattern for nodes:
```python
from .node_defs.female_person import NODE_CLASS_MAPPINGS as FEMALE_PERSON_CLASS_MAPPINGS
from .node_defs.female_person import NODE_DISPLAY_NAME_MAPPINGS as FEMALE_PERSON_DISPLAY_NAME_MAPPINGS
```

### Settings Merging
```python
settings = settings_in.copy() if settings_in else {}
settings.update({
    "key": value,
})
```

### Combo Helper Usage
```python
# Always include "-" as default option
nationality_1: combo(data, "nationality_list", "British"),  # With default
eyes_color: combo(data, "eyes_color_list"),                   # No default
```

### Error Handling
- Network failures in `load_character_data()`: Print warning, return `get_default_character_data()`
- Use `get(key, default="-")` for safe dict access during prompt generation
- No try/except wrapping of node logic (let exceptions propagate to ComfyUI)

### Data Flow
1. **Person nodes** (Female/Male) → collect physical attributes
2. **Fashion nodes** → add clothing/accessories
3. **Poses/Action nodes** → add poses and gestures
4. **Scene node** → generates natural language prompt from accumulated settings
5. **Render Prompt** → displays/outputs the final prompt

### Adding New Features

**New option in JSON (no code change needed)**:
- Add entry to `character_prompt.json` under appropriate list key
- Example: Add `"hazel"` to `eyes_color_list`

**New node**:
1. Create `node_defs/new_feature.py` with class definition
2. Import in `nodes.py` with `*_CLASS_MAPPINGS` and `*_DISPLAY_NAME_MAPPINGS`
3. Add to aggregated `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`

**New JSON data key**:
1. Add key to `resources/character_prompt.json`
2. Use `combo(data, "new_key_list")` in node's `INPUT_TYPES`

### Custom Node Requirements

Each node class **must** define:
- `INPUT_TYPES()` classmethod returning dict with `required`/`optional` sections
- `RETURN_TYPES = ("PM_SETTINGS",)`
- `RETURN_NAMES = ("settings",)`
- `FUNCTION = "run"`
- `CATEGORY = "CharacterPromptBuilder"`
- `run()` method that accepts `settings_in` parameter and returns tuple

### ComfyUI Integration

`__init__.py` must export:
```python
NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS
```

---

## Copilot Instructions (from .github/copilot-instructions.md)

- **Node Structure**: Class with `INPUT_TYPES()`, `RETURN_TYPES = ("PM_SETTINGS",)`, `run()` method updating settings dict
- **Combo Inputs**: Use `combo(key)` helper to create dropdowns from JSON data; always include `"-"` as default
- **Settings Merging**: `settings = settings_in.copy() if settings_in else {}; settings.update({...})`
- **JSON Data**: Loaded via `_load_character_data()`; downloads from GitHub if missing
- Chain: Person → Fashion → Actions → Scene
- Scene node handles prompt generation; other nodes focus on data collection
- Use `get(key, default="-")` in generation for safe dict access
