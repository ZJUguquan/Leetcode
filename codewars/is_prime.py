def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  if n <=1 : return False
  return False if any( [ n%i ==0 for i in range(2,n-1) ]) else True



'Better Solution'

def is_prime(n):
  return n > 1 and all(n % i for i in xrange(2, n))


  def number_property(n):
    if n <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in xrange(2, int(n ** 0.5) + 1):
            if (n % i) == 0:
                is_prime = False
    return [is_prime, (n%2 == 0), (n%10==0)]