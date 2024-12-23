"""
Day 16: Reindeer Maze

https://adventofcode.com/2024/day/16
"""
from aoc import priority_queue, DIRECTIONS4
from itertools import product
from collections import defaultdict


Position = tuple[int, int, int]


def parse(data):
    grid = data.strip().split("\n")
    for y, x in product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] == "S":
            start = x, y, 1
        elif grid[y][x] == "E":
            end = x, y, None
    return grid, start, end


def get_next_position(position):
    x, y, heading = position
    dx, dy = DIRECTIONS4[heading]
    return x + dx, y + dy, heading


def get_moves(grid, pos, cost):
    # move forward
    nx, ny, heading = get_next_position(pos)
    if grid[ny][nx] != "#":
        yield (nx, ny, heading), cost + 1
    # turn
    x, y, heading = pos
    yield (x, y, (heading + 1) % 4), cost + 1000
    yield (x, y, (heading + 3) % 4), cost + 1000


class Candidate:

    def __init__(self, pos, cost, path):
        self.pos = pos
        self.cost = cost
        self.path = path

    def __hash__(self):
        return hash(self.pos)

    def get_move_candidates(self, grid):
        for newpos, cost in get_moves(grid, self.pos, self.cost):
            yield Candidate(pos=newpos, cost=cost, path=self.path + [newpos])


def find_shortest_path(grid, start, end, expand_end=True, taboo=None, cap=None):
    if expand_end:
        ex, ey, _ = end
        end = set([(ex, ey, h) for h in range(4)])
    else:
        end = {end}
    pq = priority_queue.PriorityQueue()
    pq.add_task(Candidate(start, 0, [start]), priority=0)
    visited = set(taboo or [])
    while pq:
        c = pq.pop_task()
        if c.pos not in visited and (cap is None or c.cost <= cap):
            visited.add(c.pos)
            if c.pos in end:
                return c.cost, c.path
            for newc in c.get_move_candidates(grid):
                pq.add_task(newc, priority=newc.cost)

    # no path found
    return None, None


def solve(data):
    grid, start, end = parse(data)
    cost, _ = find_shortest_path(grid, start, end)
    return cost


def solve2(data):
    grid, start, end = parse(data)
    main_cost, main_path = find_shortest_path(grid, start, end)
    result = set(main_path)
    taboo = set()
    for x, y, heading in product(range(len(grid[0])), range(len(grid)), range(4)):
        if grid[y][x] != '#':
            pivot = x, y, heading
            print(pivot, "taboo size", len(taboo))
            if pivot in result:
                continue
            cost1, part1 = find_shortest_path(grid, start, pivot, expand_end=False, taboo=taboo, cap=main_cost)
            if part1:
                cost2, part2 = find_shortest_path(grid, pivot, end, taboo=taboo, cap=main_cost)
                if part2 and cost1 + cost2 == main_cost:
                    # found alternative path
                    print("found new path")
                    result.update(part1)
                    result.update(part2)
                else:
                    # pivot element is not on any path
                    taboo.add(pivot)
            else:
                # pivot element is not on any path
                taboo.add(pivot)


    result = set((x, y) for x, y, _ in result)
    return len(result)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 105508

    result = solve2(input_data)
    print(f"Example 2: {result}")  # not 561
