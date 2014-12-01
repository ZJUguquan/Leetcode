
'use this later'

import itertools

def power(s):
  "Computes all of the sublists of s"
  return [list(c) for i in range(len(s)+1) for c in itertools.combinations(s, i)]

def power(s):
    """Computes all of the sublists of s"""
    res = [];  res.append([])
    # for ele in s:
    #     for exist in res:
    #         exist.append(ele)
    #         res.append(exist)

    return res


s = [1,2,3]

print(power(s))

def subset(S):
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

print(subset([12,3,4]))