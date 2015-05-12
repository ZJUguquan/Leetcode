

def sol_equa(n):
    from math import sqrt, floor, ceil
    res = []
    if int(sqrt(n)) == ceil(sqrt(n)):
        res.append([int(sqrt(n)), 0])
    for i in range(1,  int(sqrt(n)) ):
        if n % i == 0:
            p, q = i, n//i
            if (p + q) % 2 == 0 and (q - p)% 4==0:
                res.append([(p+q)//2, (q-p)//4])
    return res


print sol_equa(16)