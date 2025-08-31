"""
Quick test script for the Streamlit app components
Tests AI generation and basic functionality
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

def test_gemini_connection():
    """Test Gemini AI connection"""
    try:
        import google.generativeai as genai
        
        # Configure with API key from environment or secrets
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
        if not GOOGLE_API_KEY:
            print("❌ GOOGLE_API_KEY environment variable not set")
            return False
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Test with a simple prompt
        model = genai.GenerativeModel('models/gemini-2.5-pro')
        response = model.generate_content("Hello, can you respond with just 'AI connection successful'?")
        
        print("✅ Gemini AI Connection: SUCCESS")
        print(f"Response: {response.text}")
        return True
        
    except Exception as e:
        print(f"❌ Gemini AI Connection: FAILED - {e}")
        return False

def test_dependencies():
    """Test all required dependencies"""
    dependencies = {
        'streamlit': 'Streamlit web framework',
        'manim': 'Manim Community Edition',
        'manim_voiceover': 'Manim Voiceover',
        'gtts': 'Google Text-to-Speech',
        'pygame': 'Audio playback',
        'google.generativeai': 'Gemini AI'
    }
    
    print("🔍 Testing Dependencies:")
    print("-" * 30)
    
    all_good = True
    
    for package, description in dependencies.items():
        try:
            if package == 'manim_voiceover':
                __import__('manim_voiceover')
            elif package == 'google.generativeai':
                __import__('google.generativeai')
            else:
                __import__(package)
            print(f"✅ {description}")
        except ImportError:
            print(f"❌ {description} - Missing!")
            all_good = False
    
    return all_good

def test_animation_generation():
    """Test animation code generation"""
    try:
        from streamlit_app import AnimationGenerator
        
        generator = AnimationGenerator()
        
        # Test with simple problem
        problem = "Explain what is force in physics with a simple example"
        
        print("\n🤖 Testing Animation Generation:")
        print("-" * 35)
        print(f"Problem: {problem}")
        
        sections = generator.generate_animation_code(problem)
        
        if sections.get('code'):
            print("✅ Code generation: SUCCESS")
            print(f"Generated {len(sections['code'])} characters of code")
            
            # Check if code contains required elements
            required_elements = [
                'from manim import',
                'VoiceoverScene',
                'GTTSService',
                'voiceover'
            ]
            
            missing_elements = []
            for element in required_elements:
                if element not in sections['code']:
                    missing_elements.append(element)
            
            if missing_elements:
                print(f"⚠️  Missing elements: {missing_elements}")
            else:
                print("✅ All required elements present")
            
            return True
        else:
            print("❌ Code generation: FAILED - No code generated")
            return False
            
    except Exception as e:
        print(f"❌ Animation generation: FAILED - {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing Streamlit App Components")
    print("=" * 40)
    
    # Test dependencies
    deps_ok = test_dependencies()
    
    if not deps_ok:
        print("\n💡 Install missing dependencies:")
        print("pip install -r requirements-streamlit.txt")
        return False
    
    print("\n" + "=" * 40)
    
    # Test Gemini connection
    ai_ok = test_gemini_connection()
    
    if not ai_ok:
        print("\n❌ Cannot test animation generation without AI")
        return False
    
    print("\n" + "=" * 40)
    
    # Test animation generation
    gen_ok = test_animation_generation()
    
    print("\n" + "=" * 40)
    print("📊 TEST SUMMARY:")
    print(f"Dependencies: {'✅ PASS' if deps_ok else '❌ FAIL'}")
    print(f"Gemini AI: {'✅ PASS' if ai_ok else '❌ FAIL'}")
    print(f"Code Generation: {'✅ PASS' if gen_ok else '❌ FAIL'}")
    
    if deps_ok and ai_ok and gen_ok:
        print("\n🎉 ALL TESTS PASSED!")
        print("🚀 Ready to launch Streamlit app:")
        print("   python run_streamlit.py")
        return True
    else:
        print("\n⚠️  Some tests failed. Check issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
