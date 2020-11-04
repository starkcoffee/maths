import pytest
from maths.factors import *
from maths.necklaces import factors

def test_num_factors():
  assert num_factors([1]) == len(factors(13))
  assert num_factors([1,1,1]) == len(factors(2*3*5))
  assert num_factors([6,3,5,2]) == len(factors(2**6*3**3*5**5*7**2))
