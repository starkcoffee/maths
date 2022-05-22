from functools import reduce
from itertools import product
from collections import defaultdict

def eulerian_walks(nodes, num_crossings, counts_of_crossings_that_exist):
  valid_paths = []
  
  for path in product(nodes, repeat=num_crossings+1):
    if is_an_eulerian_walk(counts_of_crossings_that_exist, path):
      valid_paths.append(path)

  return valid_paths


def is_an_eulerian_walk(counts_of_crossings_that_exist, path):
  return crossings_counts(crossings_from_path(path)) == counts_of_crossings_that_exist

def crossings_from_path(path):
  starts= path[0:len(path)-1]
  ends = path[1:len(path)]
  return zip(starts,ends)

def crossings_counts(crossings):
  counts = defaultdict(int)

  for crossing in crossings:
    counts[ordered_pair(crossing)] += 1
  return counts

def ordered_pair(pair):
  (a, b) = pair
  return (a, b) if a < b else (b, a)


