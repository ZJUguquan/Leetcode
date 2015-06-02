from itertools import combinations
from collections import defaultdict

def valid(a):
    print a
    dit = defaultdict(int)
    i = [len(a[i]) for i in range(len(a))]
    if max(i) != min(i) :
        return False
    each_size = len(a[0][0])
    all_peo = sorted(''.join(a[0]))

    for groups in a:
        _peo = sorted(''.join(groups))
        if _peo != all_peo:
            return False
        for group in groups:
            if len(group) != each_size:
                return False
            for com in combinations(group, 2):
                com = ''.join(sorted(list(com)))
                dit[com] +=1
    if len(dit.values()) > 0:
        return max(dit.values()) == 1
    return True

s = [
    ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
    ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
    ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
    ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
    ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]

s = [['ABC', 'DEF'], ['ADE', 'CBF']]

print valid(s)