"""
Day 7: Some Assembly Required

https://adventofcode.com/2015/day/7
"""
import re
from collections import deque

MAX = 2 ** 16 - 1

def store(wires, value, dest):
    if dest not in wires:
        wires[dest] = int(value)

def copy(wires, source, dest):
    wires[dest] = wires[source]

def bit_and(wires, a, b, dest):
    wires[dest] = wires[a] & wires[b]

def bit_and_num(wires, a, b, dest):
    wires[dest] = int(a) & wires[b]

def bit_or(wires, a, b, dest):
    wires[dest] = wires[a] | wires[b]

def bit_not(wires, a, dest):
    wires[dest] = MAX ^ wires[a]

def lshift(wires, a, steps, dest):
    wires[dest] = MAX & (wires[a] << int(steps))

def rshift(wires, a, steps, dest):
    wires[dest] = wires[a] >> int(steps)

INSTRUCTIONS = [
    (r'^(\d+) -> (\w+)', store),
    (r'^([a-z]+) -> (\w+)', copy),
    (r'^([a-z]+) AND (\w+) -> (\w+)', bit_and),
    (r'^(\d+) AND (\w+) -> (\w+)', bit_and_num),
    (r'^(\w+) OR (\w+) -> (\w+)', bit_or),
    (r'^NOT (\w+) -> (\w+)', bit_not),
    (r'^(\w+) LSHIFT (\d+) -> (\w+)', lshift),
    (r'^(\w+) RSHIFT (\d+) -> (\w+)', rshift),
]

def run(data, **kwargs):
    wires = kwargs or {}
    prog = deque(data.strip().split('\n'))
    while prog:
        line = prog.popleft()
        for pattern, func in INSTRUCTIONS:
            args = re.findall(pattern, line)
            if args:
                try:
                    func(wires, *args[0])
                except KeyError:
                    prog.append(line)
    return wires

def solve(data):
    wires = run(data)
    return wires['a']

def solve2(data):
    a = solve(data)
    wires = run(data, b=a)
    return wires['a']

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
