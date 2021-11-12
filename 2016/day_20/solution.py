"""Day 20: Firewall Rules

https://adventofcode.com/2016/day/20

"""
from collections import deque
import re


def merge_boundaries(boundaries):
    result = []
    todo = deque(sorted(boundaries))
    low1, high1 = todo.popleft()

    while todo:
        low2, high2 = todo.popleft()
        if low2 <= high1 + 1:
            high1 = max(high1, high2)
        else:
            result.append((low1, high1))
            low1, high1 = low2, high2
    
    result.append((low1, high1))
    return result


def prepare_boundaries(data):
    boundaries = [(int(low), int(high)) for low, high in re.findall(r"(\d+)-(\d+)", data)]
    print('boundaries before:', len(boundaries))

    boundaries = merge_boundaries(boundaries)
    print('boundaries after:', len(boundaries))
    return boundaries


def solve(data):
    low, high = prepare_boundaries(data)[0]
    if low > 0:
        return 0
    else:
        return high +1


def count_ips(data, maxip):
    allowed = 0
    last = 0
    for low, high in prepare_boundaries(data):
        allowed += low - last
        last = high + 1

    allowed += maxip - last + 1
    return allowed


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = count_ips(input_data, 4294967295)
    print(f'Example 2: {result}')
