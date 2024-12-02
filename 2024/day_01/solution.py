"""
Historian Hysteria

https://adventofcode.com/2024/day/1

CHALLENGE: no variables, one-line functions only
"""
from typing import Iterable
from functools import partial

Column = tuple[int, ...]
NestedInt = Iterable[Iterable[int]]
NestedStr = Iterable[Iterable[str]]


def get_numbers(data: str) -> NestedStr:
    return map(lambda line: line.split(), data.strip().split("\n"))


def convert_to_int(data: Iterable[str]) -> Iterable[int]:
    return map(int, data)


def get_pairs(data: str) -> NestedInt:
    return map(convert_to_int, get_numbers(data))


def parse(data: str) -> Iterable[Column]:
    return zip(*get_pairs(data))


def sort_lists(lists: NestedInt) -> NestedInt:
    return map(sorted, lists)


def diff(a: int, b: int) -> int:
    return a - b


def absdiff(x: Iterable[int]) -> int:
    return abs(diff(*x))


def solve(data: str) -> int:
    return sum(map(absdiff, zip(*sort_lists(parse(data)))))


def prod_occurence(a: int, bb: Column) -> int:
    return a * bb.count(a)


def calc_productsum(aa: Column, bb: Column) -> int:
    return sum(map(partial(prod_occurence, bb=bb), aa))


def solve2(data: str) -> int:
    return calc_productsum(*parse(data))


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 1222801

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 22545250
