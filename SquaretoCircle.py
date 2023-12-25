from manim import *

class SquaretoCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK,opacity=0.6)

        square = Square()
        square.set_fill(GREEN,opacity=0.6)

        self.play(Create(circle),run_time = 2)
        self.play(Transform(circle,square),  run_time=2)
        