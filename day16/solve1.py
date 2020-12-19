
import re


def parse(data):
    rules = []
    nearby = []
    nb = False
    r = True
    for line in data:
        if line.startswith('nearby tickets'):
            nb = True
        elif line.startswith('your ticket'):
            r = False
        elif r and len(line.strip()) > 1:
            a, b, c, d = re.findall("(\d+)-(\d+) or (\d+)-(\d+)", line)[0]
            rules.append((int(a), int(b), int(c), int(d)))
        elif nb:
            nearby.append([int(x) for x in line.split(',')])
    return rules, nearby

ticket = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".strip().split('\n')

def solve(data):
    rules, nearby = parse(data)
    print(rules)
    invalid = []
    for nb in nearby:
        for num in nb:
            valid = False
            for a,b,c,d in rules:
                #print(a,b,c,d, num)
                if (a <= num <= b or c <= num <= d):
                    valid = True
            if not valid:
                invalid.append(num)
    print(invalid)
    return sum(invalid)


assert solve(ticket) == 71

print(solve(open('input_big.txt')))
