
import sys
import re
from pprint import pprint

def parse_rules(fn):
    rules = {}
    for line in open(fn):
        colors = re.findall("(\w+ \w+) bag", line)
        container = colors[0]
        contained = colors[1:]
        if contained[0] != "no other":
            rules[container] = contained
    return rules

def get_colors(rules):
    c = set()
    for k in rules:
        c.add(k)
        for v in rules[k]:
            c.add(v)
    return c

def search(rules, col):
    """recursive search

    ASSUMPTION: THERE ARE NO CIRCULAR DEPENDENCIES!
    OTHERWISE THIS IS AN ENDLESS LOOP
    """
    val = rules.get(col, [])
    if "shiny gold" in val:
        return True
    else:
        for child in val:
            if search(rules, child):
                return True

def check(fn):
    count = 0
    rules = parse_rules(fn)
    colors = get_colors(rules)
    for c in colors:
        if search(rules, c):
            count += 1
    return count


assert check('input.txt') == 4

#print(check('input_big.txt'))
