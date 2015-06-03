


DELTA = 10 ** -12

def side((x1, y1), (x2, y2), (x, y)):
    return (y2 - y1) * (x - x1) + (x1 - x2) * (y - y1)

def point_vs_triangle(p, (a, b, c)):
    sides = tuple(side(p1, p2, p) for (p1, p2) in ((a, b), (b, c), (c, a)))
    assert abs(sum(sides)) > DELTA
    signs = tuple(0 if abs(s) < DELTA else 1 if s > 0 else -1 for s in sides)
    return (0 if sum(signs) else -1) if 0 in signs else (1 if abs(sum(signs)) == 3 else -1)










"***********************************************************"

def side(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2) ** .5


def heron(p1, p2, p3):
    a = side(p1, p2)
    b = side(p2, p3)
    c = side(p1, p3)
    p = (a + b + c) / 2.0
    if abs(b + c - a) > 10 ** -5:
        return (p * (p - a) * (p - b) * (p - c))**.5
        # return 'outside'
    else:
        return -9999  # 'inside'


def point_vs_triangle(p, triangle):
    p1, p2, p3 = tuple(triangle)
    h1 = heron(p1, p2, p)
    h2 = heron(p2, p3, p)
    h3 = heron(p1, p3, p)
    H = heron(p1, p2, p3)
    if p1 == p2 or p2 == p3 or p3 == p1 or H <= 0:
        raise ValueError('ABC not valid triangle')
    try:
        print '\t\t', h1, h2, h3
        if (h1 + h2 + h3 - H) > 10**-5:
            return -1
        elif h1 >0 and h2 > 0 and h3> 0 and H > 0:
            if (h1 + h2 + h3 - H) < 10**-5:
                return 1
        elif -9999 in (h1, h2, h3):
            return 0
        return 1
    except:
        raise ValueError('ABC not valid triangle')

Triangle = [[0, 0], [5, 5], [5, 0]]
points = [[3, 1], [6, 6], [2, 0]]
for point in points:
    print point_vs_triangle(point, Triangle)


# Example 5: Using memoization as decorator
class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]


@Memoize
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
