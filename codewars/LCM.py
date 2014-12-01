'better way to do it'


from fractions import gcd

def lcm(*args):
    return reduce(lambda x,y: x * y / gcd(x,y), args)




def lcm(*args):
    """Compute the least common multiple of some non-negative integers"""
    def lcm2(a, b):
        'compute the least common multiple of a, and b'
        if a == b: return a
        if 0 in (a,b) or 1 in (a,b):return a*b
        m,n = min(a,b), max(a,b)
        while n % m > 0 :
            m, n = divmod(n, m)[1], m
        gcd = m
        return (a*b//gcd)

    if 0 in args: return 0
    args = sorted(args, reverse=True)
    # print(args)
    res = args[0]
    for i in args:
        if res % i >0:
            res = lcm2(res, i)
        else:
            pass
        # print(res)
    return res


print(lcm(1,2,3,4,5,6,7))



def lcm(a, b):
    '''
    compute the least common multiple of a, and b
    '''
    if a == b: return a
    if 0 in (a,b) or 1 in (a,b):return a*b
    m,n = min(a,b), max(a,b)
    while n % m > 0 :
        m, n = divmod(n, m)[1], m
    gcd = m
    return (a*b//gcd)



print(lcm(7,6))