"""
Day 21: RPG Simulator 20XX

https://adventofcode.com/2015/day/21
"""
import itertools
import re
from collections import namedtuple
from dataclasses import dataclass
from itertools import product, combinations

ITEM = re.compile(r'\s(\d+)\s+(\d+)\s+(\d+)')

SHOP = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


class Character:

    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return f"<{self.hp}; {self.damage}; {self.armor}>"

    def fight(self, opponent):
        """Returns True if character wins, otherwise False"""
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= max(self.damage - opponent.armor, 1)
            self.hp -= max(opponent.damage - self.armor, 1)

        return opponent.hp <= 0

@dataclass
class Item:

    cost: int
    damage: int
    armor: int

    def __add__(self, other):
        return Item(
            self.cost + other.cost,
            self.damage + other.damage,
            self.armor + other.armor
        )


def parse_rack(rack):
    return [Item(*map(int, item)) for item in ITEM.findall(rack)]


def parse_shop(shop):
    for rack in shop.split('\n\n'):
        yield parse_rack(rack)


def parse(data):
    hp, damage, armor = map(int, re.findall('\d+', data))
    return Character(hp, damage, armor)


def get_item_combinations(weapons, armor, rings):
    ring_combos = combinations(rings, 2)
    for w, a, (r1, r2) in product(weapons, armor, ring_combos):
        yield w + a + r1 + r2

def go_shopping(weapons, armor, rings):
    return get_item_combinations(weapons,
                                 armor + [Item(0, 0, 0)],
                                 rings + [Item(0, 0, 0), Item(0, 0, 0)])


def solve(data, shop, price_func=min, char_wins=True):
    items = parse_shop(shop)
    return price_func([
        item.cost
        for item in go_shopping((*items))
        if Character(100, item.damage, item.armor).fight(parse(data)) is char_wins
    ])


def solve2(data, shop):
    return solve(data, shop, max, False)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, SHOP)
    print(f'Example 1: {result}')
    # 121

    result = solve2(input_data, SHOP)
    print(f'Example 2: {result}')
    # 201
