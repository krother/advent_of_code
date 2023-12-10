"""
Mirage Maintenance

https://adventofcode.com/2023/day/9
"""
import re
from functools import reduce


def parse(data):
    for line in data.strip().split("\n"):
        yield([int(x) for x in re.findall(r"\-*\d+", line)])

def diff(row):
    last = row[0]
    for value in row[1:]:
        yield value - last
        last = value

def solve_diff(row, index=-1, func=sum):
    values = []
    while set(row) != {0}:
        values.append(row[index])
        row = list(diff(row))
    return func(values)
    

def solve(data):
    return sum(
        solve_diff(row)
        for row in parse(data)
    )


def cumdiff(values):
    return reduce(lambda a, b: b - a, reversed(values), 0)


def solve2(data):
    return sum(
        solve_diff(row, index=0, func=cumdiff)
        for row in parse(data)
    )


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')  # 1939607039

    result = solve2(input_data)
    print(f'Example 2: {result}')  # 1041
