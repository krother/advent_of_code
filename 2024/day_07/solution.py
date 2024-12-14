"""
Day 7: Bridge Repair

https://adventofcode.com/2024/day/7
"""
from tqdm import tqdm
from itertools import product
from operator import add, mul
import re
import math


def parse_numbers(line):
    return map(int, re.findall(r"\d+", line))


def parse(data):
    return [
        (output, numbers)
        for output, *numbers in map(parse_numbers, data.strip().split("\n"))
    ]


def concat(a, b):
    # return int(str(a) + str(b))
    # 30% faster but uglier:
    return a * 10 ** int(math.log(b, 10) + 1) + b


def calc(start, tail, oplist):
    a = start
    for op, b in zip(oplist, tail):
        a = op(a, b)
    return a


def check_equation(out, numbers, operators):
    start, *tail = numbers
    for oplist in product(operators, repeat=len(tail)):
        if calc(start, tail, oplist) == out:
            return True


def solve(data, operators=(add, mul)):
    return sum(
        out
        for out, numbers in tqdm(parse(data))
        if check_equation(out, numbers, operators)
    )


def solve2(data):
    return solve(data, operators=(add, mul, concat))


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 1289579105366

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 92148721834692
