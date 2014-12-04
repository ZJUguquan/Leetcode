'zigZag Convert'


def convert(s, nRows):
	if nRows <=1: return s
	lens = len(s)
	aString = [ ' ' for i in range(nRows)]

	row, step = 0, 1
	for i in range(lens):
		aString[i] =1



nRows = 3
aString = [ ' ' for i in range(nRows)]

print(aString)
