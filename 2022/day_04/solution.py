"""
Camp Cleanup

https://adventofcode.com/2022/day/4
"""
import re


def parse(data):
    for line in data.strip().split():
        yield map(int, re.findall(r'\d+', line))


def contains(a, b, c, d):
    return (c >= a and d <= b) or (a >= c and b <= d)


def overlaps(a, b, c, d):
    return (a <= c and c <= b) or (a <= d and c <= b)


def solve(data):
    return sum(1 for numbers in parse(data) if contains(*numbers))


def solve2(data):
    return sum(1 for numbers in parse(data) if overlaps(*numbers))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 485

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 857
