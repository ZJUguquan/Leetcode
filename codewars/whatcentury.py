def whatCentury(year):
    tail = {'1':'st', '2':'nd', '3':'rd'}
    if year % 100 == 0:
        return str(year)[:2]+ 'th'
    else:
        t = str(year)[2]
        return str(year+100)[:2] + 'th' if t not in tail else str(year+100)[:2] + tail[t]

for i in range(1999, 2305, 9):
    print(whatCentury(i))