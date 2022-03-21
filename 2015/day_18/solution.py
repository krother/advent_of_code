"""
Day 18: Like a GIF For Your Yard

https://adventofcode.com/2015/day/18
"""

from aoc import parse_hash_grid
import numpy as np


def count_neighbors(a, x, y):
    slice = a[x - 1:x + 2, y - 1:y + 2]
    return slice.sum() - slice[1, 1]

def step(a):
    b = np.zeros(a.shape, a.dtype)
    for x in range(1, a.shape[0] - 1):
        for y in range(1, a.shape[1] - 1):
            neighbors = count_neighbors(a, x, y)
            if a[x, y] == 0 and neighbors == 3:
                b[x, y] = 1
            elif a[x, y] == 1 and neighbors in (2, 3):
                b[x, y] = 1
    return b

def switch_on_corners(a):
    a[1, 1] = 1
    a[1, -2] = 1
    a[-2, 1] = 1
    a[-2, -2] = 1

def solve(data, iter, corners_on=False):
    a = parse_hash_grid(data)
    a = np.pad(a, 1)
    if corners_on:
        switch_on_corners(a)

    for _ in range(iter):
        a = step(a)
        if corners_on:
            switch_on_corners(a)
    return a.sum()

def solve2(data):
    return data

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 100)
    print(f'Example 1: {result}')

    result = solve(input_data, 100, True)
    print(f'Example 2: {result}')
