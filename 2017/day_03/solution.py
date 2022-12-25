"""
Spiral Memory

https://adventofcode.com/2017/day/3
"""
from itertools import cycle

from aoc.directions import UP, DOWN, LEFT, RIGHT, MOVES8



def solve(n):
    """returns the spiral solution for puzzle input n"""
    if n == 1:
        return 0
    circle = 0
    while True:
        edge_length = circle * 2 + 1
        inner = edge_length ** 2
        if n <= inner:
            corners = [(edge_length - 2) ** 2] + [inner - (i * (edge_length-1)) for i in range(4)]
            steps_to_corner = min([abs(c - n) for c in corners])
            steps_to_middle = edge_length // 2 - steps_to_corner
            return circle + steps_to_middle
        circle += 1


def spiral():
    """generates spiral coordinates"""
    direction_gen = cycle([UP, RIGHT, DOWN, LEFT])
    bearing = next(direction_gen)
    next_bearing = None
    x, y = 0, 0
    visited = {(0, 0)}

    while True:
        dx, dy = bearing
        x += dx
        y += dy
        yield x, y
        visited.add((x, y))

        # look around the corner
        if next_bearing is None:
            next_bearing = next(direction_gen)
        xb, yb = next_bearing
        if (x + xb, y + yb) not in visited: 
            bearing = next_bearing
            next_bearing = None


def solve2(puzzle_input):
    values = {(0, 0): 1}
    for x, y in spiral():
        result = sum([values.get((x + xv, y + yv), 0) for xv, yv in MOVES8])
        values[(x, y)] = result
        if result > puzzle_input:
            return result
        

if __name__ == '__main__':
    result = solve(265149)
    print(f'Example 1: {result}')

    result = solve2(265149)
    print(f'Example 2: {result}')
