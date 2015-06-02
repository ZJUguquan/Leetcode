print '*' * 80


class Test(object):

    def assert_equals(self, left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'
test = Test()


def direction(p1, p2):
    # give the direction from p1 to p2
    x1, y1 = p1['x'], p1['y']
    x2, y2 = p2['x'], p2['y']
    if x1 == x2:
        if y1 == y2-1:
            return 'up'
        elif y1 == y2+1:
            return 'down'
    if y1 == y2:
        if x1 == x2-1:
            return 'right'
        elif x1 == x2 + 1:
            return 'left'
    return None


def solve(map, miner=None, exit=None, output=[]):
    rows = len(map[0])
    cols = len(map)
    newmap = [[None] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if map[c][r] == True:
                newmap[r][c] = True
    # from exit ...
    if miner == exit:
        return output

    candidates = [ {'x':r, 'y':c} for r in range(max(0, exit['x']-1), min(exit['x']+2, rows))
                for c in range(max(0, exit['y']-1), min(exit['y']+2, cols) )
                if abs(r-exit['x']) + abs(c-exit['y']) == 1 and newmap[r][c]]

    print candidates
    print newmap

map = [[True, False],
    [True, True]]

print solve(map, exit={'x':1, 'y':1})