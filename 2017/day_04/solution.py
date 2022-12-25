"""
High-Entropy Passphrases

https://adventofcode.com/2017/day/4

"""
from collections import Counter

def no_anagram(data):
    tokens = data.strip().split()
    fs = set([tuple(sorted(Counter(t).items())) for t in tokens])
    return len(fs) == len(tokens)
    

def is_valid(data):
    tokens = data.strip().split()
    return len(set(tokens)) == len(tokens)


def solve(data, func=is_valid):
    return sum(map(func, data.strip().split('\n')))


def solve2(data):
    return solve(data, no_anagram)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
