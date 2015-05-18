class Warrior:
    def __init__(self,name, health=100):
        self.name= name
        self.health = health

        def strike(enemy,swings):
            #health cannot go below zero
            enemy.health=max([-1,enemy.health-(swings*10)])


from random import randint
import unittest
class Test(unittest.TestCase):
    pass

test = Test()
name=['Hattori Hanzo','Sasuke Sarutobi','Jubei Kibagami','Kotaro Fuma'][randint(0,3)]
ninja = Warrior(name)
test.assertIs(ninja.name,name,"Making the 'name' variable visible will help you complete this kata")

