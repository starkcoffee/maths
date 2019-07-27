import unittest
from functools import reduce


def add(a, b):
  c, d = (_prependZeroes(a, len(b)-len(a)), _prependZeroes(b, len(a)-len(b)))
  return _rippleCarry([ x+y for x, y in zip(c, d) ])

def _rippleCarry(a):
  # carry is acc[0], result is acc[1] - assignment expressions in python 3.8
  f = lambda acc, x:( (acc[0]+x) // 10, acc[1] + [(acc[0]+x) % 10] )
  carry, result = reduce(f, reversed(a), (0, []))
  result = list(reversed(result))
  # since carry can be > 10, split it into its digits
  carry = list(filter(lambda x: x!=0, map(lambda x: int(x), str(carry))))
  return carry + result 

def _prependZeroes(a, num_zeroes):
   return [0] * num_zeroes + a

class TestVeryArbitraryPrecision(unittest.TestCase):

  def testAdd(self):
    self.assertEqual(add([], []), [])
    self.assertEqual(add([1], []), [1])
    self.assertEqual(add([], [1]), [1])
    self.assertEqual(add([1],[1]), [2])
    self.assertEqual(add([1,2,3],[1]), [1,2,4])
    self.assertEqual(add([1],[1,2,3]), [1,2,4])
    self.assertEqual(add([1,2,3],[1,2,3]), [2,4,6])
    self.assertEqual(add([9,9,9],[9,9,9]), [1,9,9,8])
    self.assertEqual(add([243,53,9],[42,0,18]), [2,9,0,5,7])

  def testRippleCarry(self):
    self.assertEqual(_rippleCarry([1, 11]), [2, 1]) 
    self.assertEqual(_rippleCarry([0]), [0]) 
    self.assertEqual(_rippleCarry([1,2]), [1,2]) 
    self.assertEqual(_rippleCarry([42,2]), [4,2,2]) 
    self.assertEqual(_rippleCarry([2,342]), [3,6,2]) 
    self.assertEqual(_rippleCarry([1, 2,53342]), [5,3,4,6,2]) 
    self.assertEqual(_rippleCarry([642,2]), [6,4,2,2]) 

  def testPrependZeroes(self):
    self.assertEqual(_prependZeroes([1], 5), [0,0,0,0,0,1])
    self.assertEqual(_prependZeroes([1,2], 1), [0,1,2])
    self.assertEqual(_prependZeroes([1,2], 0), [1,2])
    self.assertEqual(_prependZeroes([], 1), [0])

  def testPrependZeroesIgnoresNegative(self):
    self.assertEqual(_prependZeroes([1,2], -1), [1,2])

if __name__ == '__main__':
    unittest.main()
