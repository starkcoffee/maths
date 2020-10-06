from itertools import product, chain
from functools import reduce


def necklace_count_v2(num_colours, length):
  if length == 1:
    return num_colours

  factors_excluding_self = factors(length) - {length}

  return (num_colours**length - sum(num_permutations_with_repeating_unit(num_colours, factor) for factor in factors_excluding_self))//length + sum(num_permutations_with_repeating_unit(num_colours, factor)//factor for factor in factors_excluding_self)

def num_permutations_with_repeating_unit(num_colours, length):
  factors_excluding_self = factors(length) - {length}
  return num_colours**length - sum(num_permutations_with_repeating_unit(num_colours, factor) for factor in factors_excluding_self)

def necklace_count(num_colours, length):
  return len(necklaces(range(num_colours), length))

# from https://stackoverflow.com/a/38817866
def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )

def necklaces(iterable, num):
  necklaces = set()
  for p in product(iterable, repeat=num):
    if necklaces.isdisjoint(rotations(p)): 
      necklaces.add(p)

  return necklaces

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

# returns tree of permutations of symbols as a list of tuples
def generate_tree_depth_first(symbols, depth):
  if depth == 0:
    return []

  tupelised_symbols = [ tuple(a) for a in symbols ]
  return generate_tree_depth_first_acc(tupelised_symbols, depth, ())
  
def generate_tree_depth_first_acc(tupelised_symbols, depth, branch):
  if depth == 0:
    return [ branch ]

  generate_branches = lambda acc, elem: acc + generate_tree_depth_first_acc(tupelised_symbols, depth-1, branch + elem)
  return reduce(generate_branches, tupelised_symbols, [])

