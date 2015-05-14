
mapping = {
'Four_of_a_Kind': 7,
'Full_House': 6,
'Straight': 5,
'Three_of_a_Kind': 4,
'Two_pairs': 3,
'One_pairs': 2,
'Sum_of_Cards': 1
}

name2value = ['_', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


from collections import Counter
def whatkind(allcards):
    allcards = [name2value.index(c) for c in allcards]
    c = Counter(allcards)
    max_times = max(c.values())
    if max_times == 4:
        return 'Four_of_a_Kind'
    elif max_times == 3:
        # full house
        if len(c.keys()) == 2:
            return

def texasHoldem(common, a, b):
    pass
