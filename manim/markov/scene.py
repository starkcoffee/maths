from manim import *

class GraphDiagram(Scene):
  def construct(self):
    d, s = ("Dirac", "Strozier")
    vertices = [d, s]
    edges = [(d,s), (s,d)]
    edge_config = {
      "stroke_width": 2,
      "tip_config": {"tip_length": 0.25, "tip_width": 0.25},
    }

    g = DiGraph(
      vertices,
      edges,
      edge_type=mobject.geometry.arc.CurvedDoubleArrow,
      labels=True,
      #edge_config=edge_config,
    ).scale(1.4)

    self.add(g)
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
