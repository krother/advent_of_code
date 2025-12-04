"""


https://adventofcode.com/2025/day/
"""
from aoc import parse_2d_numbers, parse_hash_grid, parse_numbers, priority_queue, is_on_grid, DIRECTIONS4
from functools import cache

def parse(data):
    for row in data.strip().split("\n"):
        yield tuple([int(i) for i in row])

@cache
def find_best_joltage(bank, n):
    if n == 0:
        return 0
    if not bank:
        return -999999999999999999999999
    tail = tuple(bank[1:])
    a = bank[0] * 10 ** (n-1) + find_best_joltage(tail, n - 1)
    b = find_best_joltage(tail, n)
    return max(a, b)


def solve(data):
    total = 0
    for bank in parse(data):
        best = find_best_joltage(bank, 2)
        total += best
    return total


def solve2(data):
    total = 0
    for bank in parse(data):
        total += find_best_joltage(bank, 12)
    return total


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 17332

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 172516781546707