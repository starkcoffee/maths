from manim import *


class CreateFlow(Scene):
    def construct(self):
      rect1 = Rectangle(width=1.0, height=4.0)
      rect1.set_color(ORANGE)
      rect1.set_fill(ORANGE, opacity=0.8)
      rect2 = Rectangle(width=1.0, height=2.0)
      rect2.set_color(BLUE)
      rect2.set_fill(BLUE, opacity=0.8)

      rect1.shift(LEFT).shift(LEFT)
      rect2.shift(RIGHT).shift(RIGHT)
      rect2.align_to(rect1, direction=DOWN)

      self.add(rect1)
      self.add(rect2)
      self.wait(5)
