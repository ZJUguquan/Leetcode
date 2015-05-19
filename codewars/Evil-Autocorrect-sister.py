
import re

def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

print autocorrect('u')
print autocorrect('you')
print autocorrect('Youuu')
print autocorrect('youtube')
print autocorrect('i miss you!')