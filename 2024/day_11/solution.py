"""
Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11
"""

cache = {}


def count_after_blinks(stone, n):
    if n == 0:
        return 1
    if (stone, n) in cache:
        return cache[(stone, n)]
    if stone == 0:
        result = count_after_blinks(1, n - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        left = int(s[: len(s) // 2])
        right = int(s[len(s) // 2 :])
        result = count_after_blinks(left, n - 1) + count_after_blinks(right, n - 1)
    else:
        result = count_after_blinks(stone * 2024, n - 1)
    cache[(stone, n)] = result
    return result


def solve(data, nblinks=25):
    total = 0
    for stone in list(map(int, data.strip().split())):
        total += count_after_blinks(stone, nblinks)
    return total


def solve2(data):
    return solve(data, nblinks=75)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 198089

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 236302670835517
