"""
Rucksack Reorganization

https://adventofcode.com/2022/day/3
"""
import string


def get_prio(char):
    if char in string.ascii_lowercase:
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26


def solve(data):
    total = 0
    for line in data.strip().split("\n"):
        n = len(line)
        first, second = set(line[: n // 2]), set(line[n // 2 :])
        chars = list(first.intersection(second))
        assert len(chars) == 1
        total += get_prio(chars[0])
    return total


def solve2(data):
    total = 0
    lines = data.strip().split("\n")
    for i in range(0, len(lines), 3):
        a, b, c = map(set, lines[i : i + 3])
        chars = set(a).intersection(set(b)).intersection(set(c))
        total += get_prio(list(chars)[0])
    return total


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")

    result = solve2(input_data)
    print(f"Example 2: {result}")
