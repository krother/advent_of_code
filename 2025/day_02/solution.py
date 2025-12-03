"""


https://adventofcode.com/2025/day/2
"""
import re

def parse(data):
    for elem in data.strip().split(","):
        start, end = elem.split("-")
        for i in range(int(start), int(end) + 1):
            yield i


def solve(data, pattern=r"^(\d+)\1$"):
    return sum(
        num
        for num in parse(data)
        if re.match(pattern, str(num))
    )


def solve2(data):
    return solve(data, pattern=r"^(\d+)\1+$")


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
