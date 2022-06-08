"""
Day 18: Duet

https://adventofcode.com/2017/day/18

"""
import string
from collections import defaultdict

def parse_arg(token, reg):
    if token in string.ascii_letters:
        return reg[token]
    return int(token)


def set_cmd(tokens, reg, stack):
    reg[tokens[1]] = parse_arg(tokens[2], reg)

def add_cmd(tokens, reg, stack):
    reg[tokens[1]] += parse_arg(tokens[2], reg)

def mul_cmd(tokens, reg, stack):
    reg[tokens[1]] *= parse_arg(tokens[2], reg)

def mod_cmd(tokens, reg, stack):
    reg[tokens[1]] %= parse_arg(tokens[2], reg)

def snd_cmd(tokens, reg, stack):
    stack.append(parse_arg(tokens[1], reg))

def rcv_cmd(tokens, reg, stack):
    if parse_arg(tokens[1], reg) != 0:
        reg['output'] = stack[-1]

def jgz_cmd(tokens, reg, stack):
    if parse_arg(tokens[1], reg) > 0:
        return parse_arg(tokens[2], reg)


COMMANDS = {
    'snd': snd_cmd,
    'set': set_cmd,
    'add': add_cmd,
    'mul': mul_cmd,
    'mod': mod_cmd,
    'rcv': rcv_cmd,
    'jgz': jgz_cmd,
}

def solve(data):
    reg = defaultdict(int)
    stack = []
    instructions = [row.strip() for row in data.strip().split('\n')]
    pc = 0
    while pc < len(instructions) and 'output' not in reg:
        row = instructions[pc]
        cmd = row[:3]
        tokens = row.split()
        pc += COMMANDS[cmd](tokens, reg, stack) or 1

    return reg, stack


def solve2(data):
    return data

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    #result = solve2(input_data)
    #print(f'Example 2: {result}')
