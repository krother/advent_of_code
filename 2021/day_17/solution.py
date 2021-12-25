"""Trick Shot

https://adventofcode.com/2021/day/17


    The probe's x position increases by its x velocity.
    The probe's y position increases by its y velocity.
    Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    Due to gravity, the probe's y velocity decreases by 1.

for part I the triangle sum also works:
    max_height = ymin * (ymin - 1) // 2 
"""
import re

MISS = -1

def parse(data):
    xmin, xmax, ymin, ymax = map(int, re.findall(r'-?\d+', data))
    return xmin, xmax, ymin, ymax

def shot(dx, dy, target):
    xmin, xmax, ymin, ymax = target
    x, y = 0, 0
    highest = 0
    while True:
        x += dx
        y += dy
        if dx > 0:
            dx -= 1
        dy -= 1
        if y > highest:
            highest = y
        if xmin <= x <= xmax and ymin <= y <= ymax:
            # target hit
            return highest
        if (x < xmin or x > xmax) and dx == 0:
            return MISS
        if y < ymin and dy < 0:
            return MISS
        

def solve(data):
    """
    dx has to be positive
    dx cannot be larger than xmax of target
    dy cannot be smaller than ymin of target
    dy cannot be higher than abs(ymin) of target,
       because the flight is a parabola;
       the probe returns to y=0 after a number
       of steps equal to dy*2, 
       so it hits y=0 with velocity -dy
    """
    target = parse(data)
    best = MISS
    hits = 0
    for dx in range(1, 130):
        for dy in range(-150, 151):
            highest = shot(dx, dy, target)
            if highest > best:
                best = highest
            if highest != MISS:
                hits += 1

    return best, hits


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    best, hits = solve(input_data)
    print(f'Example 1: {best}')  # 11175
    print(f'Example 2: {hits}')  # 3540 
