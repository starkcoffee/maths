import unittest
import decimal

def compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time))

class TestInterestStuff(unittest.TestCase):

    def test_compound_interest(self):
        res = compound_interest(1200, 5.4, 2)
        self.assertEqual(1333.0992, res)

    def test_accumulating_interest(self):
        principal = 100000
        rate = 5.4
        time = 10

        acc = principal
        for x in range(1, 11):
            acc = compound_interest(acc, rate, 1)
            print(f"{x}\t{acc}")

        self.assertEqual(acc, compound_interest(principal, rate, time))

    def test_arbitrary_repayments(self):
        principal = 100000
        rate = 5.4
        time = 10
        repayment = 10000

        acc = principal
        for x in range(1, 4):
            acc = compound_interest(acc, rate, 1) - repayment
            print(f"{x}\t{acc}")

        p = principal
        i = rate/100
        r = repayment

        res = (p-3*r) + i*(p-2*r + p-r + p) + i*i*(p-r + 2*p) + i*i*i*p

        acc = round(decimal.Decimal(acc), 2)
        res = round(decimal.Decimal(res), 2)
        self.assertEqual(acc, res)

if __name__ == '__main__':
    unittest.main()


