def levenshtein(a,b,cost=0):
	if len(a) * len(b) < 1:
		return max(len(a), len(b))

	# test if last characters of the strings match
	if a[-1] != b[-1]:
		cost = 1
	return min(levenshtein(a[:-1], b,0),
	           levenshtein(a, b[:-1],0),
	           levenshtein(a[:-1], b[:-1]) + cost
	           )


print(levenshtein("sitting", "kitten"))

