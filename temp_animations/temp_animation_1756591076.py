
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
