from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = "#3498db" # BLUE
        SECONDARY_COLOR = "#2ecc71" # GREEN
        ACCENT_COLOR = "#f39c12" # ORANGE
        TEXT_COLOR = WHITE
        BACKGROUND_COLOR = "#2c3e50" # DARK_GRAY
        # Set background color
        self.camera.background_color = BACKGROUND_COLOR
        # Scene progression
        self.intro_scene(PRIMARY_COLOR, TEXT_COLOR)
        self.problem_statement_scene(PRIMARY_COLOR, TEXT_COLOR)
        self.environment_setup_scene(PRIMARY_COLOR, SECONDARY_COLOR, TEXT_COLOR, ACCENT_COLOR)
        self.unit_conversion_scene(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR)
        self.boat_downstream_speed_scene(PRIMARY_COLOR, SECONDARY_COLOR, TEXT_COLOR, ACCENT_COLOR)
        self.ball_vertical_motion_scene(PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, SECONDARY_COLOR)
        self.ball_horizontal_motion_scene(PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, SECONDARY_COLOR)
        self.calculate_range_scene(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR)
        self.conclusion_scene(PRIMARY_COLOR, TEXT_COLOR, SECONDARY_COLOR)
    def intro_scene(self, primary_color, text_color):
        title = Text("Relative Motion: Ball on a Boat", font_size=50, color=primary_color, weight=BOLD)
        with self.voiceover(text="Hello everyone! Aaj hum ek bahut hi interesting physics problem solve karenge. Topic hai Relative Motion.") as tracker:
            self.play(Write(title), run_time=tracker.duration - 0.5)
            self.wait(0.5)
            self.play(FadeOut(title), run_time=0.8)
    def problem_statement_scene(self, primary_color, text_color):
        problem_text = Text(
        "Problem: A boat's max speed in still water is 27 km/h. "
        "It moves downstream in a river flowing at 9 km/h. "
        "A man in the boat throws a ball vertically upwards with speed of 10 m/s. "
        "Range of the ball as observed by an observer at rest on the bank is _______ cm. (Take g = 10 m/s²)",
        font_size=28,
        color=text_color,
        line_spacing=1.2
        ).to_edge(UP, buff=0.5).set_width(config.frame_width * 0.8) # 80% width for readability
        with self.voiceover(text="Ek boat ki still water mein maximum speed hai 27 km/h. Yeh boat ek river mein downstream move kar rahi hai, river ki speed hai 9 km/h. Boat mein baitha ek aadmi ek ball ko vertically upwards 10 m/s ki speed se phenkta hai. Humein calculate karna hai, ki bank par rest par baithe ek observer ko ball ka range kitna dikhega, in cm. Gravity, g = 10 m/s square.") as tracker:
            self.play(FadeIn(problem_text), run_time=tracker.duration - 0.5)
            self.wait(0.5)
            self.play(FadeOut(problem_text), run_time=0.8)
    def environment_setup_scene(self, primary_color, secondary_color, text_color, accent_color):
        # River
        river = Rectangle(width=config.frame_width, height=3, color=secondary_color, fill_opacity=0.6, stroke_width=0).to_edge(DOWN, buff=0)
        # Boat
        boat_body = Polygon(
        [-2, -0.5, 0], [2, -0.5, 0], [1.5, 0.5, 0], [-1.5, 0.5, 0],
        color=primary_color, fill_opacity=0.9
        ).scale(0.8).move_to(river.get_center() + UP * 0.5)
        man = Circle(radius=0.3, color=TEXT_COLOR, fill_opacity=1).move_to(boat_body.get_center() + UP * 0.7)
        ball = Circle(radius=0.1, color=accent_color, fill_opacity=1).move_to(man.get_center() + UP * 0.4)
        boat_group = VGroup(boat_body, man, ball).move_to(LEFT * 4 + DOWN * 1.5)
        # Observer on bank
        observer_body = Line(ORIGIN, UP*0.8).set_stroke(TEXT_COLOR, width=4)
        observer_head = Circle(radius=0.2, color=TEXT_COLOR, fill_opacity=1).next_to(observer_body, UP, buff=0.05)
        observer_label = Text("Observer", font_size=20, color=text_color).next_to(observer_head, UP, buff=0.1)
        observer = VGroup(observer_body, observer_head, observer_label).move_to(RIGHT*5.5 + DOWN*1.5 + UP*1.5) # on the bank, with some height
        # Speeds text
        still_water_speed_txt = Text("Boat Speed (still water): 27 km/h", font_size=28, color=primary_color).to_edge(UP + LEFT, buff=0.5)
        river_speed_txt = Text("River Speed: 9 km/h", font_size=28, color=secondary_color).next_to(still_water_speed_txt, DOWN, buff=0.3, aligned_edge=LEFT)
        ball_throw_speed_txt = Text("Ball Throw Speed: 10 m/s (vertical)", font_size=28, color=accent_color).next_to(river_speed_txt, DOWN, buff=0.3, aligned_edge=LEFT)
        with self.voiceover(text="Toh chaliye, is problem ko visualize karte hain. Yahan hai humari river, aur usmein boat. Boat ki still water speed hai 27 km/h. River ki speed hai 9 km/h. Aur bank par ek observer hai jo rest par hai.") as tracker:
            self.play(FadeIn(river), run_time=0.5)
            self.play(FadeIn(boat_group), run_time=1)
            self.play(FadeIn(observer), run_time=1)
            self.play(
            FadeIn(still_water_speed_txt),
            FadeIn(river_speed_txt),
            FadeIn(ball_throw_speed_txt),
            run_time=tracker.duration - 2.5 # Adjust to fit narration
            )
            self.wait(0.5)
            self.play(FadeOut(VGroup(river, boat_group, observer, still_water_speed_txt, river_speed_txt, ball_throw_speed_txt)), run_time=1)
    def unit_conversion_scene(self, primary_color, secondary_color, accent_color, text_color):
        title = Text("Step 1: Unit Conversion (km/h to m/s)", font_size=36, color=primary_color, weight=BOLD).to_edge(UP, buff=0.5)
        kmh_to_ms = Text("1 km/h = 5/18 m/s", font_size=28, color=TEXT_COLOR).next_to(title, DOWN, buff=0.5, aligned_edge=LEFT)
        boat_kmh = Text("Boat Speed = 27 km/h", font_size=28, color=primary_color)
        boat_ms_calc = Text("= 27 * (5/18) m/s", font_size=28, color=TEXT_COLOR)
        boat_ms_res = Text("= 7.5 m/s", font_size=28, color=TEXT_COLOR)
        boat_speed_group = VGroup(boat_kmh, boat_ms_calc, boat_ms_res).arrange(RIGHT, buff=0.2).next_to(kmh_to_ms, DOWN, buff=0.5, aligned_edge=LEFT)
        river_kmh = Text("River Speed = 9 km/h", font_size=28, color=secondary_color)
        river_ms_calc = Text("= 9 * (5/18) m/s", font_size=28, color=TEXT_COLOR)
        river_ms_res = Text("= 2.5 m/s", font_size=28, color=TEXT_COLOR)
        river_speed_group = VGroup(river_kmh, river_ms_calc, river_ms_res).arrange(RIGHT, buff=0.2).next_to(boat_speed_group, DOWN, buff=0.5, aligned_edge=LEFT)
        with self.voiceover(text="Sabse pehle, speeds ko m/s mein convert karte hain. 1 km/h hota hai 5/18 m/s. Boat ki speed 27 km/h, jo ki 27 times 5 by 18, yaani 7.5 m/s hoti hai.") as tracker:
            self.play(Write(title), run_time=1)
            self.play(Write(kmh_to_ms), run_time=1)
            self.play(Write(boat_speed_group[0]), run_time=0.5)
            self.play(Write(boat_speed_group[1]), run_time=0.8)
            self.play(Write(boat_speed_group[2]), run_time=0.7)
        with self.voiceover(text="Aur river ki speed 9 km/h, jo ki 9 times 5 by 18, yaani 2.5 m/s hoti hai.") as tracker:
            self.play(Write(river_speed_group[0]), run_time=0.5)
            self.play(Write(river_speed_group[1]), run_time=0.8)
            self.play(Write(river_speed_group[2]), run_time=0.7)
            self.wait(0.5)
            self.play(FadeOut(VGroup(title, kmh_to_ms, boat_speed_group, river_speed_group)), run_time=1)
    def boat_downstream_speed_scene(self, primary_color, secondary_color, text_color, accent_color):
        title = Text("Step 2: Boat's Downstream Speed", font_size=36, color=primary_color, weight=BOLD).to_edge(UP, buff=0.5)
        boat_speed = Text("Boat Speed (V_B) = 7.5 m/s", font_size=28, color=primary_color).next_to(title, DOWN, buff=0.5, aligned_edge=LEFT)
        river_speed = Text("River Speed (V_R) = 2.5 m/s", font_size=28, color=secondary_color).next_to(boat_speed, DOWN, buff=0.3, aligned_edge=LEFT)
        formula = Text("V_downstream = V_B + V_R", font_size=32, color=TEXT_COLOR).next_to(river_speed, DOWN, buff=0.5, aligned_edge=LEFT)
        calculation = Text("= 7.5 m/s + 2.5 m/s", font_size=28, color=TEXT_COLOR).next_to(formula, DOWN, buff=0.2, aligned_edge=LEFT)
        result = Text("V_downstream = 10 m/s", font_size=36, color=primary_color, weight=BOLD).next_to(calculation, DOWN, buff=0.5, aligned_edge=LEFT)
        river_line = Line(LEFT*6.5, RIGHT*6.5, color=secondary_color, stroke_width=4).to_edge(DOWN, buff=1.5)
        boat_shape = Polygon(
        [-1, -0.3, 0], [1, -0.3, 0], [0.8, 0.3, 0], [-0.8, 0.3, 0],
        color=primary_color, fill_opacity=0.9
        ).scale(0.8).move_to(river_line.get_left() + RIGHT * 1 + UP * 0.5)
        boat_vel_arrow = Arrow(ORIGIN, RIGHT*0.7, buff=0, color=primary_color, stroke_width=7).next_to(boat_shape, RIGHT, buff=0.2)
        boat_vel_label = Text("10 m/s", font_size=24, color=primary_color).next_to(boat_vel_arrow, UP, buff=0.1)
        boat_vel_group = VGroup(boat_vel_arrow, boat_vel_label)
        with self.voiceover(text="Kyunki boat downstream ja rahi hai, iski total speed relative to the bank hogi boat ki speed plus river ki speed. Isse humein boat ki horizontal velocity milegi.") as tracker:
            self.play(Write(title), run_time=1)
            self.play(FadeIn(boat_speed), run_time=0.8)
            self.play(FadeIn(river_speed), run_time=0.8)
            self.play(Write(formula), run_time=1)
            self.play(Write(calculation), run_time=1)
            self.play(Write(result), run_time=1)
            self.wait(0.5)
        with self.voiceover(text="Toh, downstream speed = 7.5 m/s plus 2.5 m/s = 10 m/s. Yeh boat ki horizontal velocity hai.") as tracker:
            self.play(FadeIn(river_line), FadeIn(boat_shape), FadeIn(boat_vel_group), run_time=1)
            self.play(boat_shape.animate.shift(RIGHT * 10), boat_vel_group.animate.shift(RIGHT * 10), run_time=tracker.duration - 1, rate_func=linear) # animate boat moving
            self.wait(0.5)
            self.play(FadeOut(VGroup(title, boat_speed, river_speed, formula, calculation, result, river_line, boat_shape, boat_vel_group)), run_time=1)
    def ball_vertical_motion_scene(self, primary_color, accent_color, text_color, secondary_color):
        title = Text("Step 3: Ball's Vertical Motion", font_size=36, color=primary_color, weight=BOLD).to_edge(UP, buff=0.5)
        u_y_text = Text("Initial Vertical Speed (u_y) = 10 m/s", font_size=28, color=accent_color).next_to(title, DOWN, buff=0.5, aligned_edge=LEFT)
        g_text = Text("Acceleration due to gravity (g) = 10 m/s²", font_size=28, color=accent_color).next_to(u_y_text, DOWN, buff=0.3, aligned_edge=LEFT)
        peak_text = Text("At maximum height, vertical velocity (v_y) = 0", font_size=28, color=TEXT_COLOR).next_to(g_text, DOWN, buff=0.5, aligned_edge=LEFT)
        time_up_formula = Text("t_up = u_y / g", font_size=32, color=TEXT_COLOR).next_to(peak_text, DOWN, buff=0.3, aligned_edge=LEFT)
        time_up_calc = Text("= 10 m/s / 10 m/s²", font_size=28, color=TEXT_COLOR).next_to(time_up_formula, DOWN, buff=0.2, aligned_edge=LEFT)
        time_up_res = Text("t_up = 1 second", font_size=36, color=accent_color, weight=BOLD).next_to(time_up_calc, DOWN, buff=0.5, aligned_edge=LEFT)
        river_line = Line(LEFT*6.5, RIGHT*6.5, color=secondary_color, stroke_width=4).to_edge(DOWN, buff=1.5)
        boat_shape = Polygon(
        [-1, -0.3, 0], [1, -0.3, 0], [0.8, 0.3, 0], [-0.8, 0.3, 0],
        color=primary_color, fill_opacity=0.9
        ).scale(0.8).move_to(LEFT * 2 + river_line.get_center()[1] + UP * 0.5) # Position for boat at start of trajectory
        ball = Circle(radius=0.15, color=accent_color, fill_opacity=1).next_to(boat_shape, UP, buff=0.2)
        with self.voiceover(text="Ab baat karte hain ball ki vertical motion ki. Aadmi ball ko vertically upwards 10 m/s ki speed se phenkta hai. Gravity hai 10 m/s square. Ball upar jaayegi aur ek point par uski vertical velocity zero ho jaayegi.") as tracker:
            self.play(Write(title), run_time=1)
            self.play(FadeIn(u_y_text), run_time=0.8)
            self.play(FadeIn(g_text), run_time=0.8)
            self.play(FadeIn(VGroup(river_line, boat_shape, ball)), run_time=1)
            self.play(ball.animate.shift(UP*3), run_time=tracker.duration-4.6, rate_func=smooth) # Animate ball up
            self.play(FadeIn(peak_text), run_time=1)
        with self.voiceover(text="Time taken to reach maximum height, t_up, is initial vertical speed divided by gravity. Yani 10 m/s divided by 10 m/s square, jo ki 1 second hai.") as tracker:
            self.play(Write(time_up_formula), run_time=1)
            self.play(Write(time_up_calc), run_time=1)
            self.play(Write(time_up_res), run_time=1)
            self.wait(0.5)
            total_time_res = Text("Total Time of Flight (T) = 2 * t_up = 2 seconds", font_size=36, color=accent_color, weight=BOLD).next_to(time_up_res, DOWN, buff=0.5, aligned_edge=LEFT)
        with self.voiceover(text="Jitna time ball ko upar jaane mein laga, utna hi time niche aane mein lagega. Toh, total time of flight hai 2 seconds.") as tracker:
            self.play(ball.animate.shift(DOWN*3), run_time=1.5, rate_func=smooth) # Animate ball down
            self.play(Write(total_time_res), run_time=tracker.duration-1.5)
            self.wait(0.5)
            self.play(FadeOut(VGroup(title, u_y_text, g_text, peak_text, time_up_formula, time_up_calc, time_up_res, total_time_res, river_line, boat_shape, ball)), run_time=1)
    def ball_horizontal_motion_scene(self, primary_color, accent_color, text_color, secondary_color):
        title = Text("Step 4: Ball's Horizontal Motion", font_size=36, color=primary_color, weight=BOLD).to_edge(UP, buff=0.5)
        concept_text = Text(
        "When the man throws the ball, it retains the boat's horizontal velocity relative to the bank.",
        font_size=28, color=TEXT_COLOR, line_spacing=1.2
        ).next_to(title, DOWN, buff=0.5).set_width(config.frame_width * 0.8)
        horizontal_vel_value = Text("Ball's Horizontal Velocity (V_x) = Boat's Downstream Speed", font_size=30, color=accent_color).next_to(concept_text, DOWN, buff=0.5, aligned_edge=LEFT)
        horizontal_vel_res = Text("V_x = 10 m/s", font_size=36, color=accent_color, weight=BOLD).next_to(horizontal_vel_value, DOWN, buff=0.3, aligned_edge=LEFT)
        river_line = Line(LEFT*6.5, RIGHT*6.5, color=secondary_color, stroke_width=4).to_edge(DOWN, buff=1.5)
        boat_shape = Polygon(
        [-1, -0.3, 0], [1, -0.3, 0], [0.8, 0.3, 0], [-0.8, 0.3, 0],
        color=primary_color, fill_opacity=0.9
        ).scale(0.8).move_to(LEFT * 4 + river_line.get_center()[1] + UP * 0.5)
        ball = Circle(radius=0.15, color=accent_color, fill_opacity=1).next_to(boat_shape, UP, buff=0.2)
        # Group boat and ball for initial horizontal movement
        boat_and_ball = VGroup(boat_shape, ball)
        path = TracedPath(ball.get_center, stroke_color=accent_color, stroke_width=5)
        with self.voiceover(text="Ab yeh sabse important point hai. Jab aadmi ball ko phenkta hai, toh ball ke paas already boat ki horizontal velocity hoti hai, jo ki bank ke relative hai. Air resistance ko ignore karte hue, ball ki yeh horizontal velocity constant rahegi.") as tracker:
            self.play(Write(title), run_time=1)
            self.play(FadeIn(concept_text), run_time=tracker.duration-1)
            self.wait(0.5)
        with self.voiceover(text="Toh, ball ki horizontal velocity, V_x, boat ki downstream speed ke barabar hogi, yaani 10 m/s.") as tracker:
            self.play(FadeIn(horizontal_vel_value), run_time=1)
            self.play(FadeIn(horizontal_vel_res), run_time=1)
            self.play(FadeIn(VGroup(river_line, boat_and_ball)), run_time=1)
            self.add(path)
            # Animate the boat and ball moving together horizontally, while ball also moves vertically
            animation_duration = tracker.duration - 4 # Adjusting time for the complex animation
            self.play(
            boat_and_ball.animate.shift(RIGHT * 8), # Boat and ball group move 8 units right
            ball.animate.shift(UP * 3), # Ball moves 3 units up relative to the boat (or its current position)
            run_time=animation_duration / 2,
            rate_func=smooth
            )
            self.play(
            ball.animate.shift(DOWN * 3), # Ball moves 3 units down relative to its current position
            run_time=animation_duration / 2,
            rate_func=smooth
            )
            self.wait(0.5)
            self.play(FadeOut(VGroup(title, concept_text, horizontal_vel_value, horizontal_vel_res, river_line, boat_and_ball, path)), run_time=1)
    def calculate_range_scene(self, primary_color, secondary_color, accent_color, text_color):
        title = Text("Step 5: Calculate Range", font_size=36, color=primary_color, weight=BOLD).to_edge(UP, buff=0.5)
        vx_val = Text("Ball's Horizontal Velocity (V_x) = 10 m/s", font_size=28, color=accent_color).next_to(title, DOWN, buff=0.5, aligned_edge=LEFT)
        total_time_val = Text("Total Time of Flight (T) = 2 seconds", font_size=28, color=accent_color).next_to(vx_val, DOWN, buff=0.3, aligned_edge=LEFT)
        range_formula = Text("Range = V_x * T", font_size=32, color=TEXT_COLOR).next_to(total_time_val, DOWN, buff=0.5, aligned_edge=LEFT)
        range_calc = Text("= 10 m/s * 2 seconds", font_size=28, color=TEXT_COLOR).next_to(range_formula, DOWN, buff=0.2, aligned_edge=LEFT)
        range_res = Text("Range = 20 meters", font_size=36, color=primary_color, weight=BOLD).next_to(range_calc, DOWN, buff=0.5, aligned_edge=LEFT)
        with self.voiceover(text="Range calculate karne ke liye, hum ball ki horizontal velocity ko total time of flight se multiply karenge. Range = V_x times T.") as tracker:
            self.play(Write(title), run_time=1)
            self.play(FadeIn(vx_val), run_time=0.8)
            self.play(FadeIn(total_time_val), run_time=0.8)
            self.play(Write(range_formula), run_time=tracker.duration - 2.6)
            self.wait(0.5)
        with self.voiceover(text="Range = 10 m/s multiplied by 2 seconds, jo ki 20 meters hota hai. Lekin humein answer centimeters mein chahiye.") as tracker:
            self.play(Write(range_calc), run_time=1)
            self.play(Write(range_res), run_time=tracker.duration - 1)
            self.wait(0.5)
            conversion_text = Text("1 meter = 100 cm", font_size=28, color=TEXT_COLOR).next_to(range_res, DOWN, buff=0.5, aligned_edge=LEFT)
            final_answer = Text("Range = 20 * 100 cm = 2000 cm", font_size=40, color=secondary_color, weight=BOLD).next_to(conversion_text, DOWN, buff=0.3, aligned_edge=LEFT)
        with self.voiceover(text="Toh, 20 meters = 20 times 100 centimeters = 2000 cm. Yeh hai ball ka range jo bank par baithe observer ko dikhega.") as tracker:
            self.play(Write(conversion_text), run_time=1)
            self.play(Write(final_answer), run_time=tracker.duration - 1)
            self.wait(0.5)
            self.play(FadeOut(VGroup(title, vx_val, total_time_val, range_formula, range_calc, range_res, conversion_text, final_answer)), run_time=1)
    def conclusion_scene(self, primary_color, text_color, secondary_color):
        summary_text = Text(
        "Summary: We combined relative motion (boat's speed) and projectile motion (ball's vertical flight) to find the range.",
        font_size=32, color=text_color, line_spacing=1.2
        ).to_edge(UP, buff=1.0).set_width(config.frame_width * 0.8)
        key_concept = Text("Key Concept: Horizontal and Vertical motions are independent.", font_size=30, color=primary_color, weight=BOLD).next_to(summary_text, DOWN, buff=0.8)
        final_ans_display = Text("Final Answer: 2000 cm", font_size=48, color=secondary_color, weight=BOLD).next_to(key_concept, DOWN, buff=0.8)
        with self.voiceover(text="Toh humne dekha ki kaise relative motion aur projectile motion ke concepts ko combine karke humne yeh problem solve ki. Iska key concept hai ki horizontal aur vertical motions independent hoti hain. Final answer hai 2000 cm.") as tracker:
            self.play(FadeIn(summary_text), run_time=1.5)
            self.play(FadeIn(key_concept), run_time=2)
            self.play(FadeIn(final_ans_display), run_time=tracker.duration - 3.5)
            self.wait(0.5)
        with self.voiceover(text="Umeed hai aapko yeh explanation pasand aaya hoga. Thank you!") as tracker:
            self.play(FadeOut(VGroup(summary_text, key_concept, final_ans_display)), run_time=tracker.duration)