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

# returns tree of permutations of symbols as a list of tuples
def generate_tree(symbols, depth):
  tupelised_symbols = [ tuple(a) for a in symbols ]
  if depth == 0:
    return []
  return generate_tree_acc(tupelised_symbols, depth-1, tupelised_symbols)

def generate_tree_acc(tupelised_symbols, depth, tree_acc):
  if depth == 0:
    return tree_acc

  next_generation_of_tree = [ a+b for a in tree_acc for b in tupelised_symbols ]
  return generate_tree_acc(tupelised_symbols, depth - 1, next_generation_of_tree) 

  
