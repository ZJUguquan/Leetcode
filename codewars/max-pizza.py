class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
        return self.memo[arg]

@Memoize
def max_pizza( cut ):
    if cut < 0:
        return -1
    if cut == 0:
        return 1
    elif cut == 1:
        return 2
    elif cut == 2:
        return 4
    else:
        return max_pizza(cut -1) + cut



def max_pizza( cut ):
    n = cut
    if cut < 0:
        return -1
    if cut == 0:
        return 1
    else:
        return 1 + n*(n+1)//2

http://weibo.com