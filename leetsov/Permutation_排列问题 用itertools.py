

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        def permutations(iterable, r=None):
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n-r, -1))
            yield tuple(pool[i] for i in indices[:r])
            while n:
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                else:
                    return
        return [ list(i) for i in permutations(num) ]


# coding: utf-8


# 下面是 Itertools 源码
def permutations(iterable):
    pool = tuple(iterable)
    n = len(pool);r = n
    indices = list(range(n))
    cycles = list(range(n, 0, -1))
    yield tuple(pool[i] for i in indices[:n])
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

ans = list(set(permutations([1,1,0,0,1,-1,-1,1])))
print(ans)
# result = []
# for ele in ans:
#   result.append(list(ele))
# print(result)