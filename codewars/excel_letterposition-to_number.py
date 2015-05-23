# coding: utf-8


import re, string

def f26(word):
    inv_mapping = {u: string.ascii_uppercase.index(u) + 1 for u in upper}
    word = word.upper()
    return sum([26**idx*inv_mapping[i] for idx, i in enumerate(word[::-1])])


def convert_to_internal(excel):
    pattern = re.compile(r'^([a-zA-Z]*)$')
    result = re.match(pattern, excel)
    word = result.group(1)
    column = f26(word)
    return column

print convert_to_internal('AB')

