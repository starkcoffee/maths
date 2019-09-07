from arbitrary_arithmetic import add

class Anum:

  def __init__(self, wholePart, fractionalPart=None):
    self.w = wholePart
    if fractionalPart != None:
      self.f = fractionalPart 
    else:
      self.f = [0]

  def __add__(self, other):
    return Anum(add(self.w, other.w))

  def __eq__(self, other):
    if isinstance(other, Anum):
      return self.w == other.w and self.f == other.f
    return False


