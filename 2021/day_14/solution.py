"""
Extended Polymerization

https://adventofcode.com/2021/day/14

Part I + II
"""
import re
from collections import defaultdict


def parse(data):
    """separate starting molecule from substitution rules"""
    start = data.strip().split('\n')[0]
    rules = dict(re.findall(r'(\w\w) -> (\w)', data))
    return start, rules

def get_pair_count(seq):
    """counts how many times each key occurs in a molecule"""
    pairs = defaultdict(int)
    for i in range(len(seq)-1):  # sliding window of size 2
        key = seq[i:i+2]         # try itertools.pairwise (3.10)
        pairs[key] += 1
    return pairs

def step(pairs, rules):
    """updates the pair count dictionary once"""
    new = defaultdict(int)
    for key in pairs:
        new[key[0] + rules[key]] += pairs[key]
        new[rules[key] + key[1]] += pairs[key]
    return new


def count_chars(pairs, seq):
    """returns a sorted list of character frequencies"""
    chars = defaultdict(int)
    for p in pairs:
        chars[p[0]] += pairs[p]
        chars[p[1]] += pairs[p]
    chars[seq[0]] += 1
    chars[seq[-1]] += 1
    return list(sorted([v // 2 for _, v in chars.items()]))


def solve(data, iter):
    seq, rules = parse(data)
    pairs = get_pair_count(seq)        
    for _ in range(iter):
        pairs = step(pairs, rules)
    count = count_chars(pairs, seq)
    return count[-1] - count[0]


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 10)
    print(f'Example 1: {result}')
    assert result == 2345

    result = solve(input_data, 40)
    print(f'Example 2: {result}')
    assert result == 2432786807053
