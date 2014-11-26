def find_most_frequent(l):
    # Write your code here.
    counter = {}
    if l == [] : return 'empty'
    for e in l:
        if e not in counter:
            counter[e] = 1
        else:
            counter[e] += 1
    maxfrequent = max(counter.values())
    res = set([key for key in counter if counter[key] == maxfrequent])
    return res # if len(res)> 0 else 'empty'

l = [1, 1, 2, 3]
l = []
print(find_most_frequent(l))



# """
# find_most_frequent([1, 1, 2, 3]) == set([1])
# find_most_frequent([1, 1, 2, 2, 3]) == set([1, 2])
# find_most_frequent([1, 1, '2', '2', 3]) == set([1, '2'])
# """


'Learning from others'

def find_most_frequent(l):
    return set(x for x in set(l) if l.count(x) ==
         max([l.count(y) for y in l]))
