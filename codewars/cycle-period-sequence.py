from unittest import TestCase
def cycle(sequence):
	counter = {}
	for i in sequence:
		if i not in counter:
			counter[i] = 1
		else:
			counter[i] += 1
	# print(counter)
	mincycle = [' ', -1]
	last_count = mincycle[1]
	last_index = mincycle[0]
	cycle_loop = []
	for idx, (k, v) in enumerate(counter.items()):
		if v != last_count:
			last_count = v
		if idx != last_index:
			last_index = idx
	print(idx, '--', k,v)
	pass

'second try'
def cycle(sequence):
	if len(set(sequence)) == 1:
		return [0, 1]
	sequence_more_than_twice = [i for i in  sequence if sequence.count(i) >= 2]
	if len(sequence_more_than_twice) < 2:
		return []
	max_occur = max(sequence_more_than_twice)
	curr_index = -1
	cache = []
	for i in sequence_more_than_twice:
		if sequence.count(i) < max_occur:
			curr_index = -1
		else:
			curr_index = sequence_more_than_twice.index(i)
			cache.append(i)
	if curr_index:
		pass

	cycle_index = []
	cache.append(sequence_more_than_twice[0])

'third try'

def amibigger(sequence):
	if len(sequence) <= 2:
		return False
	if max([sequence.count(i) for i in sequence]) < 2:
		return False
	for idx, e in enumerate(sequence):
		if idx  >0 and sequence.count(e) < sequence.count(sequence[idx - 1]) :
			return False
	return True

'Others'

def cycle(sequence):
	for j, x in enumerate(sequence):
		i = sequence.index(x)
		if 0 <= i < j:
			return [i, j - i ]
	return []

t = [1,2,3,4,2,3,4]
t = [1,2,3,4,5,3,4,5]
# t = []
print(amibigger(t))
print(cycle(t))
test =TestCase()

test.assertEqual(cycle([1,2,3,4,2,3,4]), [1,3], '1')
test.assertEqual(cycle([1,2,3,4]), []  , ' 2')