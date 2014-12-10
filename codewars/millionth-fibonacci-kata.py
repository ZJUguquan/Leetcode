'''
F(n+1) = F(n) + F(n-1)

>> F(0) = F(1) = F(2) = 1, F(3) = 2

matrix form:
    F2 F1   1 1
    F1 F0   1 0

    F3 F2  1 1   F2  F1
    F2 F1  1 0   F1  F0
'''


def prod(m1, m2):
    a1,b1,c1,d1=m1
    a2,b2,c2,d2=m2
    return (a1*a2+b1*c2,a1*b2+c1*d2,a2*c1+c2*d1,b2*c1+d1*d2)
    # return sum([m1[i]*m2[i] for i in range(len(m1))])

def pow(m, n):
    if n == 1:
        return m
    elif n == 2:
        return prod(m, m)
    if n % 2 ==1:
        return prod(pow(pow(m, n//2),2) , m)
    else:
        return pow(pow(m, n//2),2)

def fib(n):
    if n < 2: return 1
    m = (1,1,1,0)
    a,b,c,d = pow(m, n-1)
    return a

print(fib(4))


def prod(m1, m2):
    a1,b1,c1,d1=m1
    a2,b2,c2,d2=m2
    return (a1*a2+b1*c2,a1*b2+c1*d2,a2*c1+c2*d1,b2*c1+d1*d2)
    # return sum([m1[i]*m2[i] for i in range(len(m1))])

def pow(m, n):
    if n == 1:
        return m
    elif n == 2:
        return prod(m, m)
    if n % 2 ==1:
        return prod(pow(pow(m, n//2),2) , m)
    else:
        return pow(pow(m, n//2),2)

def fib(n):
    if n < 2 and n > -1: return n
    if n == -1: return 1
    m = (1,1,1,0); N = abs(n)
    a,b,c,d = pow(m, N-1)

    return a if n >0 or n%2 !=0 else -1*a




'''

def fib(n):
  if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
  a = b = x = 1
  c = y = 0
  while n:
    if n % 2 == 0:
      (a, b, c) = (a * a + b * b,
                   a * b + b * c,
                   b * b + c * c)
      n /= 2
    else:
      (x, y) = (a * x + b * y,
                b * x + c * y)
      n -= 1
  return y

'''