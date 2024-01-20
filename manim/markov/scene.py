from manim import *
from np import array

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

    path3 = Arc(radius=0.5, start_angle=(335/360)*2*PI, angle=(265/360)*2*PI, num_components=6, arc_center=array([0,0,0]))
    path3.add_tip()
    path4 = path3.copy().flip()

    path3.shift(3.5*LEFT).shift(1.3*UP)
    path4.center().shift(3.5*RIGHT).shift(1.47*UP)

    d1 = Dot().set_color(ORANGE)
    d2 = Dot().set_color(BLUE)
    d3 = Dot().set_color(ORANGE)
    d4 = Dot().set_color(BLUE)

    d1_movement = MoveAlongPath(d1, path1)
    d2_movement = MoveAlongPath(d2, path2)
    d3_movement = MoveAlongPath(d3, path3)
    d4_movement = MoveAlongPath(d4, path4)

    self.add(node1, node2)
    self.add(path1, path2, path3, path4)
    self.wait(1)
    for i in range(10):
      if i%2==0:
        self.play(d1_movement, d2_movement, d3_movement, d4_movement, rate_func=linear, run_time=1.5)
      else:
        self.play(d1_movement, d2_movement, rate_func=linear, run_time=1.5)

    

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
