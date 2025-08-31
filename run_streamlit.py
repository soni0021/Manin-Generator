"""
Launcher script for the Streamlit app
Handles setup, dependency checking, and app launching
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'streamlit',
        'manim',
        'manim_voiceover', 
        'gtts',
        'pygame',
        'google.generativeai'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'manim_voiceover':
                __import__('manim_voiceover')
            elif package == 'google.generativeai':
                __import__('google.generativeai')
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies(packages):
    """Install missing dependencies"""
    if not packages:
        return True
    
    print(f"\n🔧 Installing missing packages: {', '.join(packages)}")
    
    # Map package names to pip install names
    pip_names = {
        'manim_voiceover': 'manim-voiceover',
        'google.generativeai': 'google-generativeai'
    }
    
    install_packages = []
    for pkg in packages:
        install_packages.append(pip_names.get(pkg, pkg))
    
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install'
        ] + install_packages)
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def setup_environment():
    """Setup environment for the app"""
    project_root = Path(__file__).parent
    
    # Create necessary directories
    (project_root / "temp_animations").mkdir(exist_ok=True)
    (project_root / "media").mkdir(exist_ok=True)
    
    # Set environment variables
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'false'
    
    return True

def launch_app():
    """Launch the Streamlit app"""
    app_file = Path(__file__).parent / "streamlit_app.py"
    
    if not app_file.exists():
        print(f"❌ App file not found: {app_file}")
        return False
    
    print("🚀 Launching Streamlit app...")
    print("📱 Open your browser to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the app")
    
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', str(app_file),
            '--server.port', '8501',
            '--server.address', 'localhost'
        ])
        return True
    except KeyboardInterrupt:
        print("\n👋 App stopped by user")
        return True
    except Exception as e:
        print(f"❌ Failed to launch app: {e}")
        return False

def main():
    """Main launcher function"""
    print("🎬 Hinglish Educational Animations - Streamlit App")
    print("=" * 55)
    
    print("\n🔍 Checking dependencies...")
    missing = check_dependencies()
    
    if missing:
        print(f"\n⚠️  Missing {len(missing)} dependencies")
        install_choice = input("📦 Install missing dependencies? (y/n): ").lower().strip()
        
        if install_choice in ['y', 'yes']:
            if not install_dependencies(missing):
                print("❌ Failed to install dependencies. Please install manually:")
                print("pip install -r requirements-streamlit.txt")
                return False
        else:
            print("❌ Cannot run app without dependencies")
            print("💡 Install with: pip install -r requirements-streamlit.txt")
            return False
    
    print("\n⚙️  Setting up environment...")
    if not setup_environment():
        print("❌ Failed to setup environment")
        return False
    
    print("✅ Setup complete!")
    
    print("\n" + "="*55)
    print("🌟 FEATURES AVAILABLE:")
    print("• 🤖 AI-powered animation generation with Gemini")
    print("• 🗣️  Free Hinglish TTS with gTTS")
    print("• 🎬 Manim Community animations")
    print("• 📱 Web interface for easy use")
    print("• 🚀 Quick demo scenes")
    print("=" * 55)
    
    # Launch the app
    return launch_app()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
