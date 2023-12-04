"""
Cube Conundrum

https://adventofcode.com/2023/day/2
"""
import re


MAXCUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
PATTERN = "(\d+) (red|green|blue)"


def is_line_possible(line):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_id = int(re.findall("Game (\d+)", line)[0])
    for num, col in re.findall(PATTERN, line):
        if MAXCUBES[col] < int(num):
            return 0
    return game_id


def get_line_power(line):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    minimal = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for num, col in re.findall(PATTERN, line):
        num = int(num)
        if num > minimal[col]:
            minimal[col] = num
    return minimal["red"] * minimal["green"] * minimal["blue"]


def solve(data):
    return sum([is_line_possible(line) for line in data.split("\n")])


def solve2(data):
    return sum([get_line_power(line) for line in data.split("\n")])


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 2061

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 72596
