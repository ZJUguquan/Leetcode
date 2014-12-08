
'Character frequency'

from collections import Counter
from string import ascii_letters
def  letter_frequency(s):
	count = Counter([e.lower() for e in s if e in ascii_letters ])
	count = sorted(zip(count.keys(), count.values()), key= lambda x: (x[1], ord(x[0]) *-1 ), reverse=True)
	return count



a ='aaAabb dddDD hhcc'
print(letter_frequency(a))
# result = letter_frequency('wklv lv d vhfuhw phvvdjh')
# expected = [('v', 5), ('h', 4), ('d', 2), ('l', 2), ('w', 2), ('f', 1), ('j', 1), ('k', 1), ('p', 1), ('u', 1)]