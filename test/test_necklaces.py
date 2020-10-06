import pytest
from maths.necklaces import *

def test_necklace_count_v2():
  assert necklace_count_v2(3,1) == 3
  assert necklace_count_v2(3,2) == 6
  assert necklace_count_v2(3,3) == 11
  assert necklace_count_v2(4,6) == 700
  assert necklace_count_v2(3,4) == necklace_count(3,4)
  assert necklace_count_v2(5,8) == necklace_count(5,8)

def test_permutations_with_repeating_unit_of():
  assert num_permutations_with_repeating_unit(3, 1) == 3
  assert num_permutations_with_repeating_unit(3, 2) == 6
  assert num_permutations_with_repeating_unit(3, 3) == 24
  assert num_permutations_with_repeating_unit(3, 4) == 72

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
  assert {''.join(n) for n in necklaces('ABC', 0)} == {''}
  assert {''.join(n) for n in necklaces('ABC', 1)} == {'A', 'B', 'C'}
  assert {''.join(n) for n in necklaces('ABC', 2)} == {'AA', 'AB', 'AC','BB','BC','CC'}
  assert {''.join(n) for n in necklaces('ABC', 3)} == {'AAA','AAB','AAC','ABB','ABC','ACB','ACC','BBB','BBC','BCC','CCC'}

def test_rotations():
  assert rotations(('A','B','C')) == {('A','B','C'), ('B','C','A'), ('C','A','B')}
  assert rotations(('B','C','A')) == {('A','B','C'), ('B','C','A'), ('C','A','B')}
  assert rotations(('C','A','B')) == {('A','B','C'), ('B','C','A'), ('C','A','B')}
  assert rotations(('A',)) == {('A',)}
