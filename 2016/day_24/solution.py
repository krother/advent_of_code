"""Day 24: Air Duct Spelunking

https://adventofcode.com/2016/day/24
"""
"""
Maze Kata:

You have a maze given as a string:

##y##
#...#
##x##
#####

You start in the position marked with an x.
Find the way to the exit y.
Return the length of the shortest path.
"""
import re
from collections import deque
from itertools import permutations, combinations

class MazeException(Exception): pass

WALKABLE = '.0123456789'


class Maze:

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, maze) -> None:
        self.maze = maze.strip().split('\n')
        self.start = None
        self.end = None

    def __iter__(self):
        for y, row in enumerate(self.maze):
            for x, char in enumerate(row):
                yield (x, y), char

    def validate_maze(self):
        if self.end is None:
            raise MazeException("the maze has no exit")
        if self.start is None:
            raise MazeException("the maze has no entrance")

    def find_position(self, elem):
        for pos, char in self:
            if char == elem:
                return pos

    def find_adjacent_positions(self, position):
        possible_moves = set()
        x, y = position
        for dx, dy in self.moves:
            x_to_check, y_to_check = x + dx, y + dy
            if self.maze[y_to_check][x_to_check] in WALKABLE:
                possible_moves.add((x_to_check, y_to_check))
        return possible_moves


def find_shortest_path(maze, start=0, end=1, max_iter=1000):
    """Breadth-first graph search algorithm"""
    maze = Maze(maze)
    maze.start = maze.find_position(str(start))
    maze.end = maze.find_position(str(end))
    maze.validate_maze()

    cand = (maze.start, 0)
    candidates = deque([cand])  # queue of candidates (position, path length)

    visited = {maze.start}      # set to make sure no place is visited twice

    while candidates:
        pos, steps = candidates.popleft()  # gets oldest candidate (the one with the shortest #steps)
        if pos == maze.end:
            return steps
        for new_pos in maze.find_adjacent_positions(pos):
            if new_pos not in visited and steps < max_iter:
                candidates.append((new_pos, steps+1))
                visited.add(new_pos)
        
    raise MazeException("maximum iterations exceeded")


def get_all_paths(maze, n=4):
    result = {}
    for i, j in combinations(range(n), 2):
        result[(i, j)] = find_shortest_path(maze, i, j)
    return result


def solve(maze):
    """shortest path in a TSP"""
    n = len(re.findall(r'\d', maze))
    path_lengths = get_all_paths(maze, n)
    shortest = None
    for path in permutations(range(1, n)):
        path = list(path) + [0]
        prev = 0
        dist = 0
        for point in path:
            wp1, wp2 = sorted((prev, point))
            dist += path_lengths[(wp1, wp2)]
            prev = point
        if shortest is None or dist < shortest:
            shortest = dist
        print(path, dist)
    return shortest



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
