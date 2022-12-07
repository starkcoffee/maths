import unittest
from itertools import takewhile
from math import ceil

"""
Input: spells = [5,1,3], potions = [1,2], success = 7
Output: [4,0,3]

[5,1,3]

[[(5,1),(5,2)],[(1,1),(1,2)],[(3,1),(3,2)]]

[1,0,0]
"""

"""
redesign options to fit stuff in memory

1. go back to for loops

"""

"""
FIRST APPROACH WITH GENERATOR
"""
def gen_pairs(spells, potions):
    for spell in spells:
        yield [(spell, potion) for potion in potions]


def successVal(spell_value_tuple):
    return spell_value_tuple[0] * spell_value_tuple[1] 

def strengths(spells, potions, successThreshold):

    #spell_and_potion_tuples = map(lambda spell: [(spell, potion) for potion in potions], spells) 
    spell_and_potion_tuples = gen_pairs(spells, potions)

    filter_ge_sucess_threshold = lambda pair: successVal(pair) >= successThreshold

    count_num_successful_combos = lambda pair_list: len(list(filter(filter_ge_sucess_threshold, pair_list)))

    successful_combos = map(count_num_successful_combos, spell_and_potion_tuples)

    return list(successful_combos)

"""
SECOND APPROACH WITH MATHY MATH
"""
def count_successful_combos(spell, potions_reversed, success_threshold):
    min_factor = ceil(success_threshold / spell)
    return len(list(takewhile(lambda i: i >= min_factor, potions_reversed)))

def strengths2(spells, potions, success_threshold):
    potions.sort(reverse=True)

    return list(map(lambda spell: count_successful_combos(spell, potions, success_threshold), spells))


class StrengthsTest(unittest.TestCase):

  def test_count_successful_combos(self):
    self.assertEquals(count_successful_combos(10, [9,3,1], 50), 1)  

  def test_strengths(self):
    self.assertEquals(strengths2([5,1,3],[1,2,3,4,5], 7), [4,0,3])
    self.assertEquals(strengths2([3,1,2],[8,5,8], 16), [2,0,2])
    self.assertEquals(strengths2([1], [9], 7), [1])
    self.assertEquals(strengths2([], [], 7), [])
 
if __name__ == '__main__':
    unittest.main()
