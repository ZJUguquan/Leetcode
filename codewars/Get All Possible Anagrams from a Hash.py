#Brief

from itertools import chain, permutations

def get_words(hash_of_letters):
    return sorted(set(''.join(v) for v in permutations(chain.from_iterable(v * k for (k, v) in hash_of_letters.iteritems()))))



########################################################################

# brute method
from itertools import permutations


def get_words(hash_of_letters):
    raw_string = ''
    for count, _letters in hash_of_letters.items():
        raw_string += ''.join(count * _letters)

    res = []
    for i in permutations(raw_string):
        _ = ''.join(i)
        if _ not in res:
            res.append(_)
    return res


print get_words({1: ["a", "b", "c"]})
#  "abc", "acb", "bac", "bca", "cab", "cba"], "Nope! Try again.")

print get_words({2: ["a"], 1: ["b", "c"]})

# .: ['bcaa', 'baca', 'baac', 'cbaa', 'caba', 'caab', 'abca', 'abac', 'acba', 'acab', 'aabc', 'aacb']
#    ['aabc', 'aacb', 'abac', 'abca', 'acab', 'acba', 'baac', 'baca', 'bcaa', 'caab', 'caba', 'cbaa']