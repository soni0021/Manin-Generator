"""
Test the improved Gemini prompt for high-quality video generation
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from streamlit_app import AnimationGenerator

def test_improved_prompt():
    """Test the new structured prompt with a simple physics concept"""
    
    print("🧪 Testing Improved Gemini Prompt")
    print("=" * 50)
    
    # Initialize generator
    generator = AnimationGenerator()
    
    # Test with a simple concept
    problem_statement = "Explain what is force in physics using visual examples with objects and arrows"
    
    print(f"📝 Problem: {problem_statement}")
    print("\n🤖 Generating content with improved prompt...")
    
    try:
        sections = generator.generate_animation_code(problem_statement)
        
        if sections:
            print("\n✅ Generation successful!")
            print(f"📊 Generated sections: {list(sections.keys())}")
            
            # Check each section
            for section_name, content in sections.items():
                if content and content.strip():
                    print(f"✅ {section_name}: {len(content)} characters")
                else:
                    print(f"❌ {section_name}: Empty or missing")
            
            # Show key parts
            if sections.get('objectives'):
                print(f"\n📋 OBJECTIVES PREVIEW:")
                print(sections['objectives'][:200] + "..." if len(sections['objectives']) > 200 else sections['objectives'])
            
            if sections.get('design_plan'):
                print(f"\n🎨 DESIGN PLAN PREVIEW:")
                print(sections['design_plan'][:200] + "..." if len(sections['design_plan']) > 200 else sections['design_plan'])
            
            if sections.get('code'):
                print(f"\n💻 CODE PREVIEW (first 300 chars):")
                code_preview = sections['code'][:300] + "..." if len(sections['code']) > 300 else sections['code']
                print(code_preview)
                
                # Check for quality indicators
                quality_checks = {
                    "Has VoiceoverScene": "VoiceoverScene" in sections['code'],
                    "Has GTTSService": "GTTSService" in sections['code'],
                    "Has voiceover blocks": "with self.voiceover" in sections['code'],
                    "Uses Text() not MathTex": "Text(" in sections['code'] and "MathTex" not in sections['code'],
                    "Has color definitions": any(color in sections['code'] for color in ["BLUE", "GREEN", "RED", "ORANGE"]),
                    "Has proper positioning": any(pos in sections['code'] for pos in ["LEFT", "RIGHT", "UP", "DOWN", "shift", "to_edge"]),
                    "Has class structure": "class GeneratedAnimation" in sections['code']
                }
                
                print(f"\n🔍 QUALITY CHECKS:")
                for check, passed in quality_checks.items():
                    status = "✅" if passed else "❌"
                    print(f"{status} {check}")
                
                passed_checks = sum(quality_checks.values())
                total_checks = len(quality_checks)
                print(f"\n📊 Overall Quality: {passed_checks}/{total_checks} checks passed")
                
                if passed_checks >= total_checks * 0.8:
                    print("🎉 HIGH QUALITY CODE GENERATED!")
                    return True
                else:
                    print("⚠️ Code quality needs improvement")
                    return False
            else:
                print("❌ No code generated")
                return False
        else:
            print("❌ No content generated")
            return False
            
    except Exception as e:
        print(f"❌ Error during generation: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_prompt_improvements():
    """Show what improvements were made to the prompt"""
    
    print("\n🚀 PROMPT IMPROVEMENTS MADE:")
    print("=" * 50)
    
    improvements = [
        "🎨 Structured visual design requirements with specific color palette",
        "📐 Spatial organization rules to prevent element collisions", 
        "🎬 Animation quality standards with timing specifications",
        "📝 Clean code structure with modular scene methods",
        "🗣️ Enhanced Hinglish narration guidelines",
        "🚫 Strict prohibitions to prevent common issues",
        "✅ Quality checklist for consistent output",
        "📋 Detailed output format with all required sections",
        "🎯 Professional color scheme with hex codes",
        "⚡ Perfect audio-visual synchronization requirements"
    ]
    
    for improvement in improvements:
        print(improvement)
    
    print(f"\n📈 Expected improvements:")
    print("• No more element collisions or overlaps")
    print("• Professional, consistent color schemes")
    print("• Perfect audio-video synchronization")
    print("• Well-structured, readable code")
    print("• High-quality visual design")
    print("• Better educational content flow")

if __name__ == "__main__":
    show_prompt_improvements()
    
    print("\n" + "=" * 50)
    success = test_improved_prompt()
    
    if success:
        print(f"\n🎉 PROMPT TEST SUCCESSFUL!")
        print(f"🚀 Ready for high-quality video generation!")
    else:
        print(f"\n⚠️ Prompt needs further refinement")
    
    print(f"\n💡 To test in Streamlit app:")
    print(f"   python run_streamlit.py")
    print(f"   # Then try: 'Explain force in physics with visual examples'")
