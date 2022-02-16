"""
Day 10: Elves Look, Elves Say

https://adventofcode.com/2015/day/10
"""

def propagate(s):
    digit = s[0]
    num = 0
    result = ''
    for c in s:
        if c != digit:
            result += f'{num}{digit}'
            num = 0
            digit = c
        num += 1
    result += f'{num}{digit}'
    return result


def solve(data, rounds):
    for i in range(rounds):
        data = propagate(data)
    return len(data)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 40)
    print(f'Example 1: {result}')

    result = solve(input_data, 50)
    print(f'Example 2: {result}')
