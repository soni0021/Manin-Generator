from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import math

class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="hi"))
        
        # Define color scheme as class attributes for global access
        self.PRIMARY_COLOR = "#3498db"  # Blue
        self.SECONDARY_COLOR = "#2ecc71" # Green
        self.ACCENT_COLOR = "#f39c12"   # Orange
        self.TEXT_COLOR = WHITE
        self.IMPORTANT_COLOR = "#e74c3c" # Red
        self.BACKGROUND_COLOR = "#2c3e50"
        
        self.camera.background_color = self.BACKGROUND_COLOR
        
        # Optimized scene progression (fewer segments for speed)
        self.intro_and_setup(self.PRIMARY_COLOR, self.ACCENT_COLOR, self.TEXT_COLOR)
        self.main_animation(self.PRIMARY_COLOR, self.SECONDARY_COLOR, self.ACCENT_COLOR, self.TEXT_COLOR, self.IMPORTANT_COLOR)
        self.conclusion(self.ACCENT_COLOR, self.TEXT_COLOR)
        self.wait(1)
    
    def intro_and_setup(self, primary_color, accent_color, text_color):
        # Combined intro and setup for faster rendering
        title = Text("Rolling Sphere on Rotating Platform", font_size=42, color=primary_color)
        
        with self.voiceover(text="Namaskar! Aaj hum ek complex physics problem dekhenge - rotating platform par rolling sphere ka motion.") as tracker:
            self.play(Write(title), run_time=tracker.duration)
        
        self.play(title.animate.to_edge(UP, buff=0.5))
        
        # Quick setup view
        platform_line = Line(LEFT*3.5, RIGHT*3.5, color=primary_color, stroke_width=8)
        sphere_side = Circle(radius=0.6, color=text_color, fill_opacity=0.3, stroke_width=4)
        sphere_side.next_to(platform_line, UP, buff=0)
        
        # Force arrow
        force_arrow = Arrow(
            start=sphere_side.get_top() + LEFT*0.8,
            end=sphere_side.get_top(),
            color=accent_color,
            stroke_width=6
        )
        force_label = Text("F", font_size=28, color=accent_color).next_to(force_arrow, LEFT)
        
        setup_group = VGroup(platform_line, sphere_side, force_arrow, force_label)
        setup_group.shift(DOWN*0.5)
        
        with self.voiceover(text="Sphere par constant horizontal force F lagaaya jaata hai. Platform freely rotate kar sakta hai.") as tracker:
            self.play(Create(setup_group), run_time=tracker.duration)
        
        # Quick transition to top view
        with self.voiceover(text="Ab top view mein dekhte hain kya hota hai.") as tracker:
            self.play(FadeOut(setup_group), run_time=tracker.duration)
    
    def main_animation(self, primary_color, secondary_color, accent_color, text_color, important_color):
        # Top view - optimized animation
        platform = Circle(radius=2.8, color=primary_color, stroke_width=6)
        platform_center = Dot(platform.get_center(), color=primary_color, radius=0.08)
        
        # Sphere with visual indicators
        sphere_radius = 0.35
        sphere = Circle(radius=sphere_radius, color=text_color, fill_color=accent_color, fill_opacity=0.7, stroke_width=3)
        sphere_center = Dot(color=important_color, radius=0.06)
        
        # Initial position
        initial_pos = platform.get_center() + RIGHT*2.2
        sphere.move_to(initial_pos)
        sphere_center.move_to(initial_pos)
        
        # Create sphere group
        sphere_group = VGroup(sphere, sphere_center)
        
        with self.voiceover(text="Platform aur sphere ka top view. Orange sphere blue platform par roll karta hai.") as tracker:
            self.play(Create(platform), Create(platform_center), Create(sphere_group), run_time=tracker.duration)
        
        # Rotation indicators
        platform_rotation_arrow = CurvedArrow(
            start_point=platform.get_center() + RIGHT*1.2,
            end_point=platform.get_center() + UP*1.2,
            angle=-PI/2,
            color=important_color,
            stroke_width=4
        )
        platform_label = Text("Ωp", font_size=24, color=important_color).next_to(platform_rotation_arrow, UR, buff=0.1)
        
        sphere_rotation_arrow = CurvedArrow(
            start_point=sphere.get_center() + RIGHT*0.15,
            end_point=sphere.get_center() + UP*0.15,
            radius=0.15,
            angle=-PI/2,
            color=secondary_color,
            stroke_width=3
        )
        sphere_label = Text("ωs", font_size=20, color=secondary_color).next_to(sphere, DOWN, buff=0.3)
        
        # Path tracer for sphere motion
        path_trace = TracedPath(sphere.get_center, stroke_color=secondary_color, stroke_width=3, stroke_opacity=0.8)
        self.add(path_trace)
        
        # Animation parameters
        angle = ValueTracker(0)
        platform_rotation_ratio = -0.15  # Platform rotates slower, opposite direction
        sphere_orbital_speed = 1.0
        sphere_spin_speed = 4.0
        
        # Updaters for smooth animation
        def update_platform(mob):
            mob.rotate(angle.get_value() * platform_rotation_ratio * 0.1, about_point=platform.get_center())
        
        def update_sphere_position(mob):
            # Sphere moves in circular path
            orbital_angle = angle.get_value() * sphere_orbital_speed
            new_pos = platform.get_center() + 2.2 * np.array([np.cos(orbital_angle), np.sin(orbital_angle), 0])
            mob.move_to(new_pos)
        
        def update_sphere_spin(mob):
            # Sphere spins on its own axis
            mob.rotate(angle.get_value() * sphere_spin_speed * 0.1)
        
        platform.add_updater(update_platform)
        sphere_group.add_updater(update_sphere_position)
        sphere_center.add_updater(update_sphere_spin)
        
        with self.voiceover(text="Jab force lagti hai, sphere roll karta hai aur platform opposite direction mein rotate hota hai. Action-reaction principle!") as tracker:
            self.play(
                Create(platform_rotation_arrow), Write(platform_label),
                Create(sphere_rotation_arrow), Write(sphere_label),
                run_time=tracker.duration*0.3
            )
            self.play(angle.animate.set_value(8), run_time=tracker.duration*0.7, rate_func=linear)
        
        # Show the complex motion pattern
        with self.voiceover(text="Dekho kitna beautiful pattern banta hai! Sphere ka relative motion cycloid curve banata hai.") as tracker:
            self.play(angle.animate.set_value(16), run_time=tracker.duration, rate_func=linear)
        
        # Highlight key physics concepts
        concept_box = Rectangle(width=6, height=2.5, color=text_color, fill_opacity=0.1, stroke_width=2)
        concept_box.to_edge(RIGHT, buff=0.5)
        
        concepts = VGroup(
            Text("Key Physics:", font_size=24, color=accent_color),
            Text("• Conservation of Energy", font_size=18, color=text_color),
            Text("• Angular Momentum", font_size=18, color=text_color),
            Text("• Rolling Constraint", font_size=18, color=text_color),
            Text("• Action-Reaction", font_size=18, color=text_color)
        )
        concepts.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        concepts.move_to(concept_box.get_center())
        
        with self.voiceover(text="Is complex motion mein energy conservation, angular momentum, rolling constraint, aur action-reaction - sab concepts involved hain.") as tracker:
            self.play(Create(concept_box), Write(concepts), run_time=tracker.duration*0.5)
            self.play(angle.animate.set_value(24), run_time=tracker.duration*0.5, rate_func=linear)
        
        # Clean up updaters
        platform.clear_updaters()
        sphere_group.clear_updaters()
        sphere_center.clear_updaters()
        
        # Final state
        self.play(FadeOut(concept_box), FadeOut(concepts))
        self.play(FadeOut(platform_rotation_arrow), FadeOut(platform_label))
        self.play(FadeOut(sphere_rotation_arrow), FadeOut(sphere_label))
    
    def conclusion(self, accent_color, text_color):
        # Show final result
        result_title = Text("Complex Physics Made Visual!", font_size=44, color=accent_color)
        result_subtitle = Text("Real-world motion patterns through animation", font_size=28, color=text_color)
        result_subtitle.next_to(result_title, DOWN, buff=0.5)
        
        result_group = VGroup(result_title, result_subtitle)
        result_group.center()
        
        with self.voiceover(text="Is tarah complex physics problems ko visual animation se samajhna asan ho jaata hai. Thank you!") as tracker:
            self.play(Write(result_group), run_time=tracker.duration)
        
        # Final flourish
        self.play(
            result_title.animate.set_color(self.PRIMARY_COLOR),
            Circumscribe(result_group, color=self.SECONDARY_COLOR, fade_out=True),
            run_time=1
        )
