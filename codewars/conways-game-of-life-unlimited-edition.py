#
'''
Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:

1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

2. Any live cell with more than three live neighbours dies, as if by overcrowding.

3. Any live cell with two or three live neighbours lives on to the next generation.

4. Any dead cell with exactly three live neighbours becomes a live cell.

Each cell's neighborhood is the 8 cells immediately around it. The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively. You can take advantage of the htmlize function to get a text representation of the universe: eg:

print htmlize(cells)
'''





def neibors(x, y, board):
    '''
    count the neighbors for the position: x, y
    '''
    width, height = len(board[0]), len(board)
    count = 0
    for hor in [-1, 0, 1]:
        for ver in [-1, 0, 1]:
            if not hor == ver == 0 and (0 <= x + hor < height and
                                        0 <= y + ver < width):
                count += board[(x + hor) % height][(y + ver) % width]
    return count

def step(board, count=1):
    width, height = len(board[0]), len(board)
    for generation in range(count):
        new_board = [[False] * width for row in range(height)]
        for ind_row, row in enumerate(board):
            for ind_col, cell in enumerate(row):
                neibors_cnt = neibors(ind_row, ind_col, baord)
                current_state = board[ind_row][ind_col]
                should_live = neibors == 3 or (
                                neibors == 2 and current_state == True)
                new_board[ind_row][ind_col] = should_live

    return new_board

def get_generation(cells, generations):
    board = cells
    return step(board, generations)


def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<br/>')
    return ''.join(s)

start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]
end = [[0, 1, 0],
       [0, 0, 1],
       [1, 1, 1]]

test.describe('Glider<br/>' + htmlize(start))
# test.it('Glider 1')

resp = get_generation(start, 1)

print resp
# test.expect(resp == end, 'Got<br/>' + htmlize(resp) +
#             '<br/>instead of<br/>' + htmlize(end))
