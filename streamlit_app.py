"""
Streamlit Web App for Manim + Hinglish TTS Educational Animation System
Provides a user-friendly interface for creating educational animations with Gemini AI integration
"""

import streamlit as st
import os
import subprocess
import tempfile
import json
import time
from pathlib import Path
import google.generativeai as genai
from typing import Dict, List, Optional

# Configure page
st.set_page_config(
    page_title="Hinglish Educational Animations",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure Google AI
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "")
if not GOOGLE_API_KEY:
    st.error("⚠️ Google API Key not found. Please set GOOGLE_API_KEY in your Streamlit secrets.")
    st.stop()
genai.configure(api_key=GOOGLE_API_KEY)

class AnimationGenerator:
    """Handles animation generation using Gemini AI"""
    
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.project_root = Path(__file__).parent
    
    def get_gemini_prompt(self) -> str:
        """Get the comprehensive, structured Gemini prompt for high-quality animation generation"""
        return """
You are a senior Python educator and Manim animation expert specializing in educational content.
Create a professional, visually appealing Manim animation with synchronized Hinglish voiceover.

🎯 CORE MISSION: Transform the user's concept into a clear, engaging educational animation with perfect audio-visual synchronization.

📋 MANDATORY OUTPUT STRUCTURE:
=== LEARNING OBJECTIVES ===
• [Clear, specific learning goals - 2-4 bullet points]

=== VISUAL DESIGN PLAN ===
• Color scheme: [Primary, secondary, accent colors with hex codes]
• Layout strategy: [How elements are positioned to avoid collisions]
• Animation flow: [Logical progression of visual elements]

=== DETAILED STORYBOARD ===
Beat 1 (0-8s): [Scene description]
- Visual elements: [Specific objects and their positions]
- Animation: [What moves, transforms, or appears]
- Narration: [Exact Hinglish text]

Beat 2 (8-16s): [Scene description]
- Visual elements: [Specific objects and their positions]
- Animation: [What moves, transforms, or appears]  
- Narration: [Exact Hinglish text]

[Continue for all beats...]

=== HINGLISH NARRATION SCRIPT ===
1. [First narration line]
2. [Second narration line]
[Continue numbered...]

=== PRODUCTION-READY CODE ===
```python
[Complete, runnable code]
```

🎨 VISUAL DESIGN REQUIREMENTS:
1. COLOR PALETTE - Use professional, educational colors:
   - Primary: BLUE (#3498db) for main elements
   - Secondary: GREEN (#2ecc71) for positive/growth concepts
   - Accent: ORANGE (#f39c12) for highlights/emphasis
   - Background: DARK_GRAY (#2c3e50) or BLACK
   - Text: WHITE or LIGHT_GRAY for readability
   - Warning/Important: RED (#e74c3c) sparingly

2. SPATIAL ORGANIZATION:
   - Use a 16:9 grid system for positioning
   - Keep 10% margin from edges
   - Center important elements
   - Use LEFT/RIGHT/UP/DOWN positioning with proper spacing
   - No overlapping elements unless intentional

3. TYPOGRAPHY:
   - Title: font_size=48-60, bold, center-aligned
   - Subtitles: font_size=36-42
   - Body text: font_size=24-30
   - Labels: font_size=18-24
   - Use consistent font sizing throughout

🎬 ANIMATION QUALITY STANDARDS:
1. SMOOTH TRANSITIONS:
   - Use appropriate run_time (0.5-2 seconds per animation)
   - Synchronize perfectly with voiceover duration
   - Use easing functions for natural movement

2. ELEMENT POSITIONING:
   - Calculate exact positions to prevent collisions
   - Use .shift(), .to_edge(), .next_to() properly
   - Maintain visual hierarchy

3. TIMING PERFECTION:
   - Each voiceover block must match animation duration exactly
   - Use: with self.voiceover(text="...") as tracker: self.play(animation, run_time=tracker.duration)
   - Add strategic self.wait() for pacing

📝 CODE STRUCTURE REQUIREMENTS:
1. CLEAN ORGANIZATION (MANDATORY TEMPLATE):
```python
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = BLUE
        SECONDARY_COLOR = GREEN  
        ACCENT_COLOR = ORANGE
        TEXT_COLOR = WHITE
        
        # CRITICAL: You MUST define ALL these colors before using them!
        
        # Scene progression
        self.intro_scene()
        self.main_content() 
        self.conclusion()
    
    def intro_scene(self):
        # Introduction with title
        title = Text("Topic Title", font_size=48, color=PRIMARY_COLOR)
        # Use voiceover blocks with perfect sync
        with self.voiceover(text="English narration here") as tracker:
            self.play(Write(title), run_time=tracker.duration)
    
    def main_content(self):
        # Main educational content
        pass
        
    def conclusion(self):
        # Summary and wrap-up
        pass
```

CRITICAL: Use exactly "class GeneratedAnimation" - no other class name!

2. POSITIONING SYSTEM:
   - Use consistent positioning: LEFT*2, RIGHT*2, UP*1.5, DOWN*1.5
   - Group related elements: VGroup(element1, element2)
   - Calculate positions to avoid overlap
   - Screen dimensions: Use LEFT*7, RIGHT*7, UP*4, DOWN*4 for full screen
   - Example: Rectangle(width=14, height=2) for full width, Rectangle(width=3, height=1) for objects

3. NO LATEX/MATHTEX:
   - Use Text() for all equations: Text("F = ma", font_size=36)
   - Use Text() for mathematical symbols: Text("∑", font_size=48)
   - Create visual representations instead of complex formulas

4. MANIM CONSTANTS (USE THESE EXACT NAMES):
   - Screen dimensions: LEFT*7, RIGHT*7, UP*4, DOWN*4
   - NO FRAME_WIDTH, FRAME_HEIGHT, or other undefined constants
   - Use specific values: LEFT*6, RIGHT*6, UP*3, DOWN*3

🗣️ ENGLISH NARRATION GUIDELINES:
1. NATURAL FLOW:
   - Use clear, educational English
   - Start with greeting: "Hello" or "Today we will learn"
   - Use questioning: "Notice what happens when..."
   - End with summary: "So this was the concept of..."

2. EDUCATIONAL TONE:
   - Be engaging and informative
   - Use simple, clear explanations
   - Include key concepts and definitions

3. PRONUNCIATION-FRIENDLY:
   - Use standard English words
   - Avoid complex technical jargon
   - Keep sentences concise and clear

🚫 STRICT PROHIBITIONS:
- NO MathTex, NO LaTeX, NO Tex() objects
- NO overlapping elements without proper layering
- NO animations without corresponding voiceover
- NO hardcoded positions without margin calculations
- NO complex 3D unless specifically requested
- NO more than 5 colors in the palette

✅ QUALITY CHECKLIST:
Before generating code, ensure:
□ Color scheme is professional and consistent
□ All elements have calculated positions
□ Every animation has matching voiceover duration
□ Text is readable with proper contrast
□ No element collisions or overlaps
□ Smooth transitions between scenes
□ Clear visual hierarchy
□ Educational content is accurate

🚨 CRITICAL CODE VALIDATION:
□ Code must compile without syntax errors
□ All imports are correct and available
□ Class name is exactly "GeneratedAnimation"
□ All methods are properly indented
□ Every self.play() is inside voiceover block
□ No undefined variables or functions
□ All Manim objects exist in Community Edition
□ TTS setup is correct for English

USER PROBLEM STATEMENT:
{problem_statement}

Generate a complete, production-ready animation that meets all these standards.
"""
    
    def generate_animation_code(self, problem_statement: str) -> Dict[str, str]:
        """Generate animation code using Gemini AI"""
        try:
            prompt = self.get_gemini_prompt().format(problem_statement=problem_statement)
            
            with st.spinner("🤖 Generating animation with Gemini AI..."):
                response = self.model.generate_content(prompt)
                content = response.text
            
            # Parse the response
            sections = self._parse_gemini_response(content)
            return sections
            
        except Exception as e:
            st.error(f"Error generating animation: {str(e)}")
            return {}
    
    def _parse_gemini_response(self, content: str) -> Dict[str, str]:
        """Parse Gemini response into sections"""
        sections = {
            'objectives': '',
            'design_plan': '',
            'storyboard': '',
            'narration': '',
            'code': ''
        }
        
        # Split content by section headers
        current_section = None
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            
            if '=== LEARNING OBJECTIVES ===' in line:
                current_section = 'objectives'
                continue
            elif '=== VISUAL DESIGN PLAN ===' in line:
                current_section = 'design_plan'
                continue
            elif '=== DETAILED STORYBOARD ===' in line:
                current_section = 'storyboard'
                continue
            elif '=== HINGLISH NARRATION SCRIPT ===' in line:
                current_section = 'narration'
                continue
            elif '=== PRODUCTION-READY CODE ===' in line:
                current_section = 'code'
                continue
            
            if current_section and line:
                sections[current_section] += line + '\n'
        
        # Clean up code section
        if sections['code']:
            # Remove markdown code blocks
            code = sections['code']
            if '```python' in code:
                code = code.split('```python')[1].split('```')[0]
            elif '```' in code:
                code = code.split('```')[1].split('```')[0]
            
            # Fix indentation issues and undefined constants
            import textwrap
            
            # First, fix undefined constants
            code = code.replace('FRAME_WIDTH', '14')  # LEFT*7 to RIGHT*7 = 14 units
            code = code.replace('FRAME_HEIGHT', '8')   # UP*4 to DOWN*4 = 8 units
            code = code.replace('FRAME_RATE', '30')
            code = code.replace('PIXEL_HEIGHT', '720')
            code = code.replace('PIXEL_WIDTH', '1280')
            
            # Fix missing color definitions
            if 'PRIMARY_COLOR' not in code:
                code = code.replace('# Setup TTS (REQUIRED)', '# Setup TTS (REQUIRED)\n        \n        # Define color scheme (REQUIRED)\n        PRIMARY_COLOR = BLUE\n        SECONDARY_COLOR = GREEN\n        ACCENT_COLOR = ORANGE\n        TEXT_COLOR = WHITE')
            elif 'TEXT_COLOR' not in code:
                # Find where colors are defined and add TEXT_COLOR
                if 'PRIMARY_COLOR =' in code:
                    # Find the line with PRIMARY_COLOR and add TEXT_COLOR after it
                    lines = code.split('\n')
                    for i, line in enumerate(lines):
                        if 'PRIMARY_COLOR =' in line:
                            lines.insert(i + 1, '        TEXT_COLOR = WHITE')
                            break
                    code = '\n'.join(lines)
                else:
                    # Add all colors if none exist
                    code = code.replace('# Setup TTS (REQUIRED)', '# Setup TTS (REQUIRED)\n        \n        # Define color scheme (REQUIRED)\n        PRIMARY_COLOR = BLUE\n        SECONDARY_COLOR = GREEN\n        ACCENT_COLOR = ORANGE\n        TEXT_COLOR = WHITE')
            
            # Then, try to fix basic indentation
            try:
                # Remove any leading/trailing whitespace
                code = code.strip()
                
                # Split into lines
                lines = code.split('\n')
                fixed_lines = []
                in_class = False
                in_method = False
                in_voiceover = False
                
                for line in lines:
                    stripped = line.strip()
                    
                    # Skip empty lines
                    if not stripped:
                        fixed_lines.append('')
                        continue
                    
                    # Handle imports
                    if stripped.startswith(('from ', 'import ')):
                        fixed_lines.append(stripped)
                        continue
                    
                    # Handle class definition
                    if stripped.startswith('class '):
                        fixed_lines.append(stripped)
                        in_class = True
                        in_method = False
                        in_voiceover = False
                        continue
                    
                    # Handle method definitions
                    if stripped.startswith('def ') and in_class:
                        fixed_lines.append('    ' + stripped)
                        in_method = True
                        in_voiceover = False
                        continue
                    
                    # Handle voiceover blocks
                    if stripped.startswith('with self.voiceover'):
                        fixed_lines.append('        ' + stripped)
                        in_voiceover = True
                        continue
                    
                    # Handle method content
                    if in_method:
                        if in_voiceover:
                            # Inside voiceover block - 8 spaces
                            if stripped.startswith('self.play') or stripped.startswith('self.wait'):
                                fixed_lines.append('            ' + stripped)
                            elif stripped.startswith('#'):
                                fixed_lines.append('            ' + stripped)
                            else:
                                fixed_lines.append('            ' + stripped)
                        else:
                            # Regular method content - 4 spaces
                            if any(stripped.startswith(pattern) for pattern in [
                                'self.', 'title =', 'equation =', 'circle =', 'square =', 
                                'arrow =', 'line =', 'PRIMARY_COLOR', 'SECONDARY_COLOR'
                            ]):
                                fixed_lines.append('        ' + stripped)
                            elif stripped.startswith('#'):
                                fixed_lines.append('        ' + stripped)
                            else:
                                # Keep existing indentation if reasonable
                                if line.startswith('        ') or line.startswith('    '):
                                    fixed_lines.append(line)
                                else:
                                    fixed_lines.append('        ' + stripped)
                    else:
                        # Not in method, probably class-level
                        fixed_lines.append('    ' + stripped)
                
                sections['code'] = '\n'.join(fixed_lines)
                
            except Exception as e:
                st.warning(f"Code formatting warning: {e}")
                # Fallback: use original code
                sections['code'] = code.strip()
        
        return sections

class ManimeAnimationRunner:
    """Handles running Manim animations"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.temp_dir = self.project_root / "temp_animations"
        self.temp_dir.mkdir(exist_ok=True)
    
    def run_animation(self, code: str, scene_name: str = "GeneratedAnimation") -> Optional[str]:
        """Run the generated animation code and return video path"""
        try:
            # Create temporary Python file
            temp_file = self.temp_dir / f"temp_animation_{int(time.time())}.py"
            
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(code)
            
            st.info(f"📝 Created animation file: {temp_file.name}")
            
            # Validate the Python code syntax
            try:
                compile(code, temp_file, 'exec')
                st.success("✅ Code syntax is valid")
                
                # Additional validation checks
                if 'class GeneratedAnimation' not in code:
                    st.error("❌ Missing required class name 'GeneratedAnimation'")
                    return None
                
                if 'self.set_speech_service' not in code:
                    st.error("❌ Missing TTS setup")
                    return None
                
                if 'self.voiceover(' not in code:
                    st.error("❌ Missing voiceover blocks")
                    return None
                
                # Check for undefined constants
                undefined_constants = ['FRAME_WIDTH', 'FRAME_HEIGHT', 'FRAME_RATE', 'PIXEL_HEIGHT', 'PIXEL_WIDTH']
                found_undefined = [const for const in undefined_constants if const in code]
                
                if found_undefined:
                    st.error(f"❌ Found undefined constants: {', '.join(found_undefined)}")
                    st.error("These constants don't exist in Manim Community Edition")
                    st.error("Use: LEFT*7, RIGHT*7, UP*4, DOWN*4 instead")
                    return None
                
                # Check for undefined color variables
                required_colors = ['PRIMARY_COLOR', 'SECONDARY_COLOR', 'ACCENT_COLOR', 'TEXT_COLOR']
                missing_colors = [color for color in required_colors if color not in code]
                
                if missing_colors:
                    st.error(f"❌ Missing required color definitions: {', '.join(missing_colors)}")
                    st.error("All animations must define these color variables")
                    return None
                
                st.success("✅ All validation checks passed")
                
            except SyntaxError as e:
                st.error(f"❌ Syntax Error in generated code: {e}")
                st.error(f"Line {e.lineno}: {e.text}")
                return None
            except Exception as e:
                st.error(f"❌ Code validation error: {e}")
                return None
            
            # Run Manim with ultra-fast settings for faster processing
            cmd = [
                "manim", 
                str(temp_file), 
                scene_name,
                "-ql",  # Low quality for speed
                "--disable_caching",
                "--fps", "15",
                "--resolution", "480,360"
            ]
            
            st.info(f"🔧 Running command: {' '.join(cmd)}")
            st.info("⚡ Using ultra-fast settings: 480p15 resolution, 15 FPS, no caching")
            
            with st.spinner("🎬 Rendering animation with ultra-fast settings... This should take 30 seconds to 2 minutes"):
                result = subprocess.run(
                    cmd, 
                    capture_output=True, 
                    text=True,
                    cwd=str(self.project_root),
                    timeout=300  # 5 minute timeout
                )
            
            st.info(f"📊 Manim exit code: {result.returncode}")
            
            # Show output for debugging
            if result.stdout:
                with st.expander("📤 Manim Output", expanded=False):
                    st.text(result.stdout[-2000:])  # Last 2000 chars
            
            if result.stderr:
                with st.expander("📥 Manim Errors", expanded=result.returncode != 0):
                    st.text(result.stderr[-2000:])  # Last 2000 chars
            
            if result.returncode == 0:
                # Find the generated video file - prioritize 480p15 for fast rendering
                possible_paths = [
                    self.project_root / "media" / "videos" / temp_file.stem / "480p15",  # Primary output
                    self.project_root / "media" / "videos" / temp_file.stem / "360p15",  # Fallback
                    self.project_root / "media" / "videos" / temp_file.stem / "720p30",  # Higher quality fallback
                    self.project_root / "media" / "videos" / temp_file.stem / "1080p60", # Highest quality fallback
                ]
                
                video_found = False
                
                for media_dir in possible_paths:
                    st.info(f"🔍 Checking: {media_dir}")
                    
                    if media_dir.exists():
                        video_files = list(media_dir.glob(f"{scene_name}.mp4"))
                        all_files = list(media_dir.glob("*"))
                        
                        st.info(f"📁 Found files: {[f.name for f in all_files]}")
                        
                        if video_files:
                            video_path = str(video_files[0])
                            video_size = video_files[0].stat().st_size
                            
                            if video_size > 1000:  # Ensure it's a real video file
                                st.success(f"✅ Video found: {video_path} ({video_size:,} bytes)")
                                return video_path
                            else:
                                st.warning(f"⚠️ Video file too small: {video_size} bytes")
                        else:
                            # Try alternative file patterns
                            alt_files = list(media_dir.glob("*.mp4"))
                            if alt_files:
                                video_path = str(alt_files[0])
                                video_size = alt_files[0].stat().st_size
                                st.info(f"📹 Found alternative video: {video_path} ({video_size:,} bytes)")
                                return video_path
                
                # If no video found, show detailed error
                st.error("❌ Video file not found in any quality directory")
                
                # Show what directories exist
                base_media_dir = self.project_root / "media" / "videos" / temp_file.stem
                if base_media_dir.exists():
                    subdirs = [d for d in base_media_dir.iterdir() if d.is_dir()]
                    st.error(f"Available quality directories: {[d.name for d in subdirs]}")
                    
                    for subdir in subdirs:
                        files = list(subdir.glob("*"))
                        st.error(f"Files in {subdir.name}: {[f.name for f in files]}")
                else:
                    st.error(f"Media directory doesn't exist: {base_media_dir}")
                
                return None
            else:
                st.error(f"❌ Manim rendering failed with exit code {result.returncode}")
                return None
                
        except subprocess.TimeoutExpired:
            st.error("⏰ Animation rendering timed out (5 minutes). Try a simpler animation.")
            return None
        except Exception as e:
            st.error(f"❌ Error running animation: {str(e)}")
            import traceback
            st.error(f"Full error: {traceback.format_exc()}")
            return None
        finally:
            # Keep temporary file for debugging - don't delete immediately
            pass

def check_dependencies() -> Dict[str, bool]:
    """Check if required dependencies are installed"""
    dependencies = {
        'manim': False,
        'manim_voiceover': False,
        'gtts': False,
        'pygame': False,
        'google-generativeai': False
    }
    
    for package in dependencies.keys():
        try:
            if package == 'manim_voiceover':
                __import__('manim_voiceover')
            elif package == 'google-generativeai':
                __import__('google.generativeai')
            else:
                __import__(package)
            dependencies[package] = True
        except ImportError:
            dependencies[package] = False
    
    return dependencies

def main():
    """Main Streamlit app"""
    
    # Header
    st.title("🎬 Hinglish Educational Animations")
    st.markdown("Create educational animations with synchronized Hinglish voiceover using AI")
    
    # Sidebar
    with st.sidebar:
        st.header("🛠️ System Status")
        
        # Check dependencies
        deps = check_dependencies()
        all_deps_ok = all(deps.values())
        
        if all_deps_ok:
            st.success("✅ All dependencies installed")
        else:
            st.warning("⚠️ Missing dependencies")
            for dep, status in deps.items():
                icon = "✅" if status else "❌"
                st.write(f"{icon} {dep}")
            
            if not all_deps_ok:
                st.code("pip install manim manim-voiceover gtts pygame google-generativeai")
        
        st.markdown("---")
        
        # Quick examples
        st.header("🚀 Quick Examples")
        
        example_topics = {
            "Newton's Second Law": "Explain Newton's second law F=ma with a visual demonstration showing how force, mass, and acceleration are related.",
            "Water Molecule Structure": "Show the structure of a water molecule H2O, including bond angles, polarity, and hydrogen bonding.",
            "Cell Membrane Transport": "Demonstrate how substances cross the cell membrane through passive and active transport.",
            "Photosynthesis Process": "Explain the process of photosynthesis with the chemical equation and light/dark reactions.",
            "Atomic Structure": "Show the structure of an atom with electrons, protons, and neutrons, and explain electron shells."
        }
        
        selected_example = st.selectbox("Choose an example:", list(example_topics.keys()))
        
        if st.button("Use This Example"):
            st.session_state.problem_statement = example_topics[selected_example]
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Input")
        
        # Problem statement input
        problem_statement = st.text_area(
            "Enter your physics/chemistry/biology question or topic:",
            value=st.session_state.get('problem_statement', ''),
            height=150,
            placeholder="Example: Explain Newton's second law with a visual demonstration..."
        )
        
        # Subject selection
        subject = st.selectbox(
            "Subject Area:",
            ["Physics", "Chemistry", "Biology", "Mathematics", "General Science"]
        )
        
        # Animation settings
        st.subheader("⚙️ Settings")
        
        quality = st.select_slider(
            "Render Quality:",
            options=["Low (Fast)", "Medium", "High (Slow)"],
            value="Low (Fast)"
        )
        
        include_equations = st.checkbox("Include mathematical equations", value=True)
        include_diagrams = st.checkbox("Include diagrams/visuals", value=True)
        
        # Generate button
        generate_button = st.button("🎬 Generate Animation", type="primary", disabled=not all_deps_ok)
    
    with col2:
        st.header("🎥 Output")
        
        if generate_button and problem_statement:
            # Store the problem statement in session state
            st.session_state.current_problem = problem_statement
            
            # Initialize generators
            generator = AnimationGenerator()
            
            # Generate animation code
            sections = generator.generate_animation_code(problem_statement)
            
            # Store generated content in session state
            st.session_state.generated_sections = sections
            
        # Display generated content if it exists in session state
        if hasattr(st.session_state, 'generated_sections') and st.session_state.generated_sections.get('code'):
            sections = st.session_state.generated_sections
            
            # Show current problem and option to generate new
            col_info, col_new = st.columns([3, 1])
            with col_info:
                st.info(f"📝 Current Topic: {st.session_state.get('current_problem', 'Unknown')}")
            with col_new:
                if st.button("🆕 New Animation", help="Generate a new animation"):
                    # Clear all session state
                    for key in ['generated_sections', 'current_problem', 'video_path', 'video_bytes', 'video_code', 'render_requested']:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
            
            # Show generated content
            with st.expander("📋 Learning Objectives", expanded=True):
                st.markdown(sections.get('objectives', 'Not generated'))
            
            with st.expander("🎨 Visual Design Plan", expanded=True):
                st.markdown(sections.get('design_plan', 'Not generated'))
            
            with st.expander("🎬 Detailed Storyboard", expanded=False):
                st.markdown(sections.get('storyboard', 'Not generated'))
            
            with st.expander("🗣️ Hinglish Narration", expanded=False):
                st.markdown(sections.get('narration', 'Not generated'))
            
            with st.expander("💻 Production-Ready Code", expanded=False):
                st.code(sections.get('code', ''), language='python')
                
            # Run animation button
            render_button = st.button("▶️ Render Video", type="primary", key="render_video_btn")
            
            if render_button:
                # Store rendering request in session state
                st.session_state.render_requested = True
                st.rerun()
            
            # Handle video rendering if requested
            if hasattr(st.session_state, 'render_requested') and st.session_state.render_requested:
                st.markdown("---")
                st.subheader("🎬 Video Rendering Process")
                
                # Show the code that will be executed
                with st.expander("🔍 Code to be executed", expanded=False):
                    st.code(sections['code'], language='python')
                
                # Initialize runner
                runner = ManimeAnimationRunner()
                
                # Run the animation
                video_path = runner.run_animation(sections['code'])
                
                if video_path and os.path.exists(video_path):
                    st.success("🎉 Animation rendered successfully!")
                    
                    # Store video info in session state
                    st.session_state.video_path = video_path
                    st.session_state.video_code = sections['code']
                    
                    # Get video info
                    video_size = os.path.getsize(video_path)
                    st.info(f"📏 Video size: {video_size:,} bytes ({video_size/1024/1024:.1f} MB)")
                    
                    # Display video
                    st.subheader("🎥 Your Animation")
                    try:
                        with open(video_path, 'rb') as video_file:
                            video_bytes = video_file.read()
                            st.video(video_bytes)
                        
                        # Store video bytes for downloads
                        st.session_state.video_bytes = video_bytes
                        
                    except Exception as e:
                        st.error(f"Error displaying video: {e}")
                        st.info(f"Video file exists at: {video_path}")
                else:
                    st.error("❌ Failed to render animation. Check the errors above for details.")
                
                # Clear the render request
                st.session_state.render_requested = False
            
            # Show video and download buttons if video exists in session state
            if hasattr(st.session_state, 'video_path') and hasattr(st.session_state, 'video_bytes'):
                st.markdown("---")
                st.subheader("🎥 Generated Video")
                
                # Display video from session state
                st.video(st.session_state.video_bytes)
                
                # Download buttons
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.download_button(
                        label="📥 Download Video",
                        data=st.session_state.video_bytes,
                        file_name=f"hinglish_animation_{int(time.time())}.mp4",
                        mime="video/mp4",
                        use_container_width=True
                    )
                
                with col2:
                    st.download_button(
                        label="📥 Download Code",
                        data=st.session_state.get('video_code', sections['code']),
                        file_name=f"animation_code_{int(time.time())}.py",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col3:
                    if st.button("🗑️ Clear Video", use_container_width=True):
                        # Clear video from session state
                        if 'video_path' in st.session_state:
                            del st.session_state.video_path
                        if 'video_bytes' in st.session_state:
                            del st.session_state.video_bytes
                        if 'video_code' in st.session_state:
                            del st.session_state.video_code
                        st.rerun()
                
                # Show video info
                st.info(f"💾 Video saved at: {st.session_state.video_path}")
                st.info(f"📏 Size: {len(st.session_state.video_bytes):,} bytes ({len(st.session_state.video_bytes)/1024/1024:.1f} MB)")
            else:
                st.error("Failed to generate animation code. Please try again.")
        
        elif generate_button and not problem_statement:
            st.warning("Please enter a problem statement or topic.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    ### 💡 Tips for Better Results:
    - Be specific about the concept you want to explain
    - Mention if you want equations, diagrams, or animations
    - Use simple, clear language in your problem statement
    - Try the example topics from the sidebar for inspiration
    
    ### 🔧 Technical Details:
    - Uses **Manim Community Edition** for animations
    - **gTTS** for free Hinglish text-to-speech
    - **Gemini AI** for intelligent content generation
    - **Automatic synchronization** between audio and visuals
    """)

if __name__ == "__main__":
    main()
