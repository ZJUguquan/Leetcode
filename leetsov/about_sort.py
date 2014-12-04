# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict
from operator import itemgetter
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



m = ["abc", "cba", "cad", "zzz"]

#sorted(m, key=m[0])

print m


"Sort a dict by its value"
dict1 = {1:2, 2:3, 4:9, 10:1}

sorted(dict1.items(), key = itemgetter(1))


print dict1
# print  "before:", dict1

# sorted(dict1, key =  dict1.get)

# d = defaultdict(int)
# print "sorted:", dict1
"failed"

d_sorted_by_value = OrderedDict(sorted(dict1.items(), key = lambda x: x[1]))
print d_sorted_by_value

print d_sorted_by_value.values()



strs = ["abcd", "abc", "ab", "abcdafda"]

dd = sorted(strs, key= len, reverse = False)
print dd


A = [1, 0]
A=sorted(A)
print A