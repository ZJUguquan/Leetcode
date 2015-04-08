def find_the_ball(start, swaps):
    for turn in swaps:
        if start in turn:
            l = list(turn)
            ind = l.index(start)
            del l[ind]
            start = l[0]
        else:
            continue
    return start