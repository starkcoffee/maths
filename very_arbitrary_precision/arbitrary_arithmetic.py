from functools import reduce

def add(a, b):
  c, d = (_prependZeroes(a, len(b)-len(a)), _prependZeroes(b, len(a)-len(b)))
  return _rippleCarry([ x+y for x, y in zip(c, d) ])

def splat(carry):
  return list(map(lambda x: int(x), str(carry)))

def _rippleCarry(a):
  # carry is acc[0], result is acc[1] - assignment expressions in python 3.8
  f = lambda acc, x:( (acc[0]+x) // 10, acc[1] + [(acc[0]+x) % 10] )
  carry, result = reduce(f, reversed(a), (0, []))
  result = list(reversed(result))
  return (carry, result)

def _prependZeroes(a, num_zeroes):
   return [0] * num_zeroes + a


