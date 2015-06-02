
# coding: utf-8


from urllib import urlopen
def printcontent(url):
    print urlopen(url).read()

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
printcontent(url)

def o(msg=None):
    print( ('*'*30+str(msg)+'*'*30).center(80))

coords="179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282"

ci = map(int, coords.split(','))
ci.sort()
print ci

print len(ci)
xs = ci[::2]
ys = ci[1::2]

print xs
print ys

import matplotlib.pyplot as plt


# fig = plt.figure()
# ax = fig.add_subplot(111)

plt.plot(xs,ys)
plt.show()
