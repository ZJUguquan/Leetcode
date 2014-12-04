'Reference  others'

current = 0
def fullJustify(words, L):
	results = []
	if len(words)<1 or words is None:
		return results
	aList = []
	i = 0
	while i < len(words) - 1:
		if current + len(aList) + len(words[i]) > L:
			results.append(buildWords(aList, L))
		aList.append(word)
		current += len(word)
		i += 1


a = [1,2,3,4,5]
# b = iter(a)
for i in b:
	print(i, next(b))