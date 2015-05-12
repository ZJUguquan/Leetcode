def ride(group,comet):
    from operator import __mul__
    from functools import reduce
    kk = [ord(i) - ord('A') + 1 for i in group.upper()]
    ll = [ord(i) - ord('A') + 1 for i in comet.upper()]
    group = reduce(__mul__, kk)
    comet = reduce(__mul__, ll)
    return 'GO' if group % 47 == comet % 47 else 'STAY'


print ride('cometq', 'hvngat')
group = "STARAB"
comet = "USACO"
print ride(group, comet)