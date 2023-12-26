"""
Day 14: Parabolic Reflector Dish

https://adventofcode.com/2023/day/14
"""
from aoc.parsers import parse_hash_grid
import numpy as np


def parse(data):
    rocks = parse_hash_grid(data.strip().replace("#", ".").replace("O", "#"))
    cubes = parse_hash_grid(data.strip().replace("O", "."))
    return rocks.astype(np.uint32), cubes.astype(np.uint32)


def slide_rock(cubes, rocks, x, y):
    if y > 0:
        col = cubes[:y, x] + rocks[:y, x]
        rest = np.where(col == 1)[0]
        if rest.shape[0] > 0:
            y = rest[-1] + 1
        else:
            y = 0
    rocks[y, x] = 1
    return y


def slide_all_rocks(rocks, cubes):
    result = np.zeros(cubes.shape, np.uint32)
    for y, x in zip(*np.where(rocks == 1)):
        yy = slide_rock(cubes, result, x, y)
    return result


def count_load(final):
    mult = np.arange(final.shape[0], 0, -1, dtype=np.uint32)
    result = final.T * mult
    return result.sum()


def solve(data):
    rocks, cubes = parse(data)
    final = slide_all_rocks(rocks, cubes)
    return count_load(final)


def solve2(data):
    rocks, cubes = parse(data)
    i = 0
    recent = []
    while True:
        rocks = slide_all_rocks(rocks, cubes)
        rocks = np.rot90(rocks, 3)
        cubes = np.rot90(cubes, 3)
        i += 1
        if i % 4 == 0:
            cycles = i // 4
            for j, other in enumerate(recent):
                if np.all(rocks == other):
                    period = len(recent) - j
                    remaining = (1_000_000_000 - cycles) % period
                    target = recent[-period:][remaining]
                    return count_load(target)
            recent.append(rocks)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 109424

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 102509
