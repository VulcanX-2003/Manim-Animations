from manim import *

class Flower2(Scene):
    def construct(self):
        # Create petals for the flower
        num_petals = 10
        petal_radius = 2
        petal_color = BLUE_A
        
        petals = VGroup()
        for i in range(num_petals):
            angle = i * 360 / num_petals
            petal = self.create_petal(angle, petal_radius, petal_color)
            petals.add(petal)
            self.play(Create(petal))
        self.wait(2)

    def create_petal(self, angle, radius, color):
        petal = ParametricFunction(
            lambda t: np.array([
                radius * np.cos(t*3)+np.sin(t/2),
                radius * np.sin(t/2),
                0
            ]),
            t_range=[0, PI],
        )

        petal.rotate(angle * DEGREES)
        petal.set_color(color)

        return petal
