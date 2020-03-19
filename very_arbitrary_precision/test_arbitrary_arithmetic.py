import unittest
from arbitrary_arithmetic import *

class ArbitraryArithmeticTest(unittest.TestCase):

  def testZipAdd(self):
    self.assertEqual(zip_add([]), (0, []))
    self.assertEqual(zip_add([], []), (0, []))
    self.assertEqual(zip_add([1],[1]), (0, [2]))
    self.assertEqual(zip_add([1],[9]), (1, [0]))
    self.assertEqual(zip_add([1],[9],[1]), (1, [1]))
    self.assertEqual(zip_add([8],[8],[8]), (2, [4]))

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
    self.assertEqual(prependZeroes([1], 5), [0,0,0,0,0,1])
    self.assertEqual(prependZeroes([1,1], 1), [0,1,1])
    self.assertEqual(prependZeroes([1], 0), [1])
    self.assertEqual(prependZeroes([1], -1), [1])

  def testAppendZeroes(self):
    self.assertEqual(appendZeroes([1], 5), [1,0,0,0,0,0])
    self.assertEqual(appendZeroes([1,1], 1), [1,1,0])
    self.assertEqual(appendZeroes([1], 0), [1])
    self.assertEqual(appendZeroes([1], -1), [1])

  def testHydratePowers(self):
    self.assertEqual(hydratePowers([1, 2, 3]), [100, 20, 3])
    self.assertEqual(hydratePowers([3]), [3])

  def testRemovePowers(self):
    self.assertEqual(removePowers([100, 20, 3]), [1, 2, 3])
    self.assertEqual(type(removePowers([100, 20, 3])[0]), int)

  def testExpand(self):
    self.assertEqual(expand([3,2,5], [1,2,3]), [[3,6,9,0,0], [2,4,6,0], [5,10,15]])

  def testExpandOptimizationForLongMultiplier(self):
    self.assertEqual(expand([1,1,1,1,1,1,1,1,1,1], [1]), [[1,1,1,1,1,1,1,1,1,1]])
    self.assertEqual(expand([1], [1,1,1,1,1,1,1,1,1,1]), [[1,1,1,1,1,1,1,1,1,1]])

if __name__ == '__main__':
    unittest.main()
