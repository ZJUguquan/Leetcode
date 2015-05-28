# coding: utf-8




from pprint import pprint

# four directions

minemap = [[True, True, True],
  [False, False, True],
  [True, True, True],
 [True, True, True]
  ]


def remap(minemap):
    rows = len(minemap[0])
    columns = len(minemap)

    newmap = [ [False] * columns for r in range(rows)]
    for r in range(r):
        for c in range(columns):
            newmap[r][c] = minemap[c][r]
    pprint(newmap)

remap(minemap)

minner = {'x':0, 'y':0}
exit = {'x': 2, 'y': 2}

def solve(map, miner, exit):
    # map size:
    size = len(map)
    if size <= 1 or miner == exit:
        return []

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