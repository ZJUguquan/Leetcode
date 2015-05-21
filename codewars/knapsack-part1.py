# coding: utf-8

# Test.describe('One item')
# Test.assert_equals(knapsack(100, ((1, 1),)), [100])
# Test.assert_equals(knapsack(100, ((100, 1),)), [1])

# Test.describe('Two items')
# Test.assert_equals(knapsack(100, ((1, 1),
#                                   (3, 4))), [1, 33])
# Test.assert_equals(knapsack(100, ((60, 80),
#                                   (50, 50))), [1, 0])


# Test.describe('Three items')
# Test.assert_equals(knapsack(100, ((10, 10),
#                                   (30, 40),
#                                   (56, 78))), [1, 1, 1])
# Test.assert_equals(knapsack(100, ((11.2,  7.4),
#                                   (25.6, 17.8),
#                                   (51.0, 41.2),
#                                   (23.9, 15.6),
#                                   (27.8, 19.0))), [2, 1, 1, 0, 0])

from operator import itemgetter
from collections import OrderedDict

def knapsack(capacity, items):

    weights = [x[0] for x in items]
    bags = OrderedDict.fromkeys(weights)

    for bag in sorted(bags.items(), key=lambda x: x[0], reverse=True):
        if capacity // bag:
            bags[bag] = capacity // bag
            capacity = capacity %  bag

    return [bags[w] for w in weights]


print knapsack(100, (  (1, 1), ) )
print knapsack(100, (  (100, 1), ) )

