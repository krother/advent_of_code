"""
Binary Diagnostic

https://adventofcode.com/2021/day/3

"""
import numpy as np
from aoc import parse_2d_numbers


def array_to_int(a):
    binary = ''.join(map(str, a))
    return int(binary, base=2)
 

def solve(data):
    a = parse_2d_numbers(data)
    count = a.sum(axis=0)

    gamma = (count > a.shape[0] / 2).astype(int)
    gamma = array_to_int(gamma)

    epsi = (2 ** len(a[0]) - 1) - gamma

    return gamma * epsi


def get_bits(bits, count, i, equal):
    most_common = (count >= bits.shape[0] / 2).astype(int)
    new = []
    for b in bits:
        if (b[i] == most_common[i]) == equal:
            new.append(b)
    bits = np.array(new)
    return bits
    

def propagate_bits(a, equal):
    bits = a.copy()
    i = 0
    while len(bits) > 1:
        count = bits.sum(axis=0)
        bits = get_bits(bits, count, i, equal)
        i += 1
    return bits


def solve2(data):
    a = parse_2d_numbers(data)
    bits = propagate_bits(a, True)
    oxy = array_to_int(bits[0])

    bits = propagate_bits(a, False)
    scrub = array_to_int(bits[0])
    return oxy * scrub


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    assert result == 2743844


    result = solve2(input_data)
    print(f'Example2: {result}')
    assert result == 6677951
