
import re
from pprint import pprint
from math import sin, cos, radians

"""
    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left
             (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the 
          ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of 
          times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. 
The waypoint is relative to the ship; that is, if the ship moves, 
the waypoint moves with it.

For example, using the same instructions as above:


"""
def solve(fn):
    x = 0
    y = 0
    wx, wy = 10, 1
    for line in open(fn):
        char = line[0]
        m = int(line.strip()[1:])
        if char == 'L':
            assert m in (90, 180, 270, 0)
            nwy = round(sin(radians(m)) * wx + cos(radians(m)) * wy)
            nwx = round(cos(radians(-m)) * wx + sin(radians(-m)) * wy)
            wx, wy = nwx, nwy

        elif char == 'R':
            assert m in (90, 180, 270, 0)
            nwy = round(sin(radians(-m)) * wx + cos(radians(-m)) * wy)
            nwx = round(cos(radians(m)) * wx + sin(radians(m)) * wy)
            wx, wy = nwx, nwy
            
        elif char == 'E':
            wx += m
        elif char == 'W':
            wx -= m
        elif char == 'N':
            wy += m
        elif char == 'S':
            wy -= m
        elif char == 'F':
            x += wx * m
            y += wy * m
        print(char,m, wx, wy)
    return abs(x) + abs(y)
        


assert solve('input.txt')  == 286
solve('input2.txt')
result = solve('input_big.txt')
assert result == 145117
