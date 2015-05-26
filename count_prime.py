


def count_prime(n):
    _ =  filter( lambda x:
                len(filter(lambda y: x%y == 0,range(2,x-1))
                         ) == 0 , range(2,n) )
    return _

print count_prime(100)


# 筛法

def shaifa(n):
    output = []
    numbers = range(2, n)
    start = numbers.pop(0)
    output.append(start)
    while options[-1] ** 2 > start:
        for i in range(start**2, n, start):
            numbers.remove(i)
        start = output.pop(0)
        output.append(start)

    return output

print shaifa(25)