"""
Solution with Polygons

https://adventofcode.com/2022/day/15
"""
import re
from functools import lru_cache



class Polygon:

    def __init__(self, sensx, sensy, beax, beay):
        man = self.manhattan(sensx, sensy, beax, beay)
        self.vertices = [
            # counter-clockwise
            (sensx, sensy - man),
            (sensx - man, sensy),
            (sensx, sensy + man),
            (sensx + man, sensy),
        ]

    @staticmethod
    def manhattan(x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    def add(self, other):
        ...

    def get_center(self):
        ...
    
    def __repr__(self):
        return str(self.vertices)



def parse(data):
    for line in data.strip().split('\n'):
        yield Polygon(*map(int, re.findall(r'\-?\d+', line)))




def solve2(data, maxco):
    polygons = list(parse(data))
    poly = polygons[0]
    for p in polygons[1:]:
        poly.add(p)
    x, y = poly.get_center()
    return x * 4000000 + y


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 2000000)
    print(f'Example 1: {result}')

    result = solve2(input_data, 4000000)
    print(f'Example 2: {result}')
    assert result == 10291582906626
