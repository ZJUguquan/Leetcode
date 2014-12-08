def reverse_words(str):
    import re
    word_de = re.split('(\s+)', str)
    res = ''
    words = word_de[0::2]
    de = word_de[1::2] + ['']
    for i in range(len(de)):
        res += words[i][::-1]
        res += de[i]
    return res

print(reverse_words('yang jin   yongyong'))


'better '

import re

def reverse_words(str):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)