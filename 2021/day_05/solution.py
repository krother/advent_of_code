"""
Hydrothermal Venture

https://adventofcode.com/2021/day/5

"""
import re
from collections import defaultdict


class Vent:

    def __init__(self, x1, y1, x2, y2):
        assert x1 != x2 or y1 != y2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def horizontal(self):
        return self.y1 == self.y2

    @property
    def vertical(self):
        return self.x1 == self.x2

    @staticmethod
    def get_delta(start, end):
        if start > end:
            return -1
        elif start < end:
            return 1
        return 0

    def get_points(self):
        x = self.x1
        y = self.y1
        dx = self.get_delta(self.x1, self.x2)
        dy = self.get_delta(self.y1, self.y2)
        while x != self.x2 or y != self.y2:
            yield x, y
            x += dx
            y += dy
        yield x, y


def parse(data, diagonal):
    vents = []
    for line in data.strip().split('\n'):
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        v = Vent(x1, y1, x2, y2)
        if diagonal or v.horizontal or v.vertical:
            vents.append(v)
    return vents


def solve(data, diag):
    vents = parse(data, diag)
    count = defaultdict(int)
    for v in vents:
        for p in v.get_points():
            count[p] += 1

    total = len([v for v in count.values() if v > 1])
    return total


if __name__ == '__main__':

    input_data = open('input_data.txt').read()
    result = solve(input_data, False)
    print(f'Example 1: {result}')

    result = solve(input_data, True)
    print(f'Example 2: {result}')
