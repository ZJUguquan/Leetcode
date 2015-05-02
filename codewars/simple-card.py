mapping = dict(zip(map(str, range(2, 10)), range(2, 10) ))
# print(mapping)
mapping['T'] = 10
mapping['J'] = 11
mapping['Q'] = 12
mapping['K'] = 13
mapping['A'] = 14

def winner(deck_steve, deck_josh):
    _len = len(deck_steve)
    _ = [mapping[deck_steve[i]] - mapping[deck_josh[i]] for i in range(_len)]
    steve = sum([x > 0 for x in _])
    josh = sum([x < 0 for x in _])
    tie = sum([x == 0 for x in _])
    if steve > josh:
        return 'Steve wins {x} to {y}'.format(x=steve, y=josh)
    elif josh > steve:
        return 'Josh wins {y} to {x}'.format(x=steve, y=josh)
    else:
        return "Tie"


print(sum([True, True]))
deck_steven = ['A', '7', '8']
deck_josh = ['K', '5', '9']
print(winner(deck_steven, deck_josh))