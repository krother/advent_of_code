"""
Day 18: RAM Run

https://adventofcode.com/2024/day/18
"""
import re
import numpy as np
from aoc import priority_queue, is_on_grid, DIRECTIONS4


def parse(data):
    coords = []
    for line in data.strip().split("\n"):
        x, y = map(int, line.split(","))
        coords.append((x, y))
    return coords
                   
def create_grid(size, coords):
    a = np.zeros(shape=(size, size), dtype=np.uint(8))
    for x, y in coords:
        a[y, x] = 1
    return a


def get_next_positions(grid, pos):
    x, y = pos
    for dx, dy in DIRECTIONS4:
        nx, ny = x + dx, y + dy
        if is_on_grid(x=nx, y=ny, grid=grid):
            yield nx, ny

                   
def solve(data, size, n):
    coords = parse(data)
    return walk(coords[:n], size)

def walk(coords, size):
    grid = create_grid(size, coords)
    start = 0, 0
    end = size - 1, size - 1
    pq = priority_queue.PriorityQueue()
    pq.add_task((start, 0), priority=0)
    visited = set()
    while pq:
        pos, steps = pq.pop_task()
        if pos in visited:
            continue
        visited.add(pos)
        if pos == end:
            return steps
        for nx, ny in get_next_positions(grid, pos):
            if grid[ny, nx] == 0:
                pq.add_task(((nx, ny), steps + 1), priority=steps + 1)

def solve2(data, size):
    coords = parse(data)
    n = len(coords)
    while not walk(coords[:n], size):
        print(n)
        n -= 1
    x, y = coords[n]
    return f"{x},{y}"


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, size=71, n=1024)
    print(f'Example 1: {result}')

    result = solve2(input_data, size=71)
    print(f'Example 2: {result}')
    assert result == "50,23"
