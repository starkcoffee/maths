from arbitrary_arithmetic import *
from functools import reduce

def divByPowerOfTen(a, power):
  padded_w = prependZeroes(a.w, power-len(a.w))
  result_w = padded_w[0:len(padded_w)-power]
  result_f = padded_w[-power:] + a.f
  return Anum(result_w, result_f)

class Anum:

  def __init__(self, wholePart, fractionPart=[]):
    replaceEmptyArray = lambda x: [0] if x==[] else x 
    self.w = replaceEmptyArray(removeLeadingZeroes(wholePart))
    self.f = replaceEmptyArray(removeTrailingZeroes(fractionPart))

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
    sum_products = lambda products: reduce(lambda acc, x: x + acc, products, Anum([0]))
    multiply = lambda a,b: sum_products([Anum(p) for p in expand(a,b)])

    term1 = multiply(self.w, other.w)

    term2 = multiply(self.w, other.f)
    term2 = divByPowerOfTen(term2, len(other.f))

    term3 = multiply(self.f, other.w)
    term3 = divByPowerOfTen(term3, len(other.f))

    term4 = multiply(self.f, other.f)
    term4 = divByPowerOfTen(term4, len(self.f) + len(other.f))

    return term1 + term2 + term3 + term4

  def __eq__(self, other):
    if isinstance(other, Anum):
      return self.w == other.w and self.f == other.f
    return False

  def __str__(self):
    return str(self.w) + "," + str(self.f)

  def __repr__(self):
    return str(self.w) + "," + str(self.f)


