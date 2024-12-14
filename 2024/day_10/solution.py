"""
Day 10: Hoof It

https://adventofcode.com/2024/day/10
"""
from aoc import parse_2d_numbers, is_on_grid, DIRECTIONS4
import numpy as np


def find_adjacent_steps(grid, x, y, height):
    for dx, dy in DIRECTIONS4:
        nx, ny = x + dx, y + dy
        if is_on_grid(nx, ny, grid):
            continue
        if grid[ny, nx] == height + 1:
            yield nx, ny


def count_trailheads(grid, x, y):
    peaks = set()
    trails = 0
    heads = [(x, y, 0)]
    while heads:
        x, y, height = heads.pop()
        if height == 9:
            peaks.add((x, y))
            trails += 1
        else:
            for nx, ny in find_adjacent_steps(grid, x, y, height):
                heads.append((nx, ny, height + 1))
    return len(peaks), trails


def walk(data):
    grid = parse_2d_numbers(data)
    zeros = np.where(grid == 0)
    heads, trails = 0, 0
    for y, x in zip(*zeros):
        h, t = count_trailheads(grid, x, y)
        heads += h
        trails += t
    return heads, trails


def solve(data):
    return walk(data)[0]


def solve2(data):
    return walk(data)[1]


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 798

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 1706
