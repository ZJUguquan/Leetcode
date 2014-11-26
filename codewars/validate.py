def validate(n):
    _list = [int(s) for s in str(n)]
    lenth = len(_list)
    if length % 2 == 0:
        __list = [ _list[i] * 2 for i in range(len(_list)) if i % 2 == 0 ]
    pass



'better solution'

def validate(n):
    digits = [int(x) for x in str(n)]
    for x in xrange(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))
    return sum(digits) % 10 == 0


n = 891
_list = [int(s) for s in str(n)]
length = len(_list); __list = []
if length % 2 == 0: # length 2n
    for i in range(length):
        if i % 2 == 0:
            __list.append(_list[i]*2 if _list[i]*2 <=9 else _list[i]*2 -9 )
        else:
            __list.append(_list[i])

else: # length  2n+1
    for i in range(length):
        if i % 2 == 1:
            __list.append(_list[i]*2 if _list[i]*2 <=9 else _list[i]*2 -9 )
        else:
            __list.append(_list[i])
sumres = sum(__list)

print(sumres % 10 ==0)
