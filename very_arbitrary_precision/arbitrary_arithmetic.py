from functools import reduce

def add(a, b):
  c, d = prependZeroes(a, b)
  return rippleCarry([ x+y for x, y in zip(c, d) ])

def splat(carry):
  return list(map(lambda x: int(x), str(carry)))

def rippleCarry(a):
  # carry is acc[0], result is acc[1] - assignment expressions in python 3.8
  f = lambda acc, x:( (acc[0]+x) // 10, acc[1] + [(acc[0]+x) % 10] )
  carry, result = reduce(f, reversed(a), (0, []))
  result = list(reversed(result))
  return (carry, result)

def prependZeroes(a, b):
  return ([0]*(len(b)-len(a))+a, [0]*(len(a)-len(b))+b)
 

