# coding:utf-8
#
#
import numpy as np
import random

np.random.seed(1428)

suffix = [
    "劍", "劍法", "劍譜", "劍訣",
    "槍", "槍法", "槍訣",
    "拳", "拳法", "拳譜",
    "刀", "刀法", "刀譜", "刀訣",
    "斬", "刺", "大法", "心訣", "心法", "訣", "寶典",
    "棍", "棍法", "棍譜", "棍訣",
    "指", "掌", "掌法", "腿", "攻", "鉤"
]

f = open('lastname.txt', 'r')
names = open('fn.txt', 'r')

ln_group = f.read().split('\n\n')
ln_group = [_.split(' ') for _ in ln_group]
# weight
weight = [100, 70, 10, 5, 1, 1]
prob = [float(i) / sum(weight) for i in weight]



name_c = [line.split()[1] for line in names.read().split('\n') if len(line) > 5]

for i in range(3, 10):
    print name_c[i]


def generate():
    r = np.random.rand()
    for ind, p in enumerate(prob):
        r -= p
        if r <= 0:
            print ind
            ln = random.choice(ln_group[ind])
            print ln
            break


# get a lname


f.close()
names.close()
