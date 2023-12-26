"""
Clumsy Crucible

https://adventofcode.com/2023/day/17
"""
from aoc.priority_queue import PriorityQueue
from aoc.parsers import parse_2d_numbers
from aoc.directions import *

REVERSE = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT, (0, 0): (0, 0)}


def find_shortest_path(data, min_steps, max_steps):
    d = parse_2d_numbers(data)
    queue = PriorityQueue()
    queue.add_task(((0, 0), 0, (0, 0), min_steps), 0)
    visited = set()
    maxx, maxy = d.shape[1], d.shape[0]
    while queue:
        (x, y), cost, last_direction, last_steps = queue.pop_task()
        if x == maxx - 1 and y == maxy - 1:
            print(cost, len(visited))
            return cost
        for direction in (UP, DOWN, LEFT, RIGHT):
            if direction == REVERSE[last_direction]:
                continue
            if direction == last_direction and last_steps == max_steps:
                continue
            elif direction == last_direction:
                steps = last_steps + 1
            elif direction != last_direction and last_steps < min_steps:
                continue
            else:
                steps = 1
            dx, dy = direction
            nx, ny = x + dx, y + dy
            if 0 <= nx < maxx and 0 <= ny < maxy:
                lookup = (nx, ny), direction, steps
                if lookup not in visited:
                    visited.add(lookup)
                    new_cost = cost + d[ny, nx]
                    task = (nx, ny), new_cost, direction, steps
                    queue.add_task(task, new_cost)


def solve(data):
    return find_shortest_path(data, 1, 3)


def solve2(data):
    return find_shortest_path(data, 4, 10)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 1099

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 1266
