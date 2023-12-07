"""
If You Give A Seed A Fertilizer

https://adventofcode.com/2023/day/5
"""
import re
from dataclasses import dataclass

@dataclass
class Range:
    start: int
    size: int

    @property
    def end(self):
        return self.start + self.size - 1
    
    def get_converted_range(self, dest_start, src_start, num):
        if src_start <= self.start and src_start + num > self.end:
            # fully contained
            return Range(
                start=dest_start + self.start - src_start,
                size=self.size
            )
        elif src_start <= self.start and src_start + num <= self.end:
            # left overlap
            return Range(
                start=dest_start + self.start - src_start,
                size=self.size - self.start + src_start + num
            )
        elif src_start > self.start and src_start + num > self.end:
            # right overlap
            return Range(
                start=dest_start + self.start - src_start,
                size=self.size - src_start + self.start
            )
        else:
            # split
            return Range(
                start=dest_start + self.start - src_start,
                size=num
            )

    def convert(self, conversion):
        result = []
        for dest_start, src_start, num in conversion:
            r = self.get_converted_range(dest_start, src_start, num)
            if r:
                result.append(r)
        if not result:
            result.append(self)
        return result


def parse(blocks):
    rules = []
    for b in blocks:
        lines = b.split("\n")
        items = []
        for line in lines[1:]:
            dest_start, src_start, num = [int(n) for n in re.findall(r"\d+", line)]
            items.append((dest_start, src_start, num))
        rules.append(items)
    return rules


def get_solution(blocks, seeds):
    rules = parse(blocks)
    items = seeds
    for conversion in rules:
        print(len(items))
        new = []
        for item in items:
            new += item.convert(conversion)
        items = new
    return min([i.start for i in items])

def solve(data):
    blocks = data.strip().split("\n\n")
    seeds = blocks[0]
    seeds = [Range(int(n), 1) for n in re.findall(r"\d+", seeds)]
    return get_solution(blocks[1:], seeds)


def solve2(data):
    blocks = data.strip().split("\n\n")
    seeds = [Range(int(m), int(n)) for m, n in re.findall(r"(\d+) (\d+)", blocks[0])]
    return get_solution(blocks[1:], seeds)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    # result = solve2(input_data)
    # print(f'Example 2: {result}')
