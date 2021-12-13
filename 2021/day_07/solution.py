"""Crabs

https://adventofcode.com/2021/day/7

"""
import numpy as np


def parse(data):
    return np.array(data.strip().split(',')).astype(int)


COST = {}

def get_cost(dist):
    if dist not in COST:
        COST[dist] = sum(range(1, dist + 1))
    return COST[dist]

cost_func2 = np.frompyfunc(get_cost, 1, 1)


def solve(data, cost_func=None):
    crabs = parse(data).reshape(-1, 1)
    targets = np.arange(min(crabs), max(crabs)+1)
    cost = np.abs(crabs - targets)
    if cost_func:
        cost = cost_func(cost)
    return min(cost.sum(axis=0))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 340056

    result = solve(input_data, cost_func2)
    print(f'Example 2: {result}')
    # 96592275
