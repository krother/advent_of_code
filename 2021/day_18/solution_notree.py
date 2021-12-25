"""Snailfish

https://adventofcode.com/2021/day/18

"""
import functools


def magnitude(tree):
    left, right = tree
    if type(left) == list:
        left = magnitude(left)
    if type(right) == list:
        right = magnitude(right)
    return 3 * left + 2 * right

def split(number):
    return [number // 2, number // 2 + number % 2]

def add_exploded_number(data, num, check_range):
    for i in check_range:
        if type(data[i]) == int:
            new = num + data[i]
            return data[:i] + [new] + data[i+1:]
    return data

def add_left(data, num):
    return add_exploded_number(data, num, range(len(data)-1, -1, -1))

def add_right(data, num):
    return add_exploded_number(data, num, range(len(data)))

def explode(data, i):
    left = add_left(data[:i], data[i+1])
    right = add_right(data[i+5:], data[i+3])
    return left + [0] + right

def to_list(data):
    num = ''
    result = []
    for c in data:
        if c.isnumeric():
            num += c
        elif num:
            result.append(int(num))
            num = ''
        if c in '[],':
            result.append(c)
    return result

def to_string(data):
    return ''.join([str(elem) for elem in data])

def check_explode(data):
    depth = 0
    for i, elem in enumerate(data):
        if elem == '[':
            depth += 1
        elif elem == ']':
            depth -= 1
        elif type(elem) == int:
            if depth >= 5 and type(data[i+2]) == int:
                data = explode(data, i-1)
                return True, data
    return False, data


def check_split(data):
    for i, elem in enumerate(data):
        if type(elem) == int:
            if elem >= 10:
                a, b = split(elem)
                new = ['[', a, ',', b, ']']
                data = data[:i] + new + data[i+1:]
                return True, data
    return False, data


def reduce(data):
    data = to_list(data)
    action = True
    while action:
        assert data.count('[') == data.count(']')
        action, data = check_explode(data)
        if not action:
            action, data = check_split(data)

    return to_string(data)


def add(a, b):
    c = '[' + a + ',' + b + ']'
    result = reduce(c)
    return result

def add_multiple(data):
    lines = data.strip().split('\n')
    result = functools.reduce(add, lines)
    return result

def solve(data):
    total = add_multiple(data)
    data = eval(total)
    return magnitude(data)

def solve2(data):
    largest = 0
    lines = data.strip().split()
    for a in lines:
        for b in lines:
            if a == b:
                continue
            m = solve(a + '\n' + b)
            if m > largest:
                largest = m
    return largest

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 4057

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 4683
