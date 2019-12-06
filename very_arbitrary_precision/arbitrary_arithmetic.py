from functools import reduce


def zip_add(*arrays):
  if len(set([ len(a) for a in arrays ])) != 1:
    raise ValueError("arrays are not same length")

  return rippleCarry([ sum(list(operands)) for operands in zip(*arrays) ])

def splat(carry):
  return list(map(lambda x: int(x), str(carry)))

# returns tuple: (left-over-carry, array-with-ripple-applied)
def rippleCarry(a):
  # carry is acc[0], result is acc[1] - assignment expressions in python 3.8
  f = lambda acc, x:( (acc[0]+x) // 10, acc[1] + [(acc[0]+x) % 10] )
  carry, result = reduce(f, reversed(a), (0, []))
  result = list(reversed(result))
  return (carry, result)

def prependZeroes(a, b):
  return ([0]*(len(b)-len(a))+a, [0]*(len(a)-len(b))+b)
 
def appendZeroes(a, b):
  return (a + [0]*(len(b)-len(a)), b +[0]*(len(a)-len(b)))

