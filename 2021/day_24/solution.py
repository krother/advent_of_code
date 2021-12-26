"""ALU

https://adventofcode.com/2021/day/24

"""

def parse_b(line, vars):
    b = line[6:]
    if b in 'wxyz':
        return vars[b]
    else:
        return int(b)

def run(prog, inp):
    vars = dict(w=0, x=0, y=0, z=0)
    for line in prog.strip().split('\n'):
        #print(line, vars)
        cmd = line[:3]
        a = line[4]
        if cmd == 'inp':
            vars[a] = int(inp[0])
            inp = inp[1:]
        else:
            b = parse_b(line, vars)
            if cmd == 'add':
                vars[a] += b
            if cmd == 'mul':
                vars[a] *= b
            if cmd == 'div':
                vars[a] = vars[a] // b
            if cmd == 'mod':
                vars[a] = vars[a] % b
            if cmd == 'eql':
                vars[a] = int(vars[a] == b)
        
    #print(vars)
    return vars['z']
    
def solve(data):
    #for i in range(99_999_999_999_999, 0, -1):
    #for i in range(11_111_111_111_111, 11_111_111_111_121):
    i = 99995969919326
    i = 48111514719111
    # if i % 10000 == 0:
    #     print(i)
    s = str(i)
    # assert '0' not in s
    result = run(data, s)
    if result == 0:
        return i

def solve2(data):
    return data

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    # result = solve2(input_data)
    # print(f'Example 2: {result}')
