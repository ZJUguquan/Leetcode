def point_vs_vector(point, vector):
    mapping = {True: -1, False: 1}
    vector.sort(key=lambda x: x[0])
    p1 = vector[0]
    p2 = vector[1]
    x1, y1 = p1
    x2, y2 = p2
    x, y = point
    if x1 == x2:
        if x == x1:
            return 0
        return mapping[x < x1]
    else:
        k = (y2 - y1) / float(x2 - x1)
        flag = k * (x - x1) + y1 - y
        if flag == 0:
            return 0
        return mapping[flag<0]

# i pass.

class Test(object):

    @staticmethod
    def assert_equals(left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'

print ord('F')
test = Test()

point = [-6560, 106]
vector = [[1997, -9034], [-4939, 4425]]
test.assert_equals(point_vs_vector(point, vector), 1)

# point = 2, 2
# test.assert_equals(point_vs_vector(point, vector), 0)

point = 2, 0
vector = [[0, 0], [1, 1]]
test.assert_equals(point_vs_vector(point, vector), 1)


# fengex

########################################################################

def point_vs_vector((px, py), ((vbx, vby), (vex, vey))):
    cp = (vex - vbx) * (py - vby) - (px - vbx) * (vey - vby)
    return (cp < 0) - (cp > 0)