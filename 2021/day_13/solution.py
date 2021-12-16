"""Transparent Origami

https://adventofcode.com/2021/day/13

"""
import re
import numpy as np
from functools import reduce


POINT = r'(\d+),(\d+)'
FOLD = r'(\w)=(\d+)'


def create_array(points):
    xsize = max(points)[0] + 1
    ysize = max(points, key=lambda p: p[1])[1] + 1
    a = np.zeros((ysize, xsize), dtype=int)
    for x, y in points:
        a[y, x] = 1
    return a


def parse(data):
    points = [(int(x), int(y)) for x, y in re.findall(POINT, data)]
    a = create_array(points)
    folds = [(c, int(d)) for c, d in re.findall(FOLD, data)]
    return a, folds


def foldy(a, row):
    b = a[:row]
    bottom = a[-1:row:-1]
    offset = row - bottom.shape[0]
    b[offset:] = b[offset:] | bottom
    return b


def foldx(a, col):
    return foldy(a.T, col).T


FOLDMAP = dict(x=foldx, y=foldy)

def fold(a, foldinfo):
    axis, position = foldinfo
    return FOLDMAP[axis](a, position)

def solve(data):
    a, instructions = parse(data)
    a = reduce(fold, instructions, a)
    return '\n'.join([''.join(['#' if c else '.' for c in row]) for row in a])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(result)
