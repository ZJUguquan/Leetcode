
mapping = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen' ,16:'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 0: ' '}
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9:'ninety'}


def wordify(n):
    if n < 20:
        return mapping[n].strip()
    if n < 100:
        t, g = map(int, str(n))
        return (tens[t] + ' ' + mapping[g]).strip()
    b, t, g = map(int, str(n))
    return (mapping[b] + ' hundred ' + wordify(t*10 + g)).strip()


for i in range(1, 1000):
    print(wordify(i))