keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]


def createDict(keys, values):
    """
    Write your code here.
    """
    if len(keys) > len(values):
        values += [None] * (len(keys)  - len(values) )
    return dict(zip(keys, values))

print(createDict(keys, values) )