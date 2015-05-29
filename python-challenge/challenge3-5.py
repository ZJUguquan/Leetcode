
# coding: utf-8


# Challenge 3
# url: equality

def o(msg=None):
    print(('*' * 30 + str(msg) + '*' * 30).center(80))

# print tuple('ABC') > ('A', 'A', 'A')

url = 'http://www.pythonchallenge.com/pc/def/equality.html'


from urllib import urlopen
from string import ascii_lowercase, ascii_uppercase
import re
# print ord('a'), ord('z'), ord('A'), ord('Z')
output = ''
content = urlopen(url).read()
content = content[490: -5]

print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content))

import re

# challenge 4
# url:linkedlist.php

start = 82930
base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url = base + str(start)
# print urlopen(url).read()
# tips: None

# 8022 ->  16044  - ....  66831

# result: peak.html

print url
i = 1
# while i < 400:
#     content = urlopen(url).read()
#     print content
#     number = re.search(r'nothing is (\d+)', content).group(1)
#     url = base + number
#     print url
#     i += 1

# One small letter,
# surrounded by EXACTLY three big bodyguards on each of its sides.



# challenge 5: peak.url
# http://www.pythonchallenge.com/pc/def/peak.html

# tips: pronounce it

url = 'http://www.pythonchallenge.com/pc/def/peak.html'
url = 'http://www.pythonchallenge.com/pc/def/banner.p'

try:
   import cPickle as pickle
except:
   import pickle
data_string = urlopen(url).read()
from pprint import pprint
pprint( pickle.loads(data_string))
data = pickle.loads(data_string)

for dd in data:
    print ''.join([d[0] * d[1] for d in dd])

# result: channel