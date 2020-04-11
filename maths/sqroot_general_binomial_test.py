import unittest
from factorial import falling_factorial
from math import factorial, pow, sqrt

def expand_general_bionomial(p, x, n):
    res = 0
    for i in range(0, n):
        res += (falling_factorial(p, i)/factorial(i))*pow(x, i)
    return res

class TestSquareRootStuff(unittest.TestCase):

    def test_expand_general_binomial(self):
        print("Actual:\t\t" , sqrt(25))
        print("10 terms:\t", expand_general_bionomial(0.5, 24, 10))
        print("100 terms:\t", expand_general_bionomial(0.5, 24, 100))
        print("150 terms:\t", expand_general_bionomial(0.5, 24, 150))
        print("200 terms:\t", expand_general_bionomial(0.5, 24, 200))


if __name__ == '__main__':
    unittest.main()
