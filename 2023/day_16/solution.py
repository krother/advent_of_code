"""
The Floor Will Be Lava

https://adventofcode.com/2023/day/16
"""
from aoc.directions import UP, DOWN, LEFT, RIGHT

ELEMENTS = {
    "/": {
        RIGHT: [UP],
        UP: [RIGHT],
        LEFT: [DOWN],
        DOWN: [LEFT],
    },
    "\\": {
        UP: [LEFT],
        LEFT: [UP],
        RIGHT: [DOWN],
        DOWN: [RIGHT],
    },
    ".": {
        UP: [UP],
        DOWN: [DOWN],
        LEFT: [LEFT],
        RIGHT: [RIGHT],
    },
    "-": {
        UP: [LEFT, RIGHT],
        DOWN: [LEFT, RIGHT],
        LEFT: [LEFT],
        RIGHT: [RIGHT],
    },
    "|": {
        UP: [UP],
        DOWN: [DOWN],
        LEFT: [UP, DOWN],
        RIGHT: [UP, DOWN],
    },
}


def get_new_position(position, direction):
    x, y = position
    dx, dy = direction
    return x + dx, y + dy


def get_next_char(field, new_pos):
    maxx, maxy = len(field[0]), len(field)
    nx, ny = new_pos
    if 0 <= nx < maxx and 0 <= ny < maxy:
        return field[ny][nx]


def find_best_energy(field, start_pos, start_direction):
    energized = set()
    tips = [(start_pos, start_direction)]
    visited = set()

    while tips:
        # visit each position/direction only once
        beam = tips.pop()
        position, direction = beam

        new_pos = get_new_position(position, direction)
        char = get_next_char(field, new_pos)
        if char and beam not in visited:
            for new_dir in ELEMENTS[char][direction]:
                tips.append((new_pos, new_dir))

        visited.add(beam)
        energized.add(position)

    return len(energized) - 1


def solve(data):
    field = data.strip().split("\n")
    return find_best_energy(field, (-1, 0), RIGHT)


def solve2(data):
    results = []
    field = data.strip().split("\n")
    for x in range(len(field[0])):
        results.append(find_best_energy(field, (x, -1), DOWN))
        results.append(find_best_energy(field, (x, len(field)), UP))
    for y in range(len(field)):
        results.append(find_best_energy(field, (-1, y), DOWN))
        results.append(find_best_energy(field, (len(field[0]), y), UP))

    return max(results)


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 7498

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 7846
