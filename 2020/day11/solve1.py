
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
        dy, dx = y + dy, x + dx
        if dy < 0 or dx < 0: continue
        if dy >= ysize or dx >= xsize: continue
        if s[dy][dx] == '#':
            count += 1
    return count

def calc_gen(s, ysize, xsize):
    new = deepcopy(s)
    for y, row in enumerate(s):
        for x, seat in enumerate(row):
            c = count_seats(s, y, x, ysize, xsize)
            if seat == '#' and c >= 4:
                new[y][x] = 'L'
            elif seat == 'L' and c == 0:
                new[y][x] = '#'
    return new

assert solve('input.txt') == 37

result = solve('input_big.txt')
assert result == 2265
print(result)
