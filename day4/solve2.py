"""
Solution for part 2
"""
import re

REQUIRED = ['byr', 'iyr', 'eyr', 'hgt',
            'hcl', 'ecl', 'pid']

def byr(psp):
    return 1920 <= int(psp['byr']) <= 2002

def iyr(psp):
    return 2010 <= int(psp['iyr']) <= 2020

def eyr(psp):
    return 2020 <= int(psp['eyr']) <= 2030

def hgt(psp):
    v = psp['hgt']
    if v.endswith('cm'):
        return 150 <= int(v[:-2]) <= 193
    elif v.endswith('in'):
        return 59 <= int(v[:-2]) <= 76
    return 0

def hcl(psp):
    return re.match("\#[0-9a-f]{6}", psp['hcl'])

def ecl(psp):
    return psp['ecl'] in "amb blu brn gry grn hzl oth".split()

def pid(psp):
    return re.match("^\d{9}$", psp['pid'])

def check(psp):
    for k in REQUIRED:
        if k not in psp:
            return 0

    # ouch, this is ugly!
    if not byr(psp): return 0
    if not iyr(psp): return 0
    if not eyr(psp): return 0
    if not hgt(psp): return 0
    if not hcl(psp): return 0
    if not ecl(psp): return 0
    if not pid(psp): return 0

    return 1

# test code. Super important!
assert byr({'byr': '2002'})
assert not byr({'byr': '2003'})

assert hgt({'hgt': '60in'})
assert hgt({'hgt': '190cm'})
assert not hgt({'hgt': '190in'})
assert not hgt({'hgt': '190'})

assert hcl({'hcl': '#123abc'})
assert not hcl({'hcl': '#123abz'})
assert not hcl({'hcl': '123abc'})

assert ecl({'ecl': 'brn'})
assert not ecl({'ecl': 'wat'})

assert pid({'pid': '000000001'})
assert not pid({'pid': '0123456789'})


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
