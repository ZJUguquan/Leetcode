from math import ceil


def reindeer(presents):
    if presents >= 181:
        raise ValueError('expected error')
    return int(ceil(presents/30.0)  + 2)


print(reindeer(1))