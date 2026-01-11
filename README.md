# ComfyUI Prompt Master

A standalone, modular portrait prompt generator for ComfyUI. Generate detailed, natural language or weighted prompts for portrait photography with extensive customization options.

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)
![Python](https://img.shields.io/badge/Python-3.10%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- 🎨 **Modular Design** - Three chainable nodes for maximum flexibility
- 📝 **Dual Output Modes** - Natural language or SD-weighted prompts
- 👤 **Comprehensive Person Options** - Age, gender, nationality, body type, face, hair, skin
- 👗 **Fashion & Accessories** - Outfits, shoes, jewelry, nails
- 📸 **Scene Control** - Camera shots, poses, lighting, location, weather
- 🔗 **Chainable Architecture** - Use only the nodes you need
- 📦 **Zero Dependencies** - Uses only Python standard library

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Prompt Master"
3. Click Install

### Method 2: Git Clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-prompt-master.git
```

### Method 3: Manual Download
1. Download the latest release
2. Extract to `ComfyUI/custom_nodes/comfyui-prompt-master`
3. Restart ComfyUI

## Nodes

### 🧑 Prompt Master - Person
Controls physical appearance including:

| Category | Options |
|----------|---------|
| **Subject** | Gender, age (18-90), nationality, body type |
| **Body** | Breast size, bum size (with weights) |
| **Face** | Face shape, eye color, expression, lips, makeup |
| **Hair** | Style, length, color, disheveled level, beard |
| **Skin** | Details, pores, freckles, dimples, moles, tan, acne |
| **Eyes** | Detail level, iris patterns, pupil shape |

### 👗 Prompt Master - Fashion
Controls clothing and accessories:

| Category | Options |
|----------|---------|
| **Style** | Fashion aesthetic (Gothic, Bohemian, Y2K, etc.) |
| **Outfit** | Regular outfits, revealing outfits |
| **Shoes** | Women's shoes, men's shoes, colors |
| **Jewelry** | Necklaces, earrings, bracelets, rings |
| **Nails** | Style, color |

### 📸 Prompt Master - Scene & Generate
Controls the shot setup and generates the final prompt:

| Category | Options |
|----------|---------|
| **Camera** | Shot type, model pose |
| **Lighting** | Light type, direction, intensity |
| **Location** | Free-text location description |
| **Environment** | Time of day, weather, season |
| **Prompts** | Prefix, suffix, negative prompt |
| **Output** | Natural language or weighted prompt mode |

## Usage

### Basic Workflow

```
[Prompt Master - Person] → [Prompt Master - Fashion] → [Prompt Master - Scene & Generate]
        ↓                           ↓                              ↓
   (settings out)          (settings in/out)              (positive, negative)
```

### Minimal Workflow
You can skip nodes you don't need:

```
[Prompt Master - Person] → [Prompt Master - Scene & Generate]
```

### Connection Guide
1. Add **Prompt Master - Person** node
2. Connect `settings` output to **Prompt Master - Fashion** `settings_in`
3. Connect Fashion's `settings` output to **Prompt Master - Scene & Generate** `settings` input
4. Connect `positive` and `negative` outputs to your sampler/CLIP nodes

## Output Modes

### Natural Language
Generates flowing, descriptive sentences:
```
A 25-year-old British woman. She has a slim build. Her face features bright blue eyes
and an oval-shaped face. Her hair is blonde, long, wavy. She wears a red silk slip dress.
Captured as a portrait. The scene is lit by golden hour light from the left.
```

### Weighted Prompt
Generates SD-style weighted tags:
```
(portrait:1.0), (British girl 25-years-old:1.5), (slim, slim body:0.8), (blue eyes:1.25),
(oval face:0.7), (blonde hair:1.25), (long hair:1.25), (wavy hair:1.25),
(wearing red silk slip dress:1.0), (golden hour light left:0.9)
```

## Examples

### Portrait Photography
```
Person: Woman, 28, Japanese, Slim
Face: Oval, Brown eyes, Serene expression
Hair: Long, Black, Straight
Fashion: Minimalist aesthetic, White blouse
Scene: Close-up portrait, Natural sunlight, Golden hour
```

### Editorial Fashion
```
Person: Woman, 22, Brazilian, Athletic
Face: Heart-shaped, Green eyes, Confident
Hair: Medium, Auburn, Wavy
Fashion: High Fashion aesthetic, Designer gown, Statement jewelry
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

### v1.0.0
- Initial release
- Three modular nodes: Person, Fashion, Scene
- Natural language and weighted prompt output modes
- Comprehensive portrait customization options
- Location and environment settings
