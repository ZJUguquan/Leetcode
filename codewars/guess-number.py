
from random import randint, seed
seed(1428)
a, b = 1, 100
target = randint(a, b)

print 'target %d' % target

def guess_number(percentile, a, b, guess_cnt = 1):
    '''
    percentile: 0~100% of interval.

    e.g.  1, 100; p=0.518 so the result -> 0.518(99) + 1 = 52.282 -. 53

    '''

    if percentile > 1 or percentile < 0:
        raise ValueError('wrong p')
    if a == b:
        return guess_cnt

    guess = min(a, b) + abs(b-a) * percentile


    if guess > target:
        print guess_cnt
        guess_number(percentile, a, guess, guess_cnt+1)
    elif guess < target:
        print guess_cnt
        guess_number(percentile, guess, b, guess_cnt+1)
    else:
        return guess_cnt


print guess_number(0.5, 1, 100, 1)
print guess_number(0.618, 1, 100, 1)