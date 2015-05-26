

# def count_prime(n):
#     _ =  filter( lambda x:
#                 len(filter(lambda y: x%y == 0,range(2,x-1))
#                          ) == 0 , range(2,n) )
#     return _

# print count_prime(100)

from time import time


def shaifa(n):
    output = []
    numbers = range(2, n)
    if numbers is not None:
        start = numbers.pop(0)
        output.append(start)
        while numbers[-1] >= start**2:
            # print numbers, '@@@@@@', output
            for i in range(start**2, n, start):
                if i in numbers:
                    numbers.remove(i)
            start = numbers.pop(0)
            output.append(start)
            if not numbers or numbers[-1] >= start**2:
                continue
            else:
                break
        output += numbers
    return output

N = 10000

nn = time()
print shaifa(N)
print 'time: ', time() - nn
nn = time()
print filter(lambda x: len(filter(lambda y: x % y == 0, range(2, x - 1))) == 0, range(2, N + 1))
print 'time: ', time() - nn
