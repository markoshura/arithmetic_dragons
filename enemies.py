# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    pass


def generate_random_dragon():
    RandomDragonType = choice(dragon_types)
    dragon = RandomDragonType()
    return dragon

def generate_random_troll():
    RandomTrollType = choice(troll_types)
    troll = RandomTrollType()
    return troll


def generate_dragon_list(dragon_number):
    enemy_list = [generate_random_dragon() for i in range(dragon_number)]
    return enemy_list

def generate_troll_list(troll_number):
    enemy_list = [generate_random_troll() for i in range(troll_number)]
    return enemy_list

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 20
        self._attack = 1
        self._color = 'зелёный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 20
        self._attack = 1
        self._color = 'красный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 20
        self._attack = 1
        self._color = 'чёрный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class Troll1(Troll):

    def __init__(self):
        self.x = randint(1,5)
        self._health = 5
        self._attack = 1
        self._color = 'загадочный'

    def question(self):
        self.set_answer(str(self.x))
        self.__quest= 'Я загадаль цифирь. Угадавай!!'
        return self.__quest

class Troll2(Troll):

    def __init__(self):
        self._health = 5
        self._attack = 1
        self._color = 'простоватый'

    def question(self):
        x = randint(1,100)
        self.__quest='Э, число ' + str(x) + ' простой, дэ?'
        delitel=2
        while delitel**2<x:
            if x%delitel==0:
                bull=0
            delitel+=1
        if delitel**2>=x:
            bull=1
        if bull==1:
            self.set_answer('Нет')
        else:
            self.set_answer('Да')

        return self.__quest


class Troll3(Troll):

    def __init__(self):
        self._health = 5
        self._attack = 1
        self._color = 'расчленяющий'

    def question(self):
        s=''
        x = randint(2,5)
        self.__quest= 'Аргх!!' + str(x) + '. Множители. Разложить. Аргх!!'
        delitel = 2
        while x>1:
            if x%delitel ==0:
                s+=str(x)+','
                x //= delitel
            else:
                delitel+=1
        self.set_answer(s)
        return self.__quest

dragon_types = [GreenDragon, RedDragon, BlackDragon]
troll_types = [Troll1, Troll2, Troll3]
