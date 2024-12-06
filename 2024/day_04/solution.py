"""
Day 4: Ceres Search

https://adventofcode.com/2024/day/4
"""
from itertools import product


def count(matrix):
    # rows
    result = sum([row.count("XMAS") for row in matrix])
    # diagonals top left to bottom right
    for x, y in product(range(len(matrix[0]) - 3), range(len(matrix) - 3)):
        for z, char in zip(range(4), "XMAS"):
            if matrix[y + z][x + z] != char:
                break
        else:
            result += 1
    return result


def rotate(matrix):
    matrix = [row[::-1] for row in matrix]
    matrix = ["".join(row) for row in zip(*matrix)]
    return matrix


def count_xmas(matrix):
    return sum(
        (
            (
                matrix[y - 1][x - 1]
                + matrix[y - 1][x + 1]
                + matrix[y][x]
                + matrix[y + 1][x - 1]
                + matrix[y + 1][x + 1]
            )
            == "MMASS"
        )
        for x, y in product(range(1, len(matrix[0]) - 1), range(1, len(matrix) - 1))
    )


def solve(data, func=count):
    total = 0
    matrix = data.strip().split()
    for _ in range(4):
        total += func(matrix)
        matrix = rotate(matrix)
    return total


def solve2(data):
    return solve(data, func=count_xmas)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 2591

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 1880
