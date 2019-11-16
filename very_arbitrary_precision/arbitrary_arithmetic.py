from functools import reduce


def zip_add(a, b):
  if len(a) != len(b):
    raise ValueError("arrays are not same length")

  return rippleCarry([ x+y for x, y in zip(a, b) ])

def splat(carry):
  return list(map(lambda x: int(x), str(carry)))

# returns (left-over-carry, array-with-ripple-applied)
def rippleCarry(a):
  # carry is acc[0], result is acc[1] - assignment expressions in python 3.8
  f = lambda acc, x:( (acc[0]+x) // 10, acc[1] + [(acc[0]+x) % 10] )
  carry, result = reduce(f, reversed(a), (0, []))
  result = list(reversed(result))
  return (carry, result)

def prependZeroes(a, b):
  return ([0]*(len(b)-len(a))+a, [0]*(len(a)-len(b))+b)
 

