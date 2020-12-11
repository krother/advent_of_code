
import re
from pprint import pprint

def solve(fn):
    data = [int(x) for x in open(fn)]
    data.sort()
    # [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]

    ones = 0
    threes = 1
    prev = 0
    for d in data:
        diff = d - prev
        prev = d
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        else:
            print(diff)
    return (ones, threes)

assert solve('input.txt') == (7, 5)

assert solve('input2.txt')  == (22, 10)

o, t  = solve('input_big.txt')
print(o, t)
print(o*t)
