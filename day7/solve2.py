
import sys
import re
from pprint import pprint

def parse_rules(fn):
    rules = {}
    numbers = {}

    for line in open(fn):
        colors = re.findall("(\w+ \w+) bag", line)
        numbers = [int(i) for i in re.findall("\d+", line)]
        container = colors[0]
        contained = list(zip(colors[1:], numbers))
        if contained:
            rules[container] = contained
    return rules

def get_colors(rules):
    c = set()
    for k in rules:
        c.add(k)
        for v, num in rules[k]:
            c.add(v)
    return c

def sum_bags(rules, col, num=1):
    """returns the number of bags contained"""
    val = rules.get(col, [])
    s = 0
    for color, number in val:
        print(color, number)
        s += number * sum_bags(rules, color, number*num)

    print(col, s)
    return s + 1

def check(fn):
    count = 0
    rules = parse_rules(fn)
    colors = get_colors(rules)
    return sum_bags(rules, "shiny gold") - 1


assert check('input2.txt') == 126

#print(check('input_big.txt'))
