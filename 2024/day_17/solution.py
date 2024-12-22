"""


https://adventofcode.com/2024/day/17
"""
from aoc import parse_2d_numbers, parse_hash_grid, parse_numbers, priority_queue, is_on_grid, DIRECTIONS4
import re


class Bunny:

    def __init__(self, a, b, c, code):
        self.a = a
        self.b = b
        self.c = c
        self.ip = 0
        self.output = ""
        self.code = code
        self.inst = dict(zip(range(8), [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]))

    def __repr__(self):
        return f"{self.a} {self.b} {self.c} {self.ip}"

    @property
    def running(self):
        return self.ip < len(self.code)
    
    def calc(self):
        opcode = self.code[self.ip]
        lop = self.code[self.ip + 1]
        if lop <= 3:
            cop = lop
        elif lop == 4:
            cop = self.a
        elif lop == 5:
            cop = self.b
        elif lop == 6:
            cop = self.c
        else:
            assert False
        f = self.inst[opcode]
        f(cop, lop)

    def adv(self, cop, lop):
        self.a = self.a // 2 ** cop
        self.ip += 2

    def bxl(self, cop, lop):
        self.b = self.b ^ lop
        self.ip += 2

    def bst(self, cop, lop):
        self.b = cop % 8
        self.ip += 2

    def jnz(self, cop, lop):
        if self.a != 0:
            self.ip = lop
        else:
            self.ip += 2

    def bxc(self, cop, lop):
        self.b = self.b ^ self.c
        self.ip += 2

    def out(self, cop, lop):
        self.output += f"{cop % 8},"
        self.ip += 2

    def bdv(self, cop, lop):
        self.b = self.a // 2 ** cop
        self.ip += 2

    def cdv(self, cop, lop):
        self.c = self.a // 2 ** cop
        self.ip += 2


def parse(data):
    return [int(x) for x in re.findall(r"\d+", data)]

def solve(data):
    a, b, c, *code = parse(data)
    bunny = Bunny(a, b, c, code)
    while bunny.running:
        bunny.calc()
    return bunny.output[:-1]


def calc(a, b, c):
    result = []
    while a > 0:
        #print("{0:8b}".format(a))
        b = a % 8       # last 3 bits
        b = b ^ 3       # invert last two bits; b < 7
        c = a // 2 ** b # shift a right by b positions
        a = a // 8      # shift a by 3 positions
        b = b ^ 5       # invert first and last bit
        b = b ^ c       # uses only 3 last bits of c
        result.append(b % 8)
    return result


def find_next_digit(digit, prefix=0):
    print("searching for digit:", digit, "with prefix", prefix)
    result = []
    for a in range(8):
        a = a + prefix
        r = calc(a, 0, 0)
        #print(a, r)
        if r and r[0] == digit:
            print(f"found: a={a}")
            result.append(a)
    #print(result)
    return result
    
def solve2(data):
    a, b, c, *code = parse(data)
    exp = ",".join(map(str, code))

    prefixes = [0]
    for digit in code[::-1]:
        print(f"\ncandidates for digit {digit}: {len(prefixes)}")
        new_prefixes = []
        for pf in prefixes:
            new_prefixes += find_next_digit(digit, pf * 8)
        prefixes = new_prefixes
        print(prefixes)
    return min(prefixes)

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    #result = solve(input_data)
    #print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
