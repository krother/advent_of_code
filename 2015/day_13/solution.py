"""title

https://adventofcode.com/2021/day/1

"""
from collections import defaultdict
from itertools import permutations
import re

PATTERN = r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."

def parse(data):
    costs = defaultdict(dict)
    for line in data.strip().split('\n'):
        name1, sign, num, name2 = re.findall(PATTERN, line)[0]
        sign = 1 if sign == 'gain' else -1
        costs[name1][name2] = int(num) * sign
    return costs

def calc_happiness(order, costs):
    total = 0
    for i in range(1, len(order)-1):
        person = order[i]
        total += costs[person][order[i - 1]]
        total += costs[person][order[i + 1]]
    total += costs[order[-1]][order[-2]]
    total += costs[order[-1]][order[0]]
    total += costs[order[0]][order[1]]
    total += costs[order[0]][order[-1]]
    return total

def best_seating(costs):
    people = list(costs)
    first = people[0]
    result = []
    for p in permutations(people[1:]):
        order = [first] + list(p)
        result.append(calc_happiness(order, costs))
    return max(result)

def solve(data):
    costs = parse(data)
    return best_seating(costs)


def solve2(data):
    costs = parse(data)
    for p in list(costs):
        costs[p]['santa'] = 0
        costs['santa'][p] = 0
    return best_seating(costs)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
