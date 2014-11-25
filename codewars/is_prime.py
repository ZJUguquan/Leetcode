def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  if n <=1 : return False
  return False if any( [ n%i ==0 for i in range(2,n-1) ]) else True



'Better Solution'

def is_prime(n):
  return n > 1 and all(n % i for i in xrange(2, n))