from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = BLUE
        SECONDARY_COLOR = GREEN
        ACCENT_COLOR = ORANGE
        TEXT_COLOR = WHITE
        BACKGROUND_COLOR = DARK_GRAY
        self.camera.background_color = BACKGROUND_COLOR
        # Scene progression
        self.intro_scene(PRIMARY_COLOR, TEXT_COLOR)
        self.main_content(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR)
        self.conclusion(ACCENT_COLOR, TEXT_COLOR)
    def intro_scene(self, PRIMARY_COLOR, TEXT_COLOR):
        # Introduction with title
        title = Text("Relative Motion: Boat & Ball Problem", font_size=48, color=PRIMARY_COLOR).to_edge(UP, buff=0.7)
        # River setup
        ground_line = Line(LEFT * 7, RIGHT * 7, color=SECONDARY_COLOR).shift(DOWN * 3)
        river_lines = VGroup(*[
        Line(LEFT * 7 + UP * i * 0.1, RIGHT * 7 + UP * i * 0.1, color=SECONDARY_COLOR).shift(DOWN * 2.5)
        for i in range(5)
        ]).set_opacity(0.6)
        # Boat
        boat_body = Rectangle(width=2.5, height=0.7, color=PRIMARY_COLOR, fill_opacity=1).shift(DOWN * 2.8 + LEFT * 4)
        boat_cabin = Rectangle(width=0.8, height=0.5, color=TEXT_COLOR, fill_opacity=1).next_to(boat_body, UP, buff=0.1).align_to(boat_body, RIGHT)
        boat = VGroup(boat_body, boat_cabin)
        with self.voiceover(text="Hello students! Aaj hum relative motion ka ek interesting problem dekhenge. Ek boat 27 kilometers per hour ki maximum speed se still water mein chal sakti hai.") as tracker:
            self.play(Write(title), run_time=tracker.duration * 0.3)
            self.play(FadeIn(ground_line), FadeIn(river_lines), run_time=tracker.duration * 0.3)
            self.play(FadeIn(boat), run_time=tracker.duration * 0.4)
            self.wait(0.5) # Short wait after first narration
            self.boat = boat
            self.river_lines = river_lines
            self.ground_line = ground_line
            self.title = title
    def main_content(self, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR):
        # Beat 2: River Flow & Downstream Concept
        observer = self.create_stick_figure().next_to(self.ground_line, LEFT, buff=0.5).shift(UP*0.5)
        v_boat_still_text = Text("V_boat_still = 27 km/h", font_size=24, color=PRIMARY_COLOR).next_to(self.boat, UP, buff=0.3)
        v_boat_still_arrow = Arrow(self.boat.get_center() + UP * 0.5, self.boat.get_center() + RIGHT * 2 + UP * 0.5, color=PRIMARY_COLOR, buff=0.1).shift(UP*0.3)
        v_river_text = Text("V_river = 9 km/h", font_size=24, color=SECONDARY_COLOR).next_to(self.boat, DOWN, buff=0.5)
        v_river_arrow = Arrow(self.boat.get_center() + DOWN * 0.3, self.boat.get_center() + RIGHT * 2 + DOWN * 0.3, color=SECONDARY_COLOR, buff=0.1).shift(DOWN*0.3)
        with self.voiceover(text="Yeh boat ek river mein downstream move kar rahi hai, jo 9 kilometers per hour ki speed se beh rahi hai. Bank par ek observer hai jo rest par hai.") as tracker:
            self.play(FadeIn(observer), run_time=tracker.duration * 0.3)
            self.play(FadeIn(v_boat_still_text), GrowArrow(v_boat_still_arrow), run_time=tracker.duration * 0.3)
            self.play(FadeIn(v_river_text), GrowArrow(v_river_arrow), run_time=tracker.duration * 0.4)
            self.add(self.get_continuous_boat_animation(self.boat, self.river_lines))
            self.wait(tracker.duration)
            # Beat 3: Man Throws Ball
            man = self.create_stick_figure().move_to(self.boat_to_point(self.boat, 0.5, 0.8))
            ball = Dot(man.get_top() + UP * 0.3, radius=0.1, color=ACCENT_COLOR, fill_opacity=1)
            v_ball_up_text = Text("V_ball_up = 10 m/s", font_size=24, color=ACCENT_COLOR).next_to(ball, UP, buff=0.5)
            v_ball_up_arrow = Arrow(ball.get_center(), ball.get_center() + UP, color=ACCENT_COLOR, buff=0.1)
        with self.voiceover(text="Boat mein baitha ek aadmi ek ball ko vertically upwards 10 meters per second ki speed se throw karta hai. Humein bank par khade observer ke liye ball ka range find karna hai.") as tracker:
            self.play(FadeIn(man), run_time=tracker.duration * 0.2)
            self.play(FadeIn(ball), run_time=tracker.duration * 0.2)
            self.play(GrowArrow(v_ball_up_arrow), FadeIn(v_ball_up_text), run_time=tracker.duration * 0.3)
            self.play(ball.animate.shift(UP * 0.5), run_time=tracker.duration * 0.3) # Simple throw animation
            self.wait(tracker.duration * 0.2)
            self.v_boat_still_text = v_boat_still_text
            self.v_boat_still_arrow = v_boat_still_arrow
            self.v_river_text = v_river_text
            self.v_river_arrow = v_river_arrow
            self.man = man
            self.ball = ball
            self.v_ball_up_text = v_ball_up_text
            self.v_ball_up_arrow = v_ball_up_arrow
            self.observer = observer
            # Beat 4: Unit Conversion
            conversion_title = Text("Unit Conversions:", font_size=30, color=PRIMARY_COLOR).to_corner(UP + RIGHT).shift(LEFT*2)
            conv1 = Text("V_boat_still = 27 km/h = 7.5 m/s", font_size=28, color=TEXT_COLOR).next_to(conversion_title, DOWN, buff=0.5).align_to(conversion_title, LEFT)
            conv2 = Text("V_river = 9 km/h = 2.5 m/s", font_size=28, color=TEXT_COLOR).next_to(conv1, DOWN, buff=0.3).align_to(conversion_title, LEFT)
            self.play(FadeOut(self.v_boat_still_arrow, self.v_river_arrow)) # Clean up arrows for space
        with self.voiceover(text="Sabse pehle, saari speeds ko consistent units mein convert karte hain, meters per second mein. 27 kilometers per hour banega 7.5 meters per second, aur 9 kilometers per hour banega 2.5 meters per second.") as tracker:
            self.play(Write(conversion_title), run_time=tracker.duration * 0.2)
            self.play(Transform(self.v_boat_still_text, conv1), run_time=tracker.duration * 0.4)
            self.play(Transform(self.v_river_text, conv2), run_time=tracker.duration * 0.4)
            self.wait(0.5) # Short wait
            self.conversion_title = conversion_title
            self.conv_group = VGroup(self.v_boat_still_text, self.v_river_text) # Now they are transformed texts
            # Beat 5: Boat's Speed Relative to Bank
            v_boat_bank_calc_title = Text("Boat's Speed (Bank):", font_size=30, color=PRIMARY_COLOR).next_to(self.conv_group, DOWN, buff=0.7).align_to(self.conversion_title, LEFT)
            v_boat_bank_eq1 = Text("V_boat_bank = V_boat_still + V_river", font_size=28, color=PRIMARY_COLOR).next_to(v_boat_bank_calc_title, DOWN, buff=0.3).align_to(self.conversion_title, LEFT)
            v_boat_bank_eq2 = Text("V_boat_bank = 7.5 m/s + 2.5 m/s", font_size=28, color=TEXT_COLOR).next_to(v_boat_bank_eq1, DOWN, buff=0.2).align_to(self.conversion_title, LEFT)
            v_boat_bank_eq3 = Text("V_boat_bank = 10 m/s", font_size=32, color=SECONDARY_COLOR, weight=BOLD).next_to(v_boat_bank_eq2, DOWN, buff=0.2).align_to(self.conversion_title, LEFT)
        with self.voiceover(text="Jab boat downstream jaati hai, toh uski speed river ki speed mein add ho jaati hai. Toh boat ki speed bank ke respect mein 7.5 plus 2.5, yani 10 meters per second hogi.") as tracker:
            self.play(Write(v_boat_bank_calc_title), run_time=tracker.duration * 0.2)
            self.play(Write(v_boat_bank_eq1), run_time=tracker.duration * 0.3)
            self.play(Write(v_boat_bank_eq2), run_time=tracker.duration * 0.3)
            self.play(Write(v_boat_bank_eq3), run_time=tracker.duration * 0.2)
            self.wait(0.5)
            self.boat_speed_calc = VGroup(v_boat_bank_calc_title, v_boat_bank_eq1, v_boat_bank_eq2, v_boat_bank_eq3)
            # Beat 6: Ball's Horizontal Velocity
            v_ball_horiz_text = Text("Ball's Horizontal Velocity (V_x) =", font_size=28, color=PRIMARY_COLOR).next_to(self.boat_speed_calc, DOWN, buff=0.7).align_to(self.conversion_title, LEFT)
            v_ball_horiz_value = Text("V_boat_bank = 10 m/s", font_size=28, color=TEXT_COLOR).next_to(v_ball_horiz_text, RIGHT, buff=0.1)
            # Show ball having horizontal velocity while man throws it
            ball_horiz_arrow = Arrow(self.ball.get_center(), self.ball.get_center() + RIGHT * 1, color=PRIMARY_COLOR, buff=0.1)
            self.play(FadeOut(self.v_ball_up_arrow, self.v_ball_up_text)) # Clean up vertical arrow, but ball stays
        with self.voiceover(text="Jab aadmi ball ko throw karta hai, toh ball ke paas boat ki horizontal velocity bhi aa jaati hai. Toh ball ki horizontal velocity bhi bank ke respect mein 10 meters per second hogi.") as tracker:
            self.play(GrowArrow(ball_horiz_arrow), run_time=tracker.duration * 0.4)
            self.play(Write(v_ball_horiz_text), Write(v_ball_horiz_value), run_time=tracker.duration * 0.6)
            self.wait(0.5)
            self.v_ball_horiz = VGroup(v_ball_horiz_text, v_ball_horiz_value)
            # Beat 7: Ball's Vertical Motion - Time of Flight
            self.play(FadeOut(self.ball, ball_horiz_arrow)) # Ball starts from boat again for path animation
            time_flight_title = Text("Time of Flight (T):", font_size=30, color=PRIMARY_COLOR).next_to(self.v_ball_horiz, DOWN, buff=0.7).align_to(self.conversion_title, LEFT)
            time_flight_eq1 = Text("Vertical Motion: u_y = 10 m/s, g = 10 m/s^2", font_size=28, color=TEXT_COLOR).next_to(time_flight_title, DOWN, buff=0.3).align_to(self.conversion_title, LEFT)
            time_flight_eq2 = Text("t_up = u_y / g = 10 / 10 = 1 s", font_size=28, color=TEXT_COLOR).next_to(time_flight_eq1, DOWN, buff=0.2).align_to(self.conversion_title, LEFT)
            time_flight_eq3 = Text("Total T = 2 * t_up = 2 * 1 s = 2 s", font_size=32, color=SECONDARY_COLOR, weight=BOLD).next_to(time_flight_eq2, DOWN, buff=0.2).align_to(self.conversion_title, LEFT)
            # Simulate ball path (parabolic relative to ground, vertical relative to boat)
            start_pos = self.boat.get_center() + UP * 0.3
            end_pos = start_pos + RIGHT * (10 * 2) # Horizontal velocity * time = 20 meters
            # Manim does not use real-world units directly for position, so we scale it visually.
            # Let's assume 1 unit in Manim is 1 meter for horizontal distance for visual clarity.
            # So, 20 meters horizontally means RIGHT*20. This will go off screen, so we need to scale.
            # Max horizontal is ~14 units (LEFT*7 to RIGHT*7). Let 1 unit = 2 meters. So 20m = RIGHT*10
            # Start the ball at an arbitrary point on the boat for the trajectory
            # It needs to appear from the man's hand.
            ball_start_point = self.boat.get_center() + UP*0.5
            ball_path_points = [
            ball_start_point + RIGHT * i * 0.5 + UP * (10*i - 5*i*i) * 0.1 for i in np.arange(0, 2.1, 0.1)
            ]
            # Re-scale for Manim screen. Horizontal range is 20m. Manim width is 14.
            # So 20m -> 10 units (factor 0.5). Vertical 10m/s, g=10, max height = u^2/2g = 100/20 = 5m.
            # Max height = 5m -> 2.5 units (factor 0.5)
            ball_trajectory = ArcBetweenPoints(
            start=self.boat.get_center() + UP*0.5,
            end=self.boat.get_center() + RIGHT*10 + UP*0.5, # 10 units horizontal for 20m visual range
            angle=0, # This will make a straight line, need to custom path or Bezier
            stroke_width=3, color=ACCENT_COLOR
            )
            # Let's create a more manual parabolic path
            trajectory_points = []
            # Simulate 2 seconds of flight
            # u_x = 10 m/s, u_y = 10 m/s, g = 10 m/s^2
            # x = u_x * t, y = u_y * t - 0.5 * g * t^2
            # For Manim, scale values for visual fit, e.g., 1 Manim unit = 2 real meters
            start_x = self.boat.get_center()[0]
            start_y = self.boat.get_center()[1] + 0.5 # start above boat
            for t_step in np.arange(0, 2.05, 0.05):
            x = start_x + (10 * t_step) * 0.5 # Scale horizontal distance by 0.5
            y = start_y + (10 * t_step - 0.5 * 10 * t_step**2) * 0.5 # Scale vertical distance by 0.5
            trajectory_points.append([x, y, 0])
            ball_trajectory = VMobject(stroke_width=3, color=ACCENT_COLOR)
            ball_trajectory.set_points_as_corners(trajectory_points)
        with self.voiceover(text="Ab vertical motion dekhte hain. Ball ko 10 meters per second se upar fenka gaya hai, aur g ki value 10 meters per second square hai. Toh max height tak pahunchne mein 1 second lagega, aur total time of flight 2 seconds hoga.") as tracker:
            self.play(FadeOut(self.title), FadeOut(self.man), FadeOut(self.observer)) # Clear some space
            self.play(Create(ball_trajectory), run_time=tracker.duration * 0.4)
            self.play(Write(time_flight_title), run_time=tracker.duration * 0.15)
            self.play(Write(time_flight_eq1), run_time=tracker.duration * 0.15)
            self.play(Write(time_flight_eq2), run_time=tracker.duration * 0.15)
            self.play(Write(time_flight_eq3), run_time=tracker.duration * 0.15)
            self.wait(tracker.duration * 0.2)
            self.time_flight_calc = VGroup(time_flight_title, time_flight_eq1, time_flight_eq2, time_flight_eq3)
            self.ball_trajectory = ball_trajectory
            # Beat 8: Calculate Range
            range_calc_title = Text("Calculate Range (R):", font_size=30, color=PRIMARY_COLOR).next_to(self.time_flight_calc, DOWN, buff=0.7).align_to(self.conversion_title, LEFT)
            range_eq1 = Text("R = Horizontal Velocity (V_x) * Total Time (T)", font_size=28, color=PRIMARY_COLOR).next_to(range_calc_title, DOWN, buff=0.3).align_to(self.conversion_title, LEFT)
            range_eq2 = Text("R = 10 m/s * 2 s", font_size=28, color=TEXT_COLOR).next_to(range_eq1, DOWN, buff=0.2).align_to(self.conversion_title, LEFT)
            range_eq3 = Text("R = 20 meters", font_size=32, color=SECONDARY_COLOR, weight=BOLD).next_to(range_eq2, DOWN, buff=0.2).align_to(self.conversion_title, LEFT)
            # Visual range indicator
            range_line = Line(self.ball_trajectory.get_start(), self.ball_trajectory.get_end(), color=SECONDARY_COLOR, stroke_width=4).shift(DOWN*0.3)
            range_label = Text("Range", font_size=24, color=TEXT_COLOR).next_to(range_line, DOWN, buff=0.2)
        with self.voiceover(text="Range calculate karne ke liye, hum horizontal velocity ko time of flight se multiply karte hain. Yeh hoga 10 meters per second times 2 seconds, jo 20 meters hai.") as tracker:
            self.play(Create(range_line), FadeIn(range_label), run_time=tracker.duration * 0.3)
            self.play(Write(range_calc_title), run_time=tracker.duration * 0.15)
            self.play(Write(range_eq1), run_time=tracker.duration * 0.15)
            self.play(Write(range_eq2), run_time=tracker.duration * 0.15)
            self.play(Write(range_eq3), run_time=tracker.duration * 0.25)
            self.wait(0.5)
            self.all_calculations = VGroup(
            self.conversion_title, self.conv_group,
            self.boat_speed_calc, self.v_ball_horiz,
            self.time_flight_calc, range_calc_title,
            range_eq1, range_eq2, range_eq3
            )
            self.range_visuals = VGroup(range_line, range_label, self.ball_trajectory)
    def conclusion(self, ACCENT_COLOR, TEXT_COLOR):
        # Beat 9: Final Answer & Conclusion
        final_conv = Text("20 meters = 2000 cm", font_size=32, color=TEXT_COLOR).move_to(ORIGIN + UP*1)
        final_answer = Text("Final Range = 2000 cm", font_size=42, color=ACCENT_COLOR, weight=BOLD).next_to(final_conv, DOWN, buff=0.5)
        with self.voiceover(text="Problem mein humein range centimeters mein pucha gaya hai. Toh 20 meters barabar hai 2000 centimeters ke. Toh bank par khade observer ke liye ball ka range 2000 centimeters hoga. Umeed hai aapko relative motion ka yeh concept clear ho gaya hoga. Thank you!") as tracker:
            self.play(
            FadeOut(self.boat),
            FadeOut(self.river_lines),
            FadeOut(self.ground_line),
            FadeOut(self.range_visuals),
            FadeOut(self.all_calculations),
            runtime=tracker.duration * 0.3
            )
            self.play(Write(final_conv), run_time=tracker.duration * 0.3)
            self.play(Write(final_answer), run_time=tracker.duration * 0.4)
            self.wait(tracker.duration * 0.2)
    def create_stick_figure(self):
        head = Circle(radius=0.15, color=WHITE, fill_opacity=1)
        body = Line(ORIGIN, DOWN * 0.8, color=WHITE)
        left_arm = Line(ORIGIN, UL * 0.5, color=WHITE).shift(DOWN * 0.2)
        right_arm = Line(ORIGIN, UR * 0.5, color=WHITE).shift(DOWN * 0.2)
        left_leg = Line(DOWN * 0.8, DOWN * 0.8 + DL * 0.5, color=WHITE)
        right_leg = Line(DOWN * 0.8, DOWN * 0.8 + DR * 0.5, color=WHITE)
        figure = VGroup(head, body, left_arm, right_arm, left_leg, right_leg)
        figure.arrange(DOWN, buff=0.05).move_to(ORIGIN)
        return figure.scale(0.8) # Adjust scale for better fit
    def boat_to_point(self, boat, x_rel, y_rel):
        """Helper to get a point on the boat based on relative coordinates (0-1)."""
        x_pos = boat.get_left()[0] + x_rel * boat.width
        y_pos = boat.get_bottom()[1] + y_rel * boat.height
        return np.array([x_pos, y_pos, 0])
    def get_continuous_boat_animation(self, boat, river_lines):
        # Continuous animation for boat and river
    def update_boat_position(mob, dt):
        # This simulates a continuous movement to the right
        mob.shift(RIGHT * dt * 0.5) # Arbitrary speed for visual effect
        if mob.get_right()[0] > 14 / 2 + 1: # If off-screen right
        mob.shift(LEFT * (14 + mob.width + 2)) # Reset to left
    def update_river_lines(mob, dt):
        mob.shift(RIGHT * dt * 0.3) # Slower than boat
        for line in mob:
        if line.get_right()[0] > 14 / 2 + 1:
        line.shift(LEFT * (14 + 2))
        return Succession(
        # Apply updaters to boat and river_lines continuously
        AnimationGroup(
        ApplyMethod(boat.add_updater, update_boat_position),
        ApplyMethod(river_lines.add_updater, update_river_lines),
        rate_func=linear
        ),
        # Keep for the entire scene duration by having a very long wait
        Wait(100)
        )