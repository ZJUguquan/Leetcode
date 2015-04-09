import re
def find(needle, haystack):
    if '_' not in needle:
        return haystack.find(needle)
    else:
        special = ['.', '^', '?', '$']
        needle = ''.join([  ( n in special and ['\\' +n] or [n])[0]   for n in needle ])
        pattern = re.compile(needle.replace('_', '.'))
        result = re.findall(pattern, haystack)
        if len(list(result))> 0:
            return  haystack.find(result[0])
        else:
            return -1



import re

def find(needle, haystack):
  special_cases = ['.', '$', '^', '?']
  needleRE = ''.join('\\' + n if n in special_cases else n for n in needle).replace('_', '.')
  a = re.search(needleRE, haystack)
  return -1 if not a else a.start()

haystack = "Once upon a midnight dreary, while I pondered, weak and weary.";
needle = '_\.'
print(find(needle, haystack))
