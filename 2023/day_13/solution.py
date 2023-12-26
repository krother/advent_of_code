"""
Point of Incidence

https://adventofcode.com/2023/day/13
"""
from aoc.parsers import parse_hash_grid
import numpy as np


def get_reflections(a):
    for x in range(1, a.shape[1]):
        cols = min(a.shape[1] - x, x)
        left = a[:, x - cols : x]
        right = a[:, x + cols - 1 : x - 1 : -1]
        c = left + right
        yield c, x


def find_reflection_index(a, target):
    for c, x in get_reflections(a):
        i, _ = np.where(c == 1)
        if len(i) == target:
            return x


def find_reflection(block, target=0):
    a = parse_hash_grid(block)
    return find_reflection_index(a, target) or find_reflection_index(a.T, target) * 100


def solve(data, target=0):
    return sum(find_reflection(block, target) for block in data.strip().split("\n\n"))


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 37025

    result = solve(input_data, 1)
    print(f"Example 2: {result}")  # 32854
