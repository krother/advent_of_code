"""
Memory Reallocation

https://adventofcode.com/2017/day/6

"""

def redistribute(data):
    data = list(data)
    i = data.index(max(data))
    c = data[i]
    data[i] = 0
    for _ in range(c):
        i += 1
        if i >= len(data):
            i = 0
        data[i] += 1
    return tuple(data)

def solve(data):
    data = tuple([int(x) for x in data.strip().split()])
    seen = set()
    cycles = 0
    while data not in seen:
        seen.add(data)
        data = redistribute(data)
        cycles += 1
    return cycles


def solve2(data):
    data = tuple([int(x) for x in data.strip().split()])
    cycles = {}
    while data not in cycles:
        cycles[data] = 0
        data = redistribute(data)
        for key in cycles:
            cycles[key] += 1
    return cycles[data]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
