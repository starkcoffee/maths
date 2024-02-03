from manim import *
from np import array

class Library(Scene):
  def construct(self):
    
    library1, library2 = self.create_libraries()
    self.wait(1)

    book = self.create_book()
    self.move_book_in_and_out_of_libraries(book, library1, library2)
    self.wait(2)

    self.morph_libraries_into_nodes(library1, library2)
    self.wait(2)

    self.draw_paths_with_probabilities()
    self.wait(2)

  def draw_paths_with_probabilities(self):
    node1to1 = Arc(radius=0.5, start_angle=(335/360)*2*PI, angle=(265/360)*2*PI, num_components=6, arc_center=array([0,0,0]))
    node1to1.add_tip()
    node1to1.shift(3.5*LEFT).shift(1.3*UP)
    node1to1_label = Text("0.8").next_to(node1to1, LEFT)

    node1to2 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -3.5)
    node1to2.shift(0.5*UP)
    node1to2_label = Text("0.2").next_to(node1to2, UP)

    node2to2 = node1to1.copy().flip()
    node2to2.center().shift(3.5*RIGHT).shift(1.47*UP)
    node2to2_label = Text("0.6").next_to(node2to2, RIGHT)

    node2to1 = CurvedArrow(2*RIGHT, 2*LEFT, radius= -3.5)
    node2to1.shift(0.5*DOWN)
    node2to1_label = Text("0.4").next_to(node2to1, DOWN)

    self.play(Create(node1to1))
    self.add(node1to1_label)
    self.play(Create(node1to2))
    self.add(node1to2_label)
    self.wait(1)
    self.play(Create(node2to2))
    self.add(node2to2_label)
    self.play(Create(node2to1))
    self.add(node2to1_label)

    return node1to1, node1to2, node2to2, node2to1

  def morph_libraries_into_nodes(self, library1, library2):
    node1 = Circle(color=ORANGE, fill_opacity=1)
    node1.shift(3*LEFT)

    node2 = Circle(color=BLUE, fill_opacity=1)
    node2.shift(3*RIGHT)

    self.play(Transform(library1, node1), Transform(library2, node2))
    return node1, node2

  def create_libraries(self):
    library1 = self.create_library(ORANGE)
    library2 = self.create_library(BLUE)
    library1.shift(3*LEFT)
    library2.shift(3*RIGHT)
    
    self.add(library1)
    self.add(library2)
    return library1, library2

  def create_book(self):
    book = SVGMobject("emoji_u1f4d5.svg")
    book.scale(0.25)
    return book

  def move_book_in_and_out_of_libraries(self, book, library1, library2):
    lineExitLibrary1 = Line(library1.get_edge_center(DOWN), library1.get_edge_center(DOWN)+DOWN*2)
    lineExitLibrary2 = Line(library2.get_edge_center(DOWN), library2.get_edge_center(DOWN)+DOWN*2)
    lineReenterLibrary1 = Line(lineExitLibrary1.end, lineExitLibrary1.start)
    lineReenterLibrary2 = Line(lineExitLibrary2.end, lineExitLibrary2.start)
    lineEnterLibrary2From1 = Line(lineExitLibrary1.end, lineExitLibrary2.end).add_line_to(lineExitLibrary2.start)
    lineEnterLibrary1From2 = Line(lineExitLibrary2.end, lineExitLibrary1.end).add_line_to(lineExitLibrary1.start)
    
    self.play(MoveAlongPath(book,lineExitLibrary1))
    self.wait(1)
    self.play(MoveAlongPath(book,lineReenterLibrary1))
    self.wait(0.5)
    self.remove(book)
    self.wait(1)

    self.play(MoveAlongPath(book,lineExitLibrary1))
    self.wait(1)
    self.play(MoveAlongPath(book,lineEnterLibrary2From1))
    self.wait(0.5)
    self.remove(book)

    self.wait(1)

    self.play(MoveAlongPath(book,lineExitLibrary2), run_time=0.3)
    self.wait(0.12)
    self.play(MoveAlongPath(book,lineReenterLibrary2), run_time=0.3)
    self.wait(0.12)
    self.remove(book)
    self.wait(0.12)

    self.play(MoveAlongPath(book,lineExitLibrary2), run_time=0.3)
    self.wait(0.12)
    self.play(MoveAlongPath(book,lineEnterLibrary1From2), run_time=0.5)
    self.wait(0.12)
    self.remove(book)

    return

  def create_library(self, color):
    building = Rectangle(color=color, fill_opacity=0, height=1.5, width=2)
    window = Rectangle(color=color, fill_opacity=0, height=0.5, width=0.3)
    windows = Group(window, window.copy(), window.copy(), window.copy()).arrange(buff=0.15)
    windows.shift(0.3*UP)
    door = Rectangle(color=color, fill_opacity=1, height=0.5, width=0.4)
    door.align_to(building, DOWN)

    return Group(building, windows, door)



