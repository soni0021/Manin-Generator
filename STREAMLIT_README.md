# 🎬 Streamlit Web App - Hinglish Educational Animations

A user-friendly web interface for creating educational animations with synchronized Hinglish voiceovers using AI.

## 🚀 Quick Start

### Option 1: Automatic Setup (Recommended)
```bash
python run_streamlit.py
```
This script will:
- Check dependencies
- Install missing packages
- Setup environment
- Launch the web app

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements-streamlit.txt

# Launch app
streamlit run streamlit_app.py
```

## 🌟 Features

### 🤖 AI-Powered Generation
- **Gemini AI Integration**: Automatically generates animation code from your problem statement
- **Intelligent Content Planning**: Creates learning objectives, storyboard, and narration
- **Subject-Aware**: Optimized for Physics, Chemistry, Biology, and Mathematics

### 🗣️ Free Hinglish TTS
- **Google Text-to-Speech**: Free, reliable voice synthesis
- **Hinglish Support**: Natural mixing of Hindi and English
- **Automatic Synchronization**: Perfect timing between audio and visuals

### 🎬 Professional Animations
- **Manim Community Edition**: High-quality mathematical animations
- **Web-Optimized Rendering**: Fast preview with low-quality renders
- **Download Options**: Get both video and source code

### 📱 User-Friendly Interface
- **No Coding Required**: Just describe your topic
- **Real-time Preview**: See objectives, storyboard, and narration
- **Example Topics**: Pre-built examples to get started
- **Responsive Design**: Works on desktop and mobile

## 🎯 How to Use

### 1. Launch the App
```bash
python run_streamlit.py
# Open browser to http://localhost:8501
```

### 2. Enter Your Topic
- Describe the concept you want to explain
- Example: "Explain Newton's second law with visual examples"
- Be specific about what you want to show

### 3. Generate Animation
- Click "Generate Animation" 
- AI creates learning objectives, storyboard, and code
- Review the generated content

### 4. Render Video
- Click "Render Video" to create your animation
- Download the MP4 file and Python code
- Share your educational content!

## 📋 Example Topics

### Physics
- "Explain Newton's second law F=ma with force and acceleration examples"
- "Show electromagnetic field lines around charges and magnets" 
- "Demonstrate wave properties like frequency and amplitude"
- "Visualize kinetic and potential energy in a pendulum"

### Chemistry
- "Show water molecule H2O structure with bond angles and polarity"
- "Explain covalent vs ionic bonding with electron sharing"
- "Demonstrate periodic table trends like atomic size"
- "Show chemical reaction mechanisms step by step"

### Biology
- "Explain cell membrane structure and transport mechanisms"
- "Show DNA replication process with base pairing"
- "Demonstrate photosynthesis light and dark reactions"
- "Explain mitosis cell division stages"

### Mathematics
- "Visualize calculus derivatives as slopes of tangent lines"
- "Show geometric proof of Pythagorean theorem"
- "Explain probability with dice and coin examples"
- "Demonstrate matrix multiplication step by step"

## ⚙️ App Interface

### Left Panel: Input
- **Topic Input**: Describe your educational concept
- **Subject Selection**: Physics, Chemistry, Biology, etc.
- **Quality Settings**: Fast preview or high-quality render
- **Content Options**: Include equations, diagrams, animations

### Right Panel: Output
- **Generated Content**: Objectives, storyboard, narration
- **Code Preview**: See the generated Python code
- **Video Player**: Watch your rendered animation
- **Download Buttons**: Get video and code files

### Sidebar: Tools
- **System Status**: Check if dependencies are installed
- **Quick Examples**: Pre-made topics to try
- **Settings**: Customize rendering options

## 🛠 Technical Details

### Architecture
- **Frontend**: Streamlit web framework
- **AI**: Google Gemini Pro for content generation
- **Animation**: Manim Community Edition
- **TTS**: Google Text-to-Speech (gTTS)
- **Audio**: pygame for playback

### API Usage
- Uses provided Google API key: `AIzaSyBKuiVHuhgiVpKHfnGr83rdh9BoHL6Hz5I`
- Free tier limits: ~60 requests per minute
- Automatic retry on rate limits

### File Structure
```
streamlit_app.py              # Main web app
run_streamlit.py             # Launcher script
demo_scenes_streamlit.py     # Quick demo animations
requirements-streamlit.txt   # Dependencies
temp_animations/            # Generated code files
media/videos/               # Rendered videos
```

## 🔧 Customization

### Adding New Examples
Edit the `example_topics` dictionary in `streamlit_app.py`:

```python
example_topics = {
    "Your Topic": "Detailed description of what to explain and show..."
}
```

### Modifying AI Prompts
Update the `get_gemini_prompt()` method in the `AnimationGenerator` class:

```python
def get_gemini_prompt(self) -> str:
    return """
    Your custom prompt here...
    {problem_statement}
    """
```

### Changing Render Settings
Modify the Manim command in `run_animation()`:

```python
cmd = [
    "manim", 
    str(temp_file), 
    scene_name,
    "-qh",  # High quality instead of -ql
    "--disable_caching"
]
```

## 🐛 Troubleshooting

### Common Issues

**App won't start:**
```bash
# Check Python version (3.8+ required)
python --version

# Reinstall dependencies
pip install -r requirements-streamlit.txt

# Try manual launch
streamlit run streamlit_app.py
```

**No video generated:**
- Check if Manim is properly installed
- Verify audio dependencies (pygame, portaudio)
- Try simpler topic descriptions
- Check browser console for errors

**AI generation fails:**
- Verify internet connection
- Check API key is valid
- Try shorter, simpler problem statements
- Wait a moment and retry (rate limits)

**Audio issues:**
```bash
# macOS
brew install portaudio
pip install pyaudio

# Linux  
sudo apt-get install portaudio19-dev
pip install pyaudio

# Windows
pip install pyaudio
```

### Getting Help

1. **Check System Status**: Use the sidebar dependency checker
2. **Try Examples**: Start with pre-made topics
3. **Simplify Input**: Use shorter, clearer descriptions
4. **Check Logs**: Look at terminal output for errors

## 🎉 Success Tips

### Writing Good Problem Statements
- ✅ "Show how Newton's F=ma works with different masses"
- ✅ "Explain water molecule polarity and hydrogen bonding" 
- ✅ "Demonstrate cell membrane transport mechanisms"
- ❌ "Teach me physics" (too broad)
- ❌ "Make a video about science" (not specific)

### Getting Best Results
1. **Be Specific**: Mention exact concepts to cover
2. **Include Visuals**: Ask for diagrams, equations, animations
3. **Set Context**: Specify audience level (high school, college, etc.)
4. **Use Examples**: Request specific examples or scenarios
5. **Keep Focused**: One main concept per animation

## 📈 Performance

### Rendering Times
- **Low Quality (-ql)**: 30-60 seconds
- **Medium Quality (-qm)**: 1-3 minutes  
- **High Quality (-qh)**: 3-10 minutes

### Optimization Tips
- Use low quality for previews
- Keep animations under 90 seconds
- Avoid complex 3D scenes for faster rendering
- Cache is automatically managed

## 🤝 Contributing

Want to improve the app? Here are some ideas:

1. **Add More Examples**: Create topic templates
2. **Improve UI**: Better styling and layout
3. **Add Features**: Video editing, custom voices
4. **Optimize Performance**: Faster rendering, better caching
5. **Fix Bugs**: Handle edge cases, improve error messages

## 📄 License

This Streamlit app is part of the Hinglish Educational Animation System and follows the same open-source license for educational use.

---

**Happy Teaching! 🎓✨**

Create amazing educational content with AI-powered animations and Hinglish narration!
