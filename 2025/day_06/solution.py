"""
Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""
from operator import add, mul
from functools import reduce
from typing import Generator, Iterable, Literal, cast
import re

Operator = Literal["+", "*"]

funcs = {"+": add, "*": mul}
start = {"+": 0, "*": 1}


def calculate(numbers: Iterable[Iterable[int]], ops: list[Operator]):
    return sum(
        reduce(funcs[op], c, start[op])
        for c, op in zip(numbers, ops)
    )

def parse(data: str) -> tuple[list[str], list[Operator]]:
    *num_block, op_block = data.strip().split("\n")
    ops = op_block.strip().split()
    return num_block, cast(list[Operator], ops)


def get_numbers(rows: list[str]) -> list[list[int]]:
    return [
        [int(i) for i in row.split()]
        for row in "\n".join(rows).split("\n\n")]

def transpose_rows(nums: list[str]) -> list[str]:
    return ["".join(t).strip() for t in list(zip(*nums))]

def prep_data(nums, ops):
    return zip(*[
        [int(n) for n in re.findall(r"\d+", row)]
        for row in nums
        ]), ops

def prep_data2(nums, ops):
    return get_numbers(transpose_rows(nums)), ops

def solve(data: str, func=prep_data):
    return calculate(*func(*parse(data)))

def solve2(data: str) -> int:
    return solve(data, prep_data2)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 3785892992137

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 7669802156452
