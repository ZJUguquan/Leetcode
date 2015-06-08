# solution


from itertools import count


def self_converge(p):
    width = len(str(p))
    previous = set()
    for i in count(1):
        s = sorted(str(p).ljust(width, '0'))
        n = int(''.join(reversed(s))) - int(''.join(s))
        if n is 0:
            return -1
        if n in previous:
            return i
        p = n
        previous.add(n)

'''description

Goal: Given a number (with a minimum of 3 digits), return the number of iterations it takes to arrive at a derived number that converges on to itself, as per the following Kaprekar routine. As a learning exercise, come up with a solution that uses recursion.

Initialize a counter to count the number of iterations
Take any four-digit number n, using at least two different digits.
Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary
Add as many zeroes so that the width of the original number is maintained.
Subtracti
 the smaller number from the bigger number. Let us call this nseq.
Check if nseq (the remainder) from Step 4 equals the previous value of n. If not, increment the iteration counter and go back to step 2 and perform it on the nseq.
Numbers with more that 4 digits will converge on a cycle of numbers. Therefore in Step 5, detect this cycle by comparing to not only the previous value, but to all previous values of n.
If there is a match, then return the count of iterations
If the sequence_number collapses to zero, then return -1
Converge values

While 3-digit numbers converge to the same unique number k which is also 3 digits long, all 4-digit numbers also converge to the same unique value k1 which is 4 digits long. However, 5 digit numbers converge to any one of the following values: 53955, 59994, 61974, 62964, 63954, 71973, 74943, 75933, 82962, 83952.
'''


subtract = lambda x: int(''.join(
    sorted(str(x), reverse=True))) - int(''.join(sorted(str(x), reverse=False)))


def self_converge(start):
    if subtract(start) == 0:
        return -1
    counter = 1
    sequence = []



    while subtract(start) not in sequence:
        print '{i}.{old} - {new} = {diff}'.format(i=counter, old=''.join(sorted(str(start), reverse=True)), new=''.join(sorted(str(start), reverse=False)),
                                                 diff=subtract(start))
        start = subtract(start)
        sequence.append(start)
        if subtract(start) not in sequence:
            counter += 1
        else:
            continue


    return counter + 1

#     print '_' * 4


canditest = [1234, 414, 50000, 1111, 123, 4321]

for c in canditest:
    print self_converge(c)
    print '*' * 55
