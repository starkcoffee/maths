from arbitrary_arithmetic import add

class Anum:

  def __init__(self, wholePart):
    self.w = wholePart

  def __add__(self, other):
    return Anum(add(self.w, other.w))

  def __eq__(self, other):
    if isinstance(other, Anum):
      return self.w == other.w
    return False


