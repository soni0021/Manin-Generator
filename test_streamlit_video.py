"""
Test the Streamlit video rendering functionality
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from streamlit_app import ManimeAnimationRunner

def test_video_generation():
    """Test video generation with a simple animation"""
    
    print("🧪 Testing Streamlit Video Generation")
    print("=" * 45)
    
    # Simple test code that should work
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
        
        # Simple animation
        title = Text("Test Video", font_size=48, color=PRIMARY_COLOR)
        
        with self.voiceover(text="Yeh ek test video hai Streamlit ke liye") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Add a shape
        circle = Circle(radius=1, color=SECONDARY_COLOR, fill_opacity=0.5)
        circle.shift(DOWN * 2)
        
        with self.voiceover(text="Dekho yeh circle hai") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        self.wait(1)
'''
    
    print("📝 Testing with simple GeneratedAnimation code...")
    print(f"📏 Code length: {len(test_code)} characters")
    
    try:
        # Initialize runner
        runner = ManimeAnimationRunner()
        print(f"✅ Runner initialized")
        print(f"📁 Temp directory: {runner.temp_dir}")
        
        # Test the animation
        print("\n🎬 Running animation...")
        video_path = runner.run_animation(test_code, "GeneratedAnimation")
        
        if video_path and os.path.exists(video_path):
            video_size = os.path.getsize(video_path)
            print(f"✅ SUCCESS! Video generated:")
            print(f"   📁 Path: {video_path}")
            print(f"   📏 Size: {video_size:,} bytes ({video_size/1024/1024:.1f} MB)")
            
            # Verify it's a real video file
            if video_size > 1000:  # At least 1KB
                print(f"✅ Video file appears valid (size > 1KB)")
                return True, video_path
            else:
                print(f"⚠️ Video file very small, might be corrupted")
                return False, video_path
        else:
            print(f"❌ FAILED: No video generated")
            print(f"   Returned path: {video_path}")
            return False, None
            
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False, None

if __name__ == "__main__":
    success, path = test_video_generation()
    
    print("\n" + "=" * 45)
    if success:
        print("🎉 VIDEO GENERATION TEST PASSED!")
        print("✅ The Streamlit app should now work correctly")
        print(f"🚀 Launch app: python run_streamlit.py")
        print(f"📹 Test video at: {path}")
    else:
        print("❌ Video generation test failed")
        print("🔧 Need to debug the animation runner")
        
    print("\n💡 Next steps:")
    print("1. If test passed: Launch Streamlit app and try rendering")
    print("2. If test failed: Check Manim installation and dependencies")
    print("3. Try with a simple topic like 'Show a circle and square'")

