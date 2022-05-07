"""
Opening the Turing Lock

https://adventofcode.com/2015/day/23
"""


def execute(reg, code):
    prog = code.split('\n')
    cursor = 0
    while cursor < len(prog):
        line = prog[cursor]
        instruction = line[:3]
        arg = line[4:]
        if instruction == 'inc':
            reg[arg] += 1
        elif instruction == 'hlf':
            assert reg[arg] % 2 == 0
            reg[arg] //= 2
        elif instruction == 'tpl':
            reg[arg] *= 3
        elif instruction == 'jmp':
            cursor += int(arg) - 1
        elif instruction == 'jie':
            r, ofs = arg.split(', ')
            if reg[r] % 2 == 0:
                cursor += int(ofs) - 1
        elif instruction == 'jio':
            r, ofs = arg.split(', ')
            if reg[r] == 1:
                cursor += int(ofs) - 1

        cursor += 1

        # TODO: upgrade to Py 3.10 and try pattern matching
        # match code.split():
        #    case ["inc", register]:
        #        reg[register] += 1

    return reg


def solve(data):
    return execute({'a': 0, 'b': 0}, data)


def solve2(data):
    return execute({'a': 1, 'b': 0}, data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
