import unittest
from arbitrary_arithmetic import *

class ArbitraryArithmeticTest(unittest.TestCase):

  def testZipAdd(self):
    self.assertEqual(zip_add([], []), (0, []))
    self.assertEqual(zip_add([1],[1]), (0, [2]))
    self.assertEqual(zip_add([1],[9]), (1, [0]))

  def testZipAddWarnsWhenArrayLengthsDifferent(self):
    with self.assertRaises(ValueError):
      zip_add([1,2], [1])

  def testRippleCarry(self):
    self.assertEqual(rippleCarry([1, 11]),(0, [2, 1])) 
    self.assertEqual(rippleCarry([0]), (0, [0])) 
    self.assertEqual(rippleCarry([1,2]), (0, [1,2])) 
    self.assertEqual(rippleCarry([42,2]), (4, [2,2])) 
    self.assertEqual(rippleCarry([2,342]), (3, [6,2])) 
    self.assertEqual(rippleCarry([1, 2,53342]), (53, [4,6,2])) 
    self.assertEqual(rippleCarry([642,2]), (64, [2,2])) 
    self.assertEqual(rippleCarry([100]), (10, [0])) 

  def testPrependZeroes(self):
    self.assertEqual(prependZeroes([1], [2,0,0,0,0,0]), ([0,0,0,0,0,1], [2,0,0,0,0,0]))
    self.assertEqual(prependZeroes([2,0,0,0,0,0], [1]), ([2,0,0,0,0,0], [0,0,0,0,0,1]))
    self.assertEqual(prependZeroes([1], [1]), ([1], [1]))
    self.assertEqual(prependZeroes([], [1]), ([0], [1]))

if __name__ == '__main__':
    unittest.main()
