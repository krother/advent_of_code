"""
Day 18: Like a Rogue

https://adventofcode.com/2016/day/18

"""

def get_next_symbol(triplet):
    first, _, last = triplet
    return '.' if first == last else '^'


def reduce_row(row):
    if len(row) < 3:
        return ''
    return get_next_symbol(row[:3]) + reduce_row(row[1:])


def get_next_row(row):
    return reduce_row('.' + row + '.')


def solve(row, nrows):
    safe_tiles = 0
    for i in range(nrows):
        safe_tiles += row.count('.')
        row = get_next_row(row)

    return safe_tiles


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data, 40)
    print(f'Example 1: {result}')

    result = solve(input_data, 400_000)
    print(f'Example 2: {result}')
