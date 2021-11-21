"""Day 23: Safe Cracking

https://adventofcode.com/2016/day/23

tgl x toggles the instruction x away (pointing at instructions like jnz does: positive means forward; negative means backward):

    For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
    For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
    The arguments of a toggled instruction are not affected.
    If an attempt is made to toggle an instruction outside the program, nothing happens.
    If toggling produces an invalid instruction (like cpy 1 2) and an attempt is later made to execute that instruction, skip it instead.
    If tgl toggles itself (for example, if a is 0, tgl a would target itself and become inc a), the resulting instruction is not executed until the next time it is reached.

"""
import re
from collections import OrderedDict


CPY = r'cpy (-?\d+|[abcd])\s+(\w)'
INC = r'inc (\w)'
DEC = r'dec (\w)'
JNZ = r'jnz (-?\d+|[abcd]) (-?\d+|[abcd])'
TGL = r'tgl (\w)'
OUT = r'out (\w)'

TGL_REPLACE = [
    ('inc', 'dec'),
    ('dec', 'inc'),
    ('tgl', 'inc'),
    ('cpy', 'jnz'),
    ('jnz', 'cpy'),
    ('out', 'out'),
]

output = []

def parse_reg_or_int(r, regs):
    return int(r) if (r.isnumeric() or r.startswith('-')) else regs[r]

def execute(lines, counter, regs):
    line = lines[counter]
    for r1, r2 in re.findall(CPY, line):
        regs[r2] = parse_reg_or_int(r1, regs)

    for r in re.findall(INC, line):
        regs[r] += 1

    for r in re.findall(DEC, line):
        regs[r] -= 1

    for r1, r2 in re.findall(JNZ, line):
        val = parse_reg_or_int(r1, regs)
        steps = parse_reg_or_int(r2, regs)
        assert r2 != 0
        if val != 0:
            return steps

    for r in re.findall(TGL, line):
        r = parse_reg_or_int(r, regs)
        modpos = counter + r
        if modpos < len(lines):
            cmd = lines[modpos]
            for old, new in TGL_REPLACE:
                if old in cmd:
                    cmd = cmd.replace(old, new)
                    break
            lines[modpos] = cmd

    for r in re.findall(OUT, line):
        r = parse_reg_or_int(r, regs)
        output.append(r)
    return 1


def solve(data, astart=0):
    regs = OrderedDict({
        'a': astart,
        'b': 0,
        'c': 0,
        'd': 0
    })
    global output
    output = []

    counter = 0
    lines = data.strip().split('\n')
    while counter < len(lines) and len(output) < 59:
        counter += execute(lines, counter, regs)

    s = ''.join(map(str, output))
    print(f"{astart:6}:", s[:12][::-1])
    assert s[:12] == s[12:24]
    if s.startswith('010101010101') or s.startswith('101010101010'):
        0 / 0

    return tuple(regs.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    i = 0
    while True:
        result = solve(input_data, astart=i)
        i += 1
    #print(f'Example 1: {result}')

    #result = solve(input_data, a=12)
    #print(f'Example 2: {result}')
