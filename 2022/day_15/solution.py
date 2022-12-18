"""


https://adventofcode.com/2022/day/15
"""
import re
from functools import lru_cache


def parse(data):
    for line in data.strip().split('\n'):
        sensx, sensy, beax, beay = map(int, re.findall(r'\-?\d+', line))
        yield sensx, sensy, beax, beay


@lru_cache
def manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def solve(data, y):
    excluded = set()
    beacons = set()
    for sensx, sensy, beax, beay in parse(data):
        if beay == y:
            beacons.add(beax)
        man = manhattan(sensx, sensy, beax, beay)
        x = sensx
        while manhattan(x, y, sensx, sensy) <= man:
            excluded.add(x)
            x += 1
        x = sensx
        while manhattan(x, y, sensx, sensy) <= man:
            excluded.add(x)
            x -= 1
    excluded = excluded.difference(beacons)
    return len(excluded)


def get_boundaries(y, maxco, sensx, sensy, beax, beay):
    man = manhattan(sensx, sensy, beax, beay)
    dy = abs(sensy - y)
    dx = man - dy
    if dx > 0:
        return max(0, sensx - dx), min(maxco, sensx + dx)


def merge_boundaries(boundaries, maxco):
    rightmost = 0
    for left, right in sorted(boundaries):
        if left - 1 <= rightmost:
            rightmost = max(rightmost, right)
            if rightmost >= maxco:
                return None
        else:
            return left - 1


def get_nonempty_boundaries(beacons, y, maxco):
    boundaries = []
    for beacon in beacons:
        bd = get_boundaries(y, maxco, *beacon)
        if bd is not None:
            boundaries.append(bd)
    return boundaries


def solve2(data, maxco):
    beacons = list(parse(data))
    for y in range(maxco+1):
        boundaries = get_nonempty_boundaries(beacons, y, maxco)
        x = merge_boundaries(boundaries, maxco)
        if x is not None:
            return x * 4000000 + y


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 2000000)
    print(f'Example 1: {result}')

    result = solve2(input_data, 4000000)
    print(f'Example 2: {result}')
    assert result == 10291582906626
