def duplicate_encode(word):
    return ''.join([(word.lower().count(i.lower()) == 1 and ['('] or [')'])[0] for i in word ])


print(duplicate_encode('(( @'))