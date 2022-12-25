"""
I Heard You Like Registers

https://adventofcode.com/2017/day/8

"""
from collections import defaultdict


def calc(data):
    all_time_max = 0

    registers = defaultdict(int)
    for instruction in data.strip().split('\n'):
        var, op, arg, _, ctrl, cmp, exp = instruction.split()
        result = eval(f"registers['{ctrl}'] {cmp} {exp}")
        arg = int(arg)
        if op == 'dec':
            arg *= -1
        if result: 
            registers[var] += arg
        all_time_max = max(all_time_max, *registers.values())

    return max(registers.values()), all_time_max

def solve(data):
    last_max, _ = calc(data)
    return last_max


def solve2(data):
    _, all_time_max = calc(data)
    return all_time_max


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
