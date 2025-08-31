"""
Simple test to verify video generation is working
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class SimpleTest(VoiceoverScene):
    def construct(self):
        # Setup TTS
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Simple animation
        title = Text("Video Test", font_size=48, color=BLUE)
        
        with self.voiceover(text="Yeh ek simple test hai") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Add equation
        equation = MathTex(r"E = mc^2", font_size=60, color=YELLOW)
        
        with self.voiceover(text="Einstein ka famous equation") as tracker:
            self.play(Transform(title, equation), run_time=tracker.duration)
        
        self.wait(1)
