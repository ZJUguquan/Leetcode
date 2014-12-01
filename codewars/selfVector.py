'''
a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
a.add(b) # should return Vector([4,6,8])
a.subtract(b) # should return Vector([-2,-2,-2])
a.dot(b) # should return 1*3+2*4+3*5 = 26
a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
a.add(c) # raises an exception
'''
class Vector:
    def __init__(self, v=[0]):
        self.stack = v

    def __repr__(self):
        res = '('
        res += ','.join([str(i) for i in self.stack])
        res += ')'
        return  res # 'vecotr:{}'.format(res)

    # def __repr__(self):
    #     res = ''
    #     for i in self.stack:
    #         res += ' '
    #         res += str(i)
    #     return 'vecotr:{}'.format(res)

    def equals(self, other):
        return all([self.stack[i] - other.stack[i] ==0 for i in range(len(self.stack))])

    def add(self, other):
        if len(self.stack) != len(other.stack):
            raise TypeError('expected a length-equal vector to be as argument.')
        return Vector([self.stack[i] + other.stack[i] for i in range(len(self.stack))])

    def subtract(self, other):
        if len(self.stack) != len(other.stack):
            raise TypeError('expected a length-equal vector to be as argument.')
        return Vector([self.stack[i] - other.stack[i] for i in range(len(self.stack))])

    def dot(self, other):
        if len(self.stack) != len(other.stack):
            raise TypeError('expected a length-equal vector to be as argument.')
        return sum([self.stack[i] * other.stack[i] for i in range(len(self.stack))])
    def norm(self):
        import math
        return math.sqrt(sum([i*2 for i in self.stack]))

a = Vector([1,2,3])
b = Vector([4,5,6])

print(a.add(b))
print(a.dot(b))
print(a.subtract(b))
print(a.norm())

d = Vector([1,2,3])
c = Vector([3,3,3,1,3])
# print(a.add(c))

print(a.equals(d))