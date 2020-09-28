import pytest

def parse(inputt):
  lines = inputt.split('\n')
  non_empty_lines = filter(lambda line: line != "", lines)
  return [ 
    (x, y) 
    for y, line in enumerate(non_empty_lines)
    for x, val in enumerate(line)
    if val == '#'
  ]

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


