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
def generate_tree_breadth_first(symbols, depth):
  if depth == 0:
    return []

  tupelised_symbols = [ tuple(a) for a in symbols ]
  return generate_tree_breadth_first_acc(tupelised_symbols, depth-1, tupelised_symbols)

def generate_tree_breadth_first_acc(tupelised_symbols, depth, tree_acc):
  if depth == 0:
    return tree_acc

  next_generation_of_tree = [ a+b for a in tree_acc for b in tupelised_symbols ]
  return generate_tree_breadth_first_acc(tupelised_symbols, depth - 1, next_generation_of_tree) 

def generate_tree_depth_first(symbols, depth):
  if depth == 0:
    return []

  tupelised_symbols = [ tuple(a) for a in symbols ]

  generate_branches = lambda acc, elem: acc + generate_branches_depth_first(tupelised_symbols, depth-1, elem)
  return reduce(generate_branches, tupelised_symbols, [])
  
def generate_branches_depth_first(tupelised_symbols, depth, branch):
  if depth == 0:
    return [ branch ]

  generate_branches = lambda acc, elem: acc + generate_branches_depth_first(tupelised_symbols, depth-1, branch + elem)
  return reduce(generate_branches, tupelised_symbols, [])

