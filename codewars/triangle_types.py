# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    shorter, mid, longer = min(a,b,c), sorted([a,b,c])[1] ,max(a,b,c)
    if shorter + mid <= longer: return 0
    mark = shorter ** 2 + mid **2 - longer ** 2

    if mark == 0:
        return 2
    elif mark <0 :
        return 3
    else:
        return 1
    print( shorter, mid, longer)



print(
triangle_type(200,200,300)
)


'better beautiful solution'

def triangle_type(a, b, c):
  x,y,z = sorted([a,b,c])
  if z >= x + y: return 0
  if z*z == x*x + y*y: return 2
  return 1 if z*z < x*x + y*y else 3

