# using Heron's formula
def side(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2) ** .5


def heron(p1, p2, p3):
    try:
        a = side(p1, p2)
        b = side(p2, p3)
        c = side(p1, p3)
        p = (a + b + c) / 2.0
        return (p * (p - a) * (p - b) * (p - c))**.5
    except ValueError:
        raise ValueError('negative number')


def point_vs_triangle(p, triangle):
    p1, p2, p3 = tuple(triangle)

    try:
        h1 = heron(p, p1, p2)
        h2 = heron(p, p2, p3)
        h3 = heron(p, p1, p3)
        H = heron(p1, p2, p3)
        print h1, h2, h3, H

        if h1 + h2 + h3 > H:
            return -1
        if abs(h1 * h2 * h3) == 10**-8:
            return 0
        return 1

    except Exception, ValueError:
        raise ValueError('ABC not valid triangle')

triangle, point = [[0, 0], [5, 5], [5, 0]], [6, 6]
p1, p2, p3 = tuple(triangle)
# print side(p1, p2)
print point_vs_triangle(point, triangle)

# triangle= [[29, 38], [9, 54], [-40, 33]]
# point= [-25.3, 39.3]
triangle = [[95, -84], [88, -86], [55, 1]]
point = [92.9, -84.6]
print point_vs_triangle(point, triangle)


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
