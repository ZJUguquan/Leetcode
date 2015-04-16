number = [i for i in range(1, 27)]
from string import ascii_uppercase
mapping = dict(zip(ascii_uppercase, number))
print(mapping)

str = 'ABC'

# print(ord('B') - 64)
s = 0
for idx, ele in enumerate(str):
    loc = len(str) - 1 - idx
    s += 26 **loc * mapping[ele]

print(s)