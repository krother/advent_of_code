"""
Treetop Tree House

https://adventofcode.com/2022/day/8
"""
from functools import reduce

from aoc.directions import UP, DOWN, LEFT, RIGHT
from aoc.parsers import parse_2d_numbers


def is_inside_grid(x, y, grid):
    return x > -1 and y > -1 and x < len(grid[0]) and y < len(grid)


def get_trees_to_border(x, y, grid, direction):
    """Returns tree sizes after start position until border"""
    x += direction[0]
    y += direction[1]
    while is_inside_grid(x, y, grid):
        yield grid[y][x]
        x += direction[0]
        y += direction[1]


def is_tree_visible(x, y, grid):
    height = grid[y][x]
    for direction in [UP, DOWN, LEFT, RIGHT]:
        visible = True
        for tree in get_trees_to_border(x, y, grid, direction):
            if tree >= height:
                visible = False
                break

        if visible:
            return True


def count_visible_trees(x, y, grid, direction):
    height = grid[y][x]
    trees = 0
    for tree in get_trees_to_border(x, y, grid, direction):
        trees += 1
        if tree >= height:
            return trees
    return trees


def solve(data):
    count = 0
    grid = parse_2d_numbers(data)
    for y, row in enumerate(grid):
        for x, height in enumerate(row):
            if is_tree_visible(x, y, grid):
                count += 1
    return count


def solve2(data):
    bestscore = 0
    grid = parse_2d_numbers(data)
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            scores = [
                count_visible_trees(x, y, grid, direction)
                for direction in [UP, DOWN, LEFT, RIGHT]
            ]
            score = reduce(lambda a, b: a*b, scores)
            bestscore = max(bestscore, score)

    return bestscore


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 1851

    result = solve2(input_data)
    print(f"Example 2: {result}")
    assert result == 574080
