import unittest

def hundreds(n):
  while True:
    if n==0:
      yield 0
    else:
      power = 100
      while n // power > 0:
        power=power*100
      yield n // (power/100)
      n = n % (power/100)
      
def closestIntSqrt(n):
  for i in range(10):
    if i**2 > n:
      return i-1
  return i

def generatePowersOf100(n):
  while n > 0:
    yield n % 100
    n = n // 100

def findY(x, powerOf10, remainder):
  print("args", x, powerOf10, remainder)
  newRemainder = remainder
  for i in range(10):
    y = i*powerOf10
    diff = 2*x*y + y*y 
    if diff > remainder:
      return ((i-1)*powerOf10, newRemainder)
    else:
      newRemainder = remainder - diff
  return (i*powerOf10, newRemainder)

def digByDigSqroot(n, desiredDigits):
  powersOf100 = list(generatePowersOf100(n))
  highestPowerOfHundered = powersOf100.pop()

  powOf10 = pow(10, len(powersOf100))
  x = closestIntSqrt(highestPowerOfHundered) * powOf10
  remainder = n - x*x

  for i in range(desiredDigits-1):
    powOf10 = powOf10/10
    (y, remainder) = findY(x, powOf10, remainder)
    x = x+y
  return x


class TestStuff(unittest.TestCase):

  def testDigByDigSqroot(self):
    self.assertEqual(digByDigSqroot(4563, 16), 67.54998149518622)
    self.assertEqual(digByDigSqroot(45637,10), 213.6281816)
    self.assertEqual(digByDigSqroot(100, 2), 10)
    self.assertEqual(digByDigSqroot(1, 1), 1)
    self.assertEqual(digByDigSqroot(1, 2), 1.0)
    print(digByDigSqroot(42, 30))

  def testGeneratePowersOf100(self):
    powersof100gen = generatePowersOf100(31326)
    listOfPowersOf100 = list(powersof100gen)
    self.assertEqual(listOfPowersOf100, [26, 13, 3])
    self.assertEqual(listOfPowersOf100.pop(), 3)

  def testClosestInSqrt(self):
    self.assertEqual(closestIntSqrt(10), 3)
    self.assertEqual(closestIntSqrt(0), 0)
    self.assertEqual(closestIntSqrt(5000), 9)

  def testHundreds(self):
    val = hundreds(2_45_24_65_43)
    self.assertEqual(next(val), 2)
    self.assertEqual(next(val), 45)
    self.assertEqual(next(val), 24)
    self.assertEqual(next(val), 65)
    self.assertEqual(next(val), 43)
    self.assertEqual(next(val), 00)
    self.assertEqual(next(val), 00)

if __name__ == '__main__':
    unittest.main()
