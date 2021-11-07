from collections import Counter

input = """abc

a
b
c

ab
ac

a
a
a
a

b""".strip()


def part_one(groups):
    count = 0
    for g in groups:
        x = set(g.replace('\n', ''))
        count += len(x)
    return count


def part_two(groups):
    count = 0
    for g in groups:
        sets = [set(line) for line in g.split('\n')]
        x = None
        for s in sets:
            if x == None:
                x = s
            x = x.intersection(s)
        count += len(x)
    return count


groups = input.split('\n\n')
assert part_one(groups) == 11
assert part_two(groups) == 6

input = open('input_big.txt').read().strip()
groups = input.split('\n\n')
print(part_one(groups))
print(part_two(groups))
