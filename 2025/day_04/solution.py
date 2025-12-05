"""

https://adventofcode.com/2025/day/4
"""

from aoc import (
    parse_hash_grid,
)
import numpy as np
from scipy.signal import convolve


def parse(data):
    return parse_hash_grid(data.replace("@", "#"))


def get_accessible_rolls(grid):
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    c = convolve(grid, kernel)
    return (c[1:-1, 1:-1] < 4) & grid


def solve(data):
    grid = parse(data)
    return get_accessible_rolls(grid).sum()


def solve2(data):
    grid = parse(data)
    orig = grid.copy()
    while (removed := get_accessible_rolls(grid)).any():
        grid -= removed
    return (orig - grid).sum()


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")

    result = solve2(input_data)
    print(f"Example 2: {result}")
