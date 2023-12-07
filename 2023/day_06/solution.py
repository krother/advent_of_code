"""
Wait For It

https://adventofcode.com/2023/day/6
"""
import re
from functools import reduce


def parse(data, remove_spaces):
    data = data.replace(" ", "") if remove_spaces else data
    times, records = data.strip().split("\n")
    return list(
        zip(
            [int(t) for t in re.findall(r"\d+", times)],
            [int(d) for d in re.findall(r"\d+", records)],
        )
    )


def analyze_race(time, record):
    return sum(
        1
        for charge in range(time)
        if charge * (time - charge) > record
    )


def solve(data, remove_spaces=False):
    return reduce(
        lambda total, race: total * analyze_race(*race),
        parse(data, remove_spaces), 1
    )


def solve2(data):
    return solve(data, remove_spaces=True)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 449550

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 28360140
