
import re

def parse(fn):
    data = []
    for line in open(fn):
        ins, num = line.strip().split()
        num = int(num)
        data.append([ins, num])
    return data

def swap(instructions, i):
    if instructions[i][0] == 'nop':
        instructions[i][0] = 'jmp'
    elif instructions[i][0] == 'jmp':
        instructions[i][0] = 'nop'

def run(instructions):
    acc = 0
    prog = 0
    visited = set()
    found = True
    while prog < len(instructions):
        if prog in visited:
            found = False
            break
        visited.add(prog)
        ins, num = instructions[prog]
        if ins == 'acc':
            acc += num
            prog += 1
        if ins == 'jmp':
            prog += num
        if ins == 'nop':
            prog += 1
    return found, acc


def solve(fn):
    instructions = parse(fn)
    for i in range(len(instructions)):
        instructions = parse(fn)
        swap(instructions, i)
        found, acc = run(instructions)
        if found:
            return acc

assert solve('input2.txt') == 8

print(solve('input_big.txt'))
