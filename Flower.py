from manim import*
import numpy as np
class Flower(Scene):
    def construct(self):
        ax = Axes(x_range=[-5,5],y_range=[-10,10])
        a,b,k = 2,3,0.5
        equation = ax.plot(lambda q: a * np.sin(k * q) + b, color = BLUE)
        self.play(Create(ax, run_time=2))
        self.play(Create(equation, run_time=2))
