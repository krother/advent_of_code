"""
Day 6: Probably a Fire Hazard

https://adventofcode.com/2015/day/6

"""
import numpy as np
import re


def solve(data):
    grid = np.zeros((1000, 1000), np.int8)
    for line in data.strip().split('\n'):
        x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
        if 'on' in line:
            grid[x1:x2 + 1, y1:y2 + 1] = 1
        elif 'off' in line:
            grid[x1:x2 + 1, y1:y2 + 1] = 0
        elif 'toggle' in line:
            grid[x1:x2 + 1, y1:y2 + 1] = 1 - grid[x1:x2 + 1, y1:y2 + 1]
        else:
            assert False
    return grid.sum()

def solve2(data):
    grid = np.zeros((1000, 1000), np.int32)
    for line in data.strip().split('\n'):
        x1, y1, x2, y2 = [int(x) for x in re.findall(r'\d+', line)]
        if 'on' in line:
            grid[x1:x2 + 1, y1:y2 + 1] += 1
        elif 'off' in line:
            grid[x1:x2 + 1, y1:y2 + 1] -= 1
            grid[grid < 0] = 0
        elif 'toggle' in line:
            grid[x1:x2 + 1, y1:y2 + 1] += 2
        else:
            assert False


    return grid.sum()
if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
