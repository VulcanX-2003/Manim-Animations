from manim import*
import math
class Design(Scene):
    def construct(self):
        ax = Axes(x_range=[-10,10],y_range=[-4,4])
        curve = ax.plot(lambda t:(math.cos(t) + math.cos(6*t)/2 + math.sin(14*t)/3 + math.sin(t) + math.sin(6*t)/2 + math.cos(14*t)/3),color = GREEN)
        self.play(Create(ax, run_time=2))
        self.play(Create(curve, run_time=5))
        self.wait(2)