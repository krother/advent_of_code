"""
Doesn't He Have Intern-Elves For This?

https://adventofcode.com/2015/day/5

"""
import re

FORBIDDEN = r'ab|cd|pq|xy'
VOWEL = r'([aeiou].*){3,}'
DOUBLE = r'(\w)\1'
REPEAT = r'(\w\w).*\1'
ABA = r'(\w)\w\1'

def is_nice(s):
    if re.findall(FORBIDDEN, s):
        return False
    if re.findall(VOWEL, s) and re.findall(DOUBLE, s):
        return True
    return False

def is_nice2(s):
    if re.findall(REPEAT, s) and re.findall(ABA, s):
        return True
    return False


def solve(data, func=is_nice):
    return sum(map(func, data.strip().split('\n')))


def solve2(data):
    return solve(data, is_nice2)

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
