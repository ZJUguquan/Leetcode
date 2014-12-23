'solu'
def whatCentury(year):
    indicators = {'1': 'st', '2': 'nd', '3': 'rd'}
    century = str(int(year) // 100 + (1 if int(year) % 100 > 0 else 0))
    return century + (indicators.get(century[-1], 'th') if century[0] != '1' else 'th')

def whatCentury(year):
    tail = {'1': 'st', '2': 'nd', '3': 'rd'}
    if year % 100 == 0:
        return str(year)[:2] + 'th'
    else:
        if year < 2000:
            return str(year + 100)[:2] + 'th'
        else:
            t = str(year + 100)[1]
            return str(year + 100)[:2] + 'th' if t not in tail else str(year + 100)[:2] + tail[t]

l = [1999, 2011, 2154, 2259, 1124, 2000]
for i in l:
    print(whatCentury(i))
