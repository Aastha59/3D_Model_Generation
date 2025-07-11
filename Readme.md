colab link - (https://colab.research.google.com/drive/13n6tJWSWfUG0W2Go7ZQTjCjA9aLVogIk?usp=sharing)

# 🎮 3D Model Generation ML Tool

Generate 3D game assets from text prompts using OpenAI's Shap-E model. Perfect for game developers, artists, and creators!

![Sample Output](https://gltf-viewer.donmccurdy.com/)  
*Example: "a fantasy sword" generated with this tool*

## 🚀 Features
- Text-to-3D generation (GLB format)
- GPU acceleration support
- Ready-to-use Colab notebook
- FastAPI server deployment option

## ⚙️ Setup

### Option 1: Google Colab (Recommended)
[![Open in Colab](https://colab.research.google.com/drive/13n6tJWSWfUG0W2Go7ZQTjCjA9aLVogIk#scrollTo=7fUxVBOZUdpW)

1. Click the Colab button above
2. Run all cells (Runtime → Run all)
3. Enter your prompt when requested

### Option 2: Local Installation
```bash
# Clone repo
git clone https://github.com/your_username/3d-ml-generator.git
cd 3d-ml-generator

# Install dependencies
pip install -r requirements.txt

# Run generation script
python generate.py --prompt "a magic staff"
