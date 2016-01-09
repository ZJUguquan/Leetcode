

def insert_dash(num):
	s = str(num)
	if len(s) < 2:
		return s
	res = ''.join([  (int(ele) * int(s[idx+1])) % 2 and ele +'-'  or ele  for idx, ele in enumerate(s[:-1]) ])
	res += s[-1]
	return res

print(insert_dash(12345123))


import re

def insert_dash(num):
    #your code here
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
