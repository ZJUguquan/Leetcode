


def spin_words(sentence):
    import re
    rev = [len(x) >= 5  and x[::-1] or x for x in re.split('\s', sentence)]
    return ''.join(rev)