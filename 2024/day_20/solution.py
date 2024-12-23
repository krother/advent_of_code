"""
Day 20: Race Condition

https://adventofcode.com/2024/day/20
"""
from itertools import product
from tqdm import tqdm
from aoc import DIRECTIONS4


def parse(data):
    grid = [list(row) for row in data.strip().split("\n")]
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] == "S":
            start = x, y
        elif grid[y][x] == "E":
            end = x, y
    return grid, start, end


def get_moves(grid, pos):
    x, y = pos
    for dx, dy in DIRECTIONS4:
        nx, ny = x + dx, y + dy
        if grid[ny][nx] != "#":
            yield (nx, ny)


def get_path(grid, start, end):
    """assume there is exactly one path"""
    path = [start]
    visited = {start}
    pos = start
    while pos != end:
        for new in get_moves(grid, pos):
            if new not in visited:
                path.append(new)
                visited.add(new)
                pos = new
    return path


def manhattan(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)


def solve(data, saving, cheat_length):
    grid, start, end = parse(data)
    path = get_path(grid, start, end)
    cheats = 0
    for i, cheat_start in tqdm(enumerate(path)):
        j = i + saving
        while j < len(path):
            cheat_end = path[j]
            m = manhattan(cheat_start, cheat_end)
            saved = j - i - m
            if m <= cheat_length and saved >= saving:
                cheats += 1
            elif m > cheat_length:
                j += m - cheat_length - 1
            j += 1
    return cheats


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data, saving=100, cheat_length=2)
    print(f"Example 1: {result}")  # 1452

    result = solve(input_data, saving=100, cheat_length=20)
    print(f"Example 2: {result}")  # 999556
