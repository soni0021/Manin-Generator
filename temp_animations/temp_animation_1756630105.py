from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
class GeneratedAnimation(VoiceoverScene):
def construct(self):
# Setup TTS (REQUIRED)
self.set_speech_service(GTTSService(lang="hi", tld="co.in"))
# Define color scheme (REQUIRED - USE THESE EXACT NAMES)
self.PRIMARY_COLOR = Color("#3498db") # Manim's BLUE is a bit different
self.SECONDARY_COLOR = GREEN
self.ACCENT_COLOR = ORANGE
self.TEXT_COLOR = WHITE
self.BG_COLOR = Color("#2c3e50") # Dark Gray
self.WARNING_COLOR = RED
# Set background color
self.camera.background_color = self.BG_COLOR
# Scene progression
self.intro_scene()
self.main_content()
self.conclusion()
def intro_scene(self):
# Introduction with title
title = Text(
"Catalyst and Chemical Equilibrium",
font_size=48,
color=self.PRIMARY_COLOR,
weight=BOLD
).to_edge(UP, buff=1)
with self.voiceover(text="Namaskar! Aaj hum samjhenge catalysts aur chemical equilibrium ke beech ka important relation.") as tracker:
self.play(Write(title), run_time=tracker.duration)
self.play(FadeOut(title))
self.wait(0.5)
def main_content(self):
# --- BEAT 2: Visualizing Equilibrium ---
reaction_text = Text("Reactants <=> Products", font_size=36, color=self.TEXT_COLOR).to_edge(UP, buff=1.5)
# Create a balance scale
base = Line(LEFT, RIGHT).scale(0.5).shift(DOWN*2)
fulcrum = Triangle().scale(0.3).next_to(base, UP, buff=0)
beam = Line(LEFT*2.5, RIGHT*2.5).next_to(fulcrum, UP, buff=0)
pan_left = VGroup(
Line(beam.get_start(), beam.get_start() + DOWN),
Circle(radius=0.5).next_to(beam.get_start() + DOWN, DOWN, buff=0)
)
pan_right = VGroup(
Line(beam.get_end(), beam.get_end() + DOWN),
Circle(radius=0.5).next_to(beam.get_end() + DOWN, DOWN, buff=0)
)
scale = VGroup(base, fulcrum, beam, pan_left, pan_right).center().shift(DOWN*0.5)
equilibrium_label = Text("Equilibrium", font_size=32, color=self.SECONDARY_COLOR).next_to(scale, UP, buff=0.5)
with self.voiceover(text="Ek reversible reaction mein, jab forward aur backward reaction ka rate same ho jaata hai, system equilibrium achieve kar leta hai. Yeh ek perfect balance jaisa hai.") as tracker:
self.play(Write(reaction_text), run_time=1.5)
self.play(Create(scale), run_time=2)
self.play(
Rotate(beam, angle=PI/12, about_point=fulcrum.get_top(), rate_func=rate_functions.wiggle),
run_time=tracker.duration - 3.5
)
self.play(Write(equilibrium_label))
self.play(FadeOut(equilibrium_label))
self.wait(0.5)
# --- BEAT 3-5: Statement I Analysis ---
statement1_title = Text("Statement I", font_size=36, color=self.TEXT_COLOR, weight=BOLD).to_corner(UL).shift(RIGHT)
statement1_text = Text(
"A catalyst cannot alter the equilibrium\nconstant of the reaction.",
font_size=28,
color=self.TEXT_COLOR
).next_to(statement1_title, DOWN, align=LEFT, buff=0.5)
statement1_group = VGroup(statement1_title, statement1_text)
with self.voiceover(text="Ab dekhte hain Statement I. Yeh kehta hai ki ek catalyst, constant temperature par, equilibrium constant ko nahi badal sakta.") as tracker:
self.play(FadeIn(statement1_group), run_time=tracker.duration)
catalyst = VGroup(
Star(n=6, color=self.ACCENT_COLOR, fill_opacity=1),
Circle(radius=0.2, color=self.BG_COLOR, fill_opacity=1)
).scale(0.5).next_to(reaction_text[10], UP, buff=0.2)
forward_arrow = Arrow(LEFT, RIGHT, color=self.ACCENT_COLOR).scale(0.5).next_to(reaction_text[10], DOWN, buff=0.2)
backward_arrow = Arrow(RIGHT, LEFT, color=self.ACCENT_COLOR).scale(0.5).next_to(forward_arrow, DOWN, buff=0.1)
with self.voiceover(text="Yeh bilkul sahi hai. Catalyst forward aur backward, dono reactions ko equally speed up karta hai. Isliye, system ka balance yaani equilibrium constant change nahi hota.") as tracker:
self.play(FadeIn(catalyst, scale=0.5), run_time=1)
self.play(
AnimationGroup(
GrowArrow(forward_arrow),
GrowArrow(backward_arrow)
),
run_time=tracker.duration - 2
)
self.play(Indicate(scale, scale_factor=1.05, color=self.TEXT_COLOR), run_time=1)
correct_mark = Text("✓", font_size=48, color=self.SECONDARY_COLOR)
correct_text = Text("Correct", font_size=32, color=self.SECONDARY_COLOR)
correct_group = VGroup(correct_mark, correct_text).arrange(RIGHT, buff=0.3).next_to(statement1_group, DOWN, buff=0.5, align=LEFT)
with self.voiceover(text="Iska matlab, equilibrium constant (Kc) ki value same rehti hai. Toh Statement I ekdum correct hai.") as tracker:
self.play(Write(correct_group), run_time=tracker.duration)
self.wait(1)
# --- BEAT 6-8: Statement II Analysis ---
self.play(FadeOut(statement1_group, correct_group, catalyst, forward_arrow, backward_arrow))
statement2_title = Text("Statement II", font_size=36, color=self.TEXT_COLOR, weight=BOLD).to_corner(UR).shift(LEFT)
statement2_text = Text(
"A catalyst can change the equilibrium\ncomposition of a system.",
font_size=28,
color=self.TEXT_COLOR
).next_to(statement2_title, DOWN, align=RIGHT, buff=0.5)
statement2_group = VGroup(statement2_title, statement2_text)
with self.voiceover(text="Ab aate hain Statement II par. Yeh kehta hai ki catalyst equilibrium composition ko change kar sakta hai.") as tracker:
self.play(FadeIn(statement2_group), run_time=tracker.duration)
reactant_label = Text("Reactants", font_size=24, color=self.PRIMARY_COLOR).next_to(pan_left, DOWN)
product_label = Text("Products", font_size=24, color=self.PRIMARY_COLOR).next_to(pan_right, DOWN)
with self.voiceover(text="Equilibrium composition ka matlab hai reactants aur products ki final मात्रा. Kyunki dono sides barabar speed se affect hui, unki final ratio change nahi hogi.") as tracker:
self.play(Write(reactant_label), Write(product_label), run_time=2)
self.play(FadeIn(catalyst, scale=0.5), run_time=1)
self.play(Indicate(scale, color=self.TEXT_COLOR, scale_factor=1.05), run_time=tracker.duration - 3)
incorrect_mark = Text("✗", font_size=48, color=self.WARNING_COLOR)
incorrect_text = Text("Incorrect", font_size=32, color=self.WARNING_COLOR)
incorrect_group = VGroup(incorrect_mark, incorrect_text).arrange(RIGHT, buff=0.3).next_to(statement2_group, DOWN, buff=0.5, align=RIGHT)
with self.voiceover(text="System equilibrium tak jaldi zaroor pahunchega, lekin composition wahi rahega. Isliye, Statement II galat hai.") as tracker:
self.play(Write(incorrect_group), run_time=tracker.duration)
self.wait(1)
# Store elements for the final scene
self.statement1_final = statement1_group.copy().add(correct_group.copy())
self.statement2_final = statement2_group.copy().add(incorrect_group.copy())
# Fade out everything before conclusion
self.play(FadeOut(VGroup(reaction_text, scale, reactant_label, product_label, statement2_group, incorrect_group, catalyst)))
def conclusion(self):
# --- BEAT 9: Final Summary ---
final_box = SurroundingRectangle(
VGroup(self.statement1_final, self.statement2_final).arrange(RIGHT, buff=2),
buff=0.5,
color=self.ACCENT_COLOR
)
final_text = Text(
"Final Answer: Statement I is correct but Statement II is incorrect.",
font_size=32,
color=self.TEXT_COLOR
).next_to(final_box, DOWN, buff=0.5)
with self.voiceover(text="Toh humne dekha ki Statement I sahi hai, aur Statement II galat hai. Isliye, sahi jawab hai: Statement I is correct but Statement II is incorrect.") as tracker:
self.play(
FadeIn(self.statement1_final.center().shift(LEFT*3.5)),
FadeIn(self.statement2_final.center().shift(RIGHT*3.5)),
run_time=2
)
self.play(Create(final_box), run_time=1.5)
self.play(Write(final_text), run_time=tracker.duration - 3.5)
self.wait(3)