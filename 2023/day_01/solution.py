"""
Trebuchet

https://adventofcode.com/2023/day/1
"""
import re


NUMBERS = "one","two","three","four","five","six","seven","eight","nine"


def parse_number(line):
    numbers = re.findall("\d", line)
    return int(numbers[0] + numbers[-1])


def solve(data):
    return sum(
        parse_number(line)
        for line in data.split("\n")
    )


def solve2(data):
    for i, word in enumerate(NUMBERS, 1):
        data = data.replace(word, f"{word}{i}{word}")  # three -> three3three
    return solve(data)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")

    result = solve2(input_data)
    print(f"Example 2: {result}")
