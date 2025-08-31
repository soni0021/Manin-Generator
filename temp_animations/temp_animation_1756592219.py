from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import math
class GeneratedAnimation(VoiceoverScene):
def construct(self):
# Setup TTS (REQUIRED)
self.set_speech_service(GTTSService(lang="hi"))
# Define color scheme (REQUIRED - USE THESE EXACT NAMES)
PRIMARY_COLOR = Color("#3498db")  # Blue
SECONDARY_COLOR = Color("#2ecc71") # Green
ACCENT_COLOR = Color("#f39c12")   # Orange
TEXT_COLOR = WHITE
IMPORTANT_COLOR = Color("#e74c3c") # Red
BACKGROUND_COLOR = Color("#2c3e50")
self.camera.background_color = BACKGROUND_COLOR
# Scene progression
self.intro_scene(PRIMARY_COLOR, TEXT_COLOR)
self.setup_and_transition(PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR)
self.animation_scene(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, IMPORTANT_COLOR)
self.concepts_scene(PRIMARY_COLOR, TEXT_COLOR)
self.conclusion(ACCENT_COLOR, TEXT_COLOR)
self.wait(1)
def intro_scene(self, primary_color, text_color):
title = Text(
"Rolling Sphere on a Rotating Platform",
font_size=48,
color=primary_color
).scale(0.8)
with self.voiceover(text="Namaskar! Aaj hum ek interesting physics problem ko visualize karenge: ek rotating platform par roll karti hui sphere.") as tracker:
self.play(Write(title), run_time=tracker.duration)
self.wait(0.5)
self.play(FadeOut(title))
def setup_and_transition(self, primary_color, accent_color, text_color):
# Side View Elements
platform_line = Line(LEFT*4, RIGHT*4, color=primary_color, stroke_width=6)
sphere_side = Circle(radius=0.7, color=text_color, fill_opacity=0.2).next_to(platform_line, UP, buff=0)
axis = DashedLine(sphere_side.get_center() + UP*1.5, sphere_side.get_center() + DOWN*2.5, color=text_color, dash_length=0.2)
axis_label = Text("O", font_size=24, color=text_color).next_to(axis, DOWN)
side_view_group = VGroup(platform_line, sphere_side, axis, axis_label)
side_view_group.center()
with self.voiceover(text="Imagine kijiye, yeh ek smooth horizontal platform hai, jo is vertical axis 'O' ke around freely ghoom sakta hai.") as tracker:
self.play(FadeIn(side_view_group), run_time=tracker.duration)
force_arrow = Arrow(
start=sphere_side.get_top() + LEFT,
end=sphere_side.get_top(),
color=accent_color,
buff=0
)
force_label = Text("F", font_size=30, color=accent_color).next_to(force_arrow, LEFT)
with self.voiceover(text="Ab, hum is sphere ke theek topmost point par ek constant horizontal force F apply karte hain.") as tracker:
self.play(GrowArrow(force_arrow), Write(force_label), run_time=tracker.duration)
self.wait(1)
side_view_full = VGroup(side_view_group, force_arrow, force_label)
with self.voiceover(text="Is situation ko behtar samajhne ke liye, chaliye ab iska top view dekhte hain.") as tracker:
self.play(FadeOut(side_view_full), run_time=tracker.duration)
self.wait(0.5)
def animation_scene(self, primary_color, secondary_color, accent_color, text_color, important_color):
# Top View Elements
platform = Circle(radius=3, color=primary_color, stroke_width=6)
platform_radius_line = Line(platform.get_center(), platform.get_right(), color=primary_color, stroke_opacity=0.5)
sphere_path_radius = 2.0
sphere_path = Circle(radius=sphere_path_radius, stroke_opacity=0)
sphere = Circle(radius=0.4, color=text_color, fill_color=accent_color, fill_opacity=0.8)
sphere_spin_line = Line(ORIGIN, UP*0.4, color=BLACK).move_to(sphere.get_center())
sphere_group = VGroup(sphere, sphere_spin_line)
platform_group = VGroup(platform, platform_radius_line)
self.play(FadeIn(platform_group), FadeIn(sphere_group.move_to(sphere_path.get_start())))
# Animators
angle = ValueTracker(0)
# The sphere moves faster than the platform rotates, let's say 5x faster
platform_rotation_ratio = -0.2
sphere_spin_ratio = 5.0 # Sphere's own spin
platform_group.add_updater(
lambda m: m.become(VGroup(platform, platform_radius_line)).rotate(
angle.get_value() * platform_rotation_ratio, about_point=platform.get_center()
)
)
sphere_group.add_updater(
lambda m: m.move_to(sphere_path.point_from_proportion((angle.get_value() / TAU) % 1))
)
sphere_spin_line.add_updater(
lambda m: m.move_to(sphere.get_center()).set_angle(angle.get_value() * sphere_spin_ratio)
)
path_trace = TracedPath(sphere.get_center, stroke_color=secondary_color, stroke_width=4, stroke_opacity=0.8)
self.add(path_trace)
with self.voiceover(text="Jaise hi sphere roll karta hai, action-reaction ki vajah se, platform opposite direction mein rotate karne lagta hai.") as tracker:
self.play(angle.animate.set_value(TAU * 0.4), run_time=tracker.duration, rate_func=linear)
# Labels for angular velocities
omega_p_arrow = CurvedArrow(
start_point=platform.get_center() + RIGHT*1.2,
end_point=platform.get_center() + UP*1.2,
angle=-TAU/4,
color=important_color
)
omega_p_label = Text("Ωp", font_size=30, color=important_color).next_to(omega_p_arrow, UR, buff=0.1)
omega_s_arrow = CurvedArrow(
start_point=sphere.get_center() + RIGHT*0.2,
end_point=sphere.get_center() + UP*0.2,
radius=0.2,
angle=-TAU/4,
color=important_color
)
omega_s_label = Text("ωs", font_size=30, color=important_color).next_to(sphere, DOWN, buff=0.5)
with self.voiceover(text="Platform ki angular velocity ko hum Ω_p (Omega-p) se denote karenge, aur sphere ki apni spin ko ω_s (omega-s) se.") as tracker:
self.play(
Create(omega_p_arrow), Write(omega_p_label),
Create(omega_s_arrow), Write(omega_s_label),
run_time=2.0
)
self.play(angle.animate.set_value(TAU * 0.8), run_time=tracker.duration-2.0, rate_func=linear)
# The final angle for one relative rotation is TAU / (1 - platform_rotation_ratio)
final_angle = TAU / (1 - platform_rotation_ratio)
with self.voiceover(text="Hamara goal hai system ki velocities tab nikalna, jab sphere platform ke relative ek poora rotation complete kar le.") as tracker:
self.play(angle.animate.set_value(final_angle), run_time=tracker.duration, rate_func=linear)
checkmark = Checkmark(color=secondary_color).scale(0.5).next_to(sphere, RIGHT)
self.play(Write(checkmark))
self.wait(1)
# Cleanup for next scene
self.play(
FadeOut(platform_group, sphere_group, path_trace, omega_p_arrow, omega_p_label, omega_s_arrow, omega_s_label, checkmark)
)
# Remove updaters to stop animation
platform_group.clear_updaters()
sphere_group.clear_updaters()
sphere_spin_line.clear_updaters()
def concepts_scene(self, primary_color, text_color):
concepts = [
"Work-Energy Theorem",
"Rolling without Slipping",
"Angular Momentum Conservation"
]
concept_mobjects = VGroup()
for concept in concepts:
text = Text(concept, font_size=30, color=text_color)
box = SurroundingRectangle(text, color=primary_color, buff=0.4, corner_radius=0.1)
concept_mobjects.add(VGroup(text, box))
concept_mobjects.arrange(DOWN, buff=0.5).center()
with self.voiceover(text="Is problem ko solve karne ke liye hum teen key concepts ka istemaal karte hain: Work-Energy Theorem, 'rolling without slipping' ki condition, aur Angular Momentum Conservation.") as tracker:
self.play(FadeIn(concept_mobjects, shift=UP), run_time=tracker.duration)
self.wait(1.5)
self.play(FadeOut(concept_mobjects, shift=DOWN))
def conclusion(self, accent_color, text_color):
conclusion_text = Text(
"Thank You for Watching!",
font_size=48,
color=accent_color
)
with self.voiceover(text="Ummid hai is animation se aapko forces aur motion ke is complex interaction ko samajhne mein madad mili hogi. Dhanyavaad!") as tracker:
self.play(Write(conclusion_text), run_time=tracker.duration)