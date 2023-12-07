"""
Scratchcards

https://adventofcode.com/2023/day/4
"""
import re
from collections import defaultdict


def parse(data):
    for line in data.strip().split("\n"):
        left, right = line.split("|")
        left = left[9:]
        left = set([int(n) for n in re.findall("\d+", left)])
        right = set([int(n) for n in re.findall("\d+", right)])
        yield left, right


def solve(data):
    result = 0
    for left, right in parse(data):
        match = len(left.intersection(right))
        if match:
            result += 2 ** (match - 1)
    return result


def solve2(data):
    total = 0
    multipliers = defaultdict(int)
    i = 1
    for left, right in parse(data):
        match = len(left.intersection(right))
        n = multipliers[i] + 1
        total += n
        if match:
            for j in range(i + 1, i + match + 1):
                multipliers[j] += n
        i += 1
    return total


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')  # 23750

    result = solve2(input_data)
    print(f'Example 2: {result}')  # 13261850
