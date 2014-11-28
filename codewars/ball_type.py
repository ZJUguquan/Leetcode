class Ball(object):
    # your code goes here

    def __init__(self, name=None):
        if name is None:
            name = "regular"
        self.ball_type = name

b1 = Ball()
b2 = Ball("super1233")
print(b1.ball_type)
print(b2.ball_type)