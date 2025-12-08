"""
Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""
from collections import defaultdict


def parse(data):
    grid = data.strip().split()
    i = data.strip().find("S")
    y = i // len(grid[0])
    x = i % len(grid[0])
    return grid, x, y


def trace(data):
    grid, x, y = parse(data)
    timelines = {x: 1}
    splits = 0
    while y < len(grid):
        new = defaultdict(int)
        for x in timelines:
            if grid[y][x] in "S.":
                new[x] += timelines[x]
            elif grid[y][x] == "^":
                new[x-1] += timelines[x]
                new[x+1] += timelines[x]
                splits += 1
        y += 1
        timelines = new
    return splits, timelines


def solve(data):
    splits, _ = trace(data)
    return splits


def solve2(data):
    _, timelines = trace(data)
    return sum(timelines.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 1628

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 27055852018812
