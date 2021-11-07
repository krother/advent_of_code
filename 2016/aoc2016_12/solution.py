"""Leonardos Monorail

https://adventofcode.com/2016/day/12

- four registers (a, b, c, and d) 
  that start at 0 
  and can hold any integer

- cpy x y copies x (either an integer or the value of a register) into register y.
- inc x increases the value of register x by one.
- dec x decreases the value of register x by one.
- jnz x y jumps to an instruction y away 
  (positive means forward; negative means backward), 
  but only if x is not zero.

The jnz instruction moves relative to itself: 
    an offset of -1 would continue at the previous instruction, 
    while an offset of 2 would skip over the next instruction.
"""
import re
from collections import OrderedDict

CPY = r'cpy (-?\d+|[abcd])\s+(\w)'
INC = r'inc (\w)'
DEC = r'dec (\w)'
JNZ = r'jnz (-?\d+|[abcd]) (-?\d+)'

def parse_reg_or_int(r, regs):
    return int(r) if (r.isnumeric() or r.startswith('-')) else regs[r]

def execute(line, regs):
    for r1, r2 in re.findall(CPY, line):
        regs[r2] = parse_reg_or_int(r1, regs)

    for r in re.findall(INC, line):
        regs[r] += 1

    for r in re.findall(DEC, line):
        regs[r] -= 1

    for r1, r2 in re.findall(JNZ, line):
        val = parse_reg_or_int(r1, regs)
        steps = int(r2)
        assert r2 != 0
        if val != 0:
            return steps

    return 1


def solve(data, ignition=0):
    regs = OrderedDict({
        'a': 0,
        'b': 0,
        'c': ignition,
        'd': 0
    })

    counter = 0
    lines = data.strip().split('\n')
    while counter < len(lines):
        counter += execute(lines[counter], regs)

    return tuple(regs.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve(input_data, ignition=1)
    print(f'Example 2: {result}')
