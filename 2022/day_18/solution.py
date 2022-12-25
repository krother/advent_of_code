"""
Boiling Boulders

https://adventofcode.com/2022/day/18
"""
DIRECTIONS = [
    (0, 0, +1),
    (0, 0, -1),
    (0, +1, 0),
    (0, -1, 0),
    (+1, 0, 0),
    (-1, 0, 0),
]
def parse(data):
    return set(
        tuple(int(p) for p in line.split(','))
        for line in data.strip().split('\n')
    )

def get_adjacent(x, y, z):
    for dx, dy, dz in DIRECTIONS:
        yield x + dx, y + dy, z + dz


def solve(data):
    drops = parse(data)
    surface = 0
    for drop in drops:
        for pos in get_adjacent(*drop):
            if pos not in drops:
                surface += 1
    return surface


def get_all_positions(drops):
    maxx = max([x for x, y, z in drops])
    maxy = max([y for x, y, z in drops])
    maxz = max([z for x, y, z in drops])
    
    to_check = []
    for x in range(-1, maxx + 2):
        for y in range(-1, maxy + 2):
            for z in range(-1, maxz + 2):
                pos = x, y, z
                if pos not in drops:
                    to_check.append(pos)
    return to_check


def solve2(data):
    drops = parse(data)
    to_check = get_all_positions(drops)
    
    exterior = set()
    changes = True
    while changes:
        changes = False
        new = []
        for pos in to_check:
            x, y, z = pos
            if x == 0 or y == 0 or z == 0:
                exterior.add(pos)
                changes = True

            for adj_pos in get_adjacent(*pos):
                if adj_pos in exterior:
                    exterior.add(pos)
                    changes = True
                    break
            if pos not in exterior:
                new.append(pos)
        to_check = new
    print(len(exterior))

    surface = 0
    for drop in drops:
        for pos in get_adjacent(*drop):
            if pos in exterior:
                surface += 1
    return surface


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 4320

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 2456
