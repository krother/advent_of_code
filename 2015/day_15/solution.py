"""
Day 15: Science for Hungry People

https://adventofcode.com/2015/day/15

"""
import re
import numpy as np


def parse(data):
    result = []
    for line in data.strip().split('\n'):
        result.append([int(x) for x in re.findall(r'-?\d+', line)])
    return np.array(result)

def calc_value(m, spoons):
    val = np.dot(spoons, m)
    val[val < 0] = 0
    return val[:-1].prod()  # no calories

def add_spoon(spoons, i):
    s = spoons.copy()
    s[i] += 1
    return s

def try_spoons(m, spoons):
    tries = []
    for i, _ in enumerate(m):
        s = add_spoon(spoons, i)
        value = calc_value(m, s)
        tries.append((value, i, s))
    best_value, _, best_spoons = max(tries)
    return best_spoons


def find_best_spoons(m, n):
    spoons = np.ones(m.shape[0], np.int32)
    n -= m.shape[0]
    while n:
        spoons = try_spoons(m, spoons)
        n -= 1
    return spoons

def calc_calories(m, spoons):
    return np.dot(m[:, 4], spoons)

def solve(data):
    m = parse(data)
    spoons = find_best_spoons(m, 100)
    return calc_value(m, spoons)

def solve2(data):
    m = parse(data)
    best_value = 0
    best_spoons = None
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k > 100:
                    continue
                l = 100 - i - j - k
                spoons = np.array([i, j, k, l])
                cal = calc_calories(m, spoons)
                if cal == 500:
                    value = calc_value(m, spoons)
                    if value > best_value:
                        best_value = value
                        best_spoons = spoons
    return best_value

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
