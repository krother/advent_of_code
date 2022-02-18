"""
Day 11: Corporate Policy

https://adventofcode.com/2015/day/11

"""
import string
import re

def next_candidate(psw):
    num = [string.ascii_lowercase.index(c) for c in psw]
    num[-1] += 1
    while 26 in num:
        idx = num.index(26)
        num[idx] = 0
        num[idx - 1] += 1

    s = ''.join([string.ascii_lowercase[i] for i in num])
    return s


FORBIDDEN = r'[ilo]'
TRIPLE = r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz'
PAIR = r'(\w)\1'

def next_valid_password(psw):
    while True:
        psw = next_candidate(psw)
        if re.findall(FORBIDDEN, psw):
            continue
        if not re.findall(TRIPLE, psw):
            continue
        if len(set(re.findall(PAIR, psw))) < 2:
            continue
        return psw


if __name__ == '__main__':
    input_data = 'cqjxjnds'
    result = next_valid_password(input_data)
    print(f'Example 1: {result}')

    result = next_valid_password(result)
    print(f'Example 2: {result}')
