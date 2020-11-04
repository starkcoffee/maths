from operator import mul
from itertools import chain, combinations 
from functools import reduce

def num_factors(prime_powers):
  return 1 + sum([reduce(mul, list(t)) for t in list(chain.from_iterable([list(combinations(prime_powers, n)) for n in range(len(prime_powers)+1)])) if t])
