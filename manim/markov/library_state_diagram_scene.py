from manim import *
from np import array

class Library(Scene):
  def construct(self):
    
    library1, library2 = self.create_libraries()
    self.wait(1)

    book = self.create_book()
    self.move_book_in_and_out_of_libraries(book, library1, library2)
    self.wait(2)

    return

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

    self.play(MoveAlongPath(book,lineExitLibrary2), run_time=0.5)
    self.wait(0.12)
    self.play(MoveAlongPath(book,lineReenterLibrary2), run_time=0.5)
    self.wait(0.12)
    self.remove(book)
    self.wait(0.25)

    self.play(MoveAlongPath(book,lineExitLibrary2), run_time=0.5)
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



