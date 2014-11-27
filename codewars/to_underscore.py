def to_underscore(astring):
    # your code here
    import string
    res = ''; astring = str(astring)
    if len(astring)>= 1:
        for i in range(len(astring)):
            if i == 0:
                res += astring[i].lower()
            elif astring[i] in string.ascii_uppercase:
                res += '_'
                res += astring[i].lower()
            else:
                res += astring[i]
    return res
print(to_underscore('TestController'))



'use re.'

import re

def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()