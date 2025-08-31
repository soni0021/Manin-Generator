"""
Main orchestrator for the Manim + Hinglish TTS Educational Animation System
Provides a unified interface for both simplified and comprehensive systems
"""

import os
import sys
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def run_simplified_system():
    """Run the simplified Hinglish Manim system"""
    print("🌟 Simplified Hinglish Manim System")
    print("=" * 40)
    print("\nAvailable demo scenes:")
    print("1. NewtonsLawDemo - Physics: Newton's Second Law")
    print("2. WaterMoleculeDemo - Chemistry: Water molecule structure")
    print("3. CellMembraneDemo - Biology: Cell membrane transport")
    
    print("\n📋 Quick commands:")
    print("manim simple_hinglish_manim.py NewtonsLawDemo")
    print("manim simple_hinglish_manim.py WaterMoleculeDemo") 
    print("manim simple_hinglish_manim.py CellMembraneDemo")
    
    print("\n🤖 For custom animations:")
    print("1. Use the Gemini prompt from README.md")
    print("2. Generate your animation code")
    print("3. Save and render with manim")
    
    return True

def run_comprehensive_system():
    """Run the comprehensive system with multiple TTS options"""
    print("🔧 Comprehensive Hinglish Manim System")
    print("=" * 42)
    
    try:
        from utils.voice_manager import tts_manager
        from config.voice_profiles import voice_manager
        
        print("\n📊 TTS Service Status:")
        status = tts_manager.get_service_status()
        
        for service_name, info in status.items():
            status_icon = "✅" if info['available'] else "❌"
            print(f"{status_icon} {info['name']}: {'Available' if info['available'] else 'Not Available'}")
            if not info['available']:
                print(f"   Install: {info['requirements']}")
        
        print("\n🎭 Voice Profiles:")
        profiles = voice_manager.list_available_profiles()
        
        for profile in profiles:
            status_icon = "🎤" if profile['has_reference_audio'] else "📝"
            print(f"{status_icon} {profile['subject'].title()}: {profile['name']}")
            if not profile['has_reference_audio']:
                print(f"   Status: {profile['status']}")
        
        print("\n🎬 Available Scenes:")
        print("Physics:")
        print("  - manim scenes/physics_scenes.py NewtonsSecondLawScene")
        print("  - manim scenes/physics_scenes.py ElectromagneticFieldScene")
        
        print("Chemistry:")
        print("  - manim scenes/chemistry_scenes.py WaterMoleculeScene")
        print("  - manim scenes/chemistry_scenes.py PeriodicTableScene")
        
        print("Biology:")
        print("  - manim scenes/biology_scenes.py CellMembraneScene")
        print("  - manim scenes/biology_scenes.py DNAReplicationScene")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error loading comprehensive system: {e}")
        print("💡 Try installing full dependencies: pip install -r requirements.txt")
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking Dependencies...")
    
    required_packages = {
        'manim': 'Manim Community Edition',
        'manim_voiceover': 'Manim Voiceover',
        'gtts': 'Google Text-to-Speech',
        'pygame': 'Audio playback support'
    }
    
    missing_packages = []
    
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"✅ {description}")
        except ImportError:
            print(f"❌ {description} - Install: pip install {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n💡 Quick fix: pip install {' '.join(missing_packages)}")
        return False
    
    print("\n✅ All core dependencies are installed!")
    return True

def show_gemini_prompt():
    """Display the Gemini integration prompt"""
    prompt = '''
🤖 GEMINI PROMPT FOR CUSTOM ANIMATIONS
=====================================

Copy this prompt into Gemini, then add your physics/chemistry/biology question:

---

You are a senior Python educator and Manim engineer.
Transform the user's STEM problem statement into a narrated Manim animation with synchronized Hinglish voiceover using Manim Community + Manim Voiceover + gTTS.

REQUIREMENTS
1) Produce, in order:
   A. Learning objectives (bullet list)
   B. Storyboard: ordered beats with timestamps (approximate seconds) and on-screen elements
   C. Hinglish narration lines per beat (Latin script, Hindi + English terms)
   D. Final runnable Python code:
      - Uses Manim CE and manim-voiceover
      - from manim_voiceover.services.gtts import GTTSService
      - self.set_speech_service(GTTSService(lang="hi"))
      - Wrap each animation in `with self.voiceover(text="...") as tracker:` and set run_time=tracker.duration
      - Cache audio via Manim Voiceover defaults; no external editors
      - Organize as a single file with one Scene subclass named ProblemAnimation
      - Keep imports minimal and pinned to public APIs only

2) Content scope:
   - Visualize the core concepts from the problem, not a full lecture
   - If equations are needed, render with MathTex
   - Include labels/titles where helpful
   - Keep total runtime ~30–90 seconds

3) Hinglish style:
   - Write Hindi in Latin script, mix English technical words naturally
   - Be concise and instructional; avoid slang
   - Pronounce equations verbally ("F equals m times a") where appropriate

4) Output format:
   === OBJECTIVES ===
   <bullets>
   === STORYBOARD ===
   <numbered beats with timestamps>
   === NARRATION ===
   <numbered lines aligned to beats>
   === CODE ===
   <full Python code block>

5) Constraints:
   - Do not invent private APIs; use documented Manim CE + Manim Voiceover patterns
   - Ensure each play() call's run_time uses tracker.duration to sync with TTS
   - Prefer simple shapes, vectors, and MathTex; avoid heavy assets
   - If problem is ambiguous, choose a reasonable pedagogical focus and state assumptions at the top

USER PROBLEM STATEMENT
<paste the problem or question here>

---

💡 WORKFLOW:
1. Copy prompt above + your question → Gemini
2. Get generated code → Save as my_animation.py
3. Run: manim my_animation.py ProblemAnimation
4. Enjoy your Hinglish educational animation! 🎬
'''
    print(prompt)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Manim + Hinglish TTS Educational Animation System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --simple              # Show simplified system info
  python main.py --comprehensive       # Show comprehensive system info
  python main.py --check-deps          # Check dependencies
  python main.py --gemini-prompt       # Show Gemini integration prompt
  python main.py --demo newton         # Run Newton's law demo
        """
    )
    
    parser.add_argument('--simple', action='store_true', 
                       help='Show simplified system information')
    parser.add_argument('--comprehensive', action='store_true',
                       help='Show comprehensive system information')
    parser.add_argument('--check-deps', action='store_true',
                       help='Check if dependencies are installed')
    parser.add_argument('--gemini-prompt', action='store_true',
                       help='Show Gemini integration prompt')
    parser.add_argument('--demo', choices=['newton', 'water', 'cell'],
                       help='Run a demo scene')
    
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if not any(vars(args).values()):
        print("🎬 Manim + Hinglish TTS Educational Animation System")
        print("=" * 55)
        print("\n🚀 RECOMMENDED: Start with the simplified system")
        print("python main.py --simple")
        print("\n🔧 For advanced users:")
        print("python main.py --comprehensive")
        print("\n📋 Other options:")
        print("python main.py --check-deps      # Check dependencies")
        print("python main.py --gemini-prompt   # Gemini integration")
        print("python main.py --demo newton     # Run demo")
        print("\n📚 Full documentation: README.md")
        return
    
    if args.check_deps:
        check_dependencies()
        return
    
    if args.gemini_prompt:
        show_gemini_prompt()
        return
    
    if args.demo:
        demo_map = {
            'newton': 'NewtonsLawDemo',
            'water': 'WaterMoleculeDemo', 
            'cell': 'CellMembraneDemo'
        }
        scene_name = demo_map[args.demo]
        cmd = f"manim simple_hinglish_manim.py {scene_name}"
        print(f"🎬 Running demo: {cmd}")
        os.system(cmd)
        return
    
    if args.simple:
        run_simplified_system()
    elif args.comprehensive:
        run_comprehensive_system()
    else:
        # Default to simplified
        run_simplified_system()

if __name__ == "__main__":
    main()

