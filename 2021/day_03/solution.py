"""
Binary Diagnostic

https://adventofcode.com/2021/day/3

"""
import numpy as np

    
def parse(data):
    lines = data.strip().split('\n')
    bits = [list(map(int, row)) for row in lines]
    a = np.array(bits)
    return a


def array_to_int(a):
    binary = ''.join(map(str, a))
    return int(binary, base=2)
 

def solve(data):
    a = parse(data)
    count = a.sum(axis=0)

    gamma = (count > a.shape[0] / 2).astype(int)
    gamma = array_to_int(gamma)

    epsi = (2 ** len(a[0]) - 1) - gamma

    return gamma * epsi



def solve2(data):
    a = parse(data)

    bits = a.copy()
    i = 0
    while len(bits) > 1:
        count = bits.sum(axis=0)
        most_common = (count >= bits.shape[0] / 2).astype(int)
        print(bits, most_common[i])
        new = []
        for b in bits:
            if b[i] == most_common[i]:
                new.append(b)
        bits = np.array(new)
        i += 1

    oxy = array_to_int(bits[0])

    bits = a.copy()
    i = 0
    while len(bits) > 1:
        count = bits.sum(axis=0)
        most_common = (count >= bits.shape[0] / 2).astype(int)
        new = []
        for b in bits:
            if b[i] != most_common[i]:
                new.append(b)
        bits = np.array(new)
        i += 1

    scrub = array_to_int(bits[0])
    print(oxy, scrub)
    return oxy * scrub


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    assert result == 2743844


    result = solve2(input_data)
    print(f'Example2: {result}')
    assert result == 6677951
