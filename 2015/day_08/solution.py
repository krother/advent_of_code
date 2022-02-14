"""
Day 8: Matchsticks

https://adventofcode.com/2015/day/8
"""
import re

def size(s):
    c = re.sub(r'^\"|\"$', '', s)
    c = re.sub(r'\\\\|\\\"|\\x[a-f0-9]{2}', 'x', c)
    return len(s), len(c)

def encode(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', r'\"')
    return len(s) + 2

def solve(data):
    result = 0
    for line in data.strip().split('\n'):
        total, chars = size(line)
        result += total - chars
    return result

def solve2(data):
    result = 0
    for line in data.strip().split('\n'):
        total, chars = size(line)
        encoded = encode(line)
        result += encoded - total
    return result

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
