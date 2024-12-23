"""
Day 15: Warehouse Woes

https://adventofcode.com/2024/day/15
"""
from aoc import DIRECTIONS4
from dataclasses import dataclass


MOVES = dict(zip("^>v<", DIRECTIONS4))
BOXES = "O[]"


@dataclass
class Box:
    positions: list[tuple[int, int]]

    def push(self, grid, move):
        new = []
        for p in self.positions:
            newpos = get_next_position(p, move)
            new.append(newpos)
            grid.push_boxes(newpos, move)
        self.positions = new


class SmallBox(Box):
    def can_be_moved(self, grid, move):
        newpos = get_next_position(self.positions[0], move)
        return grid.check_move(newpos, move)


class BigBox(Box):
    def can_be_moved(self, grid, move):
        new1 = get_next_position(self.positions[0], move)
        new2 = get_next_position(self.positions[1], move)
        if new1 == self.positions[1]:
            return grid.check_move(new2, move)
        elif new2 == self.positions[0]:
            return grid.check_move(new1, move)
        return grid.check_move(new1, move) and grid.check_move(new2, move)


class Grid:
    def __init__(self, grid):
        self.walls = set()
        self.boxes = []
        for y, row in enumerate(grid.split("\n")):
            for x, cell in enumerate(row):
                pos = x, y
                if cell == "#":
                    self.walls.add(pos)
                elif cell == "O":
                    self.boxes.append(SmallBox([pos]))
                elif cell == "[":
                    self.boxes.append(BigBox([pos, get_next_position(pos, (1, 0))]))

    def get_box_positions(self):
        result = {}
        for box in self.boxes:
            for p in box.positions:
                result[p] = box
        return result

    def calc_gps(self):
        total = 0
        for box in self.boxes:
            x, y = box.positions[0]
            total += 100 * y + x
        return total

    def check_move(self, pos, move):
        if pos in self.walls:
            return False
        if pos in self.boxcache:
            box = self.boxcache[pos]
            if not box.can_be_moved(self, move):
                return False
        return True

    def push_boxes(self, pos, move):
        if pos in self.boxcache:
            box = self.boxcache[pos]
            for p in box.positions:
                del self.boxcache[p]  # push each box once
            box.push(self, move)

    def move_player(self, pos, move):
        self.boxcache = self.get_box_positions()
        newpos = get_next_position(pos, move)
        if self.check_move(newpos, move):
            self.push_boxes(newpos, move)
            return newpos
        return pos


def get_next_position(pos, move):
    x, y = pos
    dx, dy = move
    return x + dx, y + dy


def find_start_position(grid):
    for y, row in enumerate(grid.split("\n")):
        for x, cell in enumerate(row):
            if cell == "@":
                return x, y


def parse(data):
    grid, moves = data.strip().split("\n\n")
    start = find_start_position(grid)
    grid = Grid(grid)
    moves = moves.replace("\n", "")
    return grid, moves, start


def solve(data):
    grid, moves, pos = parse(data)
    for m in moves:
        pos = grid.move_player(pos, MOVES[m])
    return grid.calc_gps()


def solve2(data):
    data = (
        data.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    )
    return solve(data)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")
    assert result == 1318523

    result = solve2(input_data)
    print(f"Example 2: {result}")
    assert result == 1337648
