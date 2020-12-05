"""
Solution for part 1
"""

REQUIRED = ['byr', 'iyr', 'eyr', 'hgt',
            'hcl', 'ecl', 'pid']

def check(psp):
    for k in REQUIRED:
        if k not in psp:
            return 0
    return 1

psp = {}
count = 0

# Thanks to Annas trick parsing the paragraphs
paragraphs = open('input.txt').read().strip().split("\n\n")

for par in paragraphs:
    psp = {}
    for pair in par.split():
        k, v = pair.split(':')
        psp[k] = v
    count += check(psp)

print(count)
