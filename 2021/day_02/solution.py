"""going deeper

https://adventofcode.com/2021/day/2
"""
import re
from functools import reduce


def parse_commands(data):
    for cmd, num in re.findall(r'(\w+)\s(\d+)', data):
        num = int(num)
        yield cmd, num


# reduce-based solution (wordier)
def execute1(position, command):
    hori, depth = position
    cmd, num = command
    if cmd == 'forward':
        return hori + num, depth
    if cmd == 'up':
        return hori, depth - num
    if cmd == 'down':
        return hori, depth + num
    

def solve(data):
    hori, depth = reduce(execute1, parse_commands(data), (0, 0))
    return hori * depth

# standard solution
def solve(data):
    hori, depth = 0, 0
    for cmd, num in parse_commands(data):
        if cmd == 'forward':
            hori += num
        if cmd == 'up':
            depth -= num
        if cmd == 'down':
            depth += num
        
    return hori * depth


def solve2(data):
    hori, depth, aim = 0, 0, 0
    for cmd, num in parse_commands(data):
        if cmd == 'forward':
            hori += num
            depth += aim * num
        if cmd == 'up':
            aim -= num
        if cmd == 'down':
            aim += num
        
    return hori * depth



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
