from manim import *
from np import array

class Library(Scene):
  def construct(self):

    library1 = create_library(ORANGE)
    library2 = create_library(BLUE)
    library1.shift(3*LEFT)
    library2.shift(3*RIGHT)

    self.add(library1)
    self.add(library2)
    self.wait(2)

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

    self.play(Transform(library1, node1), Transform(library2, node2))
    self.play(Create(path1))
    self.play(Create(path2))
    self.play(Create(path3))
    self.play(Create(path4))

    self.wait(2)


  def construct_state_diagram(self):
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

# returns a Group MObject that is a library
def create_library(color):

    building = Rectangle(color=color, fill_opacity=0, height=1.5, width=2)
    window = Rectangle(color=color, fill_opacity=0, height=0.5, width=0.3)
    windows = Group(window, window.copy(), window.copy(), window.copy()).arrange(buff=0.15)
    windows.shift(0.3*UP)
    door = Rectangle(color=color, fill_opacity=1, height=0.5, width=0.4)
    door.align_to(building, DOWN)

    return Group(building, windows, door)
 


