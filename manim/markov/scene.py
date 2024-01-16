from manim import *

class GraphDiagram(Scene):
  def construct(self):

    node1 = Circle(color=ORANGE, fill_opacity=1)
    node1.shift(3*LEFT)

    node2 = Circle(color=BLUE, fill_opacity=1)
    node2.shift(3*RIGHT)

    path1 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -3.5)
    path1.shift(0.5*UP)

    path2 = CurvedArrow(2*RIGHT, 2*LEFT, radius= -3.5)
    path2.shift(0.5*DOWN)

    self.add(node1)
    self.add(node2)
    self.add(path1)
    self.add(path2)
    self.wait(3)
    

class NumBooksBarChart(Scene):
  def construct(self):
    rect1_start = Rectangle(width=1.0, height=5.0)
    rect1_start.set_color(ORANGE)
    rect1_start.set_fill(ORANGE, opacity=0.8)

    rect2_start = Rectangle(width=1.0, height=2.0)
    rect2_start.set_color(BLUE)
    rect2_start.set_fill(BLUE, opacity=0.8)

    rect1_start.move_to(LEFT * 3)
    rect2_start.move_to(RIGHT * 3)
    rect2_start.align_to(rect1_start, direction=DOWN)

    rect1_end = Rectangle(width=1.0, height=2.0)
    rect1_end.set_color(ORANGE)
    rect1_end.set_fill(ORANGE, opacity=0.8)
    rect1_end.move_to(LEFT * 3)
    rect1_end.align_to(rect1_start, direction=DOWN)

    self.add(rect1_start)
    self.add(rect2_start)
    self.wait(2)
    self.play(Transform(rect1_start, rect1_end), run_time=3)
    self.wait(3)
