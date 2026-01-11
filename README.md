# CharacterPromptBuilder

A standalone, modular character prompt generator for ComfyUI. Generate detailed, natural language prompts for human character creation with extensive customization options.

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- 🎨 **Modular Design** - Four chainable nodes for maximum flexibility
- 📝 **Natural Language Output** - Generates flowing, descriptive prompts
- 👤 **Comprehensive Person Options** - Age, gender, nationality, body type, face, hair, skin
- 👗 **Fashion & Accessories** - Female and male outfits, shoes, jewelry, nails
- 🏃 **Action & Pose Control** - Dedicated node for actions, poses, gestures
- 📸 **Scene Control** - Camera shots, lighting, location, weather
- 🔗 **Chainable Architecture** - Use only the nodes you need
- 📦 **Zero Dependencies** - Uses only Python standard library

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Character Prompt Builder"
3. Click Install

### Method 2: Git Clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-character-prompt-builder.git
```

### Method 3: Manual Download
1. Download the latest release
2. Extract to `ComfyUI/custom_nodes/comfyui-character-prompt-builder`
3. Restart ComfyUI

## Nodes

### 🧑 Character Prompt Builder - Person
Controls physical appearance including:

| Category | Options |
|----------|---------|
| **Subject** | Gender, age (18-90), nationality, body type |
| **Body** | Breast size, bum size (with weights) |
| **Face** | Face shape, eye color, expression, lips, makeup |
| **Hair** | Style, length, color, disheveled level, beard |
| **Skin** | Details, pores, freckles, dimples, moles, tan, acne |
| **Eyes** | Detail level, iris patterns, pupil shape |

### 👗 Character Prompt Builder - Female Fashion
Controls clothing and accessories for female subjects:

| Category | Options |
|----------|---------|
| **Style** | Fashion aesthetic (Gothic, Bohemian, Y2K, etc.) |
| **Outfit** | Dresses, skirts, tops, revealing outfits |
| **Shoes** | Women's shoes, colors |
| **Jewelry** | Necklaces, earrings, bracelets, rings |
| **Nails** | Style, color |

### 🧥 Character Prompt Builder - Male Fashion
Controls clothing and accessories for male subjects:

| Category | Options |
|----------|---------|
| **Style** | Fashion aesthetic (Casual, Formal, Streetwear, etc.) |
| **Outfit** | Suits, shirts, jackets, pants, revealing outfits |
| **Shoes** | Men's shoes, colors |
| **Accessories** | Watches, ties, hats, belts |

### 🏃 Character Prompt Builder - Action
Controls pose, action, and gesture:

| Category | Options |
|----------|---------|
| **Pose** | Standing, sitting, walking, dynamic poses, etc. |
| **Action** | Gestures, activities, interactions |
| **Expression** | Additional facial/body expressions |

### 📸 Character Prompt Builder - Scene & Generate
Controls the shot setup and generates the final prompt:

| Category | Options |
|----------|---------|
| **Camera** | Shot type, angle |
| **Lighting** | Light type, direction, intensity |
| **Location** | Free-text location description |
| **Environment** | Time of day, weather, season |
| **Prompts** | Prefix, suffix, negative prompt |
| **Output** | Natural language or weighted prompt mode |

## Usage

### Basic Workflow

```
[Character Prompt Builder - Person]
      ↓
[Character Prompt Builder - Female Fashion] or [Character Prompt Builder - Male Fashion]
      ↓
[Character Prompt Builder - Action]
      ↓
[Character Prompt Builder - Scene & Generate]
      ↓
(positive, negative)
```

- Choose either the **Female Fashion** or **Male Fashion** node after the Person node, depending on subject gender.
- The **Action** node is now a separate step for poses and actions.

### Minimal Workflow

You can skip nodes you don't need:

```
[Person] → [Scene & Generate]
```

or

```
[Person] → [Female/Male Fashion] → [Scene & Generate]
```

or

```
[Person] → [Action] → [Scene & Generate]
```

### Connection Guide
1. Add **Character Prompt Builder - Person** node
2. Connect `settings` output to **Character Prompt Builder - Female Fashion** or **Male Fashion** `settings_in`
3. Connect Fashion node's `settings` output to **Character Prompt Builder - Action** `settings_in`
4. Connect Action node's `settings` output to **Character Prompt Builder - Scene & Generate** `settings` input
5. Connect `positive` and `negative` outputs to your sampler/CLIP nodes

## Output Modes

### Natural Language
Generates flowing, descriptive sentences:
```
A 25-year-old British woman. She has a slim build. Her face features bright blue eyes
and an oval-shaped face. Her hair is blonde, long, wavy. She wears a red silk slip dress.
Captured as a portrait. The scene is lit by golden hour light from the left.
```

## Examples

### Portrait Photography
```
Person: Woman, 28, Japanese, Slim
Fashion: Minimalist aesthetic, White blouse
Action: Sitting, looking away, serene
Scene: Close-up portrait, Natural sunlight, Golden hour
```

### Editorial Fashion
```
Person: Man, 22, Brazilian, Athletic
Fashion: High Fashion aesthetic, Designer suit, Statement watch
Action: Walking, confident stride
Scene: Full body, Studio lighting, Fashion editorial pose
```

## Troubleshooting

### Nodes not appearing
1. Restart ComfyUI completely
2. Check the console for error messages
3. Ensure the folder is in `ComfyUI/custom_nodes/`

### Missing options in dropdowns
The node will auto-download `portrait_prompt.json` on first use. If this fails:
1. Check your internet connection
2. The file will be created in the `resources` folder
3. Default options will be used as fallback

## Credits

This project is forked from [comfyui-easy-use](https://github.com/yolain/ComfyUI-Easy-Use).

Original Portrait Master created by:
- **AI Wiz Art (Stefano Flore)** - [stefanoflore.it](https://stefanoflore.it) | [ai-wiz.art](https://ai-wiz.art)

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Changelog

### v1.1.0
- Split Fashion node into separate Female and Male nodes
- Added Action node for poses and actions
- Updated workflow: Person → Female/Male Fashion → Action → Scene & Generate
- Improved modularity and customization
- **Removed weighted prompt output; only natural language prompts are now generated**

### v1.0.0
- Initial release
- Three modular nodes: Person, Fashion, Scene
- Natural language prompt output mode
- Comprehensive portrait customization options
- Location and environment settings
