import sys
import math

from maths.very_arbitrary_precision.anum import Anum

def digByDigSqroot(anum, desiredDigits):
  return anum 


# returns (unit, power) so that the highest hundredth is unit * 10^power
def _getHighestHundredthPower(anum):
  w_len = len(anum.w)
  power = math.floor((w_len-1)/2)
  units = 0
  if w_len > 2:
    if w_len%2 == 0:
      units = anum.w[0]*10 + anum.w[1]
    else:
      units = anum.w[0]
  return (units, power)
