import unittest
from functools import reduce


def add(a, b):

  c, d = (prependZeroes(a, len(b)-len(a)), prependZeroes(b, len(a)-len(b)))

  return [ x+y for x, y in zip(c, d) ]


################################################################################
# helper functions
def prependZeroes(a, num_zeroes):
  # itertools.repeat wd be faster but repeatability is more impt to me than speed
   return [0] * num_zeroes + a

################################################################################
class TestBig(unittest.TestCase):

  def testPrependZeroesIgnoresNegative(self):
    self.assertEqual(prependZeroes([1,2], -1), [1,2])

  def testPrependZeroes(self):
    self.assertEqual(prependZeroes([1], 5), [0,0,0,0,0,1])
    self.assertEqual(prependZeroes([1,2], 1), [0,1,2])
    self.assertEqual(prependZeroes([1,2], 0), [1,2])
    self.assertEqual(prependZeroes([], 1), [0])

  def testAdd(self):
    self.assertEqual(add([1],[1]), [2])
    self.assertEqual(add([1,2,3],[1]), [1,2,4])
    self.assertEqual(add([1],[1,2,3]), [1,2,4])
    self.assertEqual(add([1,2,3],[1,2,3]), [2,4,6])
    self.assertEqual(add([3,0,0],[1,2,3]), [2,2,3])

  @unittest.skip
  def testAddHandlesEmpties(self):
    self.assertEqual(add([], []), [0])
    self.assertEqual(add([1], []), [1])
    self.assertEqual(add([], [1]), [1])
if __name__ == '__main__':
    unittest.main()
