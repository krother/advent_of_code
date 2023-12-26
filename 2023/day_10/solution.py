"""
Pipe Maze

https://adventofcode.com/2023/day/10
"""
import numpy as np

TURNS = {
    ("|", "U"): "U",
    ("|", "D"): "D",
    ("-", "L"): "L",
    ("-", "R"): "R",
    ("L", "L"): "U",
    ("L", "D"): "R",
    ("J", "D"): "L",
    ("J", "R"): "U",
    ("7", "R"): "D",
    ("7", "U"): "L",
    ("F", "U"): "R",
    ("F", "L"): "D",
}


def parse(data):
    grid = data.strip().split("\n")
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                return (x, y), grid


def walk(pos, direction):
    x, y = pos
    if direction == "R":
        return x + 1, y
    if direction == "L":
        return x - 1, y
    if direction == "U":
        return x, y - 1
    if direction == "D":
        return x, y + 1


def turn(direction, tile):
    return TURNS[(tile, direction)]


def get_main_loop_positions(start, grid, direction):
    steps = 0
    pos = start
    path = []
    while True:
        steps += 1
        pos = walk(pos, direction)
        path.append(pos)
        tile = grid[pos[1]][pos[0]]
        if tile == "S":
            return path
        direction = turn(direction, tile)


def get_main_loop_positions(start, grid, direction):
    steps = 0
    pos = start
    path = []
    left, right = set(), set()
    while True:
        steps += 1
        pos = walk(pos, direction)
        path.append(pos)
        tile = grid[pos[1]][pos[0]]
        if tile == "S":
            return path, left, right

        # memorize adjacent spots
        x, y = pos
        if tile == "|" and direction == "U":
            left.add((x - 1, y))
            right.add((x + 1, y))
        if tile == "|" and direction == "D":
            left.add((x + 1, y))
            right.add((x - 1, y))
        if tile == "-" and direction == "R":
            left.add((x, y - 1))
            right.add((x, y + 1))
        if tile == "-" and direction == "L":
            left.add((x, y + 1))
            right.add((x, y - 1))

        if tile == "F" and direction == "U":
            left.add((x - 1, y))
            left.add((x, y - 1))
        if tile == "F" and direction == "L":
            right.add((x - 1, y))
            right.add((x, y - 1))

        if tile == "7" and direction == "U":
            right.add((x + 1, y))
            right.add((x, y - 1))
        if tile == "7" and direction == "R":
            left.add((x + 1, y))
            left.add((x, y - 1))

        if tile == "J" and direction == "D":
            left.add((x + 1, y))
            left.add((x, y + 1))
        if tile == "J" and direction == "R":
            right.add((x + 1, y))
            right.add((x, y + 1))

        if tile == "L" and direction == "L":
            left.add((x - 1, y))
            left.add((x, y + 1))
        if tile == "L" and direction == "D":
            right.add((x - 1, y))
            right.add((x, y + 1))

        direction = turn(direction, tile)


def solve(data, direction="R"):
    start, grid = parse(data)
    path, _, _ = get_main_loop_positions(start, grid, direction)
    return len(path) / 2


def count_flooded_area(grid, path, start, fn):
    a = np.ones((len(grid), len(grid[0])), dtype=np.uint8)
    for x, y in path:
        a[y, x] = 0

    for x, y in start:
        if x > 0 and y > 0 and x < len(grid[0]) and y < len(grid):
            a[y, x] = 2

    # flood
    b = np.zeros((len(grid) + 2, len(grid[0]) + 2), dtype=np.uint8) + 2
    b[1:-1, 1:-1] = a
    for i in range(max(b.shape)):
        c = b.copy()
        c[1:] += c[:-1]  # down
        indexes = np.where(c > 2)
        b[indexes] = 2

        c = b.copy()
        c[:-1] += c[1:]  # up
        indexes = np.where(c > 2)
        b[indexes] = 2

        c = b.copy()
        c[:, 1:] += c[:, :-1]  # right
        indexes = np.where(c > 2)
        b[indexes] = 2

        c = b.copy()
        c[:, :-1] += c[:, 1:]  # left
        indexes = np.where(c > 2)
        b[indexes] = 2

    indexes = np.where(b == 2)
    b[indexes] = 0
    return b.sum()


def solve2(data, direction="R"):
    start, grid = parse(data)
    path, left, right = get_main_loop_positions(start, grid, direction)

    # remove path from adjacent
    left = left - set(path)
    right = right - set(path)

    countleft = count_flooded_area(grid, path, left, "left.csv")
    countright = count_flooded_area(grid, path, right, "right.csv")
    print(countleft, countright)  # two numbers, not sure which one is the solution!
    return max(countleft, countright)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data, "U")
    print(f"Example 1: {result}")  # 6870

    result = solve2(input_data, "U")
    print(f"Example 2: {result}")  # 287 !!!
