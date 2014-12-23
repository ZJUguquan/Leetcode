
'''
"Any word or phrase that exactly reproduces the letters in another order is an anagram." (Wikipedia). Add numbers to this definition to be more interest.

Examples of anagrams:
'''
import string
def isAnagram(test, original):
    o = string.digits + string.ascii_letters
    return sorted(''.join([i.lower() for i in test if i in o])) == sorted(''.join([i.lower() for i in original if i in o]))

i = [('William Shakespeare', 'I am a weakish speller'),
('silent','listen'),
('12345 ',' 54321!@#!')
]
for e in i:
    print(isAnagram(i[0], i[1]))

p = string.punctuation
