"""
Day 1 - Secret Entrance

https://adventofcode.com/2025/day/1
"""

def parse(data):
    for line in data.strip().split("\n"):
        direction, num = line[0], int(line[1:])
        yield num if direction == "R" else -num

def solve(data):
    pos = 50
    zeros = 0
    for num in parse(data):
        pos += num 
        pos = pos % 100
        zeros += pos == 0
    return zeros


def solve2(data):
    pos = 50
    zeros = 0
    for num in parse(data):
        print(pos, num, zeros)
        if pos != 0 and (
            num < 0 and abs(num) % 100 > pos
        ) or (
            num > 0 and num % 100 > 100 - pos
        ):
            zeros += 1
        zeros += abs(num) // 100 + (pos == 0)
        pos = (num + pos) % 100
    return zeros


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 1011

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 5937
