"""
Checksum

https://adventofcode.com/2017/day/2

"""

def parse(data):
    for row in data.strip().split('\n'):
        yield [int(x) for x in row.strip().split()]

def find_even_divisors(row):
    for i, big in enumerate(row):
        for j, small in enumerate(row):
            if i != j and (big % small == 0):
                return big / small

def solve(data):
    return sum([
        max(row)-min(row)
        for row in parse(data)
    ])

def solve2(data):
    checksum = 0
    for row in parse(data):
        checksum += find_even_divisors(row)
    return checksum


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 34925

    result = solve2(input_data.strip())
    print(f'Example 2: {result}')
