"""
Test script specifically for video generation
Tests the complete pipeline from code generation to video rendering
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

def test_simple_manim_render():
    """Test basic Manim rendering without Streamlit"""
    print("🎬 Testing Basic Manim Video Generation")
    print("-" * 45)
    
    # Create a simple test scene
    test_code = '''
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class TestVideoScene(VoiceoverScene):
    def construct(self):
        # Setup TTS
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Simple animation
        title = Text("Test Video", font_size=48, color=BLUE)
        
        with self.voiceover(text="Yeh ek test video hai") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.wait(1)
'''
    
    # Write test file
    test_file = Path("test_scene.py")
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_code)
    
    try:
        print(f"📝 Created test file: {test_file}")
        
        # Run Manim
        cmd = ["manim", str(test_file), "TestVideoScene", "-ql", "--disable_caching"]
        print(f"🔧 Running command: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        print(f"📊 Exit code: {result.returncode}")
        
        if result.stdout:
            print("📤 STDOUT:")
            print(result.stdout)
        
        if result.stderr:
            print("📥 STDERR:")
            print(result.stderr)
        
        # Check for video file
        media_dir = Path("media/videos/test_scene/480p15")
        video_file = media_dir / "TestVideoScene.mp4"
        
        if video_file.exists():
            print(f"✅ Video generated successfully: {video_file}")
            print(f"📏 File size: {video_file.stat().st_size} bytes")
            return True, str(video_file)
        else:
            print(f"❌ Video file not found at: {video_file}")
            print(f"📁 Media directory exists: {media_dir.exists()}")
            if media_dir.exists():
                print(f"📋 Directory contents: {list(media_dir.glob('*'))}")
            return False, None
            
    except subprocess.TimeoutExpired:
        print("⏰ Command timed out after 5 minutes")
        return False, None
    except Exception as e:
        print(f"❌ Error: {e}")
        return False, None
    finally:
        # Clean up
        if test_file.exists():
            test_file.unlink()

def test_streamlit_animation_runner():
    """Test the Streamlit animation runner component"""
    print("\n🎬 Testing Streamlit Animation Runner")
    print("-" * 40)
    
    try:
        from streamlit_app import ManimeAnimationRunner
        
        runner = ManimeAnimationRunner()
        print(f"✅ AnimationRunner initialized")
        print(f"📁 Temp directory: {runner.temp_dir}")
        
        # Test with simple code
        test_code = '''
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="hi"))
        
        title = Text("Streamlit Test", font_size=48, color=RED)
        
        with self.voiceover(text="Streamlit se banaya gaya test video") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        equation = MathTex(r"E = mc^2", font_size=60, color=YELLOW)
        
        with self.voiceover(text="Einstein ka famous equation") as tracker:
            self.play(Transform(title, equation), run_time=tracker.duration)
'''
        
        print("🔧 Running animation through Streamlit runner...")
        video_path = runner.run_animation(test_code, "GeneratedAnimation")
        
        if video_path and os.path.exists(video_path):
            print(f"✅ Streamlit runner success: {video_path}")
            print(f"📏 File size: {os.path.getsize(video_path)} bytes")
            return True, video_path
        else:
            print(f"❌ Streamlit runner failed")
            return False, None
            
    except Exception as e:
        print(f"❌ Error testing Streamlit runner: {e}")
        import traceback
        traceback.print_exc()
        return False, None

def test_ai_generation_and_render():
    """Test complete pipeline: AI generation + video rendering"""
    print("\n🤖 Testing Complete AI → Video Pipeline")
    print("-" * 45)
    
    try:
        from streamlit_app import AnimationGenerator, ManimeAnimationRunner
        
        # Generate code with AI
        generator = AnimationGenerator()
        problem = "Show a simple circle and square with basic animation"
        
        print(f"📝 Problem: {problem}")
        print("🤖 Generating code with AI...")
        
        sections = generator.generate_animation_code(problem)
        
        if not sections.get('code'):
            print("❌ AI code generation failed")
            return False, None
        
        print(f"✅ AI generated {len(sections['code'])} characters of code")
        
        # Extract just the code part
        code = sections['code']
        
        # Clean up the code if it has markdown formatting
        if '```python' in code:
            code = code.split('```python')[1].split('```')[0]
        elif '```' in code:
            code = code.split('```')[1].split('```')[0]
        
        print("🎬 Rendering with generated code...")
        
        # Render video
        runner = ManimeAnimationRunner()
        video_path = runner.run_animation(code, "GeneratedAnimation")
        
        if video_path and os.path.exists(video_path):
            print(f"✅ Complete pipeline success: {video_path}")
            print(f"📏 File size: {os.path.getsize(video_path)} bytes")
            return True, video_path
        else:
            print("❌ Video rendering failed in complete pipeline")
            return False, None
            
    except Exception as e:
        print(f"❌ Error in complete pipeline: {e}")
        import traceback
        traceback.print_exc()
        return False, None

def check_manim_installation():
    """Check Manim installation and configuration"""
    print("🔍 Checking Manim Installation")
    print("-" * 35)
    
    try:
        import manim
        print(f"✅ Manim version: {manim.__version__}")
        
        # Check config
        from manim import config
        print(f"📁 Media directory: {config.media_dir}")
        print(f"🎥 Video directory: {config.video_dir}")
        print(f"📊 Quality: {config.quality}")
        
        # Check for ffmpeg
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ FFmpeg is available")
        else:
            print("❌ FFmpeg not found - required for video generation")
            
        return True
        
    except Exception as e:
        print(f"❌ Manim installation issue: {e}")
        return False

def main():
    """Run all video generation tests"""
    print("🧪 Video Generation Test Suite")
    print("=" * 50)
    
    # Check Manim installation
    if not check_manim_installation():
        print("\n❌ Manim installation issues - cannot proceed")
        return False
    
    print("\n" + "=" * 50)
    
    # Test 1: Basic Manim render
    basic_success, basic_video = test_simple_manim_render()
    
    # Test 2: Streamlit runner
    runner_success, runner_video = test_streamlit_animation_runner()
    
    # Test 3: Complete pipeline
    pipeline_success, pipeline_video = test_ai_generation_and_render()
    
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    print(f"Basic Manim Render: {'✅ PASS' if basic_success else '❌ FAIL'}")
    if basic_video:
        print(f"  Video: {basic_video}")
    
    print(f"Streamlit Runner: {'✅ PASS' if runner_success else '❌ FAIL'}")
    if runner_video:
        print(f"  Video: {runner_video}")
    
    print(f"Complete AI Pipeline: {'✅ PASS' if pipeline_success else '❌ FAIL'}")
    if pipeline_video:
        print(f"  Video: {pipeline_video}")
    
    if basic_success and runner_success and pipeline_success:
        print("\n🎉 ALL VIDEO TESTS PASSED!")
        print("🚀 Video generation is working correctly")
        return True
    else:
        print("\n⚠️  Some video tests failed")
        print("🔧 Check the error messages above for debugging")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
