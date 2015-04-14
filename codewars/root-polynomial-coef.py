from itertools import combinations
from operator import mul

def polyCoeffs(roots):
    roots = [-i for i in roots]
    result = []
    for i in range(len(roots), 0, -1):
        iteror = combinations(roots, i)
        s = 0
        for each in iteror:
            s += reduce(mul, each)
        result.append(s)
        # res = sum(list(iteror))
    result.append(1)
    return result[::-1]
        # result.append(res)

roots = [1, 2, 3, 4]
print(polyCoeffs(roots))



#########################################################



from itertools import product

def mulCoeffs(p, q):
    ret = [0,] * (len(p) + len(q) - 1)
    for ((i, a), (j, b)) in product(enumerate(reversed(p)),enumerate(reversed(q))):
        ret[len(p) + len(q) - i - j - 2] += a * b
    return ret

def polyCoeffs(roots):
    return reduce(mulCoeffs, ((1, -c) for c in roots), (1,))