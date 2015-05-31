# float sign (fPoint p1, fPoint p2, fPoint p3)
# {
#     return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
# }

# bool PointInTriangle (fPoint pt, fPoint v1, fPoint v2, fPoint v3)
# {
#     bool b1, b2, b3;

#     b1 = sign(pt, v1, v2) < 0.0f;
#     b2 = sign(pt, v2, v3) < 0.0f;
#     b3 = sign(pt, v3, v1) < 0.0f;

#     return ((b1 == b2) && (b2 == b3));
# }


# def sign(p1, p2, p3):
#     return (p1[0]-p3[0])*(p2[1]-p3[1]) - (p2[0]-p3[0]) *(p1[1]-p3[1])


# def oneline(A, B, C):
#     (x1, y1), (x2, y2), (x3, y3) = A, B, C
#     if x1==x2 and x2 == x3:
#         return True
#     if (x1 != x2 and x1 !=x3) and (y2-y1)/float(x2-x1) == (y3-y1)/float(x3-x1):
#         return True
#     return False

# def point_vs_triangle(point, triangle):
#     A, B, C = tuple(triangle)
#     (x1, y1), (x2, y2), (x3, y3) = A, B, C

#     if oneline(A, B, C):
#         raise ValueError('Not a valid triangle')

#     if any([oneline(A,B,point), oneline(A,C,point), oneline(B,C,point)]):
#         return 0
#     v1, v2, v3 = triangle
#     b1 = sign(point, v1, v2) < 0
#     b2 = sign(point, v2, v3) < 0
#     b3 = sign(point, v3, v1) < 0
#     if b1 == b2 and b2 == b3:
#         return 1
#     else:
#         return -1


# using Heron's formula
def side(p1, p2):
    x1, y1 = p1; x2, y2 = p2
    return ((x1-y1)**2 + (x2-y2)**2)**.5

def heron(p1, p2, p3):
    a = side(p1, p2)
    b = side(p2, p3)
    c = side(p1, p3)
    p = (a+b+c)/2.0
    return (p*(p-a)*(p-b)*(p-c))**.5

def heron(p, [p1, p2, p3]):
    h1 = heron(p, p1, p2)
    h2 = heron(p, p2, p3)
    h3 = heron(p, p1, p3)
    try:
        H = heron(p1, p2, p3)
        if h1*h2*h3 == 0:
            return 0

        if h1 + h2 + h3 == H:
            return 1
        return -1
    except Exception, ValueError:
        raise ValueError('ABC not valid triangle')










triangle = [[0,0], [5,5], [5,0]]
p = [3, 1]
p = [6, 6]
print point_vs_triangle(p, triangle)



