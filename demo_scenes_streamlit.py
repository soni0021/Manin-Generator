"""
Demo scenes specifically optimized for Streamlit app
Faster rendering, simpler animations for web interface
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class StreamlitBaseScene(VoiceoverScene):
    """Base scene optimized for Streamlit with faster rendering"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Setup gTTS for Hindi
        self.set_speech_service(GTTSService(lang="hi"))

class QuickPhysicsDemo(StreamlitBaseScene):
    """Quick physics demo - Newton's law in 30 seconds"""
    
    def construct(self):
        # Title
        title = Text("Newton का Second Law", font_size=40, color=BLUE)
        
        with self.voiceover(text="Newton ka second law: Force equals mass times acceleration") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Equation
        equation = MathTex(r"F = ma", font_size=60, color=YELLOW)
        
        with self.voiceover(text="F matlab force, m matlab mass, a matlab acceleration") as tracker:
            self.play(Transform(title, equation), run_time=tracker.duration)
        
        # Simple demonstration
        box1 = Square(side_length=1, color=RED, fill_opacity=0.7).shift(LEFT*2)
        box2 = Square(side_length=2, color=BLUE, fill_opacity=0.7).shift(RIGHT*2)
        
        with self.voiceover(text="Same force, different mass, different acceleration") as tracker:
            self.play(Create(box1), Create(box2), run_time=tracker.duration)
            self.play(box1.animate.shift(UP*2), box2.animate.shift(UP*1), run_time=tracker.duration)

class QuickChemistryDemo(StreamlitBaseScene):
    """Quick chemistry demo - Water molecule in 30 seconds"""
    
    def construct(self):
        title = Text("Water Molecule - H₂O", font_size=40, color=BLUE)
        
        with self.voiceover(text="Water molecule mein oxygen aur hydrogen atoms hain") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Simple molecular structure
        oxygen = Circle(radius=0.5, color=RED, fill_opacity=0.8)
        h1 = Circle(radius=0.3, color=WHITE, fill_opacity=0.8).shift(LEFT*1.2 + UP*0.5)
        h2 = Circle(radius=0.3, color=WHITE, fill_opacity=0.8).shift(RIGHT*1.2 + UP*0.5)
        
        bond1 = Line(oxygen.get_center(), h1.get_center(), color=YELLOW, stroke_width=6)
        bond2 = Line(oxygen.get_center(), h2.get_center(), color=YELLOW, stroke_width=6)
        
        molecule = VGroup(oxygen, h1, h2, bond1, bond2)
        
        with self.voiceover(text="Covalent bonds se jude hain. Polar molecule hai") as tracker:
            self.play(FadeOut(title))
            self.play(Create(molecule), run_time=tracker.duration)

class QuickBiologyDemo(StreamlitBaseScene):
    """Quick biology demo - Cell in 30 seconds"""
    
    def construct(self):
        title = Text("Cell Structure", font_size=40, color=GREEN)
        
        with self.voiceover(text="Cell life ki basic unit hai") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        # Simple cell structure
        cell_membrane = Circle(radius=3, color=GREEN, stroke_width=4)
        nucleus = Circle(radius=1, color=BLUE, fill_opacity=0.6)
        
        with self.voiceover(text="Cell membrane aur nucleus. Membrane selective permeable hai") as tracker:
            self.play(FadeOut(title))
            self.play(Create(cell_membrane), Create(nucleus), run_time=tracker.duration)

# Scene registry for Streamlit app
DEMO_SCENES = {
    "Physics - Newton's Law": {
        "scene_class": QuickPhysicsDemo,
        "description": "Quick demonstration of F=ma with visual examples",
        "duration": "~30 seconds"
    },
    "Chemistry - Water Molecule": {
        "scene_class": QuickChemistryDemo,
        "description": "Water molecule structure and bonding",
        "duration": "~30 seconds"
    },
    "Biology - Cell Structure": {
        "scene_class": QuickBiologyDemo,
        "description": "Basic cell components and membrane",
        "duration": "~30 seconds"
    }
}
