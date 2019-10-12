from arbitrary_arithmetic import add

class Anum:

  def __init__(self, wholePart, fractionPart=None):
    self.w = wholePart
    if fractionPart != None:
      self.f = fractionPart 
    else:
      self.f = [0]

  def __add__(self, other):
    carry, sum_w = add(self.w, other.w)
    if carry != 0:
      sum_w = list(map(lambda x: int(x), str(carry))) + sum_w
    return Anum(sum_w, self.f)

  def __eq__(self, other):
    if isinstance(other, Anum):
      return self.w == other.w and self.f == other.f
    return False

  def __str__(self):
    return str(self.w) + "," + str(self.f)

  def __repr__(self):
    return str(self.w) + "," + str(self.f)

