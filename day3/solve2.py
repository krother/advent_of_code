"""
quick implementation to solve the real thing
"""
from functools import reduce

forest = open('input.txt').read().strip().split('\n')
width = len(forest[0])
height = len(forest)

def check_slope(slope):
    x, y = 0, 0
    dx, dy = slope
    trees = 0

    while y < height - 1:
        x += dx
        y += dy
        if x >= width:
            x -= width
        if forest[y][x] == '#':
            trees += 1
    return trees

# part 1
print(check_slope((3, 1)))

# part 2
SLOPES = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(reduce(lambda a,b:a*b, map(check_slope, SLOPES)))
