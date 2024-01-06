from manim import *


class CreateFlow(Scene):
    def construct(self):
      rect1_start = Rectangle(width=1.0, height=5.0)
      rect1_start.set_color(ORANGE)
      rect1_start.set_fill(ORANGE, opacity=0.8)

      rect2_start = Rectangle(width=1.0, height=2.0)
      rect2_start.set_color(BLUE)
      rect2_start.set_fill(BLUE, opacity=0.8)

      rect1_start.shift(LEFT).shift(LEFT).shift(LEFT)
      rect2_start.shift(RIGHT).shift(RIGHT).shift(RIGHT)
      rect2_start.align_to(rect1_start, direction=DOWN)

      rect1_end = Rectangle(width=1.0, height=2.0)
      rect1_end.set_color(ORANGE)
      rect1_end.set_fill(ORANGE, opacity=0.8)
      rect1_end.shift(LEFT).shift(LEFT).shift(LEFT)
      rect1_end.align_to(rect1_start, direction=DOWN)

      self.add(rect1_start)
      self.add(rect2_start)
      self.wait(2)
      self.play(Transform(rect1_start, rect1_end))
      self.wait(3)
