

game_state = [4, 2, 5, 1, 6]

from operator import xor

def choose_move(game_state):
    """Chooses a move to play given a game state"""
    x = reduce(xor, game_state)
    for i, amt in enumerate(game_state):
        if amt ^ x < amt:
            return (i, amt - (amt ^ x))


def choose_move(game_state):
    N_piles = len(game_state)
    if N_piles == 1:
        return (0, game_state[0])
    binnary_heap = [bin(i)[2:] for i in (game_state)]

    return binnary_heap

print(choose_move(game_state))
