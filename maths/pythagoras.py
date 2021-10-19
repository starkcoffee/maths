from math import sqrt
import cProfile

#return number of triplets with c less than n
def num_triplets(n):

  # generate the set of all squares less than n
  all_c_squares = set((c**2 for c in range(1,n)))
  n_squared = n**2

  count = 0
  for b in range(1, n):
    for a in range(1, b):
      c_squared = a**2 + b**2
      if(c_squared < n_squared):
        if(c_squared in all_c_squares):
          #print(f'{a},{b},{int(sqrt(c_squared))}')
          count+=1
      else:
        # pairs are in increasing order so we can break to the next b
        break
  return count

#print(num_triplets(1000))
#cProfile.run('num_triplets(10000)')

c=100
while(True):
  print(f'N(c) for c = {c}: {num_triplets(c)/c}')
  c*=10


