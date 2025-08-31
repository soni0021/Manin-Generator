# 🚀 Quick Start Guide - Manim + Hinglish TTS

Get started with educational animations in **5 minutes**!

## ⚡ Super Quick Setup

```bash
# 1. Install minimal dependencies
pip install manim manim-voiceover gtts pygame

# 2. Run example animation
manim simple_hinglish_manim.py NewtonsLawDemo

# 3. Watch your video!
open media/videos/simple_hinglish_manim/1080p60/NewtonsLawDemo.mp4
```

## 🎬 Try All Examples

```bash
# Physics - Newton's Second Law
manim simple_hinglish_manim.py NewtonsLawDemo

# Chemistry - Water Molecule
manim simple_hinglish_manim.py WaterMoleculeDemo

# Biology - Cell Membrane
manim simple_hinglish_manim.py CellMembraneDemo
```

## 🤖 Create Custom Animation with Gemini

### Step 1: Get the Prompt
```bash
python main.py --gemini-prompt
```

### Step 2: Use with Gemini
1. Copy the prompt that appears
2. Add your physics/chemistry/biology question
3. Paste into Gemini
4. Get your custom animation code!

### Step 3: Render Your Animation
```bash
# Save Gemini's code as my_topic.py, then:
manim my_topic.py ProblemAnimation
```

## 📝 Example Custom Code

```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MyTopicScene(VoiceoverScene):
    def construct(self):
        # Setup Hindi TTS
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Your content
        title = Text("My Topic", font_size=48, color=BLUE)
        
        with self.voiceover(text="Namaskar! Aaj hum sikhenge...") as tracker:
            self.play(Write(title), run_time=tracker.duration)
```

## 🛠 Troubleshooting

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

## 🎯 What's Next?

- Read the full [README.md](README.md) for advanced features
- Explore the comprehensive system in `scenes/` folder
- Join Manim community for support
- Create amazing educational content! 🌟

**That's it! You're ready to create Hinglish educational animations! 🎉**

