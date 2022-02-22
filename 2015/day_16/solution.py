"""
An Aunt named Sue

https://adventofcode.com/2015/day/16

"""
import re

AUNT = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

SUE = r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'

def parse(data):
    for sue, k1, v1, k2, v2, k3, v3 in re.findall(SUE, data):
        yield int(sue), [(k1, int(v1)), (k2, int(v2)), (k3, int(v3))]


def check_attributes(attribs):
    for key, val in attribs:
        if AUNT[key] != val:
            return False
    return True

def check_fuzzy_attributes(attribs):
    for key, val in attribs:
        if key in {'cats', 'trees'}:
            if AUNT[key] >= val:
                return False
        elif key in {'pomerians', 'goldfish'}:
            if AUNT[key] <= val:
                return False
        else:
            if AUNT[key] != val:
                return False
    return True


def solve(data, checker=check_attributes):
    for sue, attribs in parse(data):
        if checker(attribs):
            return sue

def solve2(data):
    return solve(data, check_fuzzy_attributes)



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 103

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 405
