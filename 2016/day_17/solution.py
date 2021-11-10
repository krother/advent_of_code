"""
Day 17: Two Steps Forward

https://adventofcode.com/2016/day/17
"""
from collections import deque
from hashlib import md5
import re


START_POS = (0, 0)
END_POS = (3, 3)

VECTORS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}


def get_hash_prefix(passcode, path):
    s = passcode + path
    m = md5(s.encode()).hexdigest()
    return m[:4]

def get_open_doors(prefix):
    for char, direction in zip(prefix, 'UDLR'):
        if char in 'bcdef':
            yield direction

def add_positions(pos, direction):
    x, y = pos
    xd, yd = VECTORS[direction]
    x += xd
    y += yd
    if (0 <= x <= 3) and (0 <= y <= 3):
        return x, y

def get_moves(passcode, pos, path):
    result = []
    prefix = get_hash_prefix(passcode, path)
    for direction in get_open_doors(prefix):
        new_pos = add_positions(pos, direction)
        if new_pos:
            result.append((new_pos, path + direction))
    return result


def solve(passcode, shortest=True):
    """breadth-first graph search"""
    p = START_POS, ''
    paths = deque([p])
    longest = ''

    while paths:
        pos, path = paths.popleft()
        for new_pos, new_path in get_moves(passcode, pos, path):
            if new_pos == END_POS:
                if shortest:
                    return new_path
                elif len(new_path) > len(longest):
                    longest = new_path
            else:
                paths.append((new_pos, new_path))
    
    return longest


if __name__ == '__main__':

    # part 1
    result = solve('awrkjxxr')
    print(f'Example 1: {result}')

    # part 2
    result = len(solve('awrkjxxr', shortest=False))
    print(f'Example 2: {result}')
