# coding: utf-8

class Test(object):

    @staticmethod
    def it(msg):
        print msg
        oye()

    @staticmethod
    def assert_equals(left, right):
        if left == right:
            print left, 'passssssssssssssssssssssssssssssssssssssssssssssssssssss'
        else:
            print 'something happend, be careful!'
test = Test()


from collections import Counter


# 1. Four of a Kind: 'A hand containing four cards of equal rank'
# 2. Full House: 'A hand with three cards of one rank and two of a second rank'
# 3. Straight: 'Contains five cards of sequential rank'
# 4. Three of a Kind: 'Contains three cards of the same rank'
# 5. Two pairs: Contains two cards of the same rank, plus two cards of another rank
# 6. One pair: 'Contains two cards of the same rank'
# 7. Sum of Cards

mapping = {
    'Four_of_a_Kind': 7,   # 4 K + A
    'Full_House': 6,       # 3 K + 2 A
    'Straight': 5,         # 10 J Q K A
    'Three_of_a_Kind': 4,  # 3 K + 9 + 8
    'Two_pairs': 3,
    'One_pairs': 2,
    'Sum_of_Cards': 1
}
name2value = ['0', '1', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'J', 'Q', 'K', 'A']



def isstraight(cards):
    cards = [i - min(cards) for i in cards]
    return set([1,2,3,4,0]) == set(cards)


def straight(cards):
    cards = sorted(cards, reverse=True)
    for i in (0, 1, 2):
        temp = cards[i:i+5]
        if isstraight(temp):
            return temp[0]

print('-'*80)


def whatkind(allcards):
    # From 7 cards pick best group
    allcards = [name2value.index(c) for c in allcards]
    c = Counter(allcards)
    desc = sorted(allcards, reverse=True)
    valid_straight = set([elem - desc[-1] for elem in desc])
    c = sorted(c.items(), key=lambda x: (x[1], x[0]), reverse=True)
    # print c
    max_times = c[0][1]
    if max_times == 4:
        # Four_of_a_Kind  3333, Q
        return (7, c[0][0], max([i for i in allcards if allcards.count(i) < 4]), 0, 0)
    elif max_times == 3 and c[1][1] >= 2:
        # Full house  KKK, QQ
        return (6, c[0][0], c[1][0], 0, 0)
    elif straight(desc) is not None:
        # Straight  45678 KQ
        print straight(desc)
        return (5, straight(desc), 0, 0, 0)
    elif max_times == 3 and c[1][1] == 1:
        # Three of kind  KKK, QQ
        return (4, c[0][0], c[1][0], c[2][0], 0)
    elif max_times == 2 and c[1][1] == 2:
        # Two pairs 44 55 K
        return (3, c[0][0], c[1][0], c[2][0], 0)
    elif max_times == 2 and c[1][1] == 1:
        return (2, c[0][0], c[1][0], c[2][0], c[3][0], 0)
    else:
        return (1, desc[0], desc[1], desc[2], desc[3])


def texasHoldem(common, a, b):
    Acard = common + a
    Bcard = common + b
    Ap = whatkind(Acard)
    Bp = whatkind(Bcard)
    print Ap, Bp
    if Ap > Bp:
        return 'A'
    elif Ap == Bp:
        return 'AB'
    else:
        return 'B'

# test
# full house
allcards = ['6', '3', '3', '5', '2', '3', '3']
allcards = ['6', '6', '6', '3', '3', 'A', 'A']
allcards = ['6', '6', '6', '5', '3', '4', '2']
allcards = ['6', '6', '6', '3', 'Q', '4', 'A']
allcards = ['6', '6', 'Q', '3', 'Q', '4', 'A']
allcards = ['6', '6', 'Q', '3', 'K', '4', 'A']
allcards = ['4','3','2','5','9', 'Q','A']
print whatkind(allcards)


# A has Four of a Kind
Test.assert_equals(texasHoldem(['6','3','3','5','2'],['3','3'],['4','7']),"A")

# B has Pair
Test.assert_equals(texasHoldem(['4','3','2','5','Q'],['7','8'],['5','7']),"B")

# Even
Test.assert_equals(texasHoldem(['4','3','2','5','9'],['Q','A'],['A','Q']),"AB")


common = ['8', 'J', 'Q', 'A', '2']
a = ['9', '10']
b = ['A', 'A']

print texasHoldem(common, a, b)