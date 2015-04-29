
def is_prime(n):
    if n in (2, 3, 5): return True
    if n % 2 == 0 or n % 3 == 0: return False
    return all(n % i for i in xrange(5, int(n**.5)+1, 2))


def left_right_prime(n):
    reversed_n = int(str(n)[::-1])
    if is_prime(n) and str(n) != str(n)[::-1]:
        return is_prime(reversed_n)
    return False


def backwardsPrime(start, nd):
    res = []
    for i in range(start, nd+1):
        if left_right_prime(i):
            res.append(i)
    return res

print(is_prime(70207))
print(left_right_prime(109561))

print(backwardsPrime(109536, 109669))




'''
[70001, 70009, 70061, 70079, 70121, 70141, 70163, 70207, 70241] should equal [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]

'''



def prime(a):
    if a == 2: return True
    if a < 2 or a % 2 == 0: return False
    return not any(a % x == 0 for x in range(3, int(a**0.5) + 1, 2))

def backwardsPrime(start, nd):
    return [x for x in range(start, nd + 1) if (str(x) != str(x)[::-1]) and prime(x) and prime(int(str(x)[::-1])) ]
