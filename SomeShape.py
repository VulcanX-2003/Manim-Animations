from manim import*
import math
class SomeShape(Scene):
    def construct(self):
        ax = Axes(x_range=(-5, 5), y_range=(-5, 5),z_range =(-5,5), color=YELLOW)
        curve = ax.plot(lambda t: math.sin(t), color=GREEN)
        curve2 = ax.plot(lambda t: math.sin(t/2)+math.cos(t*t)+math.tanh(t), color=RED)
        self.play(Create(ax, run_time=2))
        self.play(Create(curve2, run_time=10), Create(curve, run_time=10))
        self.wait(2)