
# coding: utf-8




def o(msg=None):
    print( ('*'*30+str(msg)+'*'*30).center(80))


# challenge 0
print 2**38

# challenge 1
# url: map
test = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
'''
from string import ascii_lowercase
from string import maketrans
output = ''
for t in test:
    if t in ascii_lowercase:
        output += ascii_lowercase[(ascii_lowercase.index(t)+2)%26]
    else:
        output += t
print output
maps = maketrans(ascii_lowercase, ascii_lowercase[2:]+ascii_lowercase[:2])
print test.translate(maps)
print 'map'.translate(maps)


# challenge 2
# url: ocr

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
from urllib import urlopen

# content capsuled in chalen2.txt
from collections import Counter
with open('chalen2.txt', 'r') as f:
    f_content = f.read()
    c = Counter(f_content)
    print c

    res = [k for k in c if c[k] < 2]
    items = dict()
    for r in res:
        items[r] = f_content.index(r)
    print sorted(items.items(), key=lambda x: x[1])
    # answer: equality
