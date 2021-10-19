from math import sqrt
import cProfile

#return number of triplets with c less than n
def num_triplets(n):
  candidates = ((a,b) for b in range(1,2**64) for a in range (1,b+1) )

  count = 0
  (a,b) = next(candidates)
  while(b < n):
    c_squared = a**2 + b**2
    if(c_squared < n**2):
      c = sqrt(c_squared)
      if(c.is_integer()):
        #print(f'{a},{b},{int(c)}')
        count+=1
    (a,b) = next(candidates)
  return count

cProfile.run('num_triplets(10000)')



