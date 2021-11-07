
import re
from itertools import combinations, chain

data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')


def getx(mask):
    return [2**(len(mask)-1-i) for i, c in enumerate(mask) if c == 'X']

def get_combinations(xpos):
    total = [combinations(xpos, i) for i in range(len(xpos)+1)]
    return [sum(c) for c in chain(*total)]


assert getx('0X0X') == [4, 1]
assert getx('0000000000000000000000000000000X0X0X') == [16, 4, 1]
assert getx('00000000000000000000000000000000X0XX') == [8,2,1]
assert getx('000000000000000000000000000000000XXX') == [4,2,1]

get_combinations([4, 2, 1])    
get_combinations([2,8, 16, 1])

def get_addresses(mask, addr):
    result = []
    ors = ''.join(['1' if c=='1' else '0' for c in mask])
    ors = int(ors, 2)
    xpos = getx(mask)
    zeroing = 2**36 - sum(xpos) - 1
    addr = addr & zeroing
    addr = addr | ors
    
    for ofs in get_combinations(xpos):
        result.append(addr + ofs)
    result.sort()
    return result
    
get_addresses('00000000000000000000000000000000X0XX', 26)
get_addresses('00000000000000000000000000000010X0XX', 26)
get_addresses('000000000000000000000000000000000XXX', 7)

def solve(data):
    mem = {}
    for line in data:
        if line.startswith('mask'):
            mask = re.findall("([01X]+)", line)[0]
        else:
            addr = int(re.findall('\[(\d+)\]', line)[0])
            num = int(re.findall('\=\s(\d+)', line)[0])
            for addr in get_addresses(mask, addr):
                mem[addr] = num
    return sum(mem.values())

assert solve(data) == 208

print(solve(open('input_big.txt')))
