from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class QuickNewtonTest(VoiceoverScene):
    def construct(self):
        # Setup TTS
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Colors
        PRIMARY_COLOR = BLUE
        ACCENT_COLOR = ORANGE
        TEXT_COLOR = WHITE
        
        # Quick title
        title = Text("Newton's Second Law", font_size=48, color=PRIMARY_COLOR)
        
        with self.voiceover(text="Newton ka second law: F equals ma") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Quick formula
        formula = Text("F = ma", font_size=60, color=ACCENT_COLOR)
        
        with self.voiceover(text="Force equals mass times acceleration") as tracker:
            self.play(Transform(title, formula), run_time=tracker.duration)
        
        # Simple demo
        box = Square(side_length=1, color=PRIMARY_COLOR, fill_opacity=0.7).shift(LEFT*2)
        arrow = Arrow(LEFT*3, LEFT*1, color=ACCENT_COLOR, stroke_width=8)
        
        with self.voiceover(text="Force lagane se object accelerate hota hai") as tracker:
            self.play(Create(box), Create(arrow), run_time=tracker.duration)
            self.play(box.animate.shift(RIGHT*4), run_time=tracker.duration)
        
        self.wait(1)

