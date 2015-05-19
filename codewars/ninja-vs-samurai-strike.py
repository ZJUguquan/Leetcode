# coding: utf-8


Position = {'high': 'h', 'low': 'l'}

class Warrior():

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ""
        self.deceased = False
        self.zombie = False

    def attack(self, enemy, position):
        damage = 0
        if enemy.block != position:
            if position == Position['high']:
                damage += 10
            else:
                damage  += 5
        if enemy.block == "":
            damage += 5
        enemy.set_health(enemy.health - damage)
        if enemy.health == 0:
            enemy.deceased = True
            enemy.zombie = False
        elif enemy.deceased == True:
            enemy.zombie = True


    def set_health(self, new_health):
        self.health = max(0, new_health)


ninja = Warrior('Hanzo Hattori')
samurai = Warrior('Ryōma Sakamoto')

samurai.block = 'l'
ninja.attack(samurai, 'h')
print samurai.name
print samurai.health

########################################################################
# class Warrior:

#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health

#         def strike(enemy, swings):
#             # health cannot go below zero
#             enemy.health = max([-1, enemy.health - (swings * 10)])


# from random import randint
# import unittest


# class Test(unittest.TestCase):
#     pass

# test = Test()
# name = ['Hattori Hanzo', 'Sasuke Sarutobi',
#         'Jubei Kibagami', 'Kotaro Fuma'][randint(0, 3)]
# ninja = Warrior(name)
# test.assertIs(ninja.name, name,
#               "Making the 'name' variable visible will help you complete this kata")
