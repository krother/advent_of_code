"""
Day 11: Radioisotope Thermoelectric Generators

https://adventofcode.com/2016/day/11
"""
import re
from itertools import combinations
from functools import reduce
from copy import deepcopy
from collections import deque


ELEVATOR = r'F(\d) E'
ITEM = r'\w[GM]'

LEVELS = 4
CHAR, KIND = 0, 1
UP, DOWN = +1, -1

MAXBIT = 2 ** 14


BIT_VALUES = {'H': 1, 'L': 2, # test
              'R': 1, 'O': 2, 'P': 4, 'S': 8,  # prod
              'T': 16, 'D': 32, 'E': 64
}

def is_floor_valid(binary):
    """
    Checks whether the binary representation of a floor is valid.
    The upper six bits represent the radiation generators,
    the lower six bits the corresponding microchips
    """
    chips = binary & 127
    gens = binary // 128
    mod_chip = chips & (127 - gens)  # NAND
    if mod_chip and gens:
        return False
    return True


VALID_FLOORS = {x for x in range(2**14) if is_floor_valid(x)}



def convert_items_to_binary(items):
    binary = 0
    for i in items:
        if i.endswith('G'):
            binary += 128 * BIT_VALUES[i[0]]
        else:
            binary += BIT_VALUES[i[0]]
    return binary
    

def get_items_on_floor(floor):
    result = []
    bit = MAXBIT
    while bit:
        if floor // bit:
            result.append(bit)
            floor -= bit
        bit = bit // 2
    return result


class Building:

    def __init__(self):
        self.elevator = 0
        self.floors = []
        self.steps = 0

    def setup(self, data):
        self.elevator = int(re.findall(ELEVATOR, data)[0]) - 1
        self.parse_floors(data)

    def copy(self):
        b = Building()
        b.elevator = self.elevator
        b.floors = self.floors[:]
        b.steps = self.steps + 1
        return b

    def __repr__(self):
        return f"<E{self.elevator+1} {self.floors}>"

    def __hash__(self):
        return hash((self.elevator, tuple(self.floors)))

    def is_complete(self):
        if sum(self.floors[:3]) == 0:
            return True

    def __eq__(self, other):
        return hash(self) == hash(other)

    @property
    def current_floor(self):
        return self.floors[self.elevator]

    @staticmethod
    def can_move(ele):
        return 0 <= ele < LEVELS

    def get_possible_moves(self):
        """yields tuples of (gen:int, chip:int) to add/subtract from floor"""
        items = get_items_on_floor(self.current_floor)
        for m in list(combinations(items, 1)) + list(combinations(items, 2)):
            m = sum(m)
            yield m, UP
            yield m, DOWN

    def move(self, mov, direction):
        ele_new = self.elevator + direction
        if self.can_move(ele_new):
            b = self.copy()
            b.floors[self.elevator] -= mov
            b.floors[ele_new] += mov
            b.elevator = ele_new
            if (
                b.current_floor in VALID_FLOORS and 
                b.floors[self.elevator] in VALID_FLOORS
            ):
                return b

    def get_moves(self):
        for m, direction in self.get_possible_moves():
            bnew = self.move(m, direction)
            if bnew:
                yield bnew

    def parse_floors(self, data):
        self.floors = []
        for f in data.strip().split('\n'):
            items = re.findall(ITEM, f)
            self.floors.append(convert_items_to_binary(items))
        self.floors = self.floors[::-1]



def solve(data):
    """breadth-first graph search"""
    b = Building()
    b.setup(data)
    buildings = deque([b])
    visited = {b}

    while buildings:
        b = buildings.popleft()
        for bnew in b.get_moves():
            if bnew not in visited:
                if bnew.is_complete():
                    return bnew.steps
                buildings.append(bnew)
                visited.add(bnew)

    return shortest


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    # part 2
    input_data = """F4 .  .  .  .  .
F3 .  RM RG OG OM 
F2 .  PM SM .  .  
F1 E  TG TM PG SG DG DM EG EM""" # DG DM EG EM
    result = solve(input_data)
    print(f'Example1: {result}')
