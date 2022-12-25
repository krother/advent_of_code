"""
Stream Processing

https://adventofcode.com/2017/day/9
"""
import re

def remove_garbage(data):
    data = re.sub(r'\!.', '', data)
    data = re.sub(r'<[^>]+>', '', data)
    return data


def solve(data):
    data = remove_garbage(data)
    total = 0
    depth = 0
    for char in data:
        if char == '{':
            depth += 1
        elif char == '}':
            total += depth
            depth -= 1
    return total

def solve2(data):
    data = re.sub(r'\!.', '', data)
    garbage = re.findall(r'<([^>]+)>', data)
    return sum([len(g) for g in garbage])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
