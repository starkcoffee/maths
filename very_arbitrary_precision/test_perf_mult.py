import unittest
import timeit
from anum import *

class PerfMultTest(unittest.TestCase):

  def testLargeMult1(self):
    largeMult = lambda: Anum([5]) * Anum([1] + [0]*1000) 
    result = timeit.timeit(largeMult, number=10) 
    print(result)

  def testLargeMult2(self):
    largeMult = lambda: Anum([1] + [0]*1000) * Anum([5,0])
    result = timeit.timeit(largeMult, number=10) 
    print(result)

  def testLargeZeroes(self):
    largeMult = lambda: Anum([1] + [0]*100) * Anum([1] + [0]*100)
    result = timeit.timeit(largeMult, number=10) 
    print(result)

if __name__ == '__main__':
    unittest.main()

