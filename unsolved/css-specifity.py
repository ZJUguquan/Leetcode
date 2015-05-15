

def score_one(s):
    return s.count('#'), s.count('.'), int(s[0] not in '#.*')

def score(selector):
    vadd = lambda xs, ys: [x + y for x, y in zip(xs, ys)]
    return tuple(reduce(vadd, map(score_one, selector.split())))

def compare(s1, s2):
  return [s2, s1][score(s1) > score(s2)]


########################################################################

import re

def compare(a, b):
    return a if specificity(a) > specificity(b) else b

def specificity(s):
    return [len(re.findall(r, s)) for r in (r'#\w+', r'\.\w+', r'(^| )\w+')]