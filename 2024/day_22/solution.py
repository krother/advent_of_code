"""
Day 22: Monkey Market

https://adventofcode.com/2024/day/22
"""
from aoc import parse_numbers
from collections import defaultdict
from functools import cache
import numpy as np


@cache
def get_secret(n):
    n = n ^ (n * 64) % 16777216
    n = n ^ (n // 32) % 16777216
    n = n ^ (n * 2048) % 16777216
    return n


def get_secret_seq(sec, n=2000):
    result = []
    for _ in range(n):
        sec = get_secret(sec)
        result.append(sec)
    return np.array(result)


def solve(data):
    result = 0
    for sec in parse_numbers(data):
        result += get_secret_seq(sec)[-1]
    return result


def solve2(data):
    sequences = defaultdict(int)

    for sec in parse_numbers(data):
        windows = {}
        seq = get_secret_seq(sec)
        prices = seq % 10
        diff = np.diff(prices)
        keys = np.lib.stride_tricks.as_strided(
            diff, strides=diff.strides * 2, shape=(diff.size - 4 + 1, 4)
        )
        for i in range(4, prices.shape[0]):
            key = tuple(keys[i - 4])
            windows.setdefault(key, prices[i])
        for part in windows:
            sequences[part] += windows[part]

    return max(sequences.values())


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 17262627539

    result = solve2(input_data)
    print(f"Example 2: {result}")
    assert result == 1986
