# coding: utf-8




from pprint import pprint

# four directions


def remap(minemap):
    rows = len(minemap[0])
    columns = len(minemap)
    newmap = [[9] * columns for r in range(rows)]
    for r in range(rows):
        for c in range(columns):
            newmap[r][c] = minemap[c][r]
    return newmap


minemap = [[True, True, True],
  [False, False, True],
  [False, False, True],
 [True, True, True]
  ]

pprint(remap(minemap))
print '_' * 40

def candidate_neibors(position, minemap):
    # position (i, j)
    r, c = position
    minemap = remap(minemap)
    size_r, size_c = len(minemap), len(minemap[0])
    return [ (minemap[i][j], [i, j])  for i in range(max(0,r-1), min(r+2, size_r)) for j in range(max(0,c-1), min(c+2, size_c)) if abs(i-position[0]) + abs(j-position[1]) == 1 and minemap[i][j]]


directions ={(0, 1): 'right', (0, -1): 'left', (1, 0): 'up', (-1, 0): 'down' }

def solve(map, miner, exit, remapFlag=False):
    size = len(map)
    if size <= 1 or miner == exit:
        return []
    if not remapFlag:
        map = remap(map)
        remapFlag = True

    exits = tuple([exit['x'], exit['y']])

    options = candidate_neibors(exits, minemap)

    print options

    for option in options:
        new_exit = {'x': option[1][0], 'y': option[1][1]}


solve(minemap, {'x':0,'y':0}, {'x':2,'y':0})

if __name__ == '__main__':
    print 'o ha you'



# Test.describe('A trivial map (1x1)')
# minemap = [[True]]

# Test.it('Should return an empty array, since we\'re already at the goal')
# Test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':0,'y':0}), [])

# Test.describe('A pretty simple map (2x2)')
# minemap = [[True, False],
#     [True, True]]

# Test.it('Should return the only correct move')
# Test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':1,'y':0}), ['right'])

# Test.it('Should return the only moves necessary')
# Test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':1,'y':1}), ['right', 'down'])

# Test.describe('A linear map(1x4)')
# minemap = [[True], [True], [True], [True]]

# Test.it('Should return a chain of moves to the right')
# Test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':3,'y':0}), ['right', 'right', 'right'])

# Test.it('Should return a chain of moves to the left')
# Test.assert_equals(solve(minemap, {'x':3,'y':0}, {'x':0,'y':0}), ['left', 'left', 'left'])

# Test.describe('Should walk around an obstacle (3x3 map)')
# minemap = [[True, True, True],
#   [False, False, True],
#   [True, True, True]]

# Test.it('Should return the right sequence of moves')
# Test.assert_equals(solve(minemap, {'x':0,'y':0}, {'x':2,'y':0}), ['down', 'down', 'right', 'right', 'up', 'up'])