'''
Each die cannot be used in multiple combinations the same time, so three pairs of 2, 3 and 5 will worth you only 750 points (for three pairs), not 850 (for three pairs and two fives). But you can select multiple combinations, 2 2 2 1 6 will worth you 300 points (200 for three-of-kind '2' plus 100 for single '1' die)

'''

'others best solution until now '

def get_score(dice):
  score_map = [1000, 200, 300, 400, 500, 600]
  histo = [len([i for i in dice if i == x]) for x in xrange(1, 7)]

  # special cases
  if all(n==1 for n in histo): return 1000                  # 1 of each
  if len([bin for bin in histo if bin==2]) == 3: return 750 # 3 pairs

  score = 0
  for i, n in enumerate(histo):
    if 3 <= n <= 6:    score += (n-2)*score_map[i]  # 3-6 of a kind
    elif i==0 or i==4: score += n*score_map[i]/10   # individuals

  return score or "Zonk"


def get_score(dice):
    dice = sorted(dice)
    counter = {};
    for i in range(1,7):
        counter[i] = dice.count(i)
    max_occurence = max(list(counter.values()))
    #counter_reverse = dict(zip(counter.values(), counter.keys()))
    score = 0
    if max_occurence ==1 and len(dice) == 6 :# straight  once every element.
        score = 1000
    elif max_occurence >= 3:
        if max_occurence == 3 and len([ i for i in dice if dice.count(i) == 3]) == 6:
            t1, t2 = dice[0], dice[5]
            score += t2 * 100
            score += t1 * 100 if t1 >= 2 else 1000
        else:
            target = [i for i in dice if dice.count(i) == max_occurence].pop()
            if target in (2,3,4,6):
                score = (max_occurence-2) * 100 *  target if target >= 2 else 1000 * (max_occurence-2)
                score += dice.count(1) * 100 + dice.count(5) * 50
            elif target in (1,5):
                score = (max_occurence-2) * 100 *  target if target >= 2 else 1000 * (max_occurence-2)
                eleminated = [ i for i in dice if dice.count(i) < max_occurence and i in (1,5)]
                score += eleminated.count(1) * 100 + eleminated.count(5) * 50
    elif len([i for i in dice if dice.count(i) == 2]) == 6:
        score = 750
    else: # other patterns
        # every 1 , every 5
        score += dice.count(1) * 100 + dice.count(5) * 50
    return score or "Zonk"


dice = [1,1,1,1,5]
dice = [5,5,5,5,1]
dice = [1,1,1,6,6,6]
#print([i for i in dice if dice.count(i) == 2])
print(get_score(dice))




"""test cases
Test.describe("Example tests")
Test.assert_equals(get_score([1]), 100)
Test.assert_equals(get_score([2]), "Zonk")
Test.assert_equals(get_score([3]), "Zonk")
Test.assert_equals(get_score([4]), "Zonk")
Test.assert_equals(get_score([5]), 50)
Test.assert_equals(get_score([6]), "Zonk")
Test.assert_equals(get_score([1,1]), 200)
Test.assert_equals(get_score([1,1,1]), 1000)
Test.assert_equals(get_score([1,2,3,4,5,6]), 1000)
Test.assert_equals(get_score([2,2,3,3,6,6]), 750)
Test.assert_equals(get_score([3,2,6,4,4,6]), "Zonk")

"""
"""
Combination Example roll    Points
Straight (1,2,3,4,5 and 6)  6 3 1 2 5 4 1000 points
Three pairs of any dice 2 2 4 4 1 1 750 points
Three of 1  1 4 1 1 1000 points
Three of 2  2 3 4 2 2   200 points
Three of 3  3 4 3 6 3 2 300 points
Three of 4  4 4 4   400 points
Three of 5  2 5 5 5 4   500 points
Three of 6  6 6 2 6 600 points
Four of a kind  1 1 1 1 4 6 2 × Three-of-a-kind score (in example, 2000 pts)
Five of a kind  5 5 5 4 5 5 3 × Three-of-a-kind score (in example, 1500 pts)
Six of a kind   4 4 4 4 4 4 4 × Three-of-a-kind score (in example, 1600 pts)
Every 1 4 3 1 2 2   100 points
Every 5 5 2 6   50 points
"""