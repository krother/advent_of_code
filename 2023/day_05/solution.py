"""
If You Give A Seed A Fertilizer

https://adventofcode.com/2023/day/5
"""
import re
from dataclasses import dataclass


@dataclass
class ConversionRule:

    dest_start: int
    src_start: int
    size: int

    @property
    def src_end(self):
        return self.src_start + self.size

    @property
    def dest_end(self):
        return self.dest_start + self.size

    def __repr__(self):
        return f"<convert {self.src_start}..{self.src_end-1} -> {self.dest_start}..{self.dest_end-1}>"

    def convert(self, rng):
        # left part until src_start
        size = min(self.src_start - rng.start, rng.size)
        left = Range(rng.start, size)

        # right part after src_end
        start = max(self.src_end + 1, rng.start)
        size = rng.end - start
        right = Range(start, size)

        # center -> actual conversion
        start = max(self.src_start, rng.start)
        end = min(self.src_end, rng.end)
        size = end - start
        mod = self.dest_start - self.src_start
        center = Range(start + mod, size)

        return left, center, right


@dataclass
class Range:
    start: int
    size: int

    @property
    def end(self):
        return self.start + self.size

    def __hash__(self):
        return hash((self.start, self.size))

    def __repr__(self):
        if self.size > 0:
            return f"{self.start}..{self.end - 1}"
        return "-"


def parse_rules(blocks):
    conversions = []
    for b in blocks:
        lines = b.split("\n")
        rules = []
        for line in lines[1:]:
            dest_start, src_start, num = [int(n) for n in re.findall(r"\d+", line)]
            rules.append(ConversionRule(dest_start, src_start, num))
        conversions.append(rules)
    return conversions


def simple_seed_parser(block):
    return [Range(int(n), 1) for n in re.findall(r"\d+", block)]


def ranged_seed_parser(block):
    return [Range(int(m), int(n)) for m, n in re.findall(r"(\d+) (\d+)", block)]


def parse(data, seed_parser):
    blocks = data.strip().split("\n\n")
    seeds = seed_parser(blocks[0])
    rules = parse_rules(blocks[1:])
    return seeds, rules


def get_solution(rules, seeds):
    items = set(seeds)
    for conversion in rules:
        new = set()
        for rule in conversion:
            remaining = set()
            for item in items:
                left, center, right = rule.convert(item)

                if left.size > 0:
                    remaining.add(left)
                if right.size > 0:
                    remaining.add(right)
                if center.size > 0:
                    new.add(center)
            items = remaining

        items = new.union(items)
    return min([i.start for i in items])


def solve(data):
    seeds, rules = parse(data, simple_seed_parser)
    return get_solution(rules, seeds)


def solve2(data):
    seeds, rules = parse(data, ranged_seed_parser)
    return get_solution(rules, seeds)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 424490994

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 15290096
