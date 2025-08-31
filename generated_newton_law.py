from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="hi", tld="co.in"))
        
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = BLUE_C # Using Manim's palette which is close to #3498db
        SECONDARY_COLOR = GREEN_C # Close to #2ecc71
        ACCENT_COLOR = ORANGE # Close to #f39c12
        TEXT_COLOR = WHITE
        
        self.camera.background_color = DARK_GRAY
        
        # Scene progression
        self.intro_scene(PRIMARY_COLOR, ACCENT_COLOR, SECONDARY_COLOR, TEXT_COLOR)
        self.main_content(PRIMARY_COLOR, ACCENT_COLOR, SECONDARY_COLOR, TEXT_COLOR)
        self.conclusion(PRIMARY_COLOR, TEXT_COLOR)
        self.wait(2)
    
    def intro_scene(self, primary_color, accent_color, secondary_color, text_color):
        # Title
        title = Text("Newton's Second Law of Motion", font_size=48, color=text_color)
        
        with self.voiceover(text="Namaskar! Aaj hum Newton's Second Law of Motion samjhenge.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.wait(0.5)
        self.play(FadeOut(title))
        
        # Formula
        formula = Text("F = ma", font_size=60, color=primary_color).to_edge(UP, buff=0.75)
        
        with self.voiceover(text="Iska famous formula hai F = ma.") as tracker:
            self.play(Write(formula), run_time=tracker.duration)
        
        # Define variables
        f_label = Text("Force (bal)", font_size=24, color=text_color).shift(LEFT*3 + DOWN*1)
        m_label = Text("Mass (vajan)", font_size=24, color=text_color).shift(ORIGIN + DOWN*1)
        a_label = Text("Acceleration (gati)", font_size=24, color=text_color).shift(RIGHT*3 + DOWN*1)
        
        with self.voiceover(text="Yahan F ka matlab hai Force, yaani bal.") as tracker:
            self.play(Write(f_label), run_time=tracker.duration)
        
        with self.voiceover(text="m ka matlab hai Mass, yaani object ka vajan.") as tracker:
            self.play(Write(m_label), run_time=tracker.duration)
        
        with self.voiceover(text="Aur a ka matlab hai Acceleration, yaani uski speed badhne ki dar.") as tracker:
            self.play(Write(a_label), run_time=tracker.duration)
        
        self.wait(1)
        self.play(FadeOut(f_label), FadeOut(m_label), FadeOut(a_label))
        
        # Keep formula on screen
        self.formula = formula
    
    def main_content(self, primary_color, accent_color, secondary_color, text_color):
        ground = Line(LEFT * 7, RIGHT * 7, color=GRAY).shift(DOWN * 2)
        self.play(Create(ground))
        
        # --- SCENARIO 1: VARYING FORCE ---
        with self.voiceover(text="Chalo ek example dekhte hain. Maan lo yeh ek block hai jiska mass 'm' hai.") as tracker:
            block1 = Square(side_length=1.0, color=primary_color, fill_opacity=1).move_to(LEFT * 4 + DOWN * 1.5)
            mass_label1 = Text("m", font_size=24, color=text_color).move_to(block1.get_center())
            block_group1 = VGroup(block1, mass_label1)
            self.play(FadeIn(block_group1), run_time=tracker.duration)
        
        with self.voiceover(text="Jab hum ispar thoda sa Force 'F' lagate hain, toh isme thodi si Acceleration 'a' aati hai.") as tracker:
            force1 = Arrow(start=block_group1.get_left() + LEFT*1.5, end=block_group1.get_left(), color=accent_color, buff=0.1)
            force_label1 = Text("F", font_size=24, color=accent_color).next_to(force1, LEFT)
            accel1 = Arrow(start=UP*0.2, end=UP*0.2 + RIGHT*0.8, color=secondary_color).next_to(block_group1, UP, buff=0.2)
            accel_label1 = Text("a", font_size=24, color=secondary_color).next_to(accel1, UP)
            
            self.play(FadeIn(force1), FadeIn(force_label1))
            self.play(
                block_group1.animate.shift(RIGHT * 3),
                Create(accel1),
                FadeIn(accel_label1),
                run_time=tracker.duration - 1
            )
        
        self.wait(1)
        self.play(FadeOut(block_group1), FadeOut(force1), FadeOut(force_label1), FadeOut(accel1), FadeOut(accel_label1))
        
        with self.voiceover(text="Lekin agar hum Force double kar dein, yaani '2F', toh dekho kya hota hai.") as tracker:
            block_group1.move_to(LEFT * 4 + DOWN * 1.5)
            force2 = Arrow(start=block_group1.get_left() + LEFT*2.5, end=block_group1.get_left(), color=accent_color, buff=0.1)
            force_label2 = Text("2F", font_size=24, color=accent_color).next_to(force2, LEFT)
            self.play(FadeIn(block_group1), FadeIn(force2), FadeIn(force_label2), run_time=tracker.duration)
        
        with self.voiceover(text="Acceleration bhi double ho jaati hai! Force zyada, toh acceleration bhi zyada.") as tracker:
            accel2 = Arrow(start=UP*0.2, end=UP*0.2 + RIGHT*1.6, color=secondary_color).next_to(block_group1, UP, buff=0.2)
            accel_label2 = Text("2a", font_size=24, color=secondary_color).next_to(accel2, UP)
            self.play(
                block_group1.animate.shift(RIGHT * 6),
                Create(accel2),
                FadeIn(accel_label2),
                run_time=tracker.duration
            )
        
        self.play(FadeOut(block_group1), FadeOut(force2), FadeOut(force_label2), FadeOut(accel2), FadeOut(accel_label2))
        
        # --- SCENARIO 2: VARYING MASS ---
        with self.voiceover(text="Ab socho, agar hum Force utna hi rakhein, lekin mass double, yaani '2m' kar dein... toh kya hoga?") as tracker:
            block2 = Rectangle(height=1.5, width=1.5, color=primary_color, fill_opacity=1).move_to(LEFT * 4 + DOWN * 1.25)
            mass_label2 = Text("2m", font_size=24, color=text_color).move_to(block2.get_center())
            block_group2 = VGroup(block2, mass_label2)
            force1_new = Arrow(start=block_group2.get_left() + LEFT*1.5, end=block_group2.get_left(), color=accent_color, buff=0.1)
            force_label1_new = Text("F", font_size=24, color=accent_color).next_to(force1_new, LEFT)
            self.play(FadeIn(block_group2), FadeIn(force1_new), FadeIn(force_label1_new), run_time=tracker.duration)
        
        with self.voiceover(text="Dekho, acceleration aadhi ho gayi!") as tracker:
            accel3 = Arrow(start=UP*0.2, end=UP*0.2 + RIGHT*0.4, color=secondary_color).next_to(block_group2, UP, buff=0.2)
            accel_label3 = Text("a/2", font_size=24, color=secondary_color).next_to(accel3, UP)
            self.play(
                block_group2.animate.shift(RIGHT * 1.5),
                Create(accel3),
                FadeIn(accel_label3),
                run_time=tracker.duration
            )
        
        self.play(FadeOut(block_group2), FadeOut(force1_new), FadeOut(force_label1_new), FadeOut(accel3), FadeOut(accel_label3), FadeOut(ground))
    
    def conclusion(self, primary_color, text_color):
        summary1 = Text("More Force -> More Acceleration", font_size=36, color=text_color)
        summary2 = Text("More Mass -> Less Acceleration", font_size=36, color=text_color)
        summary_group = VGroup(summary1, summary2).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        
        with self.voiceover(text="Toh isse saabit hota hai: Force badhne se acceleration badhti hai, aur mass badhne se acceleration kam ho jaati hai.") as tracker:
            self.play(Write(summary_group), run_time=tracker.duration)
        
        with self.voiceover(text="Yeh hi hai Newton's Second Law.") as tracker:
            self.play(
                self.formula.animate.scale(1.2).set_color(GREEN_C),
                Circumscribe(self.formula, color=GREEN_C),
                run_time=tracker.duration
            )
