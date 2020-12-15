
import re


data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

def solve(data):
    total = 0
    mem = {}
    for line in data:
        if line.startswith('mask'):
            mask = re.findall("([01X]+)", line)[0]
            # create string with 1s for all bits to be set
            ors = ''.join(['1' if c=='1' else '0' for c in mask])
            # create string with 0s for all bits to be deleted
            ands = ''.join(['0' if c=='0' else '1' for c in mask])
            ands = int(ands, 2)
            ors = int(ors, 2)
        else:
            addr = int(re.findall('\[(\d+)\]', line)[0])
            num = re.findall('\=\s(\d+)', line)[0]
            num = int(num)
            a = num & ands  # delete bits
            a = a | ors     # set bits
            mem[addr] = a
            print(a)
    return sum(mem.values())


assert solve(data)  == 165

print(solve(open('input_big.txt')))
