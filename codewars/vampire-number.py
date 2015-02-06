def vampire_test(x, y):
    sx, sy = str(x), str(y)
    return len(sx) == len(sy) and set(sx).union(set(sy)) == set(str(x*y) ) and (sx[-1], sy[-1]) != ('0', '0')


print(vampire_test(21, 60))
print(vampire_test(210, 600))
print(vampire_test(246, 510))



def vampire_test(x, y):
    sx, sy = str(x), str(y)
    if (x, y) == (0, 0):
        return False
    return  set(sx).union(set(sy)) == set(str(x*y) )