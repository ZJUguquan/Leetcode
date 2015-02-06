def midpoint_sum(ints):
    if len(ints) < 3:
        return None
    lens = len(ints) - 1
    for idx in range(1, lens):
        if sum(ints[:idx]) == sum(ints[idx+1:]):
            return idx
    return None

ints=[4,9,0,1,2,3,4]
ints = [9, 0 ,1,2,3,4]
ints = [0, 0, 1]
print(midpoint_sum(ints))