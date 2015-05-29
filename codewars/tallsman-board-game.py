def get_required(player,enemy):
    left, right = sum(player), sum(enemy)
    if left == right:
        return 'Random'
    elif left - right >= 6:
        return 'Auto-win'
    elif left - right <= - 6:
        return 'Auto-lose'
    elif left - right > 0:
        diff = 6 - (left-right) +1

        return '({}..6)'.format(diff)
    elif right - left > 0:
        diff = 6 - (right -left) -1
        if diff == 0:
            return '(1..0)'
        else:
            return '(1..{})'.format(diff)