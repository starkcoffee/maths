
def digByDigSqroot(n, desiredDigits):
  powersOf100 = list(_generatePowersOf100(n))
  highestPowerOfHundered = powersOf100.pop()

  powOf10 = pow(10, len(powersOf100))
  x = _closestIntSqrt(highestPowerOfHundered) * powOf10
  remainder = n - x*x

  for i in range(desiredDigits-1):
    powOf10 = powOf10/10
    (y, remainder) = _findY(x, powOf10, remainder)
    x = x+y
  return x


def _hundreds(n):
  while True:
    if n==0:
      yield 0
    else:
      power = 100
      while n // power > 0:
        power=power*100
      yield n // (power/100)
      n = n % (power/100)
      
def _closestIntSqrt(n):
  for i in range(10):
    if i**2 > n:
      return i-1
  return i

def _generatePowersOf100(n):
  while n > 0:
    yield n % 100
    n = n // 100

def _findY(x, powerOf10, remainder):
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


