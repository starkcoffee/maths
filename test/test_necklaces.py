import pytest
from maths.necklaces import *

def test_generate_tree_breadth_first():
  assert generate_tree_breadth_first(['A','B','C'], 0) == []
  assert generate_tree_breadth_first(['A','B','C'], 1) == [('A',),('B',),('C',)]
  assert generate_tree_breadth_first(['A','B'], 2) == [('A','A'),('A','B'),('B','A'),('B','B')]
  assert generate_tree_breadth_first(['A','B','C'], 3)[9] == ('B','A','A')

def test_generate_tree_depth_first():
  assert generate_tree_depth_first(['A','B','C'], 0) == []
  assert generate_tree_depth_first(['A','B','C'], 1) == [('A',),('B',),('C',)]
  assert generate_tree_depth_first(['A','B'], 2) == [('A','A'),('A','B'),('B','A'),('B','B')]
  assert generate_tree_depth_first(['A','B','C'], 3)[9] == ('B','A','A')

def test_necklaces():
  assert necklaces('ABC', 0) == {}
  assert necklaces('ABC', 1) == {'A', 'B', 'C'}
  assert necklaces('ABC', 2) == {'AA', 'AB', 'AC','BB','BC','CC'}
  assert necklaces('ABC', 3) == {'AAA','AAB','AAC','ABB','ABC','ACB','ACC','BBB','BBC','BCC','CCC'}

def test_rotations():
  assert rotations(('A','B','C')) == {('A','B','C'), ('B','C','A'), ('C','A','B')}
  assert rotations(('B','C','A')) == {('A','B','C'), ('B','C','A'), ('C','A','B')}
  assert rotations(('C','A','B')) == {('A','B','C'), ('B','C','A'), ('C','A','B')}
  assert rotations(('A',)) == {('A',)}
