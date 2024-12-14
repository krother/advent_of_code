"""


https://adventofcode.com/2024/day/12
"""
from aoc import is_on_grid, DIRECTIONS4
from itertools import product


class Grid:
    def __init__(self, data):
        self.grid = data.strip().split("\n")

    def get_total_price(self, sides):
        visited = set()
        price = 0
        for x, y in product(range(len(self.grid[0])), range(len(self.grid))):
            if (x, y) not in visited:
                price += self.walk_area(x, y, visited, sides)
        return price

    def walk_area(self, x, y, seen, sides=False):
        char = self.grid[y][x]
        area = 0
        edges = set()
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if (x, y) not in seen:
                seen.add((x, y))
                area += 1
                for dx, dy in DIRECTIONS4:
                    nx, ny = x + dx, y + dy
                    if (
                        is_on_grid(x=nx, y=ny, grid=self.grid)
                        and self.grid[ny][nx] == char
                    ):
                        stack.append((nx, ny))
                    else:
                        edges.add((x, y, (dx, dy)))

        if sides:
            return area * count_sides(edges)

        return area * len(edges)


def on_same_side(e1, e2):
    x1, y1, d1 = e1
    x2, y2, d2 = e2
    dx, dy = d1
    return (x1 == x2 + dy and y1 == y2 and d1 == d2) or (
        x1 == x2 and y1 == y2 + dx and d1 == d2
    )


def merge_groups(groups):
    for g1, g2 in product(groups, groups):
        if g1 is g2:
            continue
        for e1, e2 in product(g1, g2):
            if on_same_side(e1, e2):
                g1.extend(g2)
                groups.remove(g2)
                return


def count_sides(edges):
    groups = [[e] for e in edges]
    old_length = 0
    while len(groups) != old_length:
        old_length = len(groups)
        merge_groups(groups)
    return len(groups)


def solve(data, sides=False):
    grid = Grid(data)
    return grid.get_total_price(sides)


def solve2(data):
    return solve(data, True)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 1344578

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 814302
