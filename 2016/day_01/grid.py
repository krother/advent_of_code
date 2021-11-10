
import re

VECTORS = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}

TURNS = {
    'R': {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N',
    },
    'L': {
        'N': 'W',
        'E': 'N',
        'S': 'E',
        'W': 'S',
    }
}

def turn(direction, rl):
    return TURNS[rl][direction]    

def get_steps(path):
    x, y = 0, 0
    direction = 'N'
    steps = re.findall(r'([RL])(\d+)', path)

    for leftright, dist in steps:
        direction = turn(direction, leftright)
        dx, dy = VECTORS[direction]
        for _ in range(int(dist)):
            x += dx
            y += dy
            yield x, y


def walk(path):
    *_, (x, y) = get_steps(path)
    return abs(x) + abs(y)


def walk_until_visited(path):
    visited = set()
    for x, y in get_steps(path):
        if (x, y) in visited:
            return abs(x) + abs(y)
        visited.add((x, y))


if __name__ == '__main__':
    path = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
    print('\npart 1:')
    result = walk(path)
    print(result)

    print('\npart 2:')
    result = walk_until_visited(path)
    print(result)


