from math import sqrt
import cProfile

#return number of triplets with c less than n
def num_triplets(n):

  count = 0
  for b in range(1, n):
    for a in range(1, b):
      c_squared = a**2 + b**2
      if(c_squared < n**2):
        c = sqrt(c_squared)
        if(c.is_integer()):
          #print(f'{a},{b},{int(c)}')
          count+=1
      else:
        # pairs are in increasing order so we can break to the next b
        break
  return count

#print(num_triplets(1000))
cProfile.run('num_triplets(10000)')



