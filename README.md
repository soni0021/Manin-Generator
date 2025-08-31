# 🎬 Manim + Hinglish TTS Educational Animation System

A powerful system for creating educational animations with synchronized Hinglish (Hindi-English) voiceovers using Manim Community Edition and AI-powered content generation.

![Manim Animations](https://img.shields.io/badge/Manim-Community%20Edition-blue)
![TTS](https://img.shields.io/badge/TTS-Hinglish%20Voiceover-green)
![AI](https://img.shields.io/badge/AI-Gemini%20Powered-orange)
![Streamlit](https://img.shields.io/badge/Web-Streamlit%20App-purple)

## 🌟 What This Project Does

Create professional educational animations in **Hinglish** (Hindi-English) with:
- **AI-powered content generation** using Google Gemini
- **Automatic voiceover synchronization** with animations
- **Multiple TTS services** including free Google TTS
- **Web interface** for easy content creation
- **Subject-specific animations** for Physics, Chemistry, Biology, and Math

## 🚀 Quick Start (5 minutes!)

### Option 1: Web App (Recommended for Beginners)
```bash
# Launch the web interface
python run_streamlit.py

# Open http://localhost:8501 in your browser
# Just describe your topic and let AI create everything!
```

### Option 2: Command Line
```bash
# Install minimal dependencies
pip install -r requirements-simple.txt

# Run example animation
manim simple_hinglish_manim.py NewtonsLawDemo

# Watch your video!
open media/videos/simple_hinglish_manim/1080p60/NewtonsLawDemo.mp4
```

## 🎯 Key Features

### 🤖 AI-Powered Content Generation
- **Gemini 2.5 Pro integration** for intelligent content creation
- **Automatic learning objectives** and storyboard generation
- **Hinglish narration** that perfectly syncs with animations
- **Subject-specific prompts** for Physics, Chemistry, Biology, Math

### 🎬 Professional Animations
- **Manim Community Edition** for mathematical animations
- **Multiple quality settings** (preview to high-quality)
- **Automatic timing** between audio and visual elements
- **Export options** (MP4, source code)

### 🗣️ Hinglish Voiceover System
- **Free Google TTS** with Hindi language support
- **Voice cloning** capabilities (with XTTS v2)
- **Audio caching** for faster renders
- **Perfect synchronization** with animations

### 📱 User-Friendly Interface
- **Streamlit web app** - no coding required
- **Real-time preview** of generated content
- **Responsive design** works on all devices
- **Quick examples** for common topics

## 🛠 Installation

### Prerequisites
- Python 3.8+
- FFmpeg (for video processing)
- Git

### Quick Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd "Manin Animations"

# Install minimal dependencies (recommended)
pip install -r requirements-simple.txt

# Or install full system
pip install -r requirements.txt
```

### System-Specific Setup

#### macOS
```bash
# Install FFmpeg
brew install ffmpeg

# Install audio dependencies
brew install portaudio
```

#### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install ffmpeg portaudio19-dev python3-dev

# Install Python packages
pip install -r requirements-simple.txt
```

#### Windows
```bash
# Install FFmpeg from https://ffmpeg.org/download.html
# Add to PATH environment variable

# Install Python packages
pip install -r requirements-simple.txt
```

## 📁 Project Structure

```
Manin Animations/
├── 🚀 run_streamlit.py              # Launch web app
├── 🌟 simple_hinglish_manim.py      # Simplified system (recommended)
├── 📱 streamlit_app.py              # Web interface
├── 🎬 main.py                       # Command line orchestrator
├── 📋 requirements-simple.txt       # Minimal dependencies
├── 📋 requirements.txt              # Full system dependencies
├── 🎭 scenes/                       # Pre-built animations
│   ├── physics_scenes.py            # Physics animations
│   ├── chemistry_scenes.py          # Chemistry animations
│   └── biology_scenes.py            # Biology animations
├── ⚙️ config/                       # Configuration files
│   ├── tts_config.py                # TTS service settings
│   └── voice_profiles.py            # Voice configurations
├── 🛠️ utils/                        # Utility functions
│   ├── hinglish_processor.py        # Text processing
│   └── voice_manager.py             # TTS management
└── 📁 media/                        # Generated content
    ├── videos/                      # Animation videos
    ├── voiceovers/                  # Audio files
    └── texts/                       # Generated text content
```

## 🎬 Usage Examples

### 1. Web Interface (Easiest)
```bash
python run_streamlit.py
```
Then:
1. Enter your topic (e.g., "Explain Newton's second law")
2. Select subject area
3. Click "Generate Content"
4. Review and render your animation
5. Download video and source code

### 2. Command Line Examples
```bash
# Physics - Newton's Second Law
manim simple_hinglish_manim.py NewtonsLawDemo

# Chemistry - Water Molecule Structure
manim simple_hinglish_manim.py WaterMoleculeDemo

# Biology - Cell Membrane Transport
manim simple_hinglish_manim.py CellMembraneDemo

# Custom animation with Gemini
python main.py --gemini-prompt
```

### 3. Custom Animation Code
```python
from simple_hinglish_manim import HinglishEducationScene

class MyTopicScene(HinglishEducationScene):
    def construct(self):
        title = Text("My Topic", font_size=48, color=BLUE)
        
        with self.voiceover(text="Namaskar! Aaj hum sikhenge...") as tracker:
            self.play(Write(title), run_time=tracker.duration)
```

## 🎯 Available Scenes

### Physics
- **Newton's Second Law** - Force, mass, acceleration
- **Electromagnetic Fields** - Field lines and interactions
- **Wave Propagation** - Sound and light waves
- **Thermodynamics** - Heat transfer and cycles

### Chemistry
- **Water Molecule** - Structure and bonding
- **Periodic Table** - Element properties and trends
- **Chemical Reactions** - Balancing equations
- **Molecular Orbitals** - Bonding and anti-bonding

### Biology
- **Cell Membrane** - Transport mechanisms
- **DNA Replication** - Genetic processes
- **Photosynthesis** - Plant energy conversion
- **Cell Division** - Mitosis and meiosis

### Mathematics
- **Calculus** - Derivatives and integrals
- **Geometry** - Shapes and transformations
- **Probability** - Statistics and distributions
- **Algebra** - Equations and functions

## 🔧 Configuration

### TTS Services
The system supports multiple TTS services with automatic fallback:

1. **Google TTS (Free)** - Default, reliable Hindi support
2. **XTTS v2** - Voice cloning capabilities
3. **ElevenLabs** - High-quality voice synthesis

### Voice Profiles
Subject-specific voice configurations in `config/voice_profiles.py`:
- Physics: Clear, authoritative voice
- Chemistry: Precise, technical voice
- Biology: Warm, engaging voice
- Mathematics: Logical, structured voice

## 🚀 Advanced Features

### Custom Voice Cloning
```python
from utils.voice_manager import tts_manager

# Clone a voice from reference audio
tts_manager.clone_voice(
    reference_audio="path/to/audio.wav",
    voice_name="my_voice"
)
```

### Audio Caching
- Automatic caching of generated audio
- Faster subsequent renders
- Configurable cache management

### Quality Settings
- **Preview**: Fast rendering for testing
- **Standard**: Balanced quality and speed
- **High**: Production quality output

## 🐛 Troubleshooting

### Common Issues

**Audio not working?**
```bash
# macOS
brew install portaudio

# Linux
sudo apt-get install portaudio19-dev

# Then
pip install pyaudio
```

**Import errors?**
```bash
pip install --upgrade manim manim-voiceover gtts
```

**Video rendering issues?**
```bash
# Check FFmpeg installation
ffmpeg -version

# Reinstall FFmpeg if needed
```

**Gemini API errors?**
- Check your API key in the configuration
- Ensure you have sufficient API quota
- Verify internet connectivity

### Performance Tips
- Use preview quality for testing
- Enable audio caching for faster renders
- Close other applications during rendering
- Use SSD storage for better I/O performance

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Check code quality
flake8 .
black .
```

## 📚 Resources

### Documentation
- [Manim Community Documentation](https://docs.manim.community/)
- [Manim Voiceover](https://manim-voiceover.readthedocs.io/)
- [Google TTS](https://gtts.readthedocs.io/)

### Community
- [Manim Discord](https://discord.gg/mMRrZQW)
- [Manim GitHub](https://github.com/ManimCommunity/manim)
- [Streamlit Community](https://discuss.streamlit.io/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Manim Community** for the amazing animation engine
- **Google Gemini** for AI-powered content generation
- **Google TTS** for reliable voice synthesis
- **Streamlit** for the web interface framework

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/discussions)
- **Email**: [your-email@example.com]

---

**Ready to create amazing Hinglish educational animations? Start with `python run_streamlit.py` and let AI do the heavy lifting! 🚀**

Made with ❤️ for educational content creators worldwide.

# Manin-Generator
