"""Day 15: Timing is Everything

https://adventofcode.com/2016/day/15

"""
import re
from itertools import count


def parse_discs(data):
    result = []
    for line in data.strip().split('\n'):
        disc = re.findall(r'(\d+) positions;.+ position (\d+)', line)[0]
        result.append([int(x) for x in disc])

    return result


def is_open(disc_no, positions, startpos, time):
    return (time + disc_no + startpos) % positions == 0


def check_discs(discs, time):
    return all((
        is_open(i, positions, startpos, time)
        for i, (positions, startpos) in enumerate(discs, 1)
    ))      


def solve(data):
    discs = parse_discs(data)
    for t in count(start=0, step=1):
        if check_discs(discs, t):
            return t



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data += "Disc #7 has 11 positions; at time=0, it is at position 0."
    result = solve(input_data)
    print(f'Example2: {result}')
