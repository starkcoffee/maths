
def digByDigSqroot(n, desiredDigits):
  units_highestHundredth, power_highestHundredth = _getHighestHundredth(n)

  powOf10 = power_highestHundredth 
  x = _closestIntSqrt(units_highestHundredth) * pow(10, powOf10)
  remainder = n - x*x

  for i in range(desiredDigits-1):
    powOf10 = powOf10 -1
    (y, remainder) = _findY(x, powOf10, remainder)
    x = x+y
  return x

# returns (unit, power) so that the highest hundredth is unit * 100^power
def _getHighestHundredth(n):
  units = n%100
  power = 0
  n = n // 100
  while n > 0:
    units = n%100
    power = power + 1
    n = n // 100

  return units, power 

def _findY(x, powerOf10, remainder):
  print("finding next digit", x, powerOf10, remainder)

  newRemainder = remainder
  for i in range(11):
    y = i* pow(10, powerOf10)
    diff = 2*x*y + y*y 
    #if powerOf10 < 12:
    #  print(i, diff)
    if diff > remainder:
      return ((i-1)* pow(10, powerOf10), newRemainder)
    else:
      newRemainder = remainder - diff

def _closestIntSqrt(n):
  for i in range(10):
    if i**2 > n:
      return i-1
  return i



