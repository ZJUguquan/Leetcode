adict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 
    'e': '.', 'f': '..-.', 'g':'--.', 'h':'....', 
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
    'm':'--','n':'-.','o': '---','p':'.--.','q':'--.-',
    'r':'.-.','s':'...','t':'-', 'u':'..-','v':'...-',
    'w':'.--','x':'-..-','y':'-.--','z':'--..'
    '1':'.----', '2':'..---','3':'...--','4':'....-',
    '5': '.....','6':'-....','7':'--...','8':'---..',
    '9':'----.', '0':'-----'

}
adict2 = dict(zip(adict.values(), adict.keys() ))
print(adict2)

def more(m):
	import re
	result = ''
	words =  re.split('(\s+)', m)
	for w in words:
		if w in adict2:
			result += adict2[w].upper()
		if w.count(' ') > 1:
			result += ' '
	return result
m = '.... . -.--   .--- ..- -.. .'
print(more(m))
import re
print(re.split('(\s+)', m))