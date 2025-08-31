"""
Simplified Hinglish Manim Animation System
Based on the streamlined architecture: Manim Community + Manim Voiceover + gTTS

This is the recommended approach for creating educational animations with Hinglish narration.
Much simpler than the comprehensive system in other files.
"""

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class HinglishEducationScene(VoiceoverScene):
    """
    Base scene for Hinglish educational content using the simplified architecture.
    Uses gTTS for reliable, free TTS with automatic audio-animation synchronization.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Setup gTTS for Hindi with Latin script Hinglish
        self.set_speech_service(GTTSService(lang="hi"))

class NewtonsLawDemo(HinglishEducationScene):
    """
    Example scene demonstrating Newton's Second Law
    Shows the simplified workflow: narration -> animation sync via tracker.duration
    """
    
    def construct(self):
        # Title and introduction
        title = Text("Newton का Second Law", font_size=48, color=BLUE)
        
        with self.voiceover(text="Namaskar! Aaj hum Newton ke second law ke baare mein sikhenge. Force equals mass times acceleration.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.play(title.animate.to_edge(UP))
        
        # Show the equation
        equation = MathTex(r"F = ma", font_size=72, color=YELLOW)
        
        with self.voiceover(text="Yeh hai Newton ka second law ka mathematical form. F matlab Force, m matlab mass, a matlab acceleration.") as tracker:
            self.play(Write(equation), run_time=tracker.duration)
        
        # Visual demonstration
        self.play(equation.animate.to_edge(LEFT))
        
        # Create two objects with different masses
        small_box = Square(side_length=1, color=RED, fill_opacity=0.7)
        large_box = Square(side_length=2, color=BLUE, fill_opacity=0.7)
        
        small_box.to_edge(RIGHT).shift(UP*2)
        large_box.to_edge(RIGHT).shift(DOWN*2)
        
        # Mass labels
        m1_label = Text("m = 1 kg", font_size=24).next_to(small_box, UP)
        m2_label = Text("m = 4 kg", font_size=24).next_to(large_box, UP)
        
        with self.voiceover(text="Dekho, yahan do objects hain. Chhota box ka mass 1 kg hai, bada box ka mass 4 kg hai.") as tracker:
            self.play(
                Create(small_box),
                Create(large_box),
                Write(m1_label),
                Write(m2_label),
                run_time=tracker.duration
            )
        
        # Apply same force
        force_arrow1 = Arrow(start=LEFT*2, end=RIGHT*1, color=GREEN, stroke_width=8)
        force_arrow2 = Arrow(start=LEFT*2, end=RIGHT*1, color=GREEN, stroke_width=8)
        
        force_arrow1.next_to(small_box, LEFT)
        force_arrow2.next_to(large_box, LEFT)
        
        force_label = Text("Same Force = 10 N", font_size=24, color=GREEN)
        force_label.next_to(equation, DOWN, buff=1)
        
        with self.voiceover(text="Ab main same force apply karunga dono objects par. 10 Newton ka force.") as tracker:
            self.play(
                Create(force_arrow1),
                Create(force_arrow2), 
                Write(force_label),
                run_time=tracker.duration
            )
        
        # Show different accelerations
        with self.voiceover(text="Dekho kya hota hai! Chhota box zyada fast move karta hai kyunki uska mass kam hai.") as tracker:
            # Small box accelerates more
            self.play(
                small_box.animate.shift(RIGHT*3),
                m1_label.animate.shift(RIGHT*3),
                force_arrow1.animate.shift(RIGHT*3),
                run_time=tracker.duration*0.3
            )
            
            # Large box accelerates less
            self.play(
                large_box.animate.shift(RIGHT*1.5),
                m2_label.animate.shift(RIGHT*1.5),
                force_arrow2.animate.shift(RIGHT*1.5),
                run_time=tracker.duration*0.7
            )
        
        # Show calculations
        calc1 = MathTex(r"a_1 = \frac{10}{1} = 10 \text{ m/s}^2", font_size=32, color=RED)
        calc2 = MathTex(r"a_2 = \frac{10}{4} = 2.5 \text{ m/s}^2", font_size=32, color=BLUE)
        
        calculations = VGroup(calc1, calc2)
        calculations.arrange(DOWN, buff=0.5)
        calculations.next_to(force_label, DOWN, buff=1)
        
        with self.voiceover(text="Calculation dekho. Chhote box ka acceleration 10 meter per second square hai. Bade box ka sirf 2.5 meter per second square.") as tracker:
            self.play(Write(calculations), run_time=tracker.duration)
        
        # Conclusion
        conclusion = Text("Same Force, Different Mass → Different Acceleration!", 
                         font_size=32, color=GOLD)
        conclusion.to_edge(DOWN)
        
        with self.voiceover(text="Conclusion: Same force, different mass, toh different acceleration milta hai. Yahi hai Newton ka second law!") as tracker:
            self.play(Write(conclusion), run_time=tracker.duration)
        
        self.wait(2)

class WaterMoleculeDemo(HinglishEducationScene):
    """
    Example chemistry scene showing water molecule structure
    """
    
    def construct(self):
        # Title
        title = Text("Water Molecule - H₂O", font_size=48, color=BLUE)
        
        with self.voiceover(text="Ab chemistry mein water molecule dekhte hain. H2O ka structure bahut interesting hai.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.play(title.animate.to_edge(UP))
        
        # Create atoms
        oxygen = Circle(radius=0.8, color=RED, fill_opacity=0.8)
        hydrogen1 = Circle(radius=0.4, color=WHITE, fill_opacity=0.8)
        hydrogen2 = Circle(radius=0.4, color=WHITE, fill_opacity=0.8)
        
        # Position atoms
        oxygen.move_to(ORIGIN)
        hydrogen1.move_to(LEFT * 1.5 + UP * 0.8)
        hydrogen2.move_to(RIGHT * 1.5 + UP * 0.8)
        
        # Atom labels
        o_label = Text("O", font_size=32, color=WHITE, weight=BOLD)
        h1_label = Text("H", font_size=24, color=BLACK, weight=BOLD)
        h2_label = Text("H", font_size=24, color=BLACK, weight=BOLD)
        
        o_label.move_to(oxygen.get_center())
        h1_label.move_to(hydrogen1.get_center())
        h2_label.move_to(hydrogen2.get_center())
        
        with self.voiceover(text="Water molecule mein teen atoms hain. Ek oxygen atom aur do hydrogen atoms.") as tracker:
            self.play(
                Create(oxygen), Write(o_label),
                Create(hydrogen1), Write(h1_label),
                Create(hydrogen2), Write(h2_label),
                run_time=tracker.duration
            )
        
        # Covalent bonds
        bond1 = Line(oxygen.get_center(), hydrogen1.get_center(), color=YELLOW, stroke_width=8)
        bond2 = Line(oxygen.get_center(), hydrogen2.get_center(), color=YELLOW, stroke_width=8)
        
        with self.voiceover(text="Oxygen aur hydrogen atoms covalent bonds se jude hain. Electrons share karte hain.") as tracker:
            self.play(Create(bond1), Create(bond2), run_time=tracker.duration)
        
        # Show bond angle
        angle_arc = Arc(
            radius=1,
            start_angle=np.pi*0.75,
            angle=np.pi*0.5,
            color=ORANGE,
            stroke_width=6
        )
        angle_arc.move_arc_center_to(oxygen.get_center())
        
        angle_label = Text("104.5°", font_size=28, color=ORANGE)
        angle_label.next_to(angle_arc, UP)
        
        with self.voiceover(text="Bond angle 104.5 degrees hai. Yeh perfect tetrahedral angle nahi hai kyunki lone pairs repulsion karte hain.") as tracker:
            self.play(Create(angle_arc), Write(angle_label), run_time=tracker.duration)
        
        # Show polarity
        charges = VGroup(
            Text("δ⁻", font_size=32, color=RED).next_to(oxygen, DOWN),
            Text("δ⁺", font_size=24, color=BLUE).next_to(hydrogen1, UP),
            Text("δ⁺", font_size=24, color=BLUE).next_to(hydrogen2, UP)
        )
        
        with self.voiceover(text="Water molecule polar hai. Oxygen par partial negative charge, hydrogen par partial positive charge.") as tracker:
            self.play(Write(charges), run_time=tracker.duration)
        
        # Properties
        properties = VGroup(
            Text("Properties of Water:", font_size=28, color=GOLD),
            Text("• High boiling point", font_size=20),
            Text("• Dissolves ionic compounds", font_size=20),
            Text("• Hydrogen bonding", font_size=20),
            Text("• Essential for life", font_size=20)
        )
        properties.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        properties.to_edge(RIGHT)
        
        with self.voiceover(text="Water ke kayi unique properties hain. High boiling point, ionic compounds dissolve karta hai, hydrogen bonding, aur life ke liye essential hai.") as tracker:
            self.play(Write(properties), run_time=tracker.duration)
        
        self.wait(2)

class CellMembraneDemo(HinglishEducationScene):
    """
    Example biology scene showing cell membrane structure
    """
    
    def construct(self):
        title = Text("Cell Membrane Structure", font_size=48, color=GREEN)
        
        with self.voiceover(text="Biology mein cell membrane dekhte hain. Yeh cell ki boundary hai aur selective permeability provide karta hai.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.play(title.animate.to_edge(UP))
        
        # Phospholipid bilayer
        # Top layer
        top_heads = VGroup()
        top_tails = VGroup()
        
        for i in range(8):
            x_pos = i * 1.2 - 4.2
            
            # Hydrophilic head
            head = Circle(radius=0.15, color=BLUE, fill_opacity=0.8)
            head.move_to([x_pos, 1, 0])
            top_heads.add(head)
            
            # Hydrophobic tails
            tail1 = Line([x_pos - 0.05, 0.85, 0], [x_pos - 0.05, 0.2, 0], color=YELLOW, stroke_width=4)
            tail2 = Line([x_pos + 0.05, 0.85, 0], [x_pos + 0.05, 0.2, 0], color=YELLOW, stroke_width=4)
            top_tails.add(VGroup(tail1, tail2))
        
        # Bottom layer (flipped)
        bottom_heads = VGroup()
        bottom_tails = VGroup()
        
        for i in range(8):
            x_pos = i * 1.2 - 4.2
            
            head = Circle(radius=0.15, color=BLUE, fill_opacity=0.8)
            head.move_to([x_pos, -1, 0])
            bottom_heads.add(head)
            
            tail1 = Line([x_pos - 0.05, -0.85, 0], [x_pos - 0.05, -0.2, 0], color=YELLOW, stroke_width=4)
            tail2 = Line([x_pos + 0.05, -0.85, 0], [x_pos + 0.05, -0.2, 0], color=YELLOW, stroke_width=4)
            bottom_tails.add(VGroup(tail1, tail2))
        
        bilayer = VGroup(top_heads, top_tails, bottom_heads, bottom_tails)
        
        with self.voiceover(text="Cell membrane phospholipid bilayer se bana hai. Blue circles hydrophilic heads hain, yellow lines hydrophobic tails hain.") as tracker:
            self.play(Create(bilayer), run_time=tracker.duration)
        
        # Labels
        labels = VGroup(
            Text("Hydrophilic Head", font_size=18, color=BLUE).to_edge(LEFT).shift(UP*2),
            Text("(Water-loving)", font_size=14, color=BLUE).to_edge(LEFT).shift(UP*1.5),
            Text("Hydrophobic Tail", font_size=18, color=YELLOW).to_edge(LEFT).shift(UP*0.5),
            Text("(Water-fearing)", font_size=14, color=YELLOW).to_edge(LEFT)
        )
        
        with self.voiceover(text="Hydrophilic heads water ko attract karte hain, hydrophobic tails water se repel karte hain.") as tracker:
            self.play(Write(labels), run_time=tracker.duration)
        
        # Show membrane proteins
        # Channel protein
        channel = Rectangle(width=0.3, height=2.2, color=RED, fill_opacity=0.8)
        channel_hole = Rectangle(width=0.1, height=2, color=BLACK, fill_opacity=1)
        channel.move_to([2, 0, 0])
        channel_hole.move_to([2, 0, 0])
        
        # Integral protein
        integral = Ellipse(width=0.8, height=2.2, color=PURPLE, fill_opacity=0.8)
        integral.move_to([-2, 0, 0])
        
        proteins = VGroup(channel, channel_hole, integral)
        
        with self.voiceover(text="Membrane mein proteins bhi embedded hote hain. Red channel protein, purple integral protein.") as tracker:
            self.play(Create(proteins), run_time=tracker.duration)
        
        # Functions
        functions = VGroup(
            Text("Membrane Functions:", font_size=24, color=GOLD),
            Text("• Selective permeability", font_size=18),
            Text("• Cell recognition", font_size=18),
            Text("• Transport regulation", font_size=18),
            Text("• Maintains cell shape", font_size=18)
        )
        functions.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        functions.to_edge(RIGHT)
        
        with self.voiceover(text="Cell membrane ke main functions hain selective permeability, cell recognition, transport regulation, aur cell shape maintain karna.") as tracker:
            self.play(Write(functions), run_time=tracker.duration)
        
        self.wait(2)

# Gemini Integration Helper
def create_gemini_prompt_template():
    """
    Returns the streamlined Gemini prompt for generating Manim animations
    """
    return '''
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
'''

if __name__ == "__main__":
    # Example usage - render one of the demo scenes
    print("Simplified Hinglish Manim System")
    print("================================")
    print("\nAvailable demo scenes:")
    print("1. NewtonsLawDemo - Physics demonstration")
    print("2. WaterMoleculeDemo - Chemistry demonstration") 
    print("3. CellMembraneDemo - Biology demonstration")
    print("\nTo render a scene, use:")
    print("manim simple_hinglish_manim.py NewtonsLawDemo")
    print("\nFor Gemini integration, use the prompt template:")
    print(create_gemini_prompt_template())
