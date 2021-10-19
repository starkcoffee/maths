import pytest
from math import nan
from collections import defaultdict

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

  # handle vertical lines
  if m == None:
    return x == c

  try:
    m1 = (y - c)/x
    return round(m1,6) == round(m,6)
  except ZeroDivisionError:
    return True

class Galaxy: 
  
  def __init__(self):
    self.points = set()
    self.lines = {}
    self.sightLineCounts = defaultdict(lambda: 0)

  def add_new_line(self, p1, p2):
    line = line_eqn(p1, p2)
    self.lines[line] = sorted([p1,p2])
    self.sightLineCounts[p1] += 1
    self.sightLineCounts[p2] += 1

  # line represented as (m, c)
  def add_to_existing_line(self, p, line):
    points_on_line = self.lines[line]

    points_on_line = sorted(points_on_line + [p])
    self.lines[line] = points_on_line

    p_index = points_on_line.index(p)
    self.sightLineCounts[p] += 1
    if p_index == 0:
      self.sightLineCounts[points_on_line[1]] += 1
    elif p_index == len(points_on_line) - 1:
      self.sightLineCounts[points_on_line[p_index-1]] += 1
    else:
      self.sightLineCounts[p] += 1

  def add_point(self, point):
    points_to_exclude_when_building_new_lines = [point]
    for line in self.lines:
        print(line)
        if is_on_line(line, point):
          points_to_exclude_when_building_new_lines += self.lines[line]
          self.add_to_existing_line(point, line)

    for p_other in set(self.points) - set(points_to_exclude_when_building_new_lines):
      self.add_new_line(point, p_other)
    self.points.add(point)

  def station_candidate(self):
    return max(self.sightLineCounts, key=lambda k: self.sightLineCounts[k])

def find_station_candidate(inputt):
  points = parse(inputt)
  g = Galaxy()
  for point in points:
    g.add_point(point)
  print(g.sightLineCounts)
  return g.station_candidate()

def test_find_station_candidate():
  inputt = '''
.#..#
.....
#####
'''
  assert find_station_candidate(inputt) == (3,4)
 
def test_station_candidate_when_single():
  g = Galaxy()
  g.add_new_line((1,1),(3,3))
  g.add_to_existing_line((2,2), (1,0))

  assert g.station_candidate() == (2,2)

def test_station_candidate_when_multiple():
  g = Galaxy()
  g.add_new_line((1,1),(3,3))

  assert g.station_candidate() == (1,1)

def test_add_to_existing_line_inc_sightlines_correctly_when_point_not_on_end_of_line():
  g = Galaxy()
  g.add_new_line((1,1),(3,3))

  g.add_to_existing_line((2,2), (1,0))

  assert g.sightLineCounts[(1,1)] == 1
  assert g.sightLineCounts[(2,2)] == 2
  assert g.sightLineCounts[(3,3)] == 1

def test_add_to_existing_line_inc_sightlines_correctly_when_point_at_beginning_of_line():
  g = Galaxy()
  g.add_new_line((2,2),(3,3))

  g.add_to_existing_line((1,1), (1,0))

  assert g.sightLineCounts[(1,1)] == 1
  assert g.sightLineCounts[(2,2)] == 2
  assert g.sightLineCounts[(3,3)] == 1

def test_add_to_existing_line_inc_sightlines_correctly_when_point_at_end_of_line():
  g = Galaxy()
  g.add_new_line((1,1),(2,2))

  g.add_to_existing_line((3,3), (1,0))

  assert g.sightLineCounts[(1,1)] == 1
  assert g.sightLineCounts[(2,2)] == 2
  assert g.sightLineCounts[(3,3)] == 1

def test_add_to_existing_line_adds_point_to_points_on_line_in_order():
  g = Galaxy()
  g.add_new_line((1,1),(3,3))

  g.add_to_existing_line((2,2), (1,0))

  assert g.lines[(1,0)] == [(1,1),(2,2),(3,3)]

def test_add_new_line_adds_new_line_to_galaxy():
  g = Galaxy()

  g.add_new_line((1,1),(3,3))

  assert g.lines[(1,0)] == [(1,1),(3,3)]
  assert g.sightLineCounts[(1,1)] == 1
  assert g.sightLineCounts[(3,3)] == 1

def test_add_new_line_stores_points_in_sorted_order():
  g = Galaxy()

  g.add_new_line((3,3),(1,1))

  assert g.lines[(1,0)] == [(1,1),(3,3)]

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

