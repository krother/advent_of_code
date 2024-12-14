"""
Day 3: Mull It Over

https://adventofcode.com/2024/day/3
"""
import re


def solve(data):
    total = 0
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", data):
        total += int(a) * int(b)
    return total


def solve2(data):
    total = 0
    enabled = True
    for inst in re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))", data):
        if inst[0] and enabled:
            a, b = re.findall(r"\d+", inst[0])
            total += int(a) * int(b)
        elif inst[1]:
            enabled = True
        elif inst[2]:
            enabled = False
    return total


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")

    result = solve2(input_data)
    print(f"Example 2: {result}")
