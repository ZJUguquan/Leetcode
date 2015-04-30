
import re

text = "'test'; --when comment started - this is not 'literal'"
#"select aaa, bbb, ccc, /*'ddd'?*/ into row from table;"
#"if a>'data'and b<'nnn' then c:='test'; end if;"
#"select 'text' into row from table where a = 'value'"
text = re.sub(r'/\*.*?\*/', '', text)
text = re.sub(r'--.*\n?', '', text)
print(text)
res = []
for m in re.finditer(r'(\'.*?\')', text):
    # print(m.start(), m.start() + len(m.group()) )
    res.append( (m.start(), m.start() + len(m.group()) ))

print(res)



## solution

import re
def get_textliterals(pv_code):
  print pv_code
  result = [(match.start(1), match.end(1)) for match in re.finditer(r"(?:--[^\n]*\n?|/\*.*?\*/|((?:'[^']*')+|'[^']*$)|.)", pv_code, re.MULTILINE) if match.group(1)]
  return result
