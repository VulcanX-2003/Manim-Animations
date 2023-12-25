from manim import*

class SecondExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-10, 10), y_range=(-10, 10))
        curve = ax.plot(lambda x: (x+4)*(x+2)*x*(x-2)/2, color=BLUE)
        area = ax.get_area(curve, x_range=(-2, 0))
        self.play(Create(ax, run_time=2), Create(curve, run_time=10))
        self.play(FadeIn(area))
        self.wait(2)