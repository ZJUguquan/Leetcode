from collections import Counter
def find_duplicates(employees):
    newe = []
    output = []
    for idx, ew in enumerate(employees):
        print ew
        e = Counter([ ew.last_name , ew.user_name , ew.first_name])
        print e
        if e not in newe:
            newe.append(e)
        else:
            output.append(ew)
            del employees[idx]
    print '*' * 80
    print employees
    return output


<__main__.Employee instance at 0x7f794760f8c0>
Counter({'JoJo': 1, 'Joestar': 1, 'Johnatan': 1})
<__main__.Employee instance at 0x7f794759c248>
Counter({'Dio': 1, 'DIO': 1, 'Brando': 1})
<__main__.Employee instance at 0x7f794759c290>
Counter({'JoJo': 1, 'Joestar': 1, 'Joseph': 1})
<__main__.Employee instance at 0x7f794759c2d8>
Counter({'': 1, 'Kars': 1, 'the ultimate being': 1})
<__main__.Employee instance at 0x7f794759c320>
Counter({'JoJo': 1, 'Joestar': 1, 'Johnatan': 1})
********************************************************************************
[<__main__.Employee instance at 0x7f794760f8c0>, <__main__.Employee instance at 0x7f794759c248>, <__main__.Employee instance at 0x7f794759c290>, <__main__.Employee instance at 0x7f794759c2d8>]
Test Passed
Test Passed
<__main__.Employee instance at 0x7f794760f8c0>
Counter({'JoJo': 1, 'Joestar': 1, 'Johnatan': 1})
<__main__.Employee instance at 0x7f794759c248>
Counter({'Dio': 1, 'DIO': 1, 'Brando': 1})
<__main__.Employee instance at 0x7f794759c290>
Counter({'JoJo': 1, 'Joestar': 1, 'Joseph': 1})
<__main__.Employee instance at 0x7f794759c2d8>
Counter({'': 1, 'Kars': 1, 'the ultimate being': 1})
<__main__.Employee instance at 0x7f794759c488>
Counter({'JoJo': 1, 'Joestar': 1, 'Johnatan': 1})
********************************************************************************
[<__main__.Employee instance at 0x7f794760f8c0>,
 <__main__.Employee instance at 0x7f794759c248>,
 <__main__.Employee instance at 0x7f794759c290>,
 <__main__.Employee instance at 0x7f794759c2d8>,
 <__main__.Employee instance at 0x7f794759c4d0>]

It should return the sole triple duplicate in this test:

[<__main__.Employee instance at 0x7f794759c488>] should equal [<__main__.Employee instance at 0x7f794759c488>, <__main__.Employee instance at 0x7f794759c4d0>]
