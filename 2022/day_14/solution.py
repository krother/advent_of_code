"""
Regolith Reservoir

https://adventofcode.com/2022/day/14
"""
import numpy as np
import re


def parse(data):
    paths = []
    x = []
    y = []
    for line in data.strip().split('\n'):
        prev = None
        for pair in re.findall(r"(\d+),(\d+)", line):
            a, b = map(int, pair)
            if prev is not None:
                paths.append((prev, (a, b)))
            prev = (a, b)
            x.append(a)
            y.append(b)
    return paths, min(x), max(x), min(y), max(y)


def draw_cave(cave, xmin, xmax, ymin, ymax):
    print()
    cavepart = cave[:ymax+2, 495-ymax:505+ymax]
    for row in cavepart:
        c = ""
        for char in row:
            c += dict(zip((0, 1, 2), ".#o"))[char]
        print(c)


def create_cave(paths, xmin, xmax, ymin, ymax):
    xmin = min(xmin, 500 - ymax)
    xmax = max(xmax, 500 + ymax)
    cave = np.zeros((ymax + 5, xmax + 5), np.uint8)
    for (xfrom, yfrom), (xto, yto) in paths:
        x, y = xfrom, yfrom
        while x != xto or y != yto:
            cave[y, x] = 1
            print(x, y, '#')
            if x < xto: 
                x += 1
            if y < yto:
                y += 1
            if y > yto:
                y -= 1
            if x > xto:
                x -= 1
        cave[y, x] = 1
        print(x, y, '#')
    return cave


def fill_cave(cave, xmin, xmax, ymin, ymax, bottomless):
    sand = 0
    while cave[0, 500] == 0:
        #draw_cave(cave, xmin, xmax, ymin, ymax)
        x, y = 500, 0
        sand += 1
        while cave[y, x] == 0:
            if y == ymax + 1:
                if bottomless:
                    return sand - 1
                else:
                    cave[y, x] = 2
                    break
            elif cave[y + 1, x] == 0:
                y += 1
            elif cave[y + 1, x - 1] == 0:
                y += 1
                x -= 1
            elif cave[y + 1, x + 1] == 0:
                y += 1
                x += 1
            else:
                cave[y, x] = 2
                break
    return sand
            


def solve(data, bottomless=True):
    paths, xmin, xmax, ymin, ymax = parse(data)
    cave = create_cave(paths, xmin, xmax, ymin, ymax)
    print(cave.sum())
    0/0
    return fill_cave(cave, xmin, xmax, ymin, ymax, bottomless=bottomless)


def solve2(data):
    return solve(data, bottomless=False)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 665

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 25434
