'isPrime'

def isPrime(x):
    return all([ x%i for i in range(2,x) ]) if x >=2 else False

print(isPrime(2))