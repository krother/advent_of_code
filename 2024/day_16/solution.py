"""


https://adventofcode.com/2024/day/16
"""
from aoc import priority_queue, DIRECTIONS4
from itertools import product
from copy import copy
from collections import defaultdict


def parse(data):
    grid = data.strip().split("\n")
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] == "S":
            start = x, y
        elif grid[y][x] == "E":
            end = x, y
    return grid, start, end


def get_next_position(pos, heading):
    x, y = pos
    dx, dy = DIRECTIONS4[heading]
    return x + dx, y + dy


def get_moves(grid, pos, heading, cost):
    # move forward
    nx, ny = get_next_position(pos, heading)
    if grid[ny][nx] != "#":
        yield (nx, ny), heading, cost + 1
    # turn
    yield pos, (heading + 1) % 4, cost + 1000
    yield pos, (heading + 3) % 4, cost + 1000


def solve(data):
    grid, start, end = parse(data)
    pq = priority_queue.PriorityQueue()
    pq.add_task((start, 1, 0), priority=0)
    visited = set()
    while pq:
        pos, heading, cost = pq.pop_task()
        if (pos, heading) in visited:
            continue
        visited.add((pos, heading))
        if pos == end:
            return cost
        for pos, heading, cost in get_moves(grid, pos, heading, cost):
            pq.add_task((pos, heading, cost), priority=cost)


def solve2(data):
    grid, start, end = parse(data)
    pq = priority_queue.PriorityQueue()
    pq.add_task((start, 1, 0, start), priority=0)
    visited = set()
    path_dict = defaultdict(set)  # all paths leading to a position
    path_cost = {}  # lowest cost to get to a position
    best_cost = None
    while pq:
        pos, heading, cost, prev = pq.pop_task()
        path_dict[pos].add(pos)
        path_dict[pos].update(path_dict[prev])
        path_cost[pos] = cost

        if (pos, heading) in visited:
            continue
        visited.add((pos, heading))

        if pos == end:
            best_cost = cost
        elif best_cost and cost > best_cost:
            return len(path_dict[end])
        else:
            for newpos, heading, cost in get_moves(grid, pos, heading, cost):
                pq.add_task((newpos, heading, cost, pos), priority=cost)

    print(path_dict[end])
    return len(path_dict[end])


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 105508

    result = solve2(input_data)
    print(f"Example 2: {result}")  # not 561
