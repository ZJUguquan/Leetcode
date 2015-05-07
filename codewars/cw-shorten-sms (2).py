

import re
def shortener(message):
    msg = message
    while len(msg) > 160 and msg.find(" ") > -1:
        words = msg.split(" ")
        last = words.pop()
        prev = words.pop()
        words.append(prev + last[0].upper() + last[1:])
        msg = " ".join(words)
    return msg
















# Original message (169 chars):

#

# Shortened message (160 chars):

target_output = '''No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.'''

message = '''No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it.'''
message = '''There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon There is no spoon'''


l = len(message)
print(l)
res = ''
gaps = message.count(' ')


delta = l - 160
marker = gaps - delta

if l - gaps > 160:
    return ''.join([w.title() for w in message.split()])

for idx, words in enumerate(message.split()):
    if idx < marker:
        res += words + ' '
    elif idx == marker:
        res += words
    else:
        res += words.title()
print res
print(len(res))

# print(res, len(res))
# print(target_output)
# print(res == target_output)





# Test Passed
myout = 'Thereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoonthereisnospoon'
print(len(myout))

target = 'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'

print(len(target))