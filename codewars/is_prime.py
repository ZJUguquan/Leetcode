
'Simple but slow'
# def is_prime(n):
#   return n > 1 and all(n % i for i in xrange(2, n))

def is_prime(n):
    if n in (2, 3, 5): return True
    if n % 2 == 0 or n % 3 == 0: return False
    return all(n % i for i in xrange(5, n, 6))


def left_right_prime(n):
    reversed_n = int(str(n)[::-1])
    if is_prime(n):
        return is_prime(reversed_n)
    return False


def backwardsPrime(start, nd):
    if start % 2:
        start += 1
    res = []
    for i in range(start+1, nd , 2):
        if left_right_prime(i):
            res.append(i)
    return res

print(is_prime(3299))
n = 97

print(back)
  # def number_property(n):
  #   if n <= 1:
  #       is_prime = False
  #   else:
  #       is_prime = True
  #       for i in xrange(2, int(n ** 0.5) + 1):
  #           if (n % i) == 0:
  #               is_prime = False
  #   return [is_prime, (n%2 == 0), (n%10==0)]


