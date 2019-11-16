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


  @unittest.skip("")
  def testCanAddWholeNumbersTogether(self):
    self.assertEqual(add([], []), (0, []))
    self.assertEqual(Anum([1]) + Anum([1]), Anum([2]))
    self.assertEqual(Anum([9,9,9]) + Anum([1]), Anum([1,0,0,0]))
    self.assertEqual(Anum([6,6,6]) + Anum([6,6,6]), Anum([1,3,3,2]))
    self.assertEqual(add([1], []), (0, [1]))
    self.assertEqual(add([], [1]), (0, [1]))
    self.assertEqual(add([1],[1]), (0, [2]))
    self.assertEqual(add([1,2,3],[1]), (0, [1,2,4]))
    self.assertEqual(add([1],[1,2,3]), (0, [1,2,4]))
    self.assertEqual(add([1,2,3],[1,2,3]), (0, [2,4,6]))
    self.assertEqual(add([9,9,9],[9,9,9]), (1, [9,9,8]))
    self.assertEqual(add([243,53,9],[42,0,18]), (29, [0,5,7]))
    self.assertEqual(add([100],[1]), (10, [1]))


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
