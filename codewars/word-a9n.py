'awesome solution'


import re
def abbreviate(s):
    ab = lambda w: w[:1] + str(len(w) - 2) + w[-1:]
    return re.sub(r'\w{4,}', lambda m: ab(m.group(0)), s)




def abbreviate(s):
    import re
    def abbword(word):
        return word[0] +str(len(word)-2) +word[-1] if len(word) >=4 else word
    words_delemetors = re.split('(\W+)', s)
    words = words_delemetors[0::2]
    delemetors = words_delemetors[1::2] +['']
    res = ''
    for i in range(0, len(words)-1):
        res +=  abbword(words[i])
        res += delemetors[i]
    res += abbword(words[-1])
    return res

# wordtr
w = 'internatio-nali zation'
w = 'yangjinyong'
w = 'cat, is-sits, the; mat; the-balloon; monolithic'
print(abbreviate(w))


# test
# Input: cat, is-sits, the; mat; the-balloon; monolithic':
#  c1t, is-s2s, t1e; m1t; t1e-b5n; m8c
# equal "cat, is-s2s, the; mat; the-b5n; m8c'"
# import re
# r = re.split(r'(\W+)', w)
# words = r[::2]
# dele = r[1::2] + ['']
# print(words)
# print(dele)

# print(abbreviate(w))