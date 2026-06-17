# 🎬 AI Video Explainer

An AI-powered animated video generator that converts text prompts into cartoon explainer videos for students and educators.

## ✨ Features
- Prompt → Script → Narration → Animated Video pipeline
- Multiple video providers (AI/ML API, stub for testing)
- Text-to-speech narration via Piper
- Sound design layer for background music & effects
- Modular architecture — swap providers easily

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/kunalroy23042009/ai-video-explainer.git
cd ai-video-explainer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup Piper TTS
bash setup_piper.sh

# 4. Configure environment
cp .env.example .env
# Fill in your API keys in .env

# 5. Run
python main.py --prompt "Explain how photosynthesis works"
```

## 🗂️ Project Structure

```
ai-video-explainer/
├── core/
│   ├── script_writer.py      # LLM-based script generation
│   ├── narrator.py           # TTS narration via Piper
│   ├── composer.py           # Assembles video + audio
│   ├── sound_design.py       # Background music & SFX
│   ├── models.py             # Data models (Pydantic)
│   └── video_providers/      # Pluggable video backends
│       ├── base.py
│       ├── aimlapi_provider.py
│       └── stub_provider.py
├── pipeline.py               # Orchestrates the full pipeline
├── main.py                   # CLI entry point
├── config.py                 # Config & env loading
└── requirements.txt
```

## 🔑 Environment Variables

See `.env.example` for all required keys.

## 📚 Use Cases
- Science concept explainers
- Math tutorial animations
- History story narrations
- Language learning clips
