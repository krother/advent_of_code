"""Day 22: Grid Computing

https://adventofcode.com/2016/day/22

"""
import re
from collections import deque
from copy import deepcopy

VECTORS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Grid:

    def __init__(self, data):
        self.xmax = 0
        self.ymax = 0
        self.moves = 0
        self.zeropos = None

        nodes = parse_all_nodes(data)
        for x, y, _, _ in nodes:
            if x > self.xmax:
                self.xmax = x
            if y > self.ymax:
                self.ymax = y

        self.grid = [['.'] * (self.xmax+1) for _ in range(self.ymax+1)]
        self.grid[0][self.xmax] = 'G'

        # find position of empty tile, we assume there is exactly one
        zerosize = 0
        for x, y, used, avail in nodes:
            if used == 0:
                assert zerosize == 0
                zerosize = avail
                self.grid[y][x] = '_'
                self.zeropos = (x, y)

        # identify not movable tiles
        for x, y, used, _ in nodes:
            if used > zerosize:
                self.grid[y][x] = '#'

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def get_moves(self):
        """check all moves from A to B"""
        zx, zy = self.zeropos
        for dx, dy in VECTORS:
            newx, newy = zx + dx, zy + dy
            if (
                0 <= newx <= self.xmax and 
                0 <= newy <= self.ymax and
                self.grid[newy][newx] != '#'
            ):
                g = deepcopy(self)
                g.grid[newy][newx] = '_'
                g.grid[zy][zx] = self.grid[newy][newx]
                g.zeropos = (newx, newy)
                g.moves += 1
                yield g


def parse_row(node):
    x, y, used, avail = map(int, re.findall(r'x(\d+)-y(\d+).+\d+T\s+(\d+)T\s+(\d+)T', node)[0])
    return x, y, used, avail

def parse_all_nodes(data):
    return [parse_row(node) for node in data. strip().split('\n') if node.startswith('/dev/')]

def is_viable_pair(node_a, node_b):
    _, _, used, _ = node_a
    _, _, _, avail = node_b
    if node_a != node_b and used > 0 and used <= avail:
        return True

def count_pairs(data):
    result = 0
    nodes = parse_all_nodes(data)

    for node_a in nodes:
        for node_b in nodes:
            if is_viable_pair(node_a, node_b):
                result += 1

    return result

def parse_grid(data):
    grid = Grid(data)
    return grid


def solve(data):
    grid = parse_grid(data)
    candidates = deque([grid])
    visited = set()
    print()
    print(str(grid))
    while candidates:
        print(len(candidates))
        grid = candidates.popleft()
        if grid.grid[0][0] == 'G':
            print()
            print(str(grid))
            return grid.moves
        for grid in grid.get_moves():
            s = str(grid)
            if s not in visited:
                candidates.append(grid)
                visited.add(s)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = count_pairs(input_data)
    print(f'Example 1: {result}')

    result = solve(input_data)
    print(f'Example 2: {result}')
