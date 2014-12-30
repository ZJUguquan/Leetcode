'i am a knight'


minus = lambda x, y: abs(ord(x) - ord(y))

def one_step_knight_position(p1, p2):
    x = minus(p1[0], p2[0])
    y = minus(p1[1], p2[1])
    if (x,y) in [(2, 1), (1, 2)]:
        return True
    return False

def one_step(p1, p2):
    if abs(p1[0] - p[2[0]]) == 1 and abs(p1[1] - p[2[1]]) == 2:
        return True
    if abs(p1[0] - p[2[0]]) == 2 and abs(p1[1] - p[2[1]]) == 1:
        return True
    return False

def in_boundary(p):
    if 1<=p[0]<=8 and 1<=p[1]<=8:
        return True
    return False

def shortest(p1, p2):

    # p1 to p2
    hori = [-1,-1, 1, 1, -2, -2, 2, 2]
    vori = [2, -2, 2, -2, 1, -1, 1, -1]
    x, y = ord(p1[0]) - 96, int(p1[1])
    x2, y2= ord(p2[0]) - 96, int(p2[1])
    if one_step((x, y), (x2, y2)):
        return 1

    next_p1_candidate = []
    for i in range(8):
        next_p1_candidate.append((x+hori[i], y+vori[i]))
    # print(next_p1_candidate)
    next_p1 = [i for i in next_p1_candidate if in_boundary(i)]
    return min([shortest ])


p1 = 'a7'
p2 = 'b3'
# print(one_step_knight_position(p1, p2))
print(shortest(p1, p2))