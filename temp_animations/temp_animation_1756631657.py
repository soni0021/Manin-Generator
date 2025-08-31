from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
class GeneratedAnimation(VoiceoverScene):
    def construct(self):
        # Setup TTS (REQUIRED)
        self.set_speech_service(GTTSService(lang="hi", tld="com")) # Changed lang to "hi" for Hinglish
        # Define color scheme (REQUIRED - USE THESE EXACT NAMES)
        PRIMARY_COLOR = BLUE
        SECONDARY_COLOR = GREEN
        ACCENT_COLOR = ORANGE
        TEXT_COLOR = WHITE
        LIGHT_GRAY = "#bdc3c7"
        BLUE_A = "#85c1e9" # Lighter blue for river
        # Scene progression
        self.intro_and_boat_speed(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY, BLUE_A)
        self.ball_throw_and_horizontal_velocity(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY)
        self.time_of_flight_calculation(PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY)
        self.range_calculation(PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY)
        self.conclusion(PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY)
    def intro_and_boat_speed(self, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY, BLUE_A):
        title = Text("गतिशील फ्रेम में प्रक्षेप्य गति", color=PRIMARY_COLOR, font_size=48).to_edge(UP)
        problem_text_line1 = Text("शांत जल में नाव की गति: 27 km/h", font_size=28, color=TEXT_COLOR).shift(UP*1.5 + LEFT*3)
        problem_text_line2 = Text("नदी का बहाव: 9 km/h", font_size=28, color=TEXT_COLOR).next_to(problem_text_line1, DOWN, buff=0.3)
        river_rect = Rectangle(width=FRAME_WIDTH, height=2, color=BLUE_A, fill_opacity=0.6).shift(DOWN*2)
        boat_rect = Rectangle(width=3, height=1, color=PRIMARY_COLOR, fill_opacity=0.8).next_to(river_rect, UP, buff=0.2).shift(LEFT*3)
        boat_speed_kmh = Text("27 km/h", font_size=24, color=TEXT_COLOR).next_to(boat_rect, UP, buff=0.3)
        river_speed_kmh = Text("9 km/h", font_size=24, color=TEXT_COLOR).next_to(river_rect, DOWN, buff=0.3)
        conversion_text = Text("मीटर प्रति सेकंड में परिवर्तन:", font_size=28, color=LIGHT_GRAY).next_to(river_speed_kmh, DOWN, buff=0.8).shift(RIGHT*1)
        boat_speed_ms = Text("7.5 m/s", font_size=24, color=ACCENT_COLOR).move_to(boat_speed_kmh.get_center())
        river_speed_ms = Text("2.5 m/s", font_size=24, color=ACCENT_COLOR).move_to(river_speed_kmh.get_center())
        downstream_calc = Text("v_downstream = 7.5 + 2.5 = 10 m/s", font_size=32, color=SECONDARY_COLOR, weight=BOLD).shift(DOWN*0.5 + RIGHT*3)
        with self.voiceover(text="नमस्ते दोस्तों! आज हम एक बहुत दिलचस्प भौतिकी समस्या हल करेंगे जिसमें सापेक्ष गति और प्रक्षेप्य गति शामिल है। समस्या यह है: एक नाव की शांत जल में अधिकतम गति 27 किलोमीटर प्रति घंटा है। और यह नाव एक नदी में अनुप्रवाह जा रही है जो 9 किलोमीटर प्रति घंटा की गति से बह रही है। सबसे पहले, इन गतियों को मीटर प्रति सेकंड में बदलते हैं।") as tracker:
            self.play(Write(title), run_time=tracker.duration * 0.2)
            self.play(FadeIn(problem_text_line1, problem_text_line2), run_time=tracker.duration * 0.3)
            self.play(Create(river_rect), FadeIn(boat_rect), run_time=tracker.duration * 0.2)
            self.play(FadeIn(boat_speed_kmh, river_speed_kmh), run_time=tracker.duration * 0.3)
        with self.voiceover(text="शांत जल में नाव की गति 27 किलोमीटर प्रति घंटा है, यानी 7.5 मीटर प्रति सेकंड। नदी का बहाव 9 किलोमीटर प्रति घंटा है, यानी 2.5 मीटर प्रति सेकंड। जब नाव अनुप्रवाह चलती है, तो उसकी कुल गति नदी के बहाव के साथ जुड़ जाती है। तो, नाव की बैंक के सापेक्ष कुल गति 7.5 जमा 2.5, यानी 10 मीटर प्रति सेकंड होगी।") as tracker:
            self.play(Write(conversion_text), run_time=tracker.duration * 0.2)
            self.play(Transform(boat_speed_kmh, boat_speed_ms), Transform(river_speed_kmh, river_speed_ms), run_time=tracker.duration * 0.3)
            self.play(FadeIn(downstream_calc), run_time=tracker.duration * 0.3)
            boat_arrow = Arrow(boat_rect.get_center(), boat_rect.get_right() + RIGHT*1.5, color=PRIMARY_COLOR).shift(UP*0.5)
            self.play(GrowArrow(boat_arrow), run_time=tracker.duration * 0.2)
            self.wait(0.5)
            self.add_to_nl(boat_rect, river_rect, downstream_calc) # Retain for next scene
            self.remove(problem_text_line1, problem_text_line2, boat_speed_kmh, river_speed_kmh, conversion_text, title, boat_arrow)
    def ball_throw_and_horizontal_velocity(self, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY):
        boat_rect = self.nl_mobjects[0] # Get boat from previous scene
        river_rect = self.nl_mobjects[1]
        downstream_calc = self.nl_mobjects[2]
        man_square = Square(side_length=0.7, color=BLUE_E, fill_opacity=0.8).next_to(boat_rect, UP, buff=0.1)
        ball_dot = Dot(radius=0.15, color=SECONDARY_COLOR).next_to(man_square, UP, buff=0.1)
        u_y_arrow = Arrow(ball_dot.get_center(), ball_dot.get_center() + UP*1.5, color=SECONDARY_COLOR, buff=0).set_stroke(width=6)
        u_y_label = Text("u_y = 10 m/s", font_size=24, color=SECONDARY_COLOR).next_to(u_y_arrow, RIGHT, buff=0.2)
        observer_dot = Dot(color=RED).shift(DOWN * 2 + LEFT * 5)
        observer_text = Text("बैंक पर दर्शक", font_size=20, color=RED).next_to(observer_dot, UP)
        ball_horizontal_velocity_text = Text("गेंद को नाव की क्षैतिज गति मिलती है", font_size=28, color=LIGHT_GRAY).shift(UP*1.5 + RIGHT*3)
        u_x_label = Text("u_x = 10 m/s", font_size=24, color=ACCENT_COLOR).next_to(downstream_calc, DOWN, buff=0.5)
        with self.voiceover(text="इसी नाव में बैठा एक आदमी एक गेंद को 10 मीटर प्रति सेकंड की गति से लंबवत ऊपर की ओर फेंकता है। ध्यान दें, यह गति नाव के सापेक्ष है। नाव गतिशील है, इसलिए बैंक पर खड़ा एक दर्शक गेंद को कैसे देखेगा? बैंक पर खड़े दर्शक के लिए, गेंद के पास नाव की क्षैतिज गति भी होगी।") as tracker:
            self.play(FadeIn(man_square, ball_dot), run_time=tracker.duration * 0.2)
            self.play(GrowArrow(u_y_arrow), FadeIn(u_y_label), run_time=tracker.duration * 0.3)
            self.play(FadeIn(observer_dot, observer_text), run_time=tracker.duration * 0.2)
            self.play(FadeIn(ball_horizontal_velocity_text), run_time=tracker.duration * 0.3)
        with self.voiceover(text="यानी, गेंद की क्षैतिज गति 10 मीटर प्रति सेकंड होगी। और उसकी ऊर्ध्वाधर गति 10 मीटर प्रति सेकंड होगी, जो ऊपर की ओर है।") as tracker:
            self.play(FadeIn(u_x_label), run_time=tracker.duration)
            self.wait(0.5)
            self.play(FadeOut(man_square, ball_dot, u_y_arrow, u_y_label, observer_dot, observer_text, ball_horizontal_velocity_text, downstream_calc))
            self.remove(boat_rect, river_rect) # Clear for next scene
    def time_of_flight_calculation(self, PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY):
        vertical_title = Text("चरण 1: उड़ान का समय (ऊर्ध्वाधर गति)", font_size=36, color=PRIMARY_COLOR).to_edge(UP)
        uy_val = Text("u_y = 10 m/s", font_size=28, color=TEXT_COLOR).shift(UP*1.5 + LEFT*3)
        ay_val = Text("a_y = -g = -10 m/s^2", font_size=28, color=TEXT_COLOR).next_to(uy_val, DOWN, buff=0.3)
        sy_val = Text("s_y = 0 (समान ऊर्ध्वाधर स्तर)", font_size=28, color=TEXT_COLOR).next_to(ay_val, DOWN, buff=0.3)
        equation_1 = Text("s_y = u_y * t + 0.5 * a_y * t^2", font_size=32, color=WHITE).next_to(sy_val, DOWN, buff=0.8)
        calculation_1 = Text("0 = 10 * t + 0.5 * (-10) * t^2", font_size=32, color=WHITE).next_to(equation_1, DOWN)
        calculation_2 = Text("0 = 10t - 5t^2", font_size=32, color=WHITE).next_to(calculation_1, DOWN)
        calculation_3 = Text("0 = t (10 - 5t)", font_size=32, color=WHITE).next_to(calculation_2, DOWN)
        result_t = Text("t = 2 seconds", font_size=36, color=ACCENT_COLOR, weight=BOLD).next_to(calculation_3, DOWN, buff=0.8)
        with self.voiceover(text="अब गेंद के ऊर्ध्वाधर गति पर ध्यान देते हैं ताकि हम उसका उड़ान समय निकाल सकें। प्रारंभिक ऊर्ध्वाधर गति 10 मीटर प्रति सेकंड है, गुरुत्वाकर्षण के कारण त्वरण -10 मीटर प्रति सेकंड वर्ग है, और ऊर्ध्वाधर विस्थापन शून्य है क्योंकि गेंद उसी स्तर पर वापस आती है जहाँ से फेंकी गई थी।") as tracker:
            self.play(FadeIn(vertical_title), run_time=tracker.duration * 0.1)
            self.play(FadeIn(uy_val, ay_val, sy_val), run_time=tracker.duration * 0.4)
            self.play(Write(equation_1), run_time=tracker.duration * 0.5)
        with self.voiceover(text="गति के दूसरे समीकरण, s = ut + ½ at² का उपयोग करके, हम पाते हैं: 0 = 10t - 5t²। इसे हल करने पर, हमें उड़ान का समय 2 सेकंड मिलता है। यह वह समय है जब तक गेंद हवा में रहती है।") as tracker:
            self.play(Write(calculation_1), run_time=tracker.duration * 0.25)
            self.play(Write(calculation_2), run_time=tracker.duration * 0.25)
            self.play(Write(calculation_3), run_time=tracker.duration * 0.25)
            self.play(Write(result_t), run_time=tracker.duration * 0.25)
            self.wait(0.5)
            self.add_to_nl(vertical_title, result_t) # Keep for transformation
            self.remove(uy_val, ay_val, sy_val, equation_1, calculation_1, calculation_2, calculation_3)
    def range_calculation(self, PRIMARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY):
        vertical_title = self.nl_mobjects[0]
        result_t = self.nl_mobjects[1]
        horizontal_title = Text("चरण 2: क्षैतिज रेंज (क्षैतिज गति)", font_size=36, color=PRIMARY_COLOR).to_edge(UP)
        ux_val_new = Text("u_x = 10 m/s", font_size=28, color=TEXT_COLOR).shift(UP*1.5 + LEFT*3)
        time_val_new = Text("उड़ान का समय (t) = 2 seconds", font_size=28, color=TEXT_COLOR).next_to(ux_val_new, DOWN, buff=0.3)
        range_equation = Text("रेंज (R) = u_x * t", font_size=32, color=WHITE).next_to(time_val_new, DOWN, buff=0.8)
        range_calculation = Text("R = 10 m/s * 2 s", font_size=32, color=WHITE).next_to(range_equation, DOWN)
        range_result_m = Text("R = 20 meters", font_size=36, color=ACCENT_COLOR, weight=BOLD).next_to(range_calculation, DOWN, buff=0.8)
        with self.voiceover(text="अब हम क्षैतिज गति की ओर बढ़ते हैं। क्षैतिज गति 10 मीटर प्रति सेकंड है, और हमने अभी गणना की है कि उड़ान का समय 2 सेकंड है। चूंकि क्षैतिज दिशा में कोई त्वरण नहीं है, हम रेंज की गणना सीधे कर सकते हैं।") as tracker:
            self.play(Transform(vertical_title, horizontal_title), run_time=tracker.duration * 0.1)
            self.play(FadeIn(ux_val_new), Transform(result_t, time_val_new), run_time=tracker.duration * 0.4)
            self.play(Write(range_equation), run_time=tracker.duration * 0.5)
        with self.voiceover(text="रेंज बराबर होती है क्षैतिज गति गुणा उड़ान का समय। तो, 10 मीटर प्रति सेकंड गुणा 2 सेकंड, हमें 20 मीटर की रेंज मिलती है।") as tracker:
            self.play(Write(range_calculation), run_time=tracker.duration * 0.5)
            self.play(Write(range_result_m), run_time=tracker.duration * 0.5)
            self.wait(0.5)
            self.add_to_nl(horizontal_title, range_result_m) # Keep for next scene
            self.remove(ux_val_new, time_val_new, range_equation, range_calculation, result_t)
    def conclusion(self, PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, TEXT_COLOR, LIGHT_GRAY):
        horizontal_title = self.nl_mobjects[0]
        range_result_m = self.nl_mobjects[1]
        final_conversion_text = Text("सेंटीमीटर में परिवर्तन:", font_size=36, color=LIGHT_GRAY).to_edge(UP)
        conversion_calc = Text("R = 20 मीटर * 100 cm/मीटर", font_size=32, color=WHITE).next_to(final_conversion_text, DOWN, buff=0.8)
        final_answer_text = Text("रेंज (R) = 2000 cm", font_size=48, color=SECONDARY_COLOR, weight=BOLD).next_to(conversion_calc, DOWN, buff=1)
        check_mark = Checkmark(color=SECONDARY_COLOR).next_to(final_answer_text, LEFT, buff=0.5)
        thank_you_text = Text("धन्यवाद!", font_size=40, color=ACCENT_COLOR).to_edge(DOWN)
        with self.voiceover(text="समस्या में हमसे रेंज सेंटीमीटर में पूछी गई थी। इसलिए, हमें 20 मीटर को सेंटीमीटर में बदलना होगा। 20 मीटर गुणा 100 सेंटीमीटर प्रति मीटर, हमें 2000 सेंटीमीटर मिलता है।") as tracker:
            self.play(Transform(horizontal_title, final_conversion_text), run_time=tracker.duration * 0.2)
            self.play(Transform(range_result_m, conversion_calc), run_time=tracker.duration * 0.8) # Transform old result to new calculation
        with self.voiceover(text="तो, बैंक पर खड़े दर्शक द्वारा देखी गई गेंद की रेंज 2000 सेंटीमीटर है। मुझे उम्मीद है कि आपको यह स्पष्टीकरण पसंद आया होगा। सीखते रहें, बढ़ते रहें! धन्यवाद!") as tracker:
            self.play(Write(final_answer_text), run_time=tracker.duration * 0.4)
            self.play(Create(check_mark), run_time=tracker.duration * 0.2)
            self.play(FadeIn(thank_you_text), run_time=tracker.duration * 0.4)
            self.wait(0.5)