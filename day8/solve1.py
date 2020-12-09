
def parse(fn):
    data = []
    for line in open(fn):
        ins, num = line.strip().split()
        num = int(num)
        data.append((ins, num))
    return data

def solve(fn):
    instructions = parse(fn)
    acc = 0
    prog = 0
    visited = set()
    while not prog in visited:
        visited.add(prog)
        ins, num = instructions[prog]
        if ins == 'acc':
            acc += num
            prog += 1
        if ins == 'jmp':
            prog += num
        if ins == 'nop':
            prog += 1
    return acc


assert solve('input.txt')  == 5

print(solve('input_big.txt'))
