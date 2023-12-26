"""
Cosmic Expansion

https://adventofcode.com/2023/day/11
"""
from aoc.parsers import parse_hash_grid


def solve(data, inc=1):
    a = parse_hash_grid(data)

    stars = []
    empty_rows = set()
    empty_cols = set()
    for y, row in enumerate(a):
        if a[y, :].sum() == 0:
            empty_rows.add(y)
        for x, char in enumerate(row):
            if char:
                stars.append((x, y))
            if y == 0 and a[:, x].sum() == 0:
                empty_cols.add(x)

    total = 0
    for i, first in enumerate(stars):
        for second in stars[i + 1 :]:
            x1, y1 = first
            x2, y2 = second
            manhattan_dist = abs(x2 - x1) + abs(y2 - y1)
            for x in range(min(x1, x2), max(x1, x2)):
                if x in empty_cols:
                    manhattan_dist += inc
            for y in range(min(y1, y2), max(y1, y2)):
                if y in empty_rows:
                    manhattan_dist += inc
            total += manhattan_dist
    return total


if __name__ == "__main__":
    input_data = open("input_data.txt").read()  # 9795148
    result = solve(input_data)
    print(f"Example 1: {result}")

    result = solve(input_data, 999_999)  # 650672493820
    print(f"Example 2: {result}")
