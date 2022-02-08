"""Medicine for Rudolph

https://adventofcode.com/2015/day/19

"""
import re
from aoc import PriorityQueue
from collections import defaultdict
from pprint import pprint


PATTERN = r'(\w+) => (\w+)'

def parse(data):
    transitions, molecule = data.strip().split('\n\n')
    transitions = [(k,v) for k, v in re.findall(PATTERN, transitions)]
    return transitions, molecule


def invert_transitions(transitions):
    tdict = {v: k for k, v in transitions}
    assert len(tdict) == len(transitions)
    return tdict
    #return [(b, a) for a, b in t]


def solve(data):
    transitions, molecule = parse(data)
    result = set()

    for char, sub in transitions:
        for m in re.finditer(char, molecule):
            mol = molecule[:m.start()] + sub + molecule[m.end():]
            result.add(mol)
    return len(result)


def tokenize(target):
    """Create dictionary of {(start, stop): (0, token)} containing every element"""
    result = {}
    token = ''
    start = 0
    for i, char in enumerate(target):
        if token and char.isupper():
            result[(start, i)] = (0, token)
            token = ''
            start = i
        token += char
    result[(start, i + 1)] = (0, token)
    return result

def growing_windows(target):
    """Run over all windows from smallest to largest"""
    for window_size in range(2, len(target) + 1):
        for start in range(len(target) - window_size + 1):
            stop = start + window_size
            yield start, stop


def concatenate_inert_gases(start, stop, target, lookup):
    """Rn and Ar are special, concatenate everything in between"""
    word = target[start:stop]
    if word.startswith('Rn') and word.endswith('Ar'):
        middle = start + 2, stop - 2
        if middle in lookup:
            moves, sub = lookup[middle]
            lookup[(start, stop)] = moves, 'Rn' + sub + 'Ar'

def concatenate_ytterbium(start, stop, first, second, m1, m2, lookup):
    """If there is an Y, concatenate the subsegments no matter what"""
    if first.endswith('Y') or second.startswith('Y'):
        lookup[(start, stop)] = m1 + m2, first + second


def check_split_window(start, stop, lookup, transitions):
    """Check all possible splits"""
    for split in range(start + 1, stop):
        assert start < split < stop
        m1, first = lookup.get((start, split), (None, None))
        m2, second = lookup.get((split, stop), (None, None))
        if first and second:
            subseq = first + second
            if subseq in transitions:
                lookup[(start, stop)] = m1 + m2 + 1, transitions[subseq]
            else:
                concatenate_ytterbium(start, stop, first, second, m1, m2, lookup)


def solve2(data):
    transitions, target = parse(data)
    transitions = invert_transitions(transitions)

    lookup = tokenize(target)

    for start, stop in growing_windows(target):
        if target[start].islower(): continue # 1.8x speedup
        concatenate_inert_gases(start, stop, target, lookup)
        check_split_window(start, stop, lookup, transitions)

    return lookup[(0, len(target))]




if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print('result 2 for input_data.txt', result)
    assert result[0] == 212

    input_data = open('input_data3.txt').read()
    result = solve2(input_data)
    print('result 2 for input_data3.txt', result)
    assert result[0] == 195

    input_data = open('input_data2.txt').read()
    result = solve2(input_data)
    print('result 2 for input_data2.txt', result)

