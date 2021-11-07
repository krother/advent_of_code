
import re
import numpy as np

def create_array(xsize, ysize):
    return np.array([list('.' * xsize)] * ysize)

def array_to_string(a):
    return '\n'.join([''.join(row) for row in a])

def rect(a, x, y):
    a[:y, :x] = '#'

def rotate_col(a, x, times):
    for _ in range(times):
        last = a[-1, x]
        a[1:, x] = a[:-1, x]
        a[0, x] = last

def rotate_row(a, y, times):
    for _ in range(times):
        last = a[y, -1]
        a[y, 1:] = a[y, :-1]
        a[y, 0] = last

def parse(instructions):
    for cmd in instructions.split('\n'):
        cmd, x, y = re.findall(r'(\D+)\W(\d+)\D+(\d+)', cmd)[0]
        yield cmd, int(x), int(y)

COMMANDS = {
    'rect': rect,
    'rotate column x': rotate_col,
    'rotate row y': rotate_row
}

def execute(instructions, a):
    for cmd, x, y in parse(instructions):
        COMMANDS[cmd](a, x, y)

def display(instructions, xsize=7, ysize=3):
    a = create_array(xsize, ysize)
    execute(instructions, a)
    return array_to_string(a)

if __name__ == '__main__':
    instructions = open('input.txt').read().strip()
    a = display(instructions, 50, 6)
    print(a.count('#'))
    print(a)
