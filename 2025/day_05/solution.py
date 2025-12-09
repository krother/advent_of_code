"""
Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""
from __future__ import annotations

import re
from pydantic import BaseModel


class Ingredients(BaseModel):
    start: int
    end: int

    def contains(self, num: int) -> bool:
        return self.start <= num <= self.end
    
    @property
    def size(self) -> int:
        return self.end - self.start + 1

    def overlaps(self, other: Ingredients) -> bool:
        return (
            (other.start <= self.start <= other.end) or
            (self.start <= other.start <= self.end)
        )
    
    def merge(self, other: Ingredients) -> Ingredients:
        return Ingredients(
            start = min(self.start, other.start),
            end = max(self.end, other.end)
        )


def parse(data: str) -> tuple[list[Ingredients], list[int]]:
    ranges = [
        Ingredients(start=a, end=b)
        for a, b in re.findall(r"(\d+)\-(\d+)", data)
    ]
    id_list = [
        int(line)
        for line in data.strip().split("\n\n")[1].split("\n")
    ]
    return ranges, id_list


def solve(data):
    ranges, id_list = parse(data)
    return sum(
        any(r.contains(num) for r in ranges)
        for num in id_list
    )


def solve2(data):
    ranges, _ = parse(data)
    done = []
    while ranges:
        first = ranges.pop()
        new = []
        target = done
        for second in ranges:
            if first.overlaps(second):
                first = first.merge(second)
                target = new
            else:
                new.append(second)
        target.append(first)
        ranges = new

    return sum(r.size for r in done)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 615

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 353716783056994
