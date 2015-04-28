
import re
print(re.sub(r'[yY]o(u+)$', 'your sister', 'you'))


def autocorrect(input):
    import re

    if len(input) == input.lower().count('u'):
        return 'your sister'
    words = input.split()
    res = []
    pattern = re.compile(r'[yY]o(u+)(\D+)')
    for w in words:
        if w.lower() == 'u'  :
            res.append('your sister')
        if re.match(pattern, w.lower()):
            match = re.match(pattern, w.lower())
            res.append('your sister'+match.group(2))
        else:
            res.append(w)
    return ' '.join(res)

input = 'I miss you!'

print(autocorrect(input))