from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="hi", tld="co.in"))
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = BLUE_C # #3498db
        SECONDARY_COLOR = GREEN_C # #2ecc71
        ACCENT_COLOR = ORANGE # #f39c12
        TEXT_COLOR = WHITE
        WARNING_COLOR = RED_C # #e74c3c
        BACKGROUND_COLOR = "#2c3e50"
        self.camera.background_color = BACKGROUND_COLOR
        # Scene progression
        self.intro_scene(PRIMARY_COLOR, TEXT_COLOR)
        self.main_content(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, WARNING_COLOR)
        self.conclusion(PRIMARY_COLOR, SECONDARY_COLOR, TEXT_COLOR)
    def intro_scene(self, primary_color, text_color):
        title = Text("Effect of Pressure on Equilibrium", font_size=48, color=primary_color)
        narration_text_1 = "Namaskar! Aaj hum samjhenge Le Chatelier's principle, aur dekhenge ki pressure badhane se is chemical equilibrium par kya asar padta hai."
        with self.voiceover(text=narration_text_1) as tracker:
        self.play(Write(title), run_time=2)
        self.play(title.animate.to_edge(UP, buff=0.5), run_time=tracker.duration - 2.5)
        # Using Text for equation to avoid LaTeX
        equation = VGroup(
        Text("2SO", font_size=36, color=text_color),
        Text("2", font_size=24, color=text_color).next_to(Text("2SO"), DOWN, buff=0.05).shift(RIGHT*0.15),
        Text("(g) + O", font_size=36, color=text_color),
        Text("2", font_size=24, color=text_color).next_to(Text("(g) + O"), DOWN, buff=0.05).shift(RIGHT*0.15),
        Text("(g) ", font_size=36, color=text_color),
        Text("⇌", font_size=48, color=text_color),
        Text(" 2SO", font_size=36, color=text_color),
        Text("3", font_size=24, color=text_color).next_to(Text(" 2SO"), DOWN, buff=0.05).shift(RIGHT*0.15),
        Text("(g)", font_size=36, color=text_color),
        ).arrange(RIGHT, buff=0.1).center().shift(UP*1.5)
        self.play(FadeIn(equation))
        self.wait(1)
        self.add(equation) # Add to scene to persist
        self.title = title # Save for later use
        self.equation = equation
    def main_content(self, primary_color, secondary_color, accent_color, text_color, warning_color):
        # Piston and molecules setup
        piston = VGroup(
        Rectangle(width=4, height=3, color=text_color),
        Line(start=LEFT*2, end=RIGHT*2, color=text_color).shift(UP*1.5)
        ).shift(DOWN*1)
        # Initial positions of molecules
        so2 = VGroup(*[Dot(color=primary_color) for _ in range(4)]).arrange_in_grid(2,2, buff=0.5).move_to(piston.get_center()+LEFT)
        o2 = VGroup(*[Dot(color=accent_color) for _ in range(2)]).arrange(DOWN, buff=0.5).next_to(so2, RIGHT)
        so3 = VGroup(*[Dot(color=secondary_color) for _ in range(4)]).arrange_in_grid(2,2, buff=0.5).next_to(o2, RIGHT, buff=0.5)
        molecules = VGroup(so2, o2, so3)
        reactants_moles = Text("Reactant Moles = 3", font_size=24, color=text_color).next_to(self.equation, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        products_moles = Text("Product Moles = 2", font_size=24, color=text_color).next_to(self.equation, DOWN, buff=0.5).to_edge(RIGHT, buff=1)
        narration_text_2 = "Yahan humare paas ek container mein reactants aur products equilibrium mein hain. Dhyan se dekhiye, reactant side par 3 moles of gas hain, aur product side par 2 moles."
        with self.voiceover(text=narration_text_2) as tracker:
        self.play(FadeIn(piston, molecules), run_time=2)
        self.play(Write(reactants_moles), Write(products_moles), run_time=tracker.duration-2)
        # Applying pressure
        pressure_arrow = Arrow(start=UP*2.5, end=piston[1].get_center(), color=accent_color, buff=0.2)
        pressure_text = Text("Pressure x2", font_size=28, color=accent_color).next_to(pressure_arrow, UP)
        narration_text_3 = "Ab sochiye, hum is system par pressure double kar dete hain. Aisa karne par, container ka volume aadha ho jaata hai."
        with self.voiceover(text=narration_text_3) as tracker:
        self.play(GrowArrow(pressure_arrow), Write(pressure_text), run_time=1.5)
        self.play(
        piston[1].animate.shift(DOWN * 1.5),
        piston[0].animate.stretch_to_fit_height(1.5).shift(DOWN*0.75),
        molecules.animate.scale(0.7).move_to(piston.get_center()+DOWN*0.75),
        run_time=tracker.duration - 1.5
        )
        self.play(FadeOut(pressure_arrow, pressure_text))
        # Show options and immediate effect
        options = VGroup(
        Text("(A) Concentration of reactants and products increases.", font_size=24),
        Text("(B) Equilibrium will shift in forward direction.", font_size=24),
        Text("(C) Equilibrium constant increases since concentration of products increases.", font_size=24),
        Text("(D) Equilibrium constant remains unchanged as concentration of reactants and products remain same.", font_size=24)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_edge(DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        conc_text = Text("Concentration = Moles / Volume ↓", font_size=24, color=accent_color).to_edge(LEFT).shift(UP*0.5)
        narration_text_4 = "Jab volume kam hota hai, toh har gas ka concentration badh jaata hai. Isliye, sabhi reactants aur products ka concentration foran hi increase ho jaayega. Is hisaab se, Option A bilkul sahi hai."
        with self.voiceover(text=narration_text_4) as tracker:
        self.play(Write(options), run_time=2)
        self.play(Write(conc_text), run_time=1.5)
        self.highlight_A = SurroundingRectangle(options[0], color=secondary_color, buff=0.1)
        self.play(Create(self.highlight_A), run_time=tracker.duration - 3.5)
        # Le Chatelier's Principle shift
        le_chatelier_text = Text("System counteracts: Shifts to fewer moles", font_size=28, color=accent_color)
        le_chatelier_text.to_edge(UP, buff=0.5).shift(DOWN*1.5) # Position below title
        forward_arrow = Arrow(self.equation[4].get_left(), self.equation[6].get_right(), color=secondary_color, buff=0.1).shift(UP*0.3)
        narration_text_5 = "Lekin, Le Chatelier's principle kehta hai ki system is change ko oppose karega. Pressure kam karne ke liye, equilibrium us direction mein shift hoga jahan gas ke moles kam hain, yaani forward direction mein."
        with self.voiceover(text=narration_text_5) as tracker:
        self.play(FadeOut(conc_text), FadeOut(self.highlight_A))
        self.play(Write(le_chatelier_text), run_time=2.5)
        self.play(
        Transform(so2[0:2], VGroup(*[Dot(color=secondary_color) for _ in range(2)]).move_to(so3.get_center())),
        FadeOut(o2[0]),
        Create(forward_arrow),
        run_time=tracker.duration - 2.5
        )
        self.check_B = Checkmark(color=secondary_color).scale(0.5).next_to(options[1], LEFT)
        self.play(Write(self.check_B))
        # Equilibrium Constant
        k_text = Text("K depends ONLY on Temperature!", font_size=32, color=warning_color)
        k_box = SurroundingRectangle(k_text, color=warning_color, buff=0.2).move_to(piston.get_center()+UP*0.5)
        k_text.move_to(k_box.get_center())
        cross_C = Cross(options[2], color=warning_color)
        cross_D = Cross(options[3], color=warning_color)
        narration_text_6 = "Ek bohot important baat: equilibrium constant 'K' sirf temperature se badalta hai, pressure se nahi. Isliye options C aur D seedhe galat ho jaate hain."
        with self.voiceover(text=narration_text_6) as tracker:
        self.play(FadeOut(piston, molecules, so2, o2, so3, le_chatelier_text, forward_arrow, reactants_moles, products_moles), run_time=1)
        self.play(FadeIn(k_box, k_text), run_time=1.5)
        self.play(Create(cross_C), Create(cross_D), run_time=tracker.duration - 2.5)
        self.play(FadeOut(k_box, k_text))
        self.options = options
        self.crosses = VGroup(cross_C, cross_D)
    def conclusion(self, primary_color, secondary_color, text_color):
        # Final analysis
        explanation = VGroup(
        Text("A: The immediate effect.", font_size=28, color=text_color),
        Text("B: The subsequent shift.", font_size=28, color=text_color)
        ).arrange(DOWN, buff=0.3).center().shift(UP*0.5)
        final_answer = Text("Option (A) is the most accurate answer.", color=secondary_color, font_size=36)
        final_answer.next_to(explanation, DOWN, buff=0.7)
        check_A_large = Checkmark(color=secondary_color).scale(0.8).next_to(self.options[0], LEFT)
        narration_text_7 = "Toh A aur B dono a-sort-of sahi hain, lekin pressure badhane ka sabse pehla aur direct result concentration ka badhna hai. Shift uske baad hota hai. Isliye, Option A sabse accurate answer hai."
        with self.voiceover(text=narration_text_7) as tracker:
        self.play(
        FadeOut(self.equation, self.title, self.crosses, self.check_B),
        self.options[2:].animate.set_opacity(0.3),
        self.options[1].animate.set_opacity(0.5),
        self.options[0].animate.move_to(UP*2).scale(1.1),
        self.options[1].animate.next_to(self.options[0], DOWN, buff=0.5),
        run_time=2
        )
        self.play(Write(check_A_large), run_time=1)
        self.play(Write(final_answer), run_time=tracker.duration-3)
        # Outro
        narration_text_8 = "Umeed hai aapko yeh concept samajh aa gaya hoga. Thank you!"
        with self.voiceover(text=narration_text_8) as tracker:
        self.play(
        FadeOut(self.options, final_answer, check_A_large),
        run_time=1
        )
        outro_text = Text("Concept Clear!", font_size=48, color=primary_color)
        self.play(Write(outro_text), run_time=tracker.duration - 1)
        self.wait(1)