
# coding: utf-8


# Challenge 3
# url: equality

def o(msg=None):
    print(('*' * 30 + str(msg) + '*' * 30).center(80))

print tuple('ABC') > ('A', 'A', 'A')

url = 'http://www.pythonchallenge.com/pc/def/equality.html'


from urllib import urlopen
from string import ascii_lowercase, ascii_uppercase
import re
print ord('a'), ord('z'), ord('A'), ord('Z')
output = ''
content = urlopen(url).read()
content = content[490: -5]

print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content))



# challenge 4
# url:linkedlist.php
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
#
# One small letter,
# surrounded by EXACTLY three big bodyguards on each of its sides.
