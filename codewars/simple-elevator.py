def goto(level,button=None):
    if button is None or (level not in (0,1,2,3) :
        return 0
    return int(button) - level



from unittest import TestCase

Test = TestCase()

Test.ass
Test.assertEquals(goto(0,'2'),2);
Test.assertEquals(3+goto(3,'1'),1);
Test.assertEquals(2+goto(2,'2'),2);