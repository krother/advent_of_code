"""
Advent of code 2020, day2

Challenge: only use one-line functions and no variables
"""

def map_fields(num1, num2, char, psw):
    return int(num1), int(num2), char[0], psw

def parse(line):
    return map_fields(*line.replace('-', ' ').strip().split())

def check_part1(num1, num2, char, psw):
    return int(num1 <= psw.count(char) <= num2)

def check_part2(num1, num2, char, psw):
    return int((psw[num1-1] == char) != (psw[num2-1] == char))

def is_valid(line, check):
    return check(*parse(line))

def count_valid_passwords(filename, check):
    return sum([is_valid(line, check) for line in open(filename)])

# use a function reference
print(count_valid_passwords('input.txt', check_part1))
print(count_valid_passwords('input.txt', check_part2))
