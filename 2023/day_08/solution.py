"""
Haunted Wasteland

https://adventofcode.com/2023/day/8
"""
import re
from functools import reduce
from itertools import cycle


def parse(data):
    pattern, paths = data.strip().split("\n\n")
    graph = {}
    for line in paths.split("\n"):
        a, b, c = re.findall(r"\w+", line)
        graph[a] = b, c
    return pattern, graph


def count_steps(pattern, graph, start, end):
    steps = 0
    loc = start
    direction = cycle(pattern)
    while not loc.endswith(end):
        left, right = graph[loc]
        loc = left if next(direction) == "L" else right
        steps += 1
    return steps


def solve(data):
    pattern, graph = parse(data)
    return count_steps(pattern, graph, "AAA", end="ZZZ")


def get_pfacs(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return {i}.union(get_pfacs(number // i))
    return {number}


def solve2(data):
    pattern, graph = parse(data)
    steps = [
        count_steps(pattern, graph, loc, end="Z")
        for loc in graph
        if loc.endswith("A")
    ]
    pfacs = set()
    for s in steps:
        pfacs = pfacs.union(get_pfacs(s))
    result = reduce(lambda a, b: a * b, pfacs, 1)
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')  # 21251

    result = solve2(input_data)    # 11678319315857
    print(f'Example 2: {result}')
