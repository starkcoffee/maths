from functools import reduce

def expand(a, b):
    multiplier, multiplicand = a, b
    # performance improvement
    if len(b) < len(a):
      multiplier, multiplicand = b, a
      
    power = lambda index: len(multiplier)-index-1 
    return [
      [i*j for j in multiplicand] + [0]*power(index) 
      for index, i in enumerate(multiplier) 
    # performance improvement
      if i != 0
    ]

def zip_add(*arrays):
  if len(set([ len(a) for a in arrays ])) != 1:
    raise ValueError("arrays are not same length")

  return rippleCarry([ sum(list(operands)) for operands in zip(*arrays) ])

def splat(carry):
  return list(map(lambda x: int(x), str(carry)))

def max_len(*arrays):
  return max(map(lambda a: len(a), arrays))

# returns tuple: (left-over-carry, array-with-ripple-applied)
def rippleCarry(a):
  # carry is acc[0], result is acc[1] - assignment expressions in python 3.8
  f = lambda acc, x:( (acc[0]+x) // 10, acc[1] + [(acc[0]+x) % 10] )
  carry, result = reduce(f, reversed(a), (0, []))
  result = list(reversed(result))
  return (carry, result)

def prependZeroes(a, num):
  return [0]*num + a
 
def appendZeroes(a, num):
  return a + [0]*num 

# turns digits into power of ten eg.
# [1, 2, 3] => [100, 20, 3]
def hydratePowers(a):
    return [i*pow(10, len(a)-ind-1) for ind, i in enumerate(a)]

def removePowers(a):
    return [i // pow(10, len(a)-ind-1) for ind, i in enumerate(a)]

