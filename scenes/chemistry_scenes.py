"""
Chemistry Scene Classes for Hinglish Educational Content
Specialized Manim scenes for chemistry concepts with voiceover integration
"""

import numpy as np
from manim import *
from manim_voiceover import VoiceoverScene

try:
    from manim_chemistry import *
    CHEMISTRY_AVAILABLE = True
except ImportError:
    CHEMISTRY_AVAILABLE = False
    print("manim-chemistry not available. Install with: pip install manim-chemistry")

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config.tts_config import TTSQuality, SubjectVoice
from utils.voice_manager import tts_manager
from scenes.physics_scenes import HinglishTTSService

class ChemistryHinglishScene(VoiceoverScene):
    """Base scene class for chemistry content with Hinglish voiceover"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject = SubjectVoice.CHEMISTRY
        self.tts_quality = TTSQuality.HIGH
        
    def setup_voice(self):
        """Setup TTS service for chemistry content"""
        self.set_speech_service(HinglishTTSService(
            quality=self.tts_quality,
            subject=self.subject
        ))

class WaterMoleculeScene(ChemistryHinglishScene):
    """Demonstrates water molecule structure and properties"""
    
    def construct(self):
        self.setup_voice()
        
        # Title
        title = Text("Water Molecule - H₂O", font_size=48, color=BLUE)
        subtitle = Text("पानी का अणु", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        with self.voiceover(text="Namaskar! Aaj hum water molecule ke structure ke baare mein sikhenge."):
            self.play(Write(title))
            self.play(Write(subtitle))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        self.show_molecular_structure()
        self.show_bond_angles()
        self.show_polarity()
        self.show_hydrogen_bonding()
    
    def show_molecular_structure(self):
        """Show the basic molecular structure of water"""
        
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
        
        with self.voiceover(text="Water molecule mein teen atoms hain. Ek oxygen atom aur do hydrogen atoms."):
            self.play(Create(oxygen), Write(o_label))
            self.play(Create(hydrogen1), Write(h1_label))
            self.play(Create(hydrogen2), Write(h2_label))
        
        # Covalent bonds
        bond1 = Line(oxygen.get_center(), hydrogen1.get_center(), color=YELLOW, stroke_width=8)
        bond2 = Line(oxygen.get_center(), hydrogen2.get_center(), color=YELLOW, stroke_width=8)
        
        with self.voiceover(text="Oxygen aur hydrogen atoms covalent bonds se jude hote hain. Electrons share karte hain."):
            self.play(Create(bond1), Create(bond2))
        
        # Show electron sharing
        electron_pairs = VGroup()
        
        # Bond 1 electrons
        e1_1 = Dot(bond1.point_from_proportion(0.3), color=GREEN, radius=0.08)
        e1_2 = Dot(bond1.point_from_proportion(0.7), color=GREEN, radius=0.08)
        
        # Bond 2 electrons  
        e2_1 = Dot(bond2.point_from_proportion(0.3), color=GREEN, radius=0.08)
        e2_2 = Dot(bond2.point_from_proportion(0.7), color=GREEN, radius=0.08)
        
        electron_pairs.add(e1_1, e1_2, e2_1, e2_2)
        
        with self.voiceover(text="Green dots electrons hain. Yeh shared electrons covalent bond banate hain."):
            self.play(Create(electron_pairs))
        
        # Molecular formula
        formula = Text("H₂O", font_size=48, color=BLUE)
        formula.to_edge(UP)
        
        with self.voiceover(text="Toh water ka molecular formula hai H₂O. Do hydrogen, ek oxygen."):
            self.play(Write(formula))
        
        self.wait(2)
        
        # Group all elements for next transformation
        self.water_molecule = VGroup(oxygen, hydrogen1, hydrogen2, o_label, h1_label, h2_label, bond1, bond2, electron_pairs)
        
    def show_bond_angles(self):
        """Show the bond angle in water molecule"""
        
        with self.voiceover(text="Ab dekhte hain bond angle. Water molecule mein bond angle 104.5 degrees hai."):
            # Move molecule to left side
            self.play(self.water_molecule.animate.to_edge(LEFT))
        
        # Draw angle arc
        oxygen_center = self.water_molecule[0].get_center()  # Oxygen atom
        h1_center = self.water_molecule[1].get_center()     # Hydrogen 1
        h2_center = self.water_molecule[2].get_center()     # Hydrogen 2
        
        # Calculate angle
        vec1 = h1_center - oxygen_center
        vec2 = h2_center - oxygen_center
        
        angle_arc = Arc(
            radius=1,
            start_angle=np.arctan2(vec1[1], vec1[0]),
            angle=np.arctan2(vec2[1], vec2[0]) - np.arctan2(vec1[1], vec1[0]),
            color=ORANGE,
            stroke_width=6
        )
        angle_arc.move_arc_center_to(oxygen_center)
        
        angle_label = Text("104.5°", font_size=28, color=ORANGE)
        angle_label.next_to(angle_arc, RIGHT)
        
        with self.voiceover(text="Yeh angle perfect 109.5 degrees nahi hai kyonki oxygen par lone pairs hain jo repulsion karte hain."):
            self.play(Create(angle_arc), Write(angle_label))
        
        # Show lone pairs on oxygen
        lone_pair1 = VGroup(
            Dot(oxygen_center + UP*0.6 + LEFT*0.2, color=PURPLE, radius=0.06),
            Dot(oxygen_center + UP*0.6 + RIGHT*0.2, color=PURPLE, radius=0.06)
        )
        
        lone_pair2 = VGroup(
            Dot(oxygen_center + DOWN*0.6 + LEFT*0.2, color=PURPLE, radius=0.06),
            Dot(oxygen_center + DOWN*0.6 + RIGHT*0.2, color=PURPLE, radius=0.06)
        )
        
        lone_pairs_label = Text("Lone Pairs", font_size=20, color=PURPLE)
        lone_pairs_label.to_edge(RIGHT).shift(UP*2)
        
        with self.voiceover(text="Purple dots lone pairs hain. Yeh bonding electrons ko push karte hain, isliye angle kam ho jaata hai."):
            self.play(Create(lone_pair1), Create(lone_pair2))
            self.play(Write(lone_pairs_label))
        
        self.wait(2)
        
        # Store for next section
        self.angle_elements = VGroup(angle_arc, angle_label, lone_pair1, lone_pair2, lone_pairs_label)
        
    def show_polarity(self):
        """Show water molecule polarity"""
        
        with self.voiceover(text="Water molecule polar hai. Oxygen zyada electronegative hai, toh electrons oxygen ki taraf attract hote hain."):
            # Clear previous angle elements
            self.play(FadeOut(self.angle_elements))
        
        # Show partial charges
        oxygen_charge = Text("δ⁻", font_size=32, color=RED)
        h1_charge = Text("δ⁺", font_size=24, color=BLUE)
        h2_charge = Text("δ⁺", font_size=24, color=BLUE)
        
        # Position charges
        oxygen_center = self.water_molecule[0].get_center()
        h1_center = self.water_molecule[1].get_center()
        h2_center = self.water_molecule[2].get_center()
        
        oxygen_charge.next_to(oxygen_center, DOWN, buff=0.2)
        h1_charge.next_to(h1_center, UP, buff=0.2)
        h2_charge.next_to(h2_center, UP, buff=0.2)
        
        with self.voiceover(text="Oxygen par partial negative charge aur hydrogen par partial positive charge hota hai."):
            self.play(Write(oxygen_charge))
            self.play(Write(h1_charge), Write(h2_charge))
        
        # Show dipole moment
        dipole_arrow = Arrow(
            start=oxygen_center + DOWN*0.8,
            end=oxygen_center + UP*1.2,
            color=GREEN,
            stroke_width=8
        )
        
        dipole_label = Text("Dipole Moment", font_size=24, color=GREEN)
        dipole_label.next_to(dipole_arrow, RIGHT)
        
        with self.voiceover(text="Isse dipole moment banta hai. Molecule ka ek end positive, doosra negative."):
            self.play(Create(dipole_arrow), Write(dipole_label))
        
        # Explanation box
        explanation = VGroup(
            Rectangle(width=6, height=3, color=WHITE, fill_opacity=0.1),
            Text("Polarity ke fayde:", font_size=24, color=YELLOW),
            Text("• Dissolves ionic compounds", font_size=20),
            Text("• High boiling point", font_size=20), 
            Text("• Surface tension", font_size=20),
            Text("• Hydrogen bonding", font_size=20)
        )
        
        explanation[1].move_to(explanation[0].get_top() + DOWN*0.3)
        for i in range(2, 6):
            explanation[i].next_to(explanation[i-1], DOWN, buff=0.1, aligned_edge=LEFT)
        
        explanation.to_edge(RIGHT)
        
        with self.voiceover(text="Polarity ke kayi fayde hain. Water ionic compounds dissolve kar sakta hai, high boiling point hai, aur hydrogen bonding karta hai."):
            self.play(Create(explanation))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
        
    def show_hydrogen_bonding(self):
        """Show hydrogen bonding between water molecules"""
        
        # Create multiple water molecules
        molecules = VGroup()
        
        for i in range(3):
            for j in range(2):
                # Create water molecule
                o = Circle(radius=0.3, color=RED, fill_opacity=0.8)
                h1 = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
                h2 = Circle(radius=0.15, color=WHITE, fill_opacity=0.8)
                
                # Position atoms
                center = np.array([i*3 - 3, j*2.5 - 1.25, 0])
                o.move_to(center)
                h1.move_to(center + np.array([-0.6, 0.4, 0]))
                h2.move_to(center + np.array([0.6, 0.4, 0]))
                
                # Bonds
                bond1 = Line(o.get_center(), h1.get_center(), color=YELLOW, stroke_width=4)
                bond2 = Line(o.get_center(), h2.get_center(), color=YELLOW, stroke_width=4)
                
                # Charges
                o_charge = Text("δ⁻", font_size=16, color=RED)
                h1_charge = Text("δ⁺", font_size=12, color=BLUE)
                h2_charge = Text("δ⁺", font_size=12, color=BLUE)
                
                o_charge.move_to(o.get_center())
                h1_charge.move_to(h1.get_center())
                h2_charge.move_to(h2.get_center())
                
                molecule = VGroup(o, h1, h2, bond1, bond2, o_charge, h1_charge, h2_charge)
                molecules.add(molecule)
        
        with self.voiceover(text="Jab kayi water molecules paas aate hain, toh hydrogen bonding hoti hai."):
            self.play(Create(molecules))
        
        # Show hydrogen bonds
        h_bonds = VGroup()
        
        # Add dotted lines between molecules to show hydrogen bonds
        for i in range(len(molecules)-1):
            if i % 2 == 0:  # Connect every other molecule
                start_molecule = molecules[i]
                end_molecule = molecules[i+1]
                
                # Get hydrogen from first molecule and oxygen from second
                h_atom = start_molecule[1]  # Hydrogen
                o_atom = end_molecule[0]   # Oxygen
                
                h_bond = DashedLine(
                    h_atom.get_center(),
                    o_atom.get_center(),
                    color=CYAN,
                    stroke_width=4
                )
                h_bonds.add(h_bond)
        
        with self.voiceover(text="Cyan colored dotted lines hydrogen bonds hain. Yeh weak bonds hain lekin bahut important hain."):
            self.play(Create(h_bonds))
        
        # Properties due to hydrogen bonding
        properties_title = Text("Hydrogen Bonding ke Effects:", font_size=32, color=GOLD)
        properties_title.to_edge(UP)
        
        properties = VGroup(
            Text("• High boiling point (100°C)", font_size=24),
            Text("• Ice floats on water", font_size=24),
            Text("• Surface tension", font_size=24),
            Text("• Capillary action", font_size=24)
        )
        
        properties.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        properties.to_edge(RIGHT)
        
        with self.voiceover(text="Hydrogen bonding ke kaaran water ka boiling point high hai, ice water par float karta hai, surface tension hota hai, aur capillary action bhi."):
            self.play(Write(properties_title))
            self.play(Write(properties))
        
        self.wait(3)
        
        # Conclusion
        conclusion = Text("Water = Life! 💧", font_size=48, color=BLUE)
        
        with self.voiceover(text="Yeh sab properties water ko life ke liye essential banati hain. Water hai toh life hai!"):
            self.play(FadeOut(Group(*self.mobjects)))
            self.play(Write(conclusion))
        
        self.wait(2)

class PeriodicTableScene(ChemistryHinglishScene):
    """Demonstrates periodic table trends"""
    
    def construct(self):
        self.setup_voice()
        
        title = Text("Periodic Table Trends", font_size=48, color=PURPLE)
        subtitle = Text("आवर्त सारणी के रुझान", font_size=32, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        with self.voiceover(text="Aaj hum periodic table ke important trends ke baare mein sikhenge."):
            self.play(Write(title))
            self.play(Write(subtitle))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        self.show_atomic_size_trend()
        self.show_ionization_energy_trend()
        self.show_electronegativity_trend()
    
    def show_atomic_size_trend(self):
        """Show atomic size trend across periods and groups"""
        
        # Create simplified periodic table section
        elements = [
            ["Li", "Be", "B", "C", "N", "O", "F"],
            ["Na", "Mg", "Al", "Si", "P", "S", "Cl"],
            ["K", "Ca", "Ga", "Ge", "As", "Se", "Br"]
        ]
        
        atomic_radii = [
            [1.52, 1.12, 0.88, 0.77, 0.70, 0.66, 0.64],
            [1.86, 1.60, 1.43, 1.17, 1.10, 1.04, 0.99],
            [2.27, 1.97, 1.35, 1.22, 1.21, 1.16, 1.14]
        ]
        
        table = VGroup()
        
        with self.voiceover(text="Pehle atomic size ka trend dekhte hain. Yahan periodic table ka ek part hai."):
            for i, row in enumerate(elements):
                for j, element in enumerate(row):
                    # Scale circle based on atomic radius
                    radius = atomic_radii[i][j] * 0.3
                    
                    circle = Circle(radius=radius, color=BLUE, fill_opacity=0.6)
                    label = Text(element, font_size=16, color=WHITE)
                    
                    pos = np.array([j*1.5 - 4.5, -i*1.5 + 1.5, 0])
                    circle.move_to(pos)
                    label.move_to(pos)
                    
                    element_group = VGroup(circle, label)
                    table.add(element_group)
            
            self.play(Create(table))
        
        # Show horizontal trend (across period)
        arrow_horizontal = Arrow(LEFT*4.5, RIGHT*0, color=RED, stroke_width=6)
        arrow_horizontal.shift(UP*1.5)
        
        h_trend_label = Text("Period mein →\nSize decreases", font_size=24, color=RED)
        h_trend_label.next_to(arrow_horizontal, UP)
        
        with self.voiceover(text="Period mein left se right jaane par atomic size decrease hota hai. Nuclear charge badhta hai toh electrons zyada attract hote hain."):
            self.play(Create(arrow_horizontal), Write(h_trend_label))
        
        # Show vertical trend (down group)
        arrow_vertical = Arrow(UP*1.5, DOWN*1.5, color=GREEN, stroke_width=6)
        arrow_vertical.shift(LEFT*4.5)
        
        v_trend_label = Text("Group mein ↓\nSize increases", font_size=24, color=GREEN)
        v_trend_label.next_to(arrow_vertical, LEFT)
        
        with self.voiceover(text="Group mein upar se neeche jaane par atomic size increase hota hai. Electron shells badhte jaate hain."):
            self.play(Create(arrow_vertical), Write(v_trend_label))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_ionization_energy_trend(self):
        """Show ionization energy trend"""
        
        title = Text("Ionization Energy Trend", font_size=36, color=YELLOW)
        definition = Text("Energy needed to remove electron", font_size=24, color=GRAY)
        definition.next_to(title, DOWN)
        
        with self.voiceover(text="Ab ionization energy ka trend dekhte hain. Yeh energy hai jo electron remove karne ke liye chahiye."):
            self.play(Write(title), Write(definition))
        
        # Create energy level diagram
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 25, 5],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE}
        )
        
        axes_labels = axes.get_axis_labels(x_label="Period", y_label="Ionization Energy (eV)")
        
        # Data points for first ionization energies
        elements_period2 = ["Li", "Be", "B", "C", "N", "O", "F", "Ne"]
        ie_values = [5.4, 9.3, 8.3, 11.3, 14.5, 13.6, 17.4, 21.6]
        
        points = VGroup()
        labels = VGroup()
        
        for i, (element, ie) in enumerate(zip(elements_period2, ie_values)):
            point = Dot(axes.c2p(i+1, ie), color=RED, radius=0.08)
            label = Text(element, font_size=16, color=WHITE)
            label.next_to(point, UP, buff=0.1)
            
            points.add(point)
            labels.add(label)
        
        # Connect points with line
        line = axes.plot_line_graph(
            x_values=list(range(1, 9)),
            y_values=ie_values,
            line_color=RED,
            vertex_dot_radius=0.08,
            stroke_width=4
        )
        
        with self.voiceover(text="Period 2 ke elements ka ionization energy trend dekho. Generally increase hota hai left se right."):
            self.play(FadeOut(title), FadeOut(definition))
            self.play(Create(axes), Write(axes_labels))
            self.play(Create(points), Write(labels))
            self.play(Create(line))
        
        # Explain anomalies
        anomaly1_arrow = Arrow(axes.c2p(2.5, 10), axes.c2p(3, 8.3), color=ORANGE)
        anomaly1_label = Text("B < Be\n(subshell effect)", font_size=18, color=ORANGE)
        anomaly1_label.next_to(anomaly1_arrow, UP)
        
        anomaly2_arrow = Arrow(axes.c2p(5.5, 15), axes.c2p(6, 13.6), color=ORANGE)
        anomaly2_label = Text("O < N\n(pairing energy)", font_size=18, color=ORANGE)
        anomaly2_label.next_to(anomaly2_arrow, UP)
        
        with self.voiceover(text="Kuch anomalies bhi hain. Boron ka IE beryllium se kam hai subshell effect ke kaaran. Oxygen ka IE nitrogen se kam hai electron pairing ke kaaran."):
            self.play(Create(anomaly1_arrow), Write(anomaly1_label))
            self.play(Create(anomaly2_arrow), Write(anomaly2_label))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
    
    def show_electronegativity_trend(self):
        """Show electronegativity trend"""
        
        title = Text("Electronegativity Trend", font_size=36, color=CYAN)
        definition = Text("Ability to attract bonding electrons", font_size=24, color=GRAY)
        definition.next_to(title, DOWN)
        
        with self.voiceover(text="Last mein electronegativity trend dekhte hain. Yeh batata hai ki atom electrons ko kitna attract karta hai."):
            self.play(Write(title), Write(definition))
        
        self.wait(1)
        self.play(FadeOut(title), FadeOut(definition))
        
        # Create electronegativity scale
        scale = NumberLine(
            x_range=[0, 4, 0.5],
            length=8,
            color=WHITE,
            include_numbers=True,
            numbers_with_elongated_ticks=[0, 1, 2, 3, 4]
        )
        
        scale_label = Text("Pauling Electronegativity Scale", font_size=24, color=WHITE)
        scale_label.next_to(scale, UP)
        
        # Notable elements on scale
        elements_en = [
            ("F", 4.0, RED),
            ("O", 3.5, ORANGE),
            ("N", 3.0, YELLOW),
            ("C", 2.5, GREEN),
            ("H", 2.1, BLUE),
            ("Li", 1.0, PURPLE),
            ("Cs", 0.7, PINK)
        ]
        
        element_markers = VGroup()
        
        for element, en_value, color in elements_en:
            point = Dot(scale.n2p(en_value), color=color, radius=0.12)
            label = Text(element, font_size=20, color=WHITE)
            label.next_to(point, UP, buff=0.2)
            
            element_markers.add(VGroup(point, label))
        
        with self.voiceover(text="Fluorine sabse zyada electronegative hai, 4.0 value. Cesium sabse kam electronegative hai."):
            self.play(Create(scale), Write(scale_label))
            self.play(Create(element_markers))
        
        # Show trend arrows
        trend_box = Rectangle(width=10, height=4, color=WHITE, fill_opacity=0.1)
        trend_box.to_edge(DOWN)
        
        trend_title = Text("Electronegativity Trends:", font_size=28, color=GOLD)
        trend_title.move_to(trend_box.get_top() + DOWN*0.3)
        
        trend1 = Text("→ Period mein: Left se Right increase", font_size=22, color=RED)
        trend2 = Text("↓ Group mein: Top se Bottom decrease", font_size=22, color=GREEN)
        trend3 = Text("🏆 Fluorine is the winner!", font_size=22, color=CYAN)
        
        trends = VGroup(trend1, trend2, trend3)
        trends.arrange(DOWN, buff=0.3)
        trends.move_to(trend_box.get_center())
        
        with self.voiceover(text="Period mein left se right electronegativity badhti hai. Group mein top se bottom kam hoti hai. Fluorine sabse zyada electronegative element hai."):
            self.play(Create(trend_box))
            self.play(Write(trend_title))
            self.play(Write(trends))
        
        self.wait(3)
        
        # Final summary
        summary = Text("Periodic Trends = Chemistry ki Key! 🔑", font_size=36, color=GOLD)
        
        with self.voiceover(text="Yeh periodic trends chemistry samajhne ki key hain. Inhe yaad rakhiye, chemistry easy ho jaayegi!"):
            self.play(FadeOut(Group(*self.mobjects)))
            self.play(Write(summary))
        
        self.wait(2)
