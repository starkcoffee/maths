import pytest
from math import nan

def parse(inputt):
  lines = inputt.split('\n')
  non_empty_lines = filter(lambda line: line != "", lines)
  return [ 
    (x, y) 
    for y, line in enumerate(non_empty_lines)
    for x, val in enumerate(line)
    if val == '#'
  ]

# returns (m, c) which represents the line defined by two points
# where y = mx + c
# except when its a vertical line, then m=None and c=x
def line_eqn(p1, p2):
  (p1_x, p1_y), (p2_x, p2_y) = p1, p2

  try:
    m = (p2_y - p1_y)/(p2_x - p1_x) 
    # using the fact that m = (p1_y - y)/(p1_x - x) and when x=0, y=c :
    c = (p1_y - m*p1_x)
  except ZeroDivisionError:
    m = None
    c = p1_x

  return m, c

def is_on_line(line, point):
  x, y = point
  m, c = line

  if m == None:
    return x == c

  try:
    m1 = (y - c)/x
    print(m1)
    return m1 == m
  except ZeroDivisionError:
    return True

def test_is_on_line():
  assert is_on_line((1,0), (3,3))
  assert is_on_line((1,0), (1,1))
  assert is_on_line((1,0), (0,0))
  assert is_on_line((-1.3333333333333333, 10.666666666666666), (5,4))
  assert is_on_line((-1.3333333333333333, 10.666666666666666), (2,8))

def test_line_eqn():
  assert line_eqn((3,3),(1,1)) == (1, 0)
  assert line_eqn((1,1),(3,3)) == (1, 0)
  #TODO how many fp digits do i need to adquately cover all possible lines in the grid?
  # for now I will use ALL OF THEM
  assert line_eqn((5,4),(2,8)) == (-1.3333333333333333, 10.666666666666666)
  assert line_eqn((3,3),(3,1)) == (None, 3)

def test_parse():
  inputt = '''
.#..#
.....
#####
....#
...##
'''
  assert parse(inputt) == [
    (1,0),(4,0),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (4,3),
    (3,4),(4,4)
  ]

