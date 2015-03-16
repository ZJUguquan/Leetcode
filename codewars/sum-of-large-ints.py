def ssum(n):
    return n * (n+1) // 2


def f(n, m):
    #My function body is ready
    smallsum =  ssum(m-1)
    if n < m:
        return ssum(n)
    s = n // m
    y = n % m
    return s * smallsum + ssum(y)
