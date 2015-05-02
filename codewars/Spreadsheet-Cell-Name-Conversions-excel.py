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