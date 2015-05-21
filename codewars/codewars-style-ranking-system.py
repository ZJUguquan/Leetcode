# coding: utf-8

def oye():
    print('*'*79)

oye()



class User(object):
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.ranks = range(-8, 0) + range(1, 9)

    def inc_progress(self, activity):
        if activity not in self.ranks:
            raise ValueError('')
        if self.rank == 8:
            return
        enhance = 0
        p1 = self.ranks.index(self.rank)
        p2 = self.ranks.index(activity)
        if p1 == p2:
            enhance = 3
        elif p2 == p1- 1:
            enhance = 1
        elif activity > self.rank:
            enhance = (p2 - p1) **2 * 10
        else:
            enhance = 0
        # print 'old info: {rank} {progress} Awesome!! You eared points {point}'.format(rank=self.rank, progress=self.progress, point=enhance)
        self.progress += enhance
        if self.progress // 100 > 0:
            self.rank = self.ranks[min(self.ranks.index(self.rank) + self.progress // 100, 15)]
            if self.rank == 8:
                self.progress = 0
        self.progress = self.progress % 100


# test case

user = User()
print  user.rank # => -8
print  user.progress # => 0

print  user.inc_progress(-1)
print  user.rank, user.progress, # => 10

oye()

print  user.inc_progress(-1) # will add 90 progress
oye()
print  user.inc_progress(1)
print  user.rank, user.progress

print  user.inc_progress(3)
print  user.rank, user.progress