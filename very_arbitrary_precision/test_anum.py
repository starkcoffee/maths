import unittest
from anum import *

class AnumTest(unittest.TestCase):

  def testTreatsEmptyArraysAsZeroes(self):
    n = Anum([], [])
    self.assertEqual(n.w, [0])
    self.assertEqual(n.f, [0])

  def testSetsFractionToZeroByDefault(self):
    n = Anum([1])
    self.assertEqual(n.w, [1])
    self.assertEqual(n.f, [0])

  def testStoresWholeAndFractionalPart(self):
    n = Anum([1], [2,3,4])
    self.assertEqual(n.w, [1])
    self.assertEqual(n.f, [2,3,4])


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

  @unittest.skip("")
  def testCanAddRationalNumbersTogether(self):
    self.assertEqual(Anum([1]) + Anum([0], [1,2,3]), Anum([1], [1,2,3]))
    self.assertEqual(Anum([1], [1,2,3]) + Anum([1], [1,2,3]), Anum([2], [2,4,6]))
    self.assertEqual(Anum([1], [9,9,9]) + Anum([0], [0,0,1]), Anum([2], [0,0,0]))
    self.assertEqual(Anum([1], [9]) + Anum([0], [0,9,9]), Anum([1], [9,9,9]))
    self.assertEqual(Anum([1], [9]) + Anum([0], [9,9]), Anum([2], [8,9]))
    self.assertEqual(Anum([1], [9]) + Anum([0], [9,9,0]), Anum([2], [8,9,0]))

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
