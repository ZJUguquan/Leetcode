# coding: utf-8
def exp_sum(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n

  for num in xrange(1, n+1):
    for i in xrange(num, n+1):
      dp[i] += dp[i-num]

  return dp[-1]

# using memoize

class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

@Memoize
def exp_sum(n):
    if n == 0: return 1
    result = 0; k = 1; sign = 1;
    while True:
        pent = (3*k**2 - k) // 2
        if pent > n: break
        result += sign * exp_sum(n - pent)
        pent += k
        if pent > n: break
        result += sign * exp_sum(n - pent)
        k += 1; sign = -sign;
    return result