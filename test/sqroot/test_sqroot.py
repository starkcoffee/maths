import unittest
import maths.sqroot.sqroot as sqroot
from maths.sqroot.sqroot import *

class TestStuff(unittest.TestCase):

  def testDigByDigSqroot(self):
    self.assertEqual(digByDigSqroot(4563, 16), 67.54998149518622)
    self.assertEqual(digByDigSqroot(45637,10), 213.6281816)
    self.assertEqual(digByDigSqroot(100, 2), 10)
    self.assertEqual(digByDigSqroot(1, 1), 1)
    self.assertEqual(digByDigSqroot(1, 2), 1.0)

  def testGetHighestHundredthPower(self):
    self.assertEqual(sqroot._getHighestHundredthPower(31326), (3, 2))
    self.assertEqual(sqroot._getHighestHundredthPower(0), (0, 0))

  def testClosestInSqrt(self):
    self.assertEqual(sqroot._closestIntSqrt(10), 3)
    self.assertEqual(sqroot._closestIntSqrt(0), 0)
    self.assertEqual(sqroot._closestIntSqrt(5000), 9)

if __name__ == '__main__':
    unittest.main()
