import unittest

def sum(a,b):
  return a+b

def g(a, b, f):
  return f(a,b)

class TestGCD(unittest.TestCase):

  def test_gcd(self):
    self.assertEqual(g(1,1,sum), 3)

if __name__ == '__main__':
    unittest.main()
