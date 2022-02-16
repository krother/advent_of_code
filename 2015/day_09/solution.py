"""
Day 9: All in a Single Night

https://adventofcode.com/2015/day/9

"""
from collections import defaultdict
import math
import re


PATTERN = r"(\w+) to (\w+) = (\d+)"

def parse(data):
    routes = defaultdict(dict)
    for line in data.strip().split('\n'):
        c1, c2, dist = re.findall(PATTERN, line)[0]
        routes[c1][c2] = int(dist)
        routes[c2][c1] = int(dist)
    return routes


def best_path(start, cities, routes, func):
    best = math.inf if func({-math.inf, math.inf}) == -math.inf else -math.inf
    for c in cities:
        length = routes[start][c]
        remaining = cities ^ {c}
        if remaining:
            length += best_path(c, remaining, routes, func)
        best = func({best, length})
    return best


def solve(data):
    routes = parse(data)
    cities = frozenset(routes)
    return min([best_path(start, cities^{start}, routes, min) for start in cities])

def solve2(data):
    routes = parse(data)
    cities = frozenset(routes)
    return max([best_path(start, cities^{start}, routes, max) for start in cities])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
