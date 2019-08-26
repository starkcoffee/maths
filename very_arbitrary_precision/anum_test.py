import unittest
from anum import *

class AnumTest(unittest.TestCase):

  def testAnumSetsPartsCorrectly(self):
    n = Anum([1])
    self.assertEqual(n.w, [1])

  def testAnumCanAddToAnother(self):
    self.assertEqual(Anum([1]) + Anum([1]), Anum([2]))

  def testEquals(self):
    self.assertEqual(Anum([1]), Anum([1]))
    self.assertNotEqual(Anum([1]), Anum([2]))
    self.assertNotEqual(Anum([1]), 1)

if __name__ == '__main__':
    unittest.main()
