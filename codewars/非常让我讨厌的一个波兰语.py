mapping = {0:'', 1: 'jeden', 2: "dwa", 3: "trzy", 4: "cztery", 5: "piec", 6: "szesc", 7: "siedem", 8: "osiem", 9: "dziewiec", 10: "dziesiec", 11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "pietnascie", 16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewietnascie", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "piecdziesiat",60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewiecdziesiat"}


class Translator(object):
    def ordering_beers(self, beers):
        print 'bbbbeers: %d' % beers
        posix = ' poprosze'
        if beers <0:
            raise ValueError('No negatives!')
        if beers == 0:
            return 'Woda mineralna' + posix
        elif beers == 1:
            return 'Jedno piwo' + posix
        elif beers in (12,13,14):
            return mapping[beers].title() + ' piw' + posix
        elif beers % 10 in (2, 3, 4):
            units = beers % 10
            tens = beers - units
            if tens > 0:
                r = mapping[tens].title() + ' ' + mapping[units]
            else:
                r = mapping[units].title()
            return (r + ' piwa' + posix).replace('  ', ' ')
        else:

            if beers in mapping:
                return mapping[beers].title() + ' piw' + posix

            units = beers % 10
            tens = beers - units
            if tens > 0:
                r = mapping[tens].title() + ' ' + mapping[units]
            else:
                r = mapping[units].title()
            return (r + ' piw' + posix).replace('  ', ' ')