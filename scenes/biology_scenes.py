"""
Biology Scene Classes for Hinglish Educational Content
Specialized Manim scenes for biology concepts with voiceover integration
"""

import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config.tts_config import TTSQuality, SubjectVoice
from utils.voice_manager import tts_manager
from scenes.physics_scenes import HinglishTTSService

class BiologyHinglishScene(VoiceoverScene):
    """Base scene class for biology content with Hinglish voiceover"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject = SubjectVoice.BIOLOGY
        self.tts_quality = TTSQuality.HIGH
        
    def setup_voice(self):
        """Setup TTS service for biology content"""
        self.set_speech_service(HinglishTTSService(
            quality=self.tts_quality,
            subject=self.subject
        ))

class CellMembraneScene(BiologyHinglishScene):
    """Demonstrates cell membrane structure and transport"""
    
    def construct(self):
        self.setup_voice()
        
        # Title
        title = Text("Cell Membrane Structure", font_size=48, color=GREEN)
        subtitle = Text("कोशिका झिल्ली की संरचना", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        with self.voiceover(text="Namaskar! Aaj hum cell membrane ki structure ke baare mein sikhenge."):
            self.play(Write(title))
            self.play(Write(subtitle))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        self.show_phospholipid_bilayer()
        self.show_membrane_proteins()
        self.show_transport_mechanisms()
    
    def show_phospholipid_bilayer(self):
        """Show phospholipid bilayer structure"""
        
        # Create phospholipid molecules
        phospholipids = VGroup()
        
        # Top layer phospholipids
        for i in range(8):
            x_pos = i * 1.5 - 5.25
            
            # Hydrophilic head (circle)
            head = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
            head.move_to([x_pos, 1.5, 0])
            
            # Hydrophobic tails (lines)
            tail1 = Line([x_pos - 0.1, 1.3, 0], [x_pos - 0.1, 0.2, 0], color=YELLOW, stroke_width=6)
            tail2 = Line([x_pos + 0.1, 1.3, 0], [x_pos + 0.1, 0.2, 0], color=YELLOW, stroke_width=6)
            
            phospholipid = VGroup(head, tail1, tail2)
            phospholipids.add(phospholipid)
        
        # Bottom layer phospholipids (flipped)
        for i in range(8):
            x_pos = i * 1.5 - 5.25
            
            # Hydrophilic head
            head = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
            head.move_to([x_pos, -1.5, 0])
            
            # Hydrophobic tails
            tail1 = Line([x_pos - 0.1, -1.3, 0], [x_pos - 0.1, -0.2, 0], color=YELLOW, stroke_width=6)
            tail2 = Line([x_pos + 0.1, -1.3, 0], [x_pos + 0.1, -0.2, 0], color=YELLOW, stroke_width=6)
            
            phospholipid = VGroup(head, tail1, tail2)
            phospholipids.add(phospholipid)
        
        with self.voiceover(text="Cell membrane phospholipid bilayer se bana hai. Dekhiye, blue circles hydrophilic heads hain."):
            self.play(Create(phospholipids))
        
        # Labels
        head_label = Text("Hydrophilic Head", font_size=20, color=BLUE)
        head_label.to_edge(LEFT).shift(UP*2)
        
        tail_label = Text("Hydrophobic Tails", font_size=20, color=YELLOW)
        tail_label.to_edge(LEFT).shift(UP*1)
        
        with self.voiceover(text="Yellow lines hydrophobic tails hain. Heads water ko attract karte hain, tails repel karte hain."):
            self.play(Write(head_label), Write(tail_label))
        
        # Show water environment
        water_molecules = VGroup()
        
        # Water above membrane
        for i in range(6):
            for j in range(2):
                water = Text("H₂O", font_size=16, color=CYAN)
                water.move_to([i*2 - 5, 2.5 + j*0.5, 0])
                water_molecules.add(water)
        
        # Water below membrane
        for i in range(6):
            for j in range(2):
                water = Text("H₂O", font_size=16, color=CYAN)
                water.move_to([i*2 - 5, -2.5 - j*0.5, 0])
                water_molecules.add(water)
        
        with self.voiceover(text="Membrane ke upar aur neeche water molecules hain. Hydrophilic heads water ke saath interact karte hain."):
            self.play(Create(water_molecules))
        
        # Show bilayer arrangement
        bilayer_label = Text("Phospholipid Bilayer", font_size=24, color=WHITE)
        bilayer_label.to_edge(RIGHT).shift(UP*2)
        
        arrangement_text = VGroup(
            Text("• Heads face water", font_size=18, color=BLUE),
            Text("• Tails face each other", font_size=18, color=YELLOW),
            Text("• Forms barrier", font_size=18, color=WHITE)
        )
        arrangement_text.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        arrangement_text.next_to(bilayer_label, DOWN, buff=0.3)
        
        with self.voiceover(text="Yeh arrangement bilayer banata hai. Heads water ki taraf, tails andar ki taraf. Isse selective barrier banta hai."):
            self.play(Write(bilayer_label))
            self.play(Write(arrangement_text))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_membrane_proteins(self):
        """Show different types of membrane proteins"""
        
        # Recreate simplified membrane
        membrane = Rectangle(width=10, height=1.5, color=GRAY, fill_opacity=0.3)
        membrane_label = Text("Cell Membrane", font_size=20, color=WHITE)
        membrane_label.next_to(membrane, UP)
        
        with self.voiceover(text="Ab membrane proteins dekhte hain. Yeh membrane mein embedded hote hain."):
            self.play(Create(membrane), Write(membrane_label))
        
        # Integral proteins (transmembrane)
        integral_protein = Rectangle(width=0.8, height=2, color=RED, fill_opacity=0.8)
        integral_protein.move_to([-3, 0, 0])
        
        integral_label = Text("Integral\nProtein", font_size=16, color=RED)
        integral_label.next_to(integral_protein, DOWN, buff=0.5)
        
        # Peripheral protein
        peripheral_protein = Ellipse(width=1.2, height=0.6, color=ORANGE, fill_opacity=0.8)
        peripheral_protein.move_to([-1, 1.2, 0])
        
        peripheral_label = Text("Peripheral\nProtein", font_size=16, color=ORANGE)
        peripheral_label.next_to(peripheral_protein, UP, buff=0.2)
        
        # Channel protein
        channel_protein = Rectangle(width=0.6, height=2, color=BLUE, fill_opacity=0.8)
        channel_hole = Rectangle(width=0.2, height=1.8, color=BLACK, fill_opacity=1)
        channel_protein.move_to([1, 0, 0])
        channel_hole.move_to([1, 0, 0])
        
        channel_group = VGroup(channel_protein, channel_hole)
        channel_label = Text("Channel\nProtein", font_size=16, color=BLUE)
        channel_label.next_to(channel_group, DOWN, buff=0.5)
        
        # Carrier protein
        carrier_protein = Ellipse(width=1, height=1.8, color=GREEN, fill_opacity=0.8)
        carrier_protein.move_to([3, 0, 0])
        
        carrier_label = Text("Carrier\nProtein", font_size=16, color=GREEN)
        carrier_label.next_to(carrier_protein, DOWN, buff=0.5)
        
        with self.voiceover(text="Integral proteins membrane ke through jaate hain. Peripheral proteins surface par hote hain."):
            self.play(Create(integral_protein), Write(integral_label))
            self.play(Create(peripheral_protein), Write(peripheral_label))
        
        with self.voiceover(text="Channel proteins mein hole hota hai substances ke liye. Carrier proteins shape change karte hain."):
            self.play(Create(channel_group), Write(channel_label))
            self.play(Create(carrier_protein), Write(carrier_label))
        
        # Show protein functions
        functions_title = Text("Protein Functions:", font_size=24, color=GOLD)
        functions_title.to_edge(RIGHT).shift(UP*2)
        
        functions = VGroup(
            Text("• Transport", font_size=18, color=BLUE),
            Text("• Recognition", font_size=18, color=GREEN),
            Text("• Enzymatic", font_size=18, color=RED),
            Text("• Structural", font_size=18, color=ORANGE)
        )
        functions.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        functions.next_to(functions_title, DOWN, buff=0.3)
        
        with self.voiceover(text="Membrane proteins ke kayi functions hain - transport, recognition, enzymatic activity, aur structural support."):
            self.play(Write(functions_title))
            self.play(Write(functions))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_transport_mechanisms(self):
        """Show different transport mechanisms across membrane"""
        
        # Setup membrane
        membrane = Rectangle(width=8, height=1, color=GRAY, fill_opacity=0.5)
        
        # Labels for inside and outside
        outside_label = Text("Outside Cell", font_size=20, color=CYAN)
        outside_label.move_to([0, 2, 0])
        
        inside_label = Text("Inside Cell", font_size=20, color=PINK)
        inside_label.move_to([0, -2, 0])
        
        with self.voiceover(text="Ab dekhte hain membrane transport mechanisms. Substances kaise membrane cross karte hain."):
            self.play(Create(membrane))
            self.play(Write(outside_label), Write(inside_label))
        
        # 1. Simple Diffusion
        self.play(membrane.animate.to_edge(LEFT, buff=2))
        self.play(outside_label.animate.shift(LEFT*2), inside_label.animate.shift(LEFT*2))
        
        # Small molecules
        molecules = VGroup()
        for i in range(3):
            molecule = Circle(radius=0.1, color=YELLOW, fill_opacity=1)
            molecule.move_to([-5, 1.5 - i*0.5, 0])
            molecules.add(molecule)
        
        diffusion_title = Text("Simple Diffusion", font_size=20, color=YELLOW)
        diffusion_title.to_edge(RIGHT).shift(UP*2.5)
        
        with self.voiceover(text="Simple diffusion mein small molecules directly membrane se pass hote hain. High concentration se low concentration."):
            self.play(Write(diffusion_title))
            self.play(Create(molecules))
            
            # Animate molecules passing through
            for molecule in molecules:
                self.play(molecule.animate.move_to([molecule.get_x() + 4, -1.5, 0]), run_time=1)
        
        # 2. Facilitated Diffusion
        self.wait(1)
        self.play(FadeOut(molecules), FadeOut(diffusion_title))
        
        # Channel protein
        channel = Rectangle(width=0.3, height=1.2, color=BLUE, fill_opacity=0.8)
        channel_hole = Rectangle(width=0.1, height=1, color=BLACK, fill_opacity=1)
        channel.move_to([-2, 0, 0])
        channel_hole.move_to([-2, 0, 0])
        
        # Larger molecules
        large_molecules = VGroup()
        for i in range(2):
            molecule = Circle(radius=0.15, color=GREEN, fill_opacity=1)
            molecule.move_to([-3, 1 - i*0.8, 0])
            large_molecules.add(molecule)
        
        facilitated_title = Text("Facilitated Diffusion", font_size=20, color=GREEN)
        facilitated_title.to_edge(RIGHT).shift(UP*2.5)
        
        with self.voiceover(text="Facilitated diffusion mein channel proteins help karte hain. Large molecules ke liye specific channels chahiye."):
            self.play(Create(channel), Create(channel_hole))
            self.play(Write(facilitated_title))
            self.play(Create(large_molecules))
            
            # Animate through channel
            for molecule in large_molecules:
                self.play(molecule.animate.move_to([-2, molecule.get_y(), 0]), run_time=0.5)
                self.play(molecule.animate.move_to([0, -molecule.get_y(), 0]), run_time=0.5)
        
        # 3. Active Transport
        self.wait(1)
        self.play(FadeOut(large_molecules), FadeOut(facilitated_title))
        self.play(FadeOut(channel), FadeOut(channel_hole))
        
        # Pump protein
        pump = Ellipse(width=0.8, height=1.2, color=RED, fill_opacity=0.8)
        pump.move_to([1, 0, 0])
        
        # ATP molecule
        atp = Text("ATP", font_size=16, color=PURPLE)
        atp.move_to([2, 0.8, 0])
        
        # Molecules going against gradient
        active_molecules = VGroup()
        for i in range(2):
            molecule = Circle(radius=0.12, color=PURPLE, fill_opacity=1)
            molecule.move_to([0, -1 + i*0.6, 0])
            active_molecules.add(molecule)
        
        active_title = Text("Active Transport", font_size=20, color=RED)
        active_title.to_edge(RIGHT).shift(UP*2.5)
        
        with self.voiceover(text="Active transport mein energy chahiye. ATP use karke molecules ko high concentration ki taraf pump karte hain."):
            self.play(Create(pump))
            self.play(Write(active_title))
            self.play(Create(atp), Create(active_molecules))
            
            # Show energy consumption and transport
            self.play(atp.animate.move_to(pump.get_center()), run_time=0.5)
            self.play(FadeOut(atp))
            
            for molecule in active_molecules:
                self.play(molecule.animate.move_to([molecule.get_x(), 1.5, 0]), run_time=1)
        
        # Summary
        summary_title = Text("Transport Summary:", font_size=24, color=GOLD)
        summary_title.to_edge(RIGHT).shift(UP*1.5)
        
        summary_points = VGroup(
            Text("• Passive: No energy", font_size=18, color=YELLOW),
            Text("• Facilitated: Proteins help", font_size=18, color=GREEN),
            Text("• Active: ATP required", font_size=18, color=RED)
        )
        summary_points.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        summary_points.next_to(summary_title, DOWN, buff=0.3)
        
        with self.voiceover(text="Summary: Passive transport mein energy nahi chahiye, facilitated mein proteins help karte hain, active mein ATP energy use hoti hai."):
            self.play(Write(summary_title))
            self.play(Write(summary_points))
        
        self.wait(3)
        
        # Conclusion
        conclusion = Text("Cell Membrane = Life's Gateway! 🚪", font_size=36, color=GREEN)
        
        with self.voiceover(text="Cell membrane life ka gateway hai. Yeh control karta hai ki kya andar jaaye aur kya bahar jaaye. Thank you!"):
            self.play(FadeOut(Group(*self.mobjects)))
            self.play(Write(conclusion))
        
        self.wait(2)

class DNAReplicationScene(BiologyHinglishScene):
    """Demonstrates DNA replication process"""
    
    def construct(self):
        self.setup_voice()
        
        title = Text("DNA Replication", font_size=48, color=PURPLE)
        subtitle = Text("डीएनए प्रतिकृति", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        with self.voiceover(text="Aaj hum DNA replication process ke baare mein sikhenge. Yeh bahut important process hai."):
            self.play(Write(title))
            self.play(Write(subtitle))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        self.show_dna_structure()
        self.show_replication_steps()
        self.show_final_result()
    
    def show_dna_structure(self):
        """Show DNA double helix structure"""
        
        # Create DNA strands
        strand1_points = []
        strand2_points = []
        
        for i in range(20):
            t = i * 0.3
            x = np.cos(t) * 1.5
            y = i * 0.3 - 3
            z = np.sin(t) * 0.5
            
            strand1_points.append([x, y, z])
            strand2_points.append([-x, y, -z])
        
        # Create strands as lines
        strand1 = VMobject()
        strand1.set_points_smoothly(strand1_points)
        strand1.set_color(BLUE)
        strand1.set_stroke_width(6)
        
        strand2 = VMobject()
        strand2.set_points_smoothly(strand2_points)
        strand2.set_color(RED)
        strand2.set_stroke_width(6)
        
        # Base pairs
        base_pairs = VGroup()
        base_labels = VGroup()
        
        bases = ["A-T", "T-A", "G-C", "C-G", "A-T", "G-C", "T-A", "C-G"]
        
        for i in range(0, 16, 2):
            # Connect corresponding points
            p1 = strand1_points[i]
            p2 = strand2_points[i]
            
            base_pair = Line(p1, p2, color=YELLOW, stroke_width=3)
            base_pairs.add(base_pair)
            
            # Add base labels
            if i < len(bases) * 2:
                base_label = Text(bases[i//2], font_size=12, color=WHITE)
                base_label.move_to([(p1[0] + p2[0])/2, (p1[1] + p2[1])/2, 0])
                base_labels.add(base_label)
        
        dna_structure = VGroup(strand1, strand2, base_pairs)
        
        with self.voiceover(text="Pehle DNA structure dekhte hain. Double helix mein do strands hain - blue aur red."):
            self.play(Create(strand1), Create(strand2))
            self.play(Create(base_pairs))
        
        with self.voiceover(text="Base pairs complementary hain. A with T, G with C. Yeh Watson-Crick base pairing hai."):
            self.play(Write(base_labels))
        
        # Move to side for replication demo
        with self.voiceover(text="Ab dekhte hain replication kaise hoti hai."):
            self.play(dna_structure.animate.to_edge(LEFT))
            self.play(base_labels.animate.to_edge(LEFT))
        
        self.dna_original = VGroup(dna_structure, base_labels)
        
    def show_replication_steps(self):
        """Show step-by-step replication process"""
        
        # Step 1: Unwinding
        step1_title = Text("Step 1: DNA Unwinding", font_size=24, color=YELLOW)
        step1_title.to_edge(RIGHT).shift(UP*3)
        
        # Show helicase enzyme
        helicase = Ellipse(width=1, height=0.6, color=GREEN, fill_opacity=0.8)
        helicase.move_to([0, 0, 0])
        
        helicase_label = Text("Helicase", font_size=16, color=GREEN)
        helicase_label.next_to(helicase, UP)
        
        with self.voiceover(text="Pehle helicase enzyme DNA strands ko unwind karta hai. Double helix khulta hai."):
            self.play(Write(step1_title))
            self.play(Create(helicase), Write(helicase_label))
        
        # Animate unwinding
        separated_strand1 = Line([-1, -1, 0], [-1, 2, 0], color=BLUE, stroke_width=6)
        separated_strand2 = Line([1, -1, 0], [1, 2, 0], color=RED, stroke_width=6)
        
        with self.voiceover(text="Strands separate ho jaate hain. Replication fork banta hai."):
            self.play(
                Transform(self.dna_original[0][0], separated_strand1),
                Transform(self.dna_original[0][1], separated_strand2),
                FadeOut(self.dna_original[0][2]),
                FadeOut(self.dna_original[1])
            )
        
        # Step 2: Primer addition
        self.wait(1)
        step2_title = Text("Step 2: Primer Addition", font_size=24, color=ORANGE)
        step2_title.move_to(step1_title.get_center())
        
        primers = VGroup()
        primer1 = Rectangle(width=0.3, height=0.2, color=ORANGE, fill_opacity=1)
        primer2 = Rectangle(width=0.3, height=0.2, color=ORANGE, fill_opacity=1)
        
        primer1.move_to([-1, -0.5, 0])
        primer2.move_to([1, -0.5, 0])
        
        primers.add(primer1, primer2)
        
        with self.voiceover(text="RNA primers add kiye jaate hain. DNA polymerase ko starting point chahiye."):
            self.play(Transform(step1_title, step2_title))
            self.play(Create(primers))
        
        # Step 3: DNA synthesis
        self.wait(1)
        step3_title = Text("Step 3: DNA Synthesis", font_size=24, color=CYAN)
        step3_title.move_to(step2_title.get_center())
        
        # DNA polymerase
        polymerase1 = Ellipse(width=0.8, height=0.5, color=PURPLE, fill_opacity=0.8)
        polymerase2 = Ellipse(width=0.8, height=0.5, color=PURPLE, fill_opacity=0.8)
        
        polymerase1.move_to([-1, -0.2, 0])
        polymerase2.move_to([1, -0.2, 0])
        
        pol_label = Text("DNA Polymerase", font_size=14, color=PURPLE)
        pol_label.next_to(polymerase1, RIGHT, buff=0.5)
        
        with self.voiceover(text="DNA polymerase enzyme new strands synthesize karta hai. Leading aur lagging strands bante hain."):
            self.play(Transform(step2_title, step3_title))
            self.play(Create(polymerase1), Create(polymerase2))
            self.play(Write(pol_label))
        
        # Show new strand synthesis
        new_strand1 = Line([-1, -0.5, 0], [-1, 1.5, 0], color=LIGHT_BLUE, stroke_width=4)
        new_strand2 = Line([1, -0.5, 0], [1, 1.5, 0], color=LIGHT_RED, stroke_width=4)
        
        with self.voiceover(text="New complementary strands bante hain. 5 prime se 3 prime direction mein synthesis hoti hai."):
            self.play(Create(new_strand1), Create(new_strand2))
        
        # Show base pairing
        new_bases = VGroup()
        for i in range(4):
            y_pos = -0.3 + i * 0.5
            base1 = Text("T", font_size=12, color=WHITE)
            base2 = Text("A", font_size=12, color=WHITE)
            
            base1.move_to([-0.7, y_pos, 0])
            base2.move_to([0.7, y_pos, 0])
            
            new_bases.add(base1, base2)
        
        with self.voiceover(text="Complementary base pairs form hote hain. A with T, G with C rule follow karta hai."):
            self.play(Write(new_bases))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_final_result(self):
        """Show final replication result"""
        
        # Two identical DNA molecules
        dna1 = VGroup(
            Line([-3, -2, 0], [-3, 2, 0], color=BLUE, stroke_width=6),
            Line([-2.5, -2, 0], [-2.5, 2, 0], color=LIGHT_BLUE, stroke_width=6)
        )
        
        dna2 = VGroup(
            Line([2.5, -2, 0], [2.5, 2, 0], color=RED, stroke_width=6),
            Line([3, -2, 0], [3, 2, 0], color=LIGHT_RED, stroke_width=6)
        )
        
        # Labels
        original_label = Text("Original\nStrand", font_size=18, color=BLUE)
        original_label.next_to(dna1, DOWN)
        
        new_label = Text("New\nStrand", font_size=18, color=LIGHT_BLUE)
        new_label.next_to(dna1, DOWN, buff=1)
        
        dna1_title = Text("DNA Molecule 1", font_size=20, color=WHITE)
        dna1_title.next_to(dna1, UP)
        
        dna2_title = Text("DNA Molecule 2", font_size=20, color=WHITE)
        dna2_title.next_to(dna2, UP)
        
        with self.voiceover(text="Replication complete! Ab do identical DNA molecules hain. Har molecule mein ek original aur ek new strand hai."):
            self.play(Create(dna1), Create(dna2))
            self.play(Write(dna1_title), Write(dna2_title))
            self.play(Write(original_label), Write(new_label))
        
        # Semi-conservative replication
        semiconservative_title = Text("Semi-Conservative Replication", font_size=28, color=GOLD)
        semiconservative_title.to_edge(UP)
        
        explanation = VGroup(
            Text("• Each new DNA has 1 old + 1 new strand", font_size=20),
            Text("• Genetic information preserved", font_size=20),
            Text("• High fidelity process", font_size=20),
            Text("• Essential for cell division", font_size=20)
        )
        explanation.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation.to_edge(DOWN)
        
        with self.voiceover(text="Yeh semi-conservative replication hai. Har new DNA mein ek purana aur ek naya strand hota hai. Genetic information perfectly preserve hoti hai."):
            self.play(Write(semiconservative_title))
            self.play(Write(explanation))
        
        self.wait(3)
        
        # Final message
        final_message = Text("DNA Replication = Life Continues! 🧬", font_size=36, color=PURPLE)
        
        with self.voiceover(text="DNA replication se life continue rehti hai. Cell division mein yeh process essential hai. Thank you for learning!"):
            self.play(FadeOut(Group(*self.mobjects)))
            self.play(Write(final_message))
        
        self.wait(2)
