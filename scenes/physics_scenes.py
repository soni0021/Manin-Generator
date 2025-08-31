"""
Physics Scene Classes for Hinglish Educational Content
Specialized Manim scenes for physics concepts with voiceover integration
"""

import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene

try:
    from manim_physics import *
    PHYSICS_AVAILABLE = True
except ImportError:
    PHYSICS_AVAILABLE = False
    print("manim-physics not available. Install with: pip install manim-physics")

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config.tts_config import TTSQuality, SubjectVoice
from utils.voice_manager import tts_manager

class PhysicsHinglishScene(VoiceoverScene):
    """Base scene class for physics content with Hinglish voiceover"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject = SubjectVoice.PHYSICS
        self.tts_quality = TTSQuality.HIGH
        
    def setup_voice(self):
        """Setup TTS service for physics content"""
        # Configure manim-voiceover to use our TTS manager
        self.set_speech_service(HinglishTTSService(
            quality=self.tts_quality,
            subject=self.subject
        ))

class NewtonsSecondLawScene(PhysicsHinglishScene):
    """Demonstrates Newton's Second Law with Hinglish explanation"""
    
    def construct(self):
        self.setup_voice()
        
        # Title
        title = Text("Newton का Second Law", font_size=48, color=BLUE)
        subtitle = Text("Force = Mass × Acceleration", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        with self.voiceover(text="Namaskar! Aaj hum sikhenge Newton ke second law ke baare mein."):
            self.play(Write(title))
            self.play(Write(subtitle))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Setup the physics demonstration
        self.demonstrate_force_mass_acceleration()
        
        # Mathematical explanation
        self.show_mathematical_relationship()
        
        # Real-world examples
        self.show_examples()
    
    def demonstrate_force_mass_acceleration(self):
        """Visual demonstration of F = ma"""
        
        # Create objects with different masses
        small_box = Rectangle(width=1, height=1, color=RED, fill_opacity=0.7)
        large_box = Rectangle(width=2, height=2, color=BLUE, fill_opacity=0.7)
        
        small_mass_label = Text("m = 1 kg", font_size=24).next_to(small_box, UP)
        large_mass_label = Text("m = 4 kg", font_size=24).next_to(large_box, UP)
        
        # Position objects
        small_box.to_edge(LEFT, buff=2)
        large_box.to_edge(LEFT, buff=2).shift(DOWN * 3)
        
        with self.voiceover(text="Dekhiye, yahan do objects hain. Ek chhota aur ek bada. Different masses hain."):
            self.play(Create(small_box), Write(small_mass_label))
            self.play(Create(large_box), Write(large_mass_label))
        
        # Apply same force to both
        force_arrow_small = Arrow(start=LEFT*2, end=RIGHT*2, color=GREEN, stroke_width=8)
        force_arrow_large = Arrow(start=LEFT*2, end=RIGHT*2, color=GREEN, stroke_width=8)
        
        force_arrow_small.next_to(small_box, LEFT)
        force_arrow_large.next_to(large_box, LEFT)
        
        force_label = Text("Same Force = 10 N", font_size=24, color=GREEN)
        force_label.to_edge(UP)
        
        with self.voiceover(text="Ab main same force apply karunga dono objects par. Dekhte hain kya hota hai."):
            self.play(Create(force_arrow_small), Create(force_arrow_large))
            self.play(Write(force_label))
        
        # Show different accelerations
        with self.voiceover(text="Dekho! Chhota object zyada fast move kar raha hai. Kyonki uska mass kam hai, acceleration zyada hai."):
            # Small box moves faster (higher acceleration)
            self.play(
                small_box.animate.shift(RIGHT * 4),
                small_mass_label.animate.shift(RIGHT * 4),
                force_arrow_small.animate.shift(RIGHT * 4),
                run_time=1
            )
            
            # Large box moves slower (lower acceleration)  
            self.play(
                large_box.animate.shift(RIGHT * 2),
                large_mass_label.animate.shift(RIGHT * 2),
                force_arrow_large.animate.shift(RIGHT * 2),
                run_time=1
            )
        
        # Show acceleration values
        accel_small = Text("a = 10 m/s²", font_size=20, color=YELLOW)
        accel_large = Text("a = 2.5 m/s²", font_size=20, color=YELLOW)
        
        accel_small.next_to(small_box, DOWN)
        accel_large.next_to(large_box, DOWN)
        
        with self.voiceover(text="Calculation dekho: F equals ma. Same force, different mass, toh different acceleration milta hai."):
            self.play(Write(accel_small), Write(accel_large))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_mathematical_relationship(self):
        """Show the mathematical relationship F = ma"""
        
        # Main equation
        equation = MathTex(r"F = ma", font_size=72, color=BLUE)
        
        with self.voiceover(text="Yeh hai Newton ka second law ka mathematical form. Force equals mass times acceleration."):
            self.play(Write(equation))
        
        # Break down the equation
        force_def = MathTex(r"F = \text{Force (Newton)}", font_size=36)
        mass_def = MathTex(r"m = \text{Mass (kg)}", font_size=36)
        accel_def = MathTex(r"a = \text{Acceleration (m/s²)}", font_size=36)
        
        definitions = VGroup(force_def, mass_def, accel_def)
        definitions.arrange(DOWN, buff=0.5)
        definitions.next_to(equation, DOWN, buff=1)
        
        with self.voiceover(text="F matlab Force, Newton mein measure karte hain. m matlab mass, kilogram mein. a matlab acceleration, meter per second square mein."):
            self.play(Write(definitions))
        
        # Show rearranged forms
        self.wait(1)
        rearranged1 = MathTex(r"a = \frac{F}{m}", font_size=48, color=GREEN)
        rearranged2 = MathTex(r"m = \frac{F}{a}", font_size=48, color=RED)
        
        rearranged_group = VGroup(rearranged1, rearranged2)
        rearranged_group.arrange(RIGHT, buff=2)
        rearranged_group.next_to(equation, DOWN, buff=1)
        
        with self.voiceover(text="Equation ko rearrange kar sakte hain. Acceleration nikalna hai toh F divided by m. Mass nikalna hai toh F divided by a."):
            self.play(Transform(definitions, rearranged_group))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_examples(self):
        """Show real-world examples"""
        
        examples_title = Text("Real Life Examples", font_size=48, color=GOLD)
        
        with self.voiceover(text="Ab dekhte hain real life mein kahan use hota hai yeh law."):
            self.play(Write(examples_title))
        
        self.wait(1)
        self.play(examples_title.animate.to_edge(UP))
        
        # Example 1: Car acceleration
        car_example = VGroup(
            Text("🚗 Car Acceleration", font_size=32),
            Text("Heavy car → Less acceleration", font_size=24, color=GRAY),
            Text("Light car → More acceleration", font_size=24, color=GRAY)
        )
        car_example.arrange(DOWN, buff=0.3)
        car_example.to_edge(LEFT)
        
        # Example 2: Rocket launch
        rocket_example = VGroup(
            Text("🚀 Rocket Launch", font_size=32),
            Text("More fuel → More force → More acceleration", font_size=20, color=GRAY)
        )
        rocket_example.arrange(DOWN, buff=0.3)
        rocket_example.next_to(car_example, RIGHT, buff=2)
        
        with self.voiceover(text="Car mein dekho - heavy car ko accelerate karna mushkil hai. Rocket mein zyada fuel burn karte hain toh zyada force milta hai."):
            self.play(Write(car_example))
            self.play(Write(rocket_example))
        
        # Example 3: Sports
        sports_example = VGroup(
            Text("⚽ Sports", font_size=32),
            Text("Cricket ball vs Football", font_size=24, color=GRAY),
            Text("Same force, different acceleration", font_size=20, color=GRAY)
        )
        sports_example.arrange(DOWN, buff=0.3)
        sports_example.next_to(car_example, DOWN, buff=1)
        
        with self.voiceover(text="Sports mein bhi same concept. Cricket ball aur football par same force lagao toh cricket ball zyada accelerate hogi kyonki uska mass kam hai."):
            self.play(Write(sports_example))
        
        self.wait(3)
        
        # Conclusion
        conclusion = Text("F = ma - Universal Law!", font_size=48, color=BLUE)
        
        with self.voiceover(text="Toh yeh hai Newton ka second law. Bahut important hai physics mein. Thank you for watching!"):
            self.play(FadeOut(Group(*self.mobjects)))
            self.play(Write(conclusion))
        
        self.wait(2)

class ElectromagneticFieldScene(PhysicsHinglishScene):
    """Demonstrates electromagnetic fields"""
    
    def construct(self):
        self.setup_voice()
        
        # Title
        title = Text("Electromagnetic Fields", font_size=48, color=PURPLE)
        subtitle = Text("विद्युत और चुंबकीय क्षेत्र", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        with self.voiceover(text="Aaj hum electromagnetic fields ke baare mein sikhenge. Yeh bahut interesting topic hai."):
            self.play(Write(title))
            self.play(Write(subtitle))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        self.show_electric_field()
        self.show_magnetic_field()
        self.show_electromagnetic_wave()
    
    def show_electric_field(self):
        """Show electric field visualization"""
        
        # Positive charge
        charge = Circle(radius=0.3, color=RED, fill_opacity=0.8)
        charge_label = Text("+Q", font_size=24, color=WHITE)
        charge_label.move_to(charge.get_center())
        
        with self.voiceover(text="Pehle electric field dekhte hain. Yahan ek positive charge hai."):
            self.play(Create(charge), Write(charge_label))
        
        # Electric field lines
        field_lines = VGroup()
        num_lines = 12
        
        for i in range(num_lines):
            angle = i * 2 * PI / num_lines
            start_point = charge.get_center() + 0.4 * np.array([np.cos(angle), np.sin(angle), 0])
            end_point = charge.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0])
            
            field_line = Arrow(start_point, end_point, color=YELLOW, stroke_width=3)
            field_lines.add(field_line)
        
        with self.voiceover(text="Charge ke around electric field lines banate hain. Yeh lines batate hain ki field ki direction kya hai."):
            self.play(Create(field_lines))
        
        # Test charge
        test_charge = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
        test_charge.to_edge(LEFT)
        test_label = Text("+q", font_size=20, color=WHITE)
        test_label.move_to(test_charge.get_center())
        
        with self.voiceover(text="Ab ek test charge laate hain. Dekho kya hota hai."):
            self.play(Create(test_charge), Write(test_label))
        
        # Show force on test charge
        force_arrow = Arrow(test_charge.get_center(), test_charge.get_center() + RIGHT*1.5, color=GREEN, stroke_width=6)
        force_label = Text("Force", font_size=20, color=GREEN)
        force_label.next_to(force_arrow, UP)
        
        with self.voiceover(text="Test charge par force lagta hai. Same charges repel karte hain, toh force right direction mein hai."):
            self.play(Create(force_arrow), Write(force_label))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_magnetic_field(self):
        """Show magnetic field visualization"""
        
        # Bar magnet
        magnet = Rectangle(width=3, height=0.8, color=GRAY, fill_opacity=0.8)
        north_pole = Rectangle(width=1.4, height=0.8, color=RED, fill_opacity=0.6)
        south_pole = Rectangle(width=1.4, height=0.8, color=BLUE, fill_opacity=0.6)
        
        north_pole.align_to(magnet, LEFT).shift(RIGHT*0.1)
        south_pole.align_to(magnet, RIGHT).shift(LEFT*0.1)
        
        n_label = Text("N", font_size=32, color=WHITE)
        s_label = Text("S", font_size=32, color=WHITE)
        n_label.move_to(north_pole.get_center())
        s_label.move_to(south_pole.get_center())
        
        with self.voiceover(text="Ab magnetic field dekhte hain. Yeh ek bar magnet hai. North aur South pole hain."):
            self.play(Create(magnet))
            self.play(Create(north_pole), Create(south_pole))
            self.play(Write(n_label), Write(s_label))
        
        # Magnetic field lines
        field_lines = VGroup()
        
        # Create curved field lines from N to S
        for i in range(5):
            y_offset = (i - 2) * 0.5
            
            # External field lines (N to S outside)
            start = north_pole.get_right() + UP * y_offset * 0.5
            end = south_pole.get_left() + UP * y_offset * 0.5
            
            # Create curved path
            control_point = start + RIGHT * 2 + UP * y_offset
            
            field_line = CurvedArrow(start, end, color=GREEN, stroke_width=3)
            field_lines.add(field_line)
        
        with self.voiceover(text="Magnetic field lines North pole se South pole ki taraf jaate hain. Yeh closed loops banate hain."):
            self.play(Create(field_lines))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_electromagnetic_wave(self):
        """Show electromagnetic wave propagation"""
        
        # Wave equations
        title = Text("Electromagnetic Wave", font_size=40, color=GOLD)
        
        with self.voiceover(text="Jab electric aur magnetic fields together oscillate karte hain, toh electromagnetic wave banta hai."):
            self.play(Write(title))
            self.play(title.animate.to_edge(UP))
        
        # Create coordinate system
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1], 
            z_range=[-2, 2, 1],
            x_length=8,
            y_length=4,
            z_length=4
        )
        
        # Electric field (oscillating in y direction)
        e_field_func = lambda t: np.sin(2 * PI * (axes.x_range[0] + t))
        e_field = ParametricFunction(
            lambda t: axes.c2p(t, e_field_func(t), 0),
            t_range=[-4, 4],
            color=RED
        )
        
        # Magnetic field (oscillating in z direction)  
        b_field = ParametricFunction(
            lambda t: axes.c2p(t, 0, e_field_func(t)),
            t_range=[-4, 4],
            color=BLUE
        )
        
        # Labels
        e_label = Text("Electric Field", font_size=24, color=RED)
        b_label = Text("Magnetic Field", font_size=24, color=BLUE)
        
        e_label.to_edge(LEFT).shift(UP*2)
        b_label.to_edge(LEFT).shift(UP*1)
        
        with self.voiceover(text="Red line electric field hai, blue line magnetic field hai. Dono perpendicular hain aur wave ki tarah propagate karte hain."):
            self.play(Create(axes))
            self.play(Create(e_field), Write(e_label))
            self.play(Create(b_field), Write(b_label))
        
        # Show wave propagation
        with self.voiceover(text="Yeh wave light ki speed se travel karta hai. 3 lakh kilometer per second!"):
            # Animate wave propagation
            for i in range(3):
                self.play(
                    e_field.animate.shift(RIGHT*0.5),
                    b_field.animate.shift(RIGHT*0.5),
                    run_time=0.5
                )
        
        # Examples
        examples = Text("Examples: Light, Radio waves, X-rays", font_size=28, color=YELLOW)
        examples.to_edge(DOWN)
        
        with self.voiceover(text="Electromagnetic waves ki examples hain light, radio waves, X-rays. Sab same principle par kaam karte hain."):
            self.play(Write(examples))
        
        self.wait(3)

# Custom TTS Service for Manim Voiceover integration
class HinglishTTSService:
    """Custom TTS service for manim-voiceover integration"""
    
    def __init__(self, quality: TTSQuality, subject: SubjectVoice):
        self.quality = quality
        self.subject = subject
        self.tts_manager = tts_manager
    
    def generate_from_text(self, text: str, cache_dir: str = None, path: str = None, **kwargs):
        """Generate audio from text for manim-voiceover"""
        import tempfile
        import os
        
        if not path:
            # Create temporary file
            temp_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
            path = temp_file.name
            temp_file.close()
        
        # Synthesize speech
        success = self.tts_manager.synthesize_speech(
            text=text,
            output_path=path,
            quality=self.quality,
            subject=self.subject,
            use_cache=True
        )
        
        if success and os.path.exists(path):
            return path
        else:
            raise Exception(f"Failed to synthesize speech: {text[:50]}...")
