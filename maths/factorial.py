import unittest

def falling_factorial(x, n):
    res = 1
    for i in range(n):
        res = res*(x-i)
    return res

class TestFactorialStuff(unittest.TestCase):

    def test_falling_factorial(self):
        self.assertEqual(1, falling_factorial(1, 1))
        self.assertEqual(60, falling_factorial(5, 3))
        self.assertEqual(0.375, falling_factorial(0.5, 3))

if __name__ == '__main__':
    unittest.main()
