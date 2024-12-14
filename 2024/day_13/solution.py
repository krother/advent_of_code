"""
Day 13: Claw Contraption

https://adventofcode.com/2024/day/13
"""
import re


def parse(data):
    result = []
    for block in data.split("\n\n"):
        result.append(map(int, re.findall(r"\d+", block, re.DOTALL)))
    return result


def calc_tokens(ax, ay, bx, by, px, py, offset):
    # make sure vectors are not colinear
    assert round(ax / ay, 6) != round(bx / by, 6)
    px, py = px + offset, py + offset

    b = (py - ay * px / ax) / (by - ay * bx / ax)
    a = (px - b * bx) / ax
    if round(a, 3) == round(a) and round(b, 3) == round(b):
        return round(a) * 3 + round(b)
    return 0


def solve(data, offset=0):
    return sum(calc_tokens(*b, offset) for b in parse(data))


def solve2(data):
    return solve(data, offset=10_000_000_000_000)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 26005

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 105620095782547
