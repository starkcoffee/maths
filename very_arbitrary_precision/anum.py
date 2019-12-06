from arbitrary_arithmetic import *


class Anum:

  def __init__(self, wholePart, fractionPart=[]):
    replaceEmptyArray = lambda x: [0] if x==[] else x 
    self.w = replaceEmptyArray(wholePart)
    self.f = replaceEmptyArray(fractionPart)

  def __add__(self, other):
    # add fractional parts
    f1, f2 = appendZeroes(self.f, other.f) 
    carry_f, sum_f = zip_add(f1, f2)    

    # add whole parts
    w1, w2 = prependZeroes(self.w, other.w) 
    carry_w, sum_w = zip_add(w1, w2)  

    if carry_w != 0:
      sum_w = splat(carry_w) + sum_w
    return Anum(sum_w, sum_f)

  def __eq__(self, other):
    if isinstance(other, Anum):
      return self.w == other.w and self.f == other.f
    return False

  def __str__(self):
    return str(self.w) + "," + str(self.f)

  def __repr__(self):
    return str(self.w) + "," + str(self.f)


