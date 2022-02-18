"""
Day 12: JSAbacusFramework.io

https://adventofcode.com/2015/day/12
"""
import re
import json


def solve(data):
    nums = [int(x) for x in re.findall(r'-?\d+', data)]
    return sum(nums)

def solve2(data):
    j = json.loads(data)
    stack = [j]
    result = 0
    while stack:
        elem = stack.pop()
        if isinstance(elem, int):
            result += elem
        elif isinstance(elem, list):
            for x in elem:
                stack.append(x)
        elif isinstance(elem, dict) and 'red' not in elem.values():
            for x in elem.values():
                stack.append(x)
        elif isinstance(elem, str):
            pass
        else:
            print(elem)
            assert False
    return result

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
