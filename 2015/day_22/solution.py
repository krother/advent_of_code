"""
Day 22: Wizard Simulator 20XX

https://adventofcode.com/2015/day/22
"""
import re
from copy import copy
from aoc import PriorityQueue

ITEM = re.compile(r'\s(\d+)\s+(\d+)\s+(\d+)')

SPELLS = ['missile', 'drain', 'recharge', 'poison', 'shield']


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

        self.poison_cooldown = 0
        self.shield_cooldown = 0
        self.recharge_cooldown = 0

    def __repr__(self):
        return f"<{self.hp}; {self.mana}>"

    @property
    def alive(self):
        return self.hp > 0 and self.mana >= 0

    def die(self):
        self.hp = -9999999999

    def pay(self, cost):
        if self.mana < cost:
            self.die()
        self.mana -= cost
        self.mana_used += cost

    def missile(self, boss):
        boss.hp -= 4
        self.pay(53)

    def poison(self, boss):
        if self.poison_cooldown:
            self.die()
        self.poison_cooldown = 6
        self.pay(173)

    def drain(self, boss):
        boss.hp -= 2
        self.hp += 2
        self.pay(73)

    def shield(self, boss):
        if self.shield_cooldown:
            self.die()
        self.armor += 7
        self.shield_cooldown = 6
        self.pay(113)

    def recharge(self, boss):
        if self.recharge_cooldown:
            self.die()
        self.recharge_cooldown = 5
        self.pay(229)

    def ongoing_effects(self, boss):
        if self.shield_cooldown:
            if self.shield_cooldown == 1:
                self.armor = 0
            self.shield_cooldown -= 1
        
        if self.poison_cooldown:
            self.poison_cooldown -= 1
            boss.hp -= 3

        if self.recharge_cooldown:
            self.recharge_cooldown -= 1
            self.mana += 101

    def cast_spell(self, boss, spell):
        self.ongoing_effects(boss)
        f = getattr(self, spell)
        f(boss)        
        self.ongoing_effects(boss)


def parse_boss(data):
    hp, damage = map(int, re.findall(r'\d+', data))
    return Boss(hp, damage)


def find_best_spells(wizard, boss, hp_drain=0):
    """
    Searches a DAG of possible combat situations using the Dijkstra algorithm
    """
    fights = PriorityQueue()
    fights.add_task((wizard, boss), 0)

    while fights:
        wizard, boss = fights.pop_task()
        if not boss.alive:
            return wizard.mana_used
        
        for sp in SPELLS:
            w = copy(wizard)
            b = copy(boss)
            w.cast_spell(b, sp)
            b.hit(w)
            w.hp -= hp_drain
            if w.alive:
                fights.add_task((w, b), w.mana_used)
        
    return -1
    


def solve(data, hp_drain=0):
    boss = parse_boss(data)
    wizard = Wizard(50, 500)
    return find_best_spells(wizard, boss, hp_drain)


def solve2(data):
    return solve(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve(input_data, 1)
    print(f'Example 2: {result}')
