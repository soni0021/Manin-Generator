"""
Debug script to test video rendering functionality
"""

import os
import subprocess
import tempfile
import time
from pathlib import Path

def test_video_rendering():
    """Test the video rendering pipeline step by step"""
    
    print("🔍 Debugging Video Rendering Pipeline")
    print("=" * 50)
    
    # Test 1: Simple working code
    test_code = '''
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = BLUE
        SECONDARY_COLOR = GREEN  
        ACCENT_COLOR = ORANGE
        TEXT_COLOR = WHITE
        
        # Simple test animation
        title = Text("Test Animation", font_size=48, color=PRIMARY_COLOR)
        
        with self.voiceover(text="Yeh ek test animation hai") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Add a simple shape
        circle = Circle(radius=1, color=SECONDARY_COLOR, fill_opacity=0.5)
        circle.shift(DOWN * 1.5)
        
        with self.voiceover(text="Dekho yeh circle hai") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        self.wait(1)
'''
    
    print("📝 Testing with simple animation code...")
    
    # Create temp directory
    temp_dir = Path("temp_debug")
    temp_dir.mkdir(exist_ok=True)
    
    # Create temporary Python file
    temp_file = temp_dir / f"debug_animation_{int(time.time())}.py"
    
    try:
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(test_code)
        
        print(f"✅ Created temp file: {temp_file}")
        
        # Run Manim command
        cmd = [
            "manim", 
            str(temp_file), 
            "GeneratedAnimation",
            "-ql",  # Low quality for testing
            "--disable_caching"
        ]
        
        print(f"🔧 Running command: {' '.join(cmd)}")
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        print(f"📊 Exit code: {result.returncode}")
        
        if result.stdout:
            print("📤 STDOUT:")
            print(result.stdout[-1000:])  # Last 1000 chars
        
        if result.stderr:
            print("📥 STDERR:")
            print(result.stderr[-1000:])  # Last 1000 chars
        
        # Check for video file
        media_dir = Path("media/videos") / temp_file.stem / "480p15"
        video_file = media_dir / "GeneratedAnimation.mp4"
        
        print(f"📁 Looking for video at: {video_file}")
        print(f"📁 Media directory exists: {media_dir.exists()}")
        
        if media_dir.exists():
            files = list(media_dir.glob("*"))
            print(f"📋 Files in media directory: {files}")
        
        if video_file.exists():
            size = video_file.stat().st_size
            print(f"✅ Video generated successfully!")
            print(f"📏 File: {video_file}")
            print(f"📏 Size: {size} bytes")
            return True, str(video_file)
        else:
            print(f"❌ Video file not found")
            return False, None
            
    except subprocess.TimeoutExpired:
        print("⏰ Command timed out")
        return False, None
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, None
    finally:
        # Clean up
        if temp_file.exists():
            temp_file.unlink()
        if temp_dir.exists():
            try:
                temp_dir.rmdir()
            except:
                pass

def test_streamlit_runner():
    """Test the Streamlit animation runner directly"""
    
    print("\n🧪 Testing Streamlit Animation Runner")
    print("=" * 40)
    
    try:
        import sys
        sys.path.append('.')
        from streamlit_app import ManimeAnimationRunner
        
        runner = ManimeAnimationRunner()
        print(f"✅ Runner initialized")
        print(f"📁 Temp directory: {runner.temp_dir}")
        
        # Simple test code
        test_code = '''
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="hi"))
        
        PRIMARY_COLOR = BLUE
        SECONDARY_COLOR = GREEN
        ACCENT_COLOR = ORANGE
        
        title = Text("Streamlit Test", font_size=48, color=PRIMARY_COLOR)
        
        with self.voiceover(text="Streamlit se test kar rahe hain") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.wait(1)
'''
        
        print("🎬 Running animation through Streamlit runner...")
        video_path = runner.run_animation(test_code, "GeneratedAnimation")
        
        if video_path and os.path.exists(video_path):
            size = os.path.getsize(video_path)
            print(f"✅ Streamlit runner success!")
            print(f"📏 Video: {video_path}")
            print(f"📏 Size: {size} bytes")
            return True, video_path
        else:
            print(f"❌ Streamlit runner failed")
            print(f"📁 Returned path: {video_path}")
            return False, None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False, None

if __name__ == "__main__":
    print("🚀 Starting Video Rendering Debug")
    print("=" * 60)
    
    # Test 1: Direct Manim command
    success1, path1 = test_video_rendering()
    
    # Test 2: Streamlit runner
    success2, path2 = test_streamlit_runner()
    
    print("\n" + "=" * 60)
    print("📊 DEBUG RESULTS")
    print("=" * 60)
    
    print(f"Direct Manim: {'✅ SUCCESS' if success1 else '❌ FAILED'}")
    if path1:
        print(f"  Video: {path1}")
    
    print(f"Streamlit Runner: {'✅ SUCCESS' if success2 else '❌ FAILED'}")
    if path2:
        print(f"  Video: {path2}")
    
    if success1 and success2:
        print("\n🎉 Both tests passed! Video rendering should work.")
    elif success1:
        print("\n⚠️ Direct Manim works, but Streamlit runner has issues.")
    elif success2:
        print("\n⚠️ Streamlit runner works, but direct Manim has issues.")
    else:
        print("\n❌ Both tests failed. Need to investigate further.")
    
    print(f"\n💡 If tests passed, try the Streamlit app:")
    print(f"   python run_streamlit.py")
