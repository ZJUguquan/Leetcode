def collatz(n):
    res = []
    res.append(n)
    while n > 1:
        if n % 2 == 0:
            res.append(n//2)
            n = n // 2
        elif n > 2:
            n = 3*n +1
            res.append(n)
        elif n == 1:
            res.append(1)
            break
    return len(res)

n = 20
print(collatz(n))