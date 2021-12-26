"""Day 1: Sonar Sweep

https://adventofcode.com/2021/day/1

"""
import pandas as pd
from aoc import parse_numbers


def count_positive_increases(s):
    return sum(s.diff() > 0)


def solve(data):
    """part 1 of the challenge"""
    s = pd.Series(parse_numbers(data))
    return count_positive_increases(s)


def triple_window(data):
    """part 2 of the challenge"""
    s = pd.Series(parse_numbers(data))
    r = s.rolling(3).sum()
    return count_positive_increases(r)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 1583

    result = triple_window(input_data)
    print(f'Example 2: {result}')
    # 1627