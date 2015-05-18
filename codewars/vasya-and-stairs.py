
from math import log



def numberOfSteps(steps, m):
    mi = (steps+1) // 2

    for i in range(mi, steps+1):
        if i % m == 0:
            return i
    return -1



# print log(64, 2)
print numberOfSteps(3, 5)
print numberOfSteps(10, 2)