"""
Supply Stacks

https://adventofcode.com/2022/day/5

"""
import re
import string
from collections import defaultdict


def parse_instructions(instructions):
    return [
        [int(num) for num in re.findall(r"\d+", line)]
        for line in instructions.strip().split("\n")
        ]

def parse_stacks(crates):
    stacks = defaultdict(list)
    lines = crates.split("\n")
    lines.pop()
    for row in reversed(lines):
        for i, col in enumerate(range(0, len(row), 4)):
            if (char := row[col + 1]) in string.ascii_uppercase:
                stacks[i+1].append(char)

    return stacks


def parse(data):
    part1, part2 = data.split('\n\n')
    stacks = parse_stacks(part1)
    instructions = parse_instructions(part2)
    return stacks, instructions



def get_stack_tops(stacks):
    return "".join(stacks[key][-1] for key in sorted(stacks))


def solve(data):
    stacks, instructions = parse(data)
    for number, source, dest in instructions:
        for _ in range(number):
            stacks[dest].append(stacks[source].pop())
    return get_stack_tops(stacks)


def solve2(data):
    stacks, instructions = parse(data)
    for number, source, dest in instructions:
        substack = stacks[source][-number:]
        stacks[source] = stacks[source][:-number]
        stacks[dest] += substack
    return get_stack_tops(stacks)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == "QMBMJDFTD"

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == "NBTVTJNFJ"
