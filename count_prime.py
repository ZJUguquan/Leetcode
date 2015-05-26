


def count_prime(n):
    _ =  filter( lambda x:
                len(filter(lambda y: x%y == 0,range(2,x-1))
                         ) == 0 , range(2,n) )
    return _

print count_prime(100)


