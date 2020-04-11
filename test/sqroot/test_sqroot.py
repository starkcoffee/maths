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

  def testGeneratePowersOf100(self):
    powersof100gen = sqroot._generatePowersOf100(31326)
    listOfPowersOf100 = list(powersof100gen)
    self.assertEqual(listOfPowersOf100, [26, 13, 3])
    self.assertEqual(listOfPowersOf100.pop(), 3)

  def testClosestInSqrt(self):
    self.assertEqual(sqroot._closestIntSqrt(10), 3)
    self.assertEqual(sqroot._closestIntSqrt(0), 0)
    self.assertEqual(sqroot._closestIntSqrt(5000), 9)

  def testHundreds(self):
    val = sqroot._hundreds(2_45_24_65_43)
    self.assertEqual(next(val), 2)
    self.assertEqual(next(val), 45)
    self.assertEqual(next(val), 24)
    self.assertEqual(next(val), 65)
    self.assertEqual(next(val), 43)
    self.assertEqual(next(val), 00)
    self.assertEqual(next(val), 00)

if __name__ == '__main__':
    unittest.main()
