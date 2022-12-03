"""
Calorie Counting

https://adventofcode.com/2022/day/1
"""

def parse_calories(data):
    return [
        sum([int(line) for line in elf.strip().split('\n')])
        for elf in data.strip().split('\n\n')
    ]


def solve(data):
    cals = parse_calories(data)
    return max(cals)


def solve2(data):
    cals = parse_calories(data)
    cals.sort()
    return sum(cals[-3:])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 72070

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 211805
