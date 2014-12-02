def always(n=0):
    ""
    return lambda x=3: 3
three = always(3)

print(three())

#Test.expect(three() == 3)


def always(n=0):
    return lambda: n


class Python():
    def __init__(self, name):
        self.name = name

bubba = Python('Bubba')
print(bubba.name) # should return 'Bubba'


class Ghost(object):
    # your code goes here
    _color = ['white','yellow','purple','red']
    def __init__(self):
        from random import randint
        c = randint(0,3)
        self.color = self._color[c]

g = Ghost()
print(g.color)

