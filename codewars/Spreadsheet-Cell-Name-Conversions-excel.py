class SpreadSheetHelper(object):

    def convert_to_display(self, internal):
        mapping = dict(zip(range(26), [chr(i) for i in range(65, 65+27)]))

        c = internal[0]
        column = ''
        while c > 26:
            c, yu = divmod(c, 26)
            column += mapping[yu]

        r = internal[1] + 1
        return "A1"

    def convert_to_internal(self, display):
        """
        Converts a display coordinate into an internal coordinate
        internal is in the form string "CR" where C is the column display name, and R is the row display name
        returns a tuple in the form (row, column)
        """
        return (0, 0)


s = SpreadSheetHelper()
print(s.convert_to_display((3, 2)))



import re


mapping = dict(zip(range(1, 27), [chr(i) for i in range(65, 65+27)]))
inv_mapping = {v:k for k, v in mapping.items()}
mapping[0]='Z'

def r26(column):
    if column <= 26:
        return mapping[column]
    else:
        m, n = divmod(column, 26)
    return r26(m) + mapping[n]

def f26(word):
    word = word.upper()
    return sum([26**idx*inv_mapping[i] for idx, i in enumerate(word[::-1])])

print(f26('AZDQDA'))
print(r26(23844653))

class SpreadSheetHelper(object):
    @classmethod
    def convert_to_display(cls, internal):
        m, n = internal
        return r26(m+1)+ str(n+1)

    @classmethod
    def convert_to_internal(cls, display):
        s = display
        pattern = re.compile(r'^([a-zA-Z]*)(\d*)$')
        result = re.match(pattern, s)
        word, number = result.group(1), result.group(2)
        column = f26(word)
        row = int(number) - 1
        return (column-1, row)

s = SpreadSheetHelper()
print SpreadSheetHelper.convert_to_display((23844652, 2342398743))
print SpreadSheetHelper.convert_to_internal('AZDQDA2342398744')





########################################
class SpreadSheetHelper(object):

    @staticmethod
    def convert_to_display(internal):
        """
        Converts an internal coordinate into a display coordinate
        internal is in the form (row, column)
        returns a string in the form "CR" where C is the column display name, and R is the row display name
        """
        #print "convert_to_display({})".format(internal)
        col, row = internal

        row += 1
        n_to_c = lambda n: chr(ord('A') + n)
        digits = []
        pow = 1
        n = col
        while n >= 0:
            mod = 26 ** pow
            div = 26 ** (pow - 1)
            digit = (n // div) % 26
            digits.append(n_to_c(digit))
            n -= mod
            pow += 1
        out_col = "".join(reversed(digits))

        result = "{}{}".format(out_col, row)
        #print "  {} -> {}".format(internal, result)
        return result


    @staticmethod
    def convert_to_internal(display):
        """
        Converts a display coordinate into an internal coordinate
        internal is in the form string "CR" where C is the column display name, and R is the row display name
        returns a tuple in the form (row, column)
        """
        #print "convert_to_internal({})".format(display)
        #print "display: {}".format(display)
        col = "".join([c for c in display if 'A' <= c <= 'Z'])
        row = int("".join([c for c in display if '0' <= c <= '9'])) - 1
        #print "col: {}, row: {}".format(col, row)

        c_to_n = lambda c: ord(c) - ord('A')
        out_col = 0
        power = 0
        for c in reversed(col):
            out_col += (c_to_n(c) % 26) * (26 ** power)
            if power > 0:
                out_col += 26 ** power
            power += 1
        result = (out_col, row)
        #print "  {} -> {}".format(display, result)
        return result