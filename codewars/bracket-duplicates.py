
using regex


import re
def string_parse(string):
    return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', string) if isinstance(string, str) else 'Please enter a valid string'

########################################################################

import itertools

def string_parse(string='aaaabbcdefffffffg'):

    if not isinstance(string, str):
        return 'Please enter a valid string'
    result = itertools.groupby(string)
    output = ''

    for _, group in result:
        li = list(group)
        if len(li) <= 2:
            output += ''.join(li)
        else:
            output += ''.join(li[:2])+'['+''.join(li[2:])+']'
    return (output)