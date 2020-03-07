from arbitrary_arithmetic import *
from functools import reduce


class Anum:

  def __init__(self, wholePart, fractionPart=[]):
    replaceEmptyArray = lambda x: [0] if x==[] else x 
    self.w = replaceEmptyArray(wholePart)
    self.f = replaceEmptyArray(fractionPart)

  def __add__(self, other):
    # add fractional parts
    max_len_f = max_len(self.f, other.f)
    padded_f_parts = list(map(lambda a: appendZeroes(a, max_len_f-len(a)), [self.f, other.f]))
    carry_f, sum_f = zip_add(*padded_f_parts)    

    # add whole parts
    max_len_w = max_len(self.w, other.w)
    padded_w_parts = list(map(lambda a: prependZeroes(a, max_len_w-len(a)), [self.w, other.w, [carry_f]]))
    carry_w, sum_w = zip_add(*padded_w_parts)  

    if carry_w != 0:
      sum_w = splat(carry_w) + sum_w
    return Anum(sum_w, sum_f)

  def __mul__(self, other):
    products = [[j*k for k in hydratePowers(self.w)] for j in hydratePowers(other.w)]
    products = [ removePowers(a) for a in products ]
    return reduce(lambda acc, x: Anum(x) + acc, products, Anum([0]))

  def __eq__(self, other):
    if isinstance(other, Anum):
      return self.w == other.w and self.f == other.f
    return False

  def __str__(self):
    return str(self.w) + "," + str(self.f)

  def __repr__(self):
    return str(self.w) + "," + str(self.f)


