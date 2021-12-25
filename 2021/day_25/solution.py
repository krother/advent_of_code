"""Sea Cucumber

https://adventofcode.com/2021/day/25

"""
import numpy as np
from itertools import count

EMPTY, CUDOWN, CURIGHT = range(3)


def cucumber2int(char):
    return CUDOWN if char == 'v' else CURIGHT if char == '>' else EMPTY


def parse(data):
    result = [
        [cucumber2int(char) for char in row]
        for row in data.strip().split('\n')
    ]
    return np.array(result, np.uint8)


def move(a, cucumber, axis):
    moving = (a == cucumber)
    dest = np.roll(moving, 1, axis=axis)
    dest = dest & (a == EMPTY)
    ori = np.roll(dest, -1, axis=axis)
    a[ori] = EMPTY
    a[dest] = cucumber


def solve(data):
    a = parse(data)
    prev = a.copy()
    for i in count(1):
        move(a, CURIGHT, axis=1)
        move(a, CUDOWN, axis=0)
        if np.all(a == prev):
            return i
        prev = a.copy()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 334
