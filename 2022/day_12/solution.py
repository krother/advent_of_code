"""
Hill Climbing Algorithm

https://adventofcode.com/2022/day/12
"""
from collections import deque
from aoc.directions import UP, DOWN, LEFT, RIGHT


def parse(data):
    grid = []
    start = None
    end = None
    for y, row in enumerate(data.strip().split('\n')):
        if 'S' in row:
            start = row.index('S'), y
            row = row.replace('S', 'a')
        if 'E' in row:
            end = row.index('E'), y
            row = row.replace('E', 'z')        
        grid.append([ord(char) - 96 for char in row])
    return grid, start, end


def get_grid_moves(grid, x, y):
    for dx, dy in [UP, DOWN, LEFT, RIGHT]:
        newx = x + dx
        newy = y + dy
        if newx < 0 or newy < 0 or newx >= len(grid[0]) or newy >= len(grid):
            continue
        yield newx, newy


def find_shortest_path(grid, start, target):
    visited = set()
    candidates = deque([(start, 0)])
    while candidates:
        pos, steps = candidates.popleft()
        if pos == target:
            return steps
        if pos in visited:
            continue
        visited.add(pos)
        height = grid[pos[1]][pos[0]]
        for x, y in get_grid_moves(grid, *pos):
            if grid[y][x] - height <= 1:
                candidates.append(((x, y), steps + 1))


def solve(data):
    grid, start, target = parse(data)
    return find_shortest_path(grid, start, target)


def solve2(data):
    paths = []
    grid, start, target = parse(data)
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == 1:
                length = find_shortest_path(grid, (x, y), target)
                if length:
                    paths.append(length)
    return min(paths)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
