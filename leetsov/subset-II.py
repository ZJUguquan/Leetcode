"""S= [1,2,2]
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]"""

def subsetsWithDup(S):
    pre, preCount = None, 1
    S.sort(); A = [ [] ]
    for n in S:
        count = len(A)
        if n == pre:
            count = preCount
        else:
            pre = n
            preCount = count
        for i in range(len(A) - count, len(A)):
            ss = A[i][:]
            ss.append(n)
            A.append(ss)
    return A

print(subsetsWithDup([1,2,3]))





class Solution:
    def subsetsWithDup(self, S):
        A = [[]]
        pre, preCount = None, 1
        S.sort()
        for n in S:
            count = len(A)
            if n == pre:
                count = preCount
            else:
                pre = n
                preCount = count
            for i in range(len(A)-count, len(A)):
                ss = A[i][:]
                ss.append(n)
                A.append(ss)
        return A


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return 'You want too big.'

    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


r2=combinations([1,2,3,4],2)

for index in r2:
    print( index )