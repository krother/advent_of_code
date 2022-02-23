"""
Extended Polymerization

https://adventofcode.com/2021/day/14

Part I : prepared for presentation at PyLadies
"""
import re
from collections import Counter


def parse(data):
    """separate starting molecule from substitution rules"""
    start = data.strip().split('\n')[0]
    rules = dict(re.findall(r'(\w\w) -> (\w)', data))
    return start, rules


def step(molecule, rules):
    """Applies substitution rules on the molecule once"""
    result = ""
    for i in range(len(molecule) - 1):  # sliding window of size 2
        key = molecule[i:i + 2]
        result += key[0] + rules[key]
    result += key[1]  # add last key
    return result


def count_chars(molecule):
    """Find most and least common character"""
    c = Counter(molecule)
    most = c.most_common()[0][1]
    least = c.most_common()[-1][1]
    return most, least


def solve(data, iter):
    """Apply substitution iter times"""
    molecule, rules = parse(data)
    for _ in range(iter):
        molecule = step(molecule, rules)
    most, least = count_chars(molecule)
    return most - least


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 10)
    print(f'Example 1: {result}')
    assert result == 2345
