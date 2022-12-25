"""
Blizzard Basin

https://adventofcode.com/2022/day/24
"""
import re

import numpy as np

from aoc.priority_queue import PriorityQueue
from aoc.directions import UP, DOWN, LEFT, RIGHT

UP_BIT, DOWN_BIT, LEFT_BIT, RIGHT_BIT = 2, 4, 8, 16
CHARS = dict(zip('.#^v<>', (0, 1, UP_BIT, DOWN_BIT, LEFT_BIT, RIGHT_BIT)))
REV_CHARS = dict(zip((0, 1, UP_BIT, DOWN_BIT, LEFT_BIT, RIGHT_BIT), '.#^v<>'))
DIRECTIONS = dict(zip('^v<>', (UP, DOWN, LEFT, RIGHT)))
WAIT = 0, 0


class BlizzardCache:

    def __init__(self, grid):
        self.grid = grid
        self.cycle_time = self.get_cycle_time()
        self.cache = self.create_cache()
        print(f'\nmaze with cycle time: {self.cycle_time}')
        assert self.cycle_time == len(self.cache)

    def get_cycle_time(self):
        cy, cx = self.grid.shape[0] - 2, self.grid.shape[1] - 2
        if cx % 10 == 0:
            return cx // 10 * cy
        else:
            return cx * cy
        
    def is_free(self, x, y, minute):
        key = minute % self.cycle_time
        return self.cache[key][y][x] == 0

    def create_cache(self):
        cache = {
            0: self.grid
        }
        a = self.grid
        for i in range(1, self.cycle_time):
            a = a.copy()
            # move blizzards
            bup = a & UP_BIT
            a ^= bup
            a[1:-2, :] |= bup[2:-1,:]
            a[-2, :] |= bup[1,:]

            bdown = a & DOWN_BIT
            a ^= bdown
            a[2:-1, :] |= bdown[1:-2,:]
            a[1, :] |= bdown[-2,:]

            bleft = a & LEFT_BIT
            a ^= bleft
            a[:, 1:-2] |= bleft[:, 2:-1]
            a[:, -2] |= bleft[:, 1]

            bright = a & RIGHT_BIT
            a ^= bright
            a[:, 2:-1] |= bright[:, 1:-2]
            a[:, 1] |= bright[:, -2]
        
            cache[i] = a
        
        return cache


class Maze:

    def __init__(self, grid, pos, target, moves=0):
        self.grid = grid
        self.pos = pos
        self.target = target
        self.moves = moves

    def target_reached(self):
        x, y, _ = self.pos
        return (x, y) == self.target
    
    def copy(self):
        return Maze(self.grid, self.pos, self.target, self.moves)

    def get_moves(self):
        for direction in UP, DOWN, LEFT, RIGHT, WAIT:
            cand = self.copy()
            if cand.move(direction):
                yield cand

    def move(self, direction):
        self.moves += 1
        x, y, _ = self.pos
        dx, dy = direction
        x, y = x + dx, y + dy
        if y < 0 or y >= self.grid.grid.shape[0]:
            return False

        if self.grid.is_free(x, y, self.moves):
            self.pos = x, y, self.moves % self.grid.cycle_time
            return True


def parse(data):
    grid = data.strip().split('\n')
    start = grid[0].index('.'), 0, 0
    target = grid[-1].index('.'), len(grid) - 1
    bc = BlizzardCache(np.array([
        [CHARS[c] for c in row]
        for row in grid
    ], np.uint8)
    )
    return Maze(bc, start, target)


def find_path(maze):
    pq = PriorityQueue()
    pq.add_task(maze, priority=0)
    visited = set()
    while pq:
        maze = pq.pop_task()
        for cand in maze.get_moves():
            if cand.target_reached():
                return cand
            if cand.pos not in visited:
                pq.add_task(cand, priority=cand.moves)
                visited.add(cand.pos)
    assert False

def solve(data):
    maze = parse(data)
    result = find_path(maze)
    return result.moves

def solve2(data):
    maze = parse(data)
    start = maze.pos[:2]
    end = maze.target
    maze = find_path(maze)
    maze.target = start
    maze = find_path(maze)
    maze.target = end
    result = find_path(maze)
    return result.moves


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
