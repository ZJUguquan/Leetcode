'i am a knight'


def position(p):
    return ord(p[0]) * 10 + int(p[1])


def in_boundary(p):
    if 1 <= p[0] <= 8 and 1 <= p[1] <= 8:
        return True
    return False


def next_position(p1):
    hori = [-1, -1, 1, 1, -2, -2, 2, 2]
    vori = [2, -2, 2, -2, 1, -1, 1, -1]
    x, y = ord(p1[0]) - 96, int(p1[1])
    next_p1_candidate = []
    for i in range(8):
        next_p1_candidate.append((x + hori[i], y + vori[i]))
    next_p1 = [i for i in next_p1_candidate if in_boundary(i)]
    return [chr(96 + i[0]) + str(i[1]) for i in next_p1]

# print(next_position('a1'))


# def one_step(p1, p2):
#     if abs(p1[0] - p2[0]) == 1 and abs(p1[1] - p2[1]) == 2:
#         return True
#     if abs(p1[0] - p2[0]) == 2 and abs(p1[1] - p2[1]) == 1:
#         return True
#     return False


def shortest(p1, p2):
    if p1 == p2:
        return 0
    next_p1_candidate = next_position(p1)
    if p2 in next_p1_candidate:
        return 1
    used_step = 1
    while p2 not in next_p1_candidate:
        for i in next_p1_candidate:
            next_p1_candidate = next_p1_candidate + next_position(i)
        used_step += 1
    return used_step


p1 = 'a1'
p2 = 'f4'
# print(one_step_knight_position(p1, p2))
print(shortest(p1, p2))
