

def make_acronym(phrase):
    print phrase
    if type(phrase) != str:
        return 'Not a string'
    else:

        for s in phrase:
            if s.isalpha() or s == ' ':
                continue
            else:
                return 'Not letters'

        res = ''.join([f[0].upper() for f in phrase.split()])
        return res


print make_acronym('YNAG JIN YONG')
print make_acronym(333)
print make_acronym('Yasfdj123 Jin132')
print make_acronym('333')

