"""
Simple test without LaTeX to verify basic video generation
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class SimpleTestNoLatex(VoiceoverScene):
    def construct(self):
        # Setup TTS
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Simple animation with basic shapes
        title = Text("Video Test", font_size=48, color=BLUE)
        
        with self.voiceover(text="Yeh ek simple test hai") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Add simple shapes instead of equations
        circle = Circle(radius=1, color=RED, fill_opacity=0.5)
        square = Square(side_length=1.5, color=GREEN, fill_opacity=0.5)
        
        with self.voiceover(text="Circle aur square dekho") as tracker:
            self.play(FadeOut(title))
            self.play(Create(circle), Create(square.shift(RIGHT*2)), run_time=tracker.duration)
        
        self.wait(1)

