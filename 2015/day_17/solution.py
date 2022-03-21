"""
Day 17: No Such Thing as Too Much

https://adventofcode.com/2015/day/17

"""
import re
from aoc import parse_numbers
from itertools import combinations
from collections import defaultdict


def solve(data, capacity):
    containers = parse_numbers(data)
    result = 0
    for n in range(1, len(containers) + 1):
        for c in combinations(containers, n):
            if sum(c) == capacity:
                result += 1
    return result

def solve2(data, capacity):
    containers = parse_numbers(data)
    result = defaultdict(int)
    for n in range(1, len(containers) + 1):
        for c in combinations(containers, n):
            if sum(c) == capacity:
                result[len(c)] += 1
    for n in sorted(result):
        return result[n]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 150)
    print(f'Example 1: {result}')

    result = solve2(input_data, 150)
    print(f'Example 2: {result}')
