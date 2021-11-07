
import re
from pprint import pprint
from math import sin, cos, radians

"""
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

"""
def solve(fn):
    facing = 0
    x = 0
    y = 0
    for line in open(fn):
        char = line[0]
        m = int(line.strip()[1:])
        if char == 'L':
            facing += m
        elif char == 'R':
            facing -= m
        elif char == 'E':
            x += m
        elif char == 'W':
            x -= m
        elif char == 'N':
            y += m
        elif char == 'S':
            y -= m
        elif char == 'F':
            x += cos(radians(facing)) * m
            y += sin(radians(facing)) * m
        print(char,m, x, y)
    return abs(x) + abs(y)
        


assert solve('input.txt')  == 25

print(solve('input_big.txt'))
