import unittest
from anum import *

class AnumTest(unittest.TestCase):

  def testSetsFractionToZeroByDefault(self):
    n = Anum([1])
    self.assertEqual(n.w, [1])
    self.assertEqual(n.f, [0])

  def testStoresFractionalPart(self):
    n = Anum([1], [2,3,4])
    self.assertEqual(n.w, [1])
    self.assertEqual(n.f, [2,3,4])

  def testCanAddWholeNumbersTogether(self):
    self.assertEqual(Anum([1]) + Anum([1]), Anum([2]))
    self.assertEqual(Anum([9,9,9]) + Anum([1]), Anum([1,0,0,0]))

  def testEquals(self):
    self.assertEqual(Anum([1]), Anum([1]))
    self.assertEqual(Anum([1], [2,3,4]), Anum([1], [2,3,4]))
    self.assertNotEqual(Anum([1]), Anum([2]))
    self.assertNotEqual(Anum([1], [2,3,4]), Anum([2], [2,3,4]))
    self.assertNotEqual(Anum([1], [2,3,4]), Anum([1], [3]))
    self.assertNotEqual(Anum([1], [2,3,4]), Anum([1]))
    self.assertNotEqual(Anum([1]), 1)

if __name__ == '__main__':
    unittest.main()
