import unittest
from anum import *

class AnumTest(unittest.TestCase):

  def testConstructorTreatsEmptyArraysAsZeroes(self):
    n = Anum([], [])
    self.assertEqual(n.w, [0])
    self.assertEqual(n.f, [0])

  def testConstructorSetsFractionToZeroByDefault(self):
    n = Anum([1])
    self.assertEqual(n.w, [1])
    self.assertEqual(n.f, [0])

  def testConstructorStoresWholeAndFractionalPart(self):
    n = Anum([1], [2,3,4])
    self.assertEqual(n.w, [1])
    self.assertEqual(n.f, [2,3,4])

  def testConstructorRemovesTrailingZeroes(self):
    self.assertEqual(Anum([0], [0,1,0]), Anum([0], [0, 1]))
    self.assertEqual(Anum([1], [0,0,0]), Anum([1], [0]))
    self.assertEqual(Anum([0]), Anum([0]))

  def testConstructorRemovesLeadingZeroes(self):
    self.assertEqual(Anum([0,0,1]), Anum([1]))
    self.assertEqual(Anum([0,0,1], [0,0,1]), Anum([1], [0,0,1]))
    self.assertEqual(Anum([0]), Anum([0]))

  def testCanAddWholeNumbersTogether(self):
    self.assertEqual(Anum([]) + Anum([]), Anum([0]))
    self.assertEqual(Anum([1]) + Anum([]), Anum([1]))
    self.assertEqual(Anum([]) + Anum([1]), Anum([1]))

    self.assertEqual(Anum([0]) + Anum([0]), Anum([0]))
    self.assertEqual(Anum([1]) + Anum([1]), Anum([2]))

    self.assertEqual(Anum([9,9,9]) + Anum([1]), Anum([1,0,0,0]))
    self.assertEqual(Anum([1]) + Anum([9,9,9]), Anum([1,0,0,0]))
    self.assertEqual(Anum([6,6,6]) + Anum([6,6,6,7]), Anum([7,3,3,3]))

    self.assertEqual(Anum([100]) + Anum([1]), Anum([1,0,1]))
    self.assertEqual(Anum([243,53,9]) + Anum([42,0,18]), Anum([2,9,0,5,7]))

    self.assertEqual(Anum([1]*10000) + Anum([1]), Anum([1]*9999 + [2]))

  def testCanAddRationalNumbersTogether(self):
    self.assertEqual(Anum([1], [1]) + Anum([0], [1]), Anum([1], [2]))
    self.assertEqual(Anum([1]) + Anum([0], [1,2,3]), Anum([1], [1,2,3]))
    self.assertEqual(Anum([1], [1,2,3]) + Anum([1], [1,2,3]), Anum([2], [2,4,6]))
    self.assertEqual(Anum([1], [9,9,9]) + Anum([0], [0,0,1]), Anum([2], [0,0,0]))
    self.assertEqual(Anum([1], [9]) + Anum([0], [0,9,9]), Anum([1], [9,9,9]))
    self.assertEqual(Anum([1], [9]) + Anum([0], [9,9]), Anum([2], [8,9]))
    self.assertEqual(Anum([1], [9]) + Anum([0], [9,9,0]), Anum([2], [8,9,0]))
    self.assertEqual(Anum([1], [9]*10000) + Anum([0],[0]*9999 + [1]), Anum([2], [0]*10000))

  def testCanMultiply(self):
    self.assertEqual(Anum([1]) * Anum([2]), Anum([2]))
    self.assertEqual(Anum([1,1]) * Anum([2]), Anum([2,2]))
    self.assertEqual(Anum([1]) * Anum([2,2]), Anum([2,2]))
    self.assertEqual(Anum([1,1]) * Anum([2,2]), Anum([2,4,2]))
    self.assertEqual(Anum([1] + [0]*9) * Anum([5,0]), Anum([5] + [0]*10))
    self.assertEqual(Anum([2]) * Anum([1], [1]), Anum([2],[2]))
    self.assertEqual(Anum([1],[1]) * Anum([2]), Anum([2],[2]))
    self.assertEqual(Anum([2]) * Anum([0], [1]), Anum([0],[2]))
    self.assertEqual(Anum([0], [1]) * Anum([2]), Anum([0],[2]))
    self.assertEqual(Anum([0], [2]) * Anum([0], [2]), Anum([0],[0, 4]))
    self.assertEqual(Anum([1], [0,0,1]) * Anum([1], [0,0,1]), Anum([1],[0, 0, 2, 0, 0, 1]))
    self.assertEqual(Anum([1], [0]*99 + [1]) * Anum([1], [0]*99 + [1]), Anum([1],[0]*99 + [2] + [0]*99 + [1]))

  def testDivByPowerOfTen(self):
    self.assertEqual(divByPowerOfTen(Anum([1,0]), 1), Anum([1],[0]))
    self.assertEqual(divByPowerOfTen(Anum([1,0]), 3), Anum([0],[0,1]))
    self.assertEqual(divByPowerOfTen(Anum([0]), 3), Anum([0],[0]))
    self.assertEqual(divByPowerOfTen(Anum([1]), 3), Anum([0],[0,0,1]))
    self.assertEqual(divByPowerOfTen(Anum([0],[1]), 3), Anum([0],[0,0,0,1]))
    self.assertEqual(divByPowerOfTen(Anum([0],[1,2,3]), 1), Anum([0],[0,1,2,3]))

  def testEquals(self):
    self.assertEqual(Anum([1]), Anum([1]))
    self.assertEqual(Anum([1], [2,3,4]), Anum([1], [2,3,4]))
    self.assertNotEqual(Anum([1]), Anum([2]))
    self.assertNotEqual(Anum([1], [2,3,4]), Anum([2], [2,3,4]))
    self.assertNotEqual(Anum([1], [2,3,4]), Anum([1], [3]))
    self.assertNotEqual(Anum([1], [2,3,4]), Anum([1]))
    self.assertNotEqual(Anum([1]), 1)

  def testToStr(self):
    self.assertEqual(str(Anum([1], [2, 3])), "[1],[2, 3]")  

if __name__ == '__main__':
    unittest.main()
