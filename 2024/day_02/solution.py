"""


https://adventofcode.com/2024/day2/
"""
from functools import partial


def parse(data):
    return [[int(x) for x in line.split()] for line in data.strip().split("\n")]


def match(prev, follow):
    """assume increasing order"""
    return prev < follow and prev + 3 >= follow


def is_safe(report):
    last = report[0]
    for x in report[1:]:
        if not match(last, x):
            return False
        last = x
    return True


def is_safe_damp(report):
    result = False
    for i in range(len(report)):
        copy = report[:]
        copy.pop(i)
        if is_safe(copy):
            result = True
    return result


def solve(data, func=is_safe):
    return sum(func(report) or func(report[::-1]) for report in parse(data))


solve2 = partial(solve, func=is_safe_damp)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 421

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 476
