adict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.', 'f': '..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
    'm':'--','n':'-.','o': '---','p':'.--.','q':'--.-',
    'r':'.-.','s':'...','t':'-', 'u':'..-','v':'...-',
    'w':'.--','x':'-..-','y':'-.--','z':'--..',
    '1':'.----', '2':'..---','3':'...--','4':'....-',
    '5': '.....','6':'-....','7':'--...','8':'---..',
    '9':'----.', '0':'-----', 'sos':'...---...'

}
adict2 = dict(zip(adict.values(), adict.keys() ))


def decodeMorse(m):
    import re
    result = ''
    words =  [w for w in re.split('(\s+)', m) if len(w) > 0]
    for w in words:
        if w in MORSE_CODE:
            result += MORSE_CODE[w].upper()
        if w.count(' ') > 1:
            result += ' '
        if w in ['!', ',']:
            result += w
    return result.strip()