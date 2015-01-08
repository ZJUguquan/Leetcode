

# Test.expect( 0 == bowling_score( [0]*20 ) )

# Test.expect( 300 == bowling_score( [10]*12 ) )
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0]
# b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0]
# b = [10] * 12
b = [9, 1] * 10 + [9]


def bowling_score(b):
    b = b[::-1]
    sum_score = 0
    turn = range(0, 10)
    for t in turn:
        if len(b) < 1:
            break
        first = b.pop()
        sum_score += first
        # strike
        if first == 10:
            # print('strike', t)
            if t < 9:
                sum_score += sum(b[:2])
                continue
            if t == 9:
                sum_score += sum(b[:2])
                break
        if len(b) > 0:
            second = b.pop()
            sum_score += second
        if first + second == 10:
            if t < 9:
                sum_score += sum(b[:1])
                continue
            if t == 9:
                sum_score += sum(b[:1])
                break
        if first + second < 10:
            continue
    return sum_score

print(bowling_score(b))


def bowling_score(rolls):
    "Compute the total score for a player's game of bowling."

    def is_spare(rolls):
        return 10 == sum(rolls[:2])

    def is_strike(rolls):
        return 10 == rolls[0]

    def calc_score(rolls, frame):
        return (sum(rolls) if frame == 10 else
                sum(rolls[:3]) + calc_score(rolls[1:], frame + 1) if is_strike(rolls) else
                sum(rolls[:3]) + calc_score(rolls[2:], frame + 1) if is_spare(rolls) else
                sum(rolls[:2]) + calc_score(rolls[2:], frame + 1))

    return calc_score(rolls, 1)
Best Practices3Clever0
0ForkLink
SeanGoku11
