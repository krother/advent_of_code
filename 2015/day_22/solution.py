"""
Day 22: Wizard Simulator 20XX

https://adventofcode.com/2015/day/22
"""
import re
from copy import copy
from aoc import PriorityQueue

ITEM = re.compile(r'\s(\d+)\s+(\d+)\s+(\d+)')


class Boss:

    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def __repr__(self):
        return f"<{self.hp}; {self.damage}>"

    @property
    def alive(self):
        return self.hp > 0        

    def hit(self, wizard):
        if self.alive:
            wizard.hp -= max(self.damage - wizard.armor, 1)


class Wizard:

    def __init__(self, hp, mana=500):
        self.hp = hp
        self.mana = mana
        self.armor = 0
        self.mana_used = 0

    def __repr__(self):
        return f"<{self.hp}; {self.mana}>"

    @property
    def alive(self):
        return self.hp > 0 and self.mana >= 0

    def pay(self, cost):
        self.mana -= cost
        self.mana_used += cost

    def missile(self, boss):
        boss.hp -= 4
        self.pay(53)

    def poison(self, boss):
        boss.hp -= 18
        self.pay(173)

    def drain(self, boss):
        boss.hp -= 2
        self.hp += 2
        self.pay(73)

    def shield(self):
        self.armor += 7
        self.pay(113)

    def recharge(self):
        self.mana += 101 * 5
        self.pay(229)

    def cast_spell(self, boss):
        self.ongoing_effects()
        ... cast
        self.ongoing_effects()

        if self.hp == 1:
            self.drain(boss)
        elif self.mana < 500:
            self.recharge()
        elif boss.hp > 20:
            self.poison(boss)
        elif boss.damage >= self.hp:
            self.shield()
        else:
            self.missile(boss)


def parse_boss(data):
    hp, damage = map(int, re.findall(r'\d+', data))
    return Boss(hp, damage)


def find_best_spells(wizard, boss):
    """
    Searches a DAG of possible combat situations using the Dijkstra algorithm
    """
    fights = PriorityQueue()
    fights.add_task((wizard, boss), 0)

    while fights:
        wizard, boss = fights.pop_task()
        if not wizard.alive:
            return -1
        if not boss.alive:
            return wizard.mana_used
        
        for sp in spells:
            w = copy(wizard)
            b = copy(boss)
            w.cast_spell(sp, b)
            b.hit(w)
            fights.add_task((w, b), w.mana_used)
    


def solve(data):
    ...


def solve2(data):
    return solve(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    # result = solve2(input_data, SHOP)
    # print(f'Example 2: {result}')
