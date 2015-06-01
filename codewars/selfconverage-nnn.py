diff = lambda x: int(''.join(sorted(str(x), reverse=True))) - int(''.join(sorted(str(x), reverse=False)))
i = 0
start = 4321
while start != diff(start):
    i += 1
    print '{i}.{old} - {new} = {diff}'.format(i=i, old=''.join(sorted(str(start), reverse=True)), new=''.join(sorted(str(start), reverse=False)), diff=diff(start))
    start = diff(start)
    if start == diff(start):
        i += 1
        print '{i}.{old} - {new} = {diff}'.format(i=i, old=''.join(sorted(str(start), reverse=True)), new=''.join(sorted(str(start), reverse=False)), diff=diff(start))

print '_'* 40
print i