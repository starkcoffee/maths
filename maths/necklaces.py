from itertools import product
from functools import reduce

def necklaces(iterable, num):
  
  necklaces = set()
  for p in product(iterable, repeat=num):
    if necklaces.isdisjoint(rotations(p)): 
      necklaces.add(p)

  str_necklaces = {''.join(n) for n in necklaces }
  return str_necklaces

def rotations(permutation):
  rotate = lambda perm, offset: tuple( perm[(i+offset) % len(perm)] for i in range(len(perm)) )
  return { rotate(permutation, i) for i in range(len(permutation)) }

# returns tree of permutations of symbols as tuples
def generate_tree(symbols, depth):
  tupelised_symbols = [ tuple(a) for a in symbols ]
  generate_next_branches = lambda acc, _: [ a+b for a in acc for b in tupelised_symbols ]
  return reduce(generate_next_branches, range(depth-1), tupelised_symbols)
