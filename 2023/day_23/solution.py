"""
A Long Walk

https://adventofcode.com/2023/day/23
"""
import re
from collections import defaultdict
from dataclasses import dataclass
from pprint import pprint
from aoc.directions import UP, DOWN, LEFT, RIGHT

REVERSE = dict(zip([UP, DOWN, LEFT, RIGHT, (0, 0)], [DOWN, UP, RIGHT, LEFT, (0, 0)]))


@dataclass
class Path:
    length: int
    end_pos: tuple[int, int]
    last_dir: tuple[int, int]


@dataclass
class Edge:
    length: int
    end_pos: tuple[int, int]


def parse(data):
    grid = data.strip().split("\n")
    start = grid[0].index("."), 0
    end = grid[-1].index("."), len(grid) - 1
    return grid, start, end


def get_possible_moves(pos, grid):
    x, y = pos
    char = grid[y][x]
    for new_dir in [UP, DOWN, LEFT, RIGHT]:
        if (
            (char == "<" and new_dir != LEFT)
            or (char == ">" and new_dir != RIGHT)
            or (char == "^" and new_dir != UP)
            or (char == "v" and new_dir != DOWN)
        ):
            continue
        dx, dy = new_dir
        nx, ny = dx + x, dy + y
        if 0 <= ny < len(grid) and grid[ny][nx] != "#":
            yield (nx, ny), new_dir


def get_crossings(grid):
    result = set()
    for y in range(len(grid)):
        for x in range(len(grid[0]) - 1):
            moves = list(get_possible_moves((x, y), grid))
            if len(moves) > 2:
                result.add((x, y))
    return result


def get_all_possible_moves(grid):
    result = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0]) - 1):
            for new_pos, new_dir in get_possible_moves((x, y), grid):
                result[(x, y)].append((new_pos, new_dir))
    return result


def explore_paths(grid, crossings, moves, start):
    result = defaultdict(list)
    stack = [(start, set(), 0, DOWN, start, 0)]
    visited_crossings = set()
    while stack:
        pos, visited, steps, last_dir, last_crossing, steps_from_crossing = stack.pop()
        visited.add(pos)
        if pos in crossings:
            if pos != last_crossing:
                # reached a crossing: discovered new path from last crossing
                result[last_crossing].append(
                    Edge(length=steps_from_crossing, end_pos=pos)
                )
            # add new starting paths
            if pos not in visited_crossings:
                for new_pos, new_dir in moves[pos]:
                    stack.append((new_pos, set(), steps + 1, new_dir, pos, 1))
            visited_crossings.add(pos)

        else:
            for new_pos, new_dir in moves[pos]:
                if (
                    new_dir != REVERSE[last_dir] and new_pos not in visited
                ):  # take one step
                    stack.append(
                        (
                            new_pos,
                            visited.copy(),
                            steps + 1,
                            new_dir,
                            last_crossing,
                            steps_from_crossing + 1,
                        )
                    )
    return result


def solve(data):
    grid, start, end = parse(data)
    max_steps = 0
    crossings = get_crossings(grid)
    crossings.add(end)
    crossings.add(start)
    moves = get_all_possible_moves(grid)
    graph = explore_paths(grid, crossings, moves, start)

    stack = [(start, set(), 0)]
    while stack:
        pos, visited, steps = stack.pop()
        visited.add(pos)
        if pos == end:
            if steps > max_steps:
                max_steps = steps
                print(max_steps)
        for edge in graph[pos]:
            if edge.end_pos not in visited:
                stack.append((edge.end_pos, visited.copy(), steps + edge.length))

    return max_steps


def solve2(data):
    data = re.sub(r"[<>v^]", ".", data)
    return solve(data)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 2250

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 6470
