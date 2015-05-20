# coding: utf-8


from collections import OrderedDict


def knapsack(capacity, items):
    weights = [w[0] for w in items]
    # assert type(weights)
    bags = OrderedDict.fromkeys(weights)
    for x, y in items:
        bags[x] = y
    for (bag, _) in sorted(bags.items(), key=lambda x: x[1]/float(x[0]), reverse=True):
            bags[bag], capacity = divmod(capacity, bag)

    return [v is not None and int(v) or 0 for v in bags.values()]


print knapsack(100, ((1, 1), ))
print knapsack(100, ((100, 1), ))
print knapsack(100, ((60, 1), (50, 4)))
print knapsack(100, ((11.2,  7.4), (25.6, 17.8), (51.0, 41.2),
    (23.9, 15.6), (27.8, 19.0) ) )
