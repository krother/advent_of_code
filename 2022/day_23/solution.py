"""
Unstable Diffusion

https://adventofcode.com/2022/day/23
"""
from aoc.directions import UP, DOWN, LEFT, RIGHT, UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT
from collections import Counter


VECTORS = {
    UP: [UP, UPLEFT, UPRIGHT],
    DOWN: [DOWN, DOWNLEFT, DOWNRIGHT],
    LEFT: [LEFT, UPLEFT, DOWNLEFT],
    RIGHT: [RIGHT, UPRIGHT, DOWNRIGHT]
}

def parse(data):
    elves = set()
    for y, row in enumerate(data.strip().split('\n')):
        for x, char in enumerate(row):
            if char == '#':
                elves.add((x, y))
    return elves


def has_adjacent(x, y, elves):
    """check all eight adjacent positions"""
    for dx, dy in [UP, DOWN, LEFT, RIGHT, UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT]:
        if (x + dx, y + dy) in elves:
            return True


def execute_candidate_moves(proposed):
    """move elf only if no other elf moves there"""
    count = Counter(dest for _, dest in proposed)
    return {
        dest if count[dest] == 1 else current
        for current, dest in proposed
    }

def get_candidate_move(elves, directions, x, y):
    if has_adjacent(x, y, elves):
        for d in directions:
            valid = True
            for dx, dy in VECTORS[d]:
                if (x + dx, y + dy) in elves:
                    valid = False
                    break
            if valid:
                return (x, y), (x + d[0], y + d[1])

    return (x, y), (x, y)


def move(elves, directions):
    proposed = [get_candidate_move(elves, directions, *pos) for pos in elves]
    return execute_candidate_moves(proposed)


def get_size(elves):
    xmin = min(x for x, y in elves)
    ymin = min(y for x, y in elves)
    xmax = max(x for x, y in elves)
    ymax = max(y for x, y in elves)
    return (xmax - xmin + 1) * (ymax - ymin + 1) - len(elves)


def solve(data, rounds):
    elves = parse(data)
    directions = [UP, DOWN, LEFT, RIGHT]
    for i in range(rounds):
        new_elves = move(elves, directions)
        if elves == new_elves:
            return i + 1
        elves = new_elves
        x = directions.pop(0)
        directions.append(x)
    
    return get_size(elves)


def solve2(data):
    return solve(data, rounds=1000)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, rounds=10)
    print(f'Example 1: {result}')
    assert result == 3684

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 862