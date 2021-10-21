from math import sqrt
import cProfile
from numpy import gcd

#return number of triplets with c less than n
def num_triplets(n):

  # generate the set of all squares less than n
  all_squares_list = [i**2 for i in range(1,n)]
  all_squares_set = set(all_squares_list)
  n_squared = n**2

  # for each pair of squares
  count = 0
  for b in range(1, n):
    b_squared = all_squares_list[b-1]
    for a in range(1, b):
      a_squared = all_squares_list[a-1]
      c_squared = a_squared + b_squared
      if(c_squared < n_squared):
        if(c_squared in all_squares_set):
          if (gcd(a,b) == 1):
            count+=1
          #print(f'{a},{b},{int(sqrt(c_squared))}')
      else:
        # pairs are in increasing order so we can break to the next b
        break
  return count


print(num_triplets(1_000_000)/1_000_000)
#cProfile.run('num_triplets(10000)')

'''
c=100
while(True):
  print(f'N(c) for c = {c}: {num_triplets(c)/c}')
  c*=10
'''
