"""
Seven Segment Search

https://adventofcode.com/2021/day/8

"""
import re


EASY = [2, 3, 4, 7]

def parse(data):
    result = []
    data = data.replace('|\n', '|')
    for line in data.strip().split('\n'):
        inp, out = line.split('|')
        segments = inp.strip().split()
        outputs = out.strip().split()
        assert len(segments) == 10
        assert len(outputs) == 4
        result.append((segments, outputs))
    return result 

def solve(data):
    easy = 0
    for _, out in parse(data):
        for digit in out:
            if len(digit) in EASY:
                easy += 1
    return easy


RULES = [
    # (digit, nseg, common_with_1, common_with_4)
    ('0', 6, 2, 3),
    ('1', 2, 2, 2),
    ('2', 5, 1, 2),
    ('3', 5, 2, 3),
    ('4', 4, 2, 4),
    ('5', 5, 1, 3),
    ('6', 6, 1, 3),
    ('7', 3, 2, 2),
    ('8', 7, 2, 4),
    ('9', 6, 2, 4)
]

def identify_digit(segments, common1, common4):
    nseg = len(segments)
    for digit, n, c1, c4 in RULES:
        if nseg == n and common1 == c1 and common4 == c4:
            return digit
    raise ValueError(f"Digit not identified: {segments}")        


def get_digits(seg, out):
    s = ' '.join(seg)
    four = set(re.findall(r'\b\w{4}\b', s)[0])
    one = set(re.findall(r'\b\w\w\b', s)[0])

    number = ''
    for digit in out:
        segments = set(digit)
        common4 = len(segments.intersection(four))
        common1 = len(segments.intersection(one))
        number += identify_digit(segments, common1, common4)
    return int(number)
    

def solve2(data):
    return sum([get_digits(seg, out) for seg, out in parse(data)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 247

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 933305