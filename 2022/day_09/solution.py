"""
Rope Bridge

https://adventofcode.com/2022/day/9
"""
from aoc.directions import UP, DOWN, LEFT, RIGHT


MOVES = dict(zip("UDLR", [UP, DOWN, LEFT, RIGHT]))


def move(pos, direction):
    x, y = pos
    dx, dy = MOVES[direction]
    return x + dx, y + dy


def drag_tail(head, tail):
    xh, yh = head
    xt, yt = tail
    xdist = xh - xt
    ydist = yh - yt
    if abs(xdist) >= 2 or abs(ydist) >= 2:
        xt += 0 if xdist == 0 else xdist // abs(xdist)  # normalize to length 1
        yt += 0 if ydist == 0 else ydist // abs(ydist)  # normalize to length 1
    return xt, yt


def parse(data):
    for line in data.strip().split('\n'):
        direction, steps = line.split()
        for _ in range(int(steps)):
            yield direction 


def solve(data):
    head = 0, 0
    tail = 0, 0
    visited = {(0, 0)}
    for direction in parse(data):
        head = move(head, direction)
        tail = drag_tail(head, tail)
        visited.add(tail)

    return len(visited)


def solve2(data):
    head = 0, 0
    snake = [(0, 0)] * 9
    visited = {(0, 0)}
    for direction in parse(data):
        head = move(head, direction)
        new = []
        prev = head
        for item in snake:
            newpos = drag_tail(prev, item)
            new.append(newpos)
            prev = newpos
        visited.add(new[-1])
        snake = new

    return len(visited)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 6243

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 2630
