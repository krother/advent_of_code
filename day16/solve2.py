
import re
import numpy as np


ticket = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".strip().split('\n')


def parse(data):
    rules = []
    your  = []
    nearby = []
    section = "rules"
    for line in data:
        if line.startswith('nearby tickets'):
            section = "nearby"
        elif line.startswith('your ticket'):
            section = "your"
        elif section == "rules" and len(line.strip()) > 1:
            s, a, b, c, d = re.findall("(\w*\s*\w+): (\d+)-(\d+) or (\d+)-(\d+)", line)[0]
            rules.append((s, int(a), int(b), int(c), int(d)))
        elif section == "your" and len(line.strip()) > 1:
            your = [int(x) for x in line.split(',')]
        elif section == "nearby":
            nearby.append([int(x) for x in line.split(',')])
    return rules, your, nearby

def is_valid(nb, rules):
    """identify if a row is valid at all"""
    for num in nb:
        valid = False
        for _, a, b, c, d in rules:  # at least one rule has to apply
            if (a <= num <= b or c <= num <= d):
                valid = True
        if not valid:
            return False
    return True


def solve(data):
    rules, your, nearby = parse(data)
    result = {}
    nearby = [nb for nb in nearby if is_valid(nb, rules)]

    # prepare solution matrix
    m = np.ones((len(your), len(rules)), dtype=int)
    for nb in nearby:
        for position, num in enumerate(nb):
            for rule, (n, a, b, c, d) in enumerate(rules):
                if not (a <= num <= b or c <= num <= d):
                    m[position, rule]  = 0

    # iterative solver
    while len(result) < len(your):
        prevsum = m.sum()
        for i, row in enumerate(m): # positions
            if row.sum() == 1:
                j = row.argmax()
                name = rules[j][0]
                print(f'position {i} is {name} [{j}]')
                result[name] = your[i]
                m[:,j] = 0  # that rule is done
        if m.sum() == prevsum:
            print('NOT SOLVABLE')
            return result, m

    return result, m


r, m = solve(ticket)
assert r['class'] == 12
assert r['row'] == 11
assert r['seat'] == 13

r, m = solve(open('input_big.txt'))

p = 1
for k in r:
    if k.startswith('departure'):
        p = p * r[k]
print(p)
assert p == 809376774329
