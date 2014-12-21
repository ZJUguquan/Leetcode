def goodVsEvil(good, evil):
    result = {'good':"Battle Result: Good triumphs over Evil" ,
              'both':"Battle Result: No victor on this battle field",
               'bad': "Battle Result: Evil eradicates all trace of Good"}
    goodvalue = [1,2,3,3,4,10]
    badvalue = [1,2,2,2,3,5,10]
    goodcount = [int(i) for i in good.split()]
    badcount = [int(i) for i in evil.split()]
    good_fight = sum([goodvalue[i] * goodcount[i] for i in range(6)])
    bad_fight = sum([badvalue[i] * badcount[i] for i in range(7)])
    # print(good_fight, bad_fight)
    if good_fight > bad_fight:
        return result['good']
    elif good_fight < bad_fight:
        return result['bad']
    else:
        return result['both']

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))
# Test

'''
Test.expect( goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good', 'Evil should win' );
Test.expect( goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == 'Battle Result: Good triumphs over Evil', 'Good should win' );
Test.expect( goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == 'Battle Result: No victor on this battle field', 'Should be a tie' );
'''




# Return "if good wins, "Battle Result: Evil eradicates all trace of Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie