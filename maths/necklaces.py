from itertools import product

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

def generate_tree(symbols, depth):
  tupelised_symbols = [ tuple(a) for a in symbols ]
  tree = tupelised_symbols
  for i in range(depth-1):
    tree = [ a+b for a in tupelised_symbols for b in tree ]
  return tree

