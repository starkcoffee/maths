import unittest
import maths.sqroot.sqroot_anum as sqroot_anum
from maths.sqroot.sqroot_anum import *

class TestSqrootAnum(unittest.TestCase):

  def testDigByDigSqroot(self):
    self.assertEqual(digByDigSqroot(Anum([1]), 1), Anum([1]))
    self.assertEqual(digByDigSqroot(Anum([4]), 1), Anum([2]))

  def testGetHighestHundredth(self):
    self.assertEqual(sqroot_anum._getHighestHundredth(Anum([6])), (0, 0))
    self.assertEqual(sqroot_anum._getHighestHundredth(Anum([2,6])), (0, 0))
    self.assertEqual(sqroot_anum._getHighestHundredth(Anum([3,2,6])), (3, 1))
    self.assertEqual(sqroot_anum._getHighestHundredth(Anum([1,3,2,6])), (13, 1))
    self.assertEqual(sqroot_anum._getHighestHundredth(Anum([3,1,3,2,6])), (3, 2))
    self.assertEqual(sqroot_anum._getHighestHundredth(Anum([5,3,1,3,2,6])), (53, 2))

if __name__ == '__main__':
    unittest.main()
