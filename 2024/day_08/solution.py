"""


https://adventofcode.com/2024/day/8
"""
from itertools import product
from math import gcd


def parse(data):
    antennas = {}
    grid = data.strip().split("\n")
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != ".":
                antennas.setdefault(cell, [])
                antennas[cell].append((x, y))
    return grid, antennas


def is_in_grid(x, y, grid):
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


def get_antinodes(grid, antpos):
    result = set()
    for (x1, y1), (x2, y2) in product(antpos, antpos):
        if (x1, y1) == (x2, y2):
            continue
        x = x2 + (x2 - x1)
        y = y2 + (y2 - y1)
        if is_in_grid(x, y, grid):
            result.add((x, y))
    return result

def get_antinodes2(grid, antpos):
    result = set()
    for (x1, y1), (x2, y2) in product(antpos, antpos):
        if (x1, y1) == (x2, y2):
            continue
        dx = (x2 - x1)
        dy = (y2 - y1)
        div = gcd(dx, dy)
        dx = dx // div
        dy = dy // div
        for i in range(len(grid)):
            x = x1 + i * dx
            y = y1 + i * dy
            if is_in_grid(x, y, grid):
                result.add((x, y))
    return result


def solve(data, func=get_antinodes):
    grid, antennas = parse(data)
    spots = set()
    for a in antennas:
        spots.update(func(grid, antennas[a]))
    return len(spots)


def solve2(data):
    return solve(data, func=get_antinodes2)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}') # 369

    result = solve2(input_data)
    print(f'Example 2: {result}') # 1169
