
from pprint import pprint
from copy import deepcopy

VECTORS = [
    (-1, -1), (-1, 0), (-1, +1),
    ( 0, -1),          ( 0, +1),
    (+1, -1), (+1, 0), (+1, +1),
]

def tostr(s):
    return ''.join([''.join(row) for row in s])

def solve(fn):
    seats = open(fn).read().strip().split()
    seats = [list(r) for r in seats]
    ysize, xsize = len(seats), len(seats[0])
    while True:
        next_gen = calc_gen(seats, ysize, xsize)
        if tostr(seats) == tostr(next_gen):
            break
        seats = next_gen
    return tostr(seats).count('#')

def count_seats(s, y, x, ysize, xsize):
    count = 0
    for dy, dx in VECTORS:
        ny, nx = y, x
        while True:
            ny, nx = ny + dy, nx + dx
            if ny < 0 or nx < 0: break
            if ny >= ysize or nx >= xsize: break
            if s[ny][nx] == '#':
                count += 1
                break
            elif s[ny][nx] == 'L':
                break
    return count

def calc_gen(s, ysize, xsize):
    new = deepcopy(s)
    for y, row in enumerate(s):
        for x, seat in enumerate(row):
            c = count_seats(s, y, x, ysize, xsize)
            if seat == '#' and c >= 5:
                new[y][x] = 'L'
            elif seat == 'L' and c == 0:
                new[y][x] = '#'
    return new


assert solve('input.txt') == 26

print(solve('input_big.txt'))
