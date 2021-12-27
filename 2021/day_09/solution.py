"""
Smoke Basin

https://adventofcode.com/2021/day/9
"""

from aoc import parse_2d_numbers
import numpy as np


checked = {}

def adjacent(data, x, y):
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1
    if x < len(data[0]) - 1:
        yield x + 1, y
    if y < len(data) - 1:
        yield x, y + 1


def is_low(data, x, y):
    current = data[y][x]
    for xx, yy in adjacent(data, x, y):
        if data[yy][xx] <= current: # not 100% clear in description 
            return False
    return True


def find_low_points(data):
    lows = []
    for y, x in np.ndindex(data.shape):
        if is_low(data, x, y):
            lows.append((x, y))
    return lows


def solve(data):
    data = parse_2d_numbers(data)
    result = 0
    for x, y in find_low_points(data):
        result += data[y][x] + 1
    return result


def get_all_positions_smaller9(data):
    todo = []
    for y, x in np.ndindex(data.shape):
        if data[y][x] != 9:
            todo.append((x, y))
    return todo


def solve2(data):
    data = parse_2d_numbers(data)
    basins = {(x, y): 0 for x, y in find_low_points(data)}
    todo = get_all_positions_smaller9(data)

    while todo:
        x, y = todo.pop()
        if (x, y) in basins:
            basins[(x, y)] += 1
        else:
            for xx, yy in adjacent(data, x, y):
                if data[yy][xx] < data[y][x]:
                    todo.append((xx, yy))
                    break

    sizes = list(sorted(basins.values()))
    prod = 1
    for i in sizes[-3:]:
        prod *= i
    return prod


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 560

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 959136
