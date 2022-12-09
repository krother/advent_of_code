"""
Tuning Trouble

https://adventofcode.com/2022/day/6
"""
from functools import partial


def find_packet(data, length):
    for i in range(len(data) + 1):
        snip = data[i - length: i]
        if len(set(snip)) == length:
            return i
        

solve = partial(find_packet, length=4)
solve2 = partial(find_packet, length=14)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 1109

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 3965
