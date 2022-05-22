import unittest
from maths.koenigsberg import *
from itertools import product
from collections import defaultdict

""" In Euler's solution to the bridges of Koenigsberg the landmasses are nodes, 
and the bridges are edges. For an excellent walkthrough and the picture of
the graph of Koenigsberg's bridges we will use see
https://www.maa.org/press/periodicals/convergence/leonard-eulers-solution-to-the-konigsberg-bridge-problem
"""
A,B,C,D,E='A','B','C','D','E'

class KoenigsbergTest(unittest.TestCase):
  

  def test_generate_permutations(self):
    # the product method will give us the permutatations with repeats of the landmasses, 
    # which gives us candidates of all paths of the graph
    self.assertEquals([(A,A), (A,B), (B,A), (B,B)], list(product([A,B], repeat=2)))

  def test_breaking_path_into_edges(self):
    # given a candidate path over the bridges, like 'CDBACABA'
    path = [C,D,B,A,C,A,B,A]
    # we want to break it up into it's individual bridge crossings like
    bridge_crossings = [(C,D), (D,B), (B,A), (A,C), (C,A), (A,B), (B,A)]

    self.assertEquals(bridge_crossings, list(crossings_from_path(path)))

  def test_compare_graphs(self):
    self.assertEquals({A:1, B:2}, defaultdict(int, A=1, B=2))
    self.assertNotEqual({3:1, 2:2, 1:3}, {3:1, 2:2})

  def test_count_edges(self):
    # once we have list of all the crossings taken, let's count the number of 
    # crossings done between the landmasses
    # if the crossings in a path were 
    crossings = [(C,D), (D,B), (B,A), (A,C), (C,A), (A,B), (B,A)]
    # the count of crossings per pair of landmasses there is
    counts = {(A,B):3, (A,C):2, (B,D):1, (C,D):1}

    self.assertEquals(counts, crossings_counts(crossings))

  # see map of Koenigsberg https://www.maa.org/sites/default/files/images/upload_library/46/1/old_convergence/Paoletti/Figure-2-perchance.png
  def test_path_is_invalid(self):
    # a path is only valid, and thus an "Eulerian walk", if the count of crossings taken matches 
    # the count of crossings that exist
    # here is the count of crossings in Koenigsberg (in the 18th century)
    koenigsberg_crossing_counts = {(A,B):2, (A,C):2, (A,D): 1, (B,D):1, (C,D):1}
    # here is a candidate path in Koenigsberg that should be invalid
    path =  [C,D,B,A,C,A,B,A]

    self.assertFalse(is_an_eulerian_walk(koenigsberg_crossing_counts, path))

  def test_path_is_valid(self):
    # we can't use an example walk from koenigsberg obviously, so let's use the 
    # House of Nicolaus http://www.eprisner.de/MAT107/Graphs/Euler.html
    haus_nicolaus_crossing_counts = {(A,B):1, (A,E):1, (B,C):1, (B,D):1, (B,E):1, (C,D):1, (C,E):1, (D,E):1 }

    path = [C,E,B,C,D,B,A,E,D]

    self.assertTrue(is_an_eulerian_walk(haus_nicolaus_crossing_counts, path))

  def test_find_valid_paths_in_koenigsberg(self):
    # now we can find out if there are any eulerian walks in Koenigsberg
    koenigsberg_landmasses = [A,B,C,D]
    koenigsberg_crossing_counts = {(A,B):2, (A,C):2, (A,D): 1, (B,D):1, (C,D):1}

    self.assertEquals([], eulerian_walks(koenigsberg_landmasses, 7, koenigsberg_crossing_counts))

  def test_find_valid_paths_in_haus_of_nicolaus(self):
    haus_nicolaus_landmasses = [A,B,C,D,E]
    haus_nicolaus_crossing_counts = {(A,B):1, (A,E):1, (B,C):1, (B,D):1, (B,E):1, (C,D):1, (C,E):1, (D,E):1 }

    walks = eulerian_walks(haus_nicolaus_landmasses, 8, haus_nicolaus_crossing_counts)
    print(f"num eulerian walks in haus nicolaus is {len(walks)}")
    print("first three walks:")
    for i in range(3):
      print(walks[i])


 
if __name__ == '__main__':
    unittest.main()
