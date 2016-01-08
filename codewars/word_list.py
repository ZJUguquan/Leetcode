from itertools import permutations


s = 'shi'
for i in permutations(s):
    print ''.join(i)



def unscramble(s):
	global word_list
	r = []
    for w in word_list:
    if set(w) = set(s):
    	r.append(w)
    return r