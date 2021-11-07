import unittest

'''
 returns a tuple (x, y, gcd) such that
  xa + yb = gcd
'''
def extended_gcd(a, b):
  assert a >= b

  q = a // b
  r = a % b

  if (r == 0):
    return (1, 1-q, b) 

  (x,y,gcd) = extended_gcd(b, r)
  return (y, x - q*y, gcd)


class TestGCD(unittest.TestCase):

  def test_extended_gcd(self):
    self.assertEqual(extended_gcd(2,1), (1,-1,1))
    self.assertEqual(extended_gcd(5,2), (-1,3,1))
    self.assertEqual(extended_gcd(100,15), (2,-13,5))

  def test_same_number(self):
    self.assertEqual(extended_gcd(5,5), (1,0,5))

  def test_smaller_number_first(self):
    with self.assertRaises(AssertionError):
      extended_gcd(2,5)

    

if __name__ == '__main__':
    unittest.main()
