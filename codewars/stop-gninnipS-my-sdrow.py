import re

def spin_words(sentence):
    return ' '.join([len(w) < 5 and w or w[::-1] for w in sentence.split() ])