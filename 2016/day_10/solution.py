"""Day 10: Bots

https://adventofcode.com/2016/day/10
"""
import re
from collections import defaultdict
from functools import reduce

BOT_VALUE = r"value (\d+) goes to bot (\d+)"
BOT_RULE = r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)" 


def parse_bots(instructions):
    bots = defaultdict(set)
    for value, bot in re.findall(BOT_VALUE, instructions):
        value = int(value)
        bot = int(bot)
        bots[bot].add(value)
    return bots


def parse_rules(instructions):
    rules = []
    for bot, low_type, low, high_type, high in re.findall(BOT_RULE, instructions):
        rules.append((
            int(bot), 
            low_type,
            int(low),
            high_type,
            int(high)
        ))

    return rules


def apply_rule(bots, outputs, bot, low_type, low, high_type, high):
    if len(bots[bot]) == 2:
        low_num = min(bots[bot])
        high_num = max(bots[bot])
        if low_type == 'bot':
            bots[low].add(low_num)
        else:
            outputs[low] = low_num
        if high_type == 'bot':
            bots[high].add(high_num)
        else:
            outputs[high] = high_num


def cycle_bots(instructions):
    bots = parse_bots(instructions)
    rules = parse_rules(instructions)
    outputs = {}

    while True:
        for r in rules:
            apply_rule(bots, outputs, *r)
        yield bots, outputs


def solve(instructions, query):
    query = set(query)
    for bots, _ in cycle_bots(instructions):
        for b in bots:
            if query == bots[b]:
                return b


def is_query_in_output(query, outputs):
    return query.intersection(set(outputs)) == query


def get_output(instructions, query):
    query = set(query)
    for _, outputs in cycle_bots(instructions):
        if is_query_in_output(query, outputs):
            return reduce(lambda a,b:a*outputs[b], query, 1)



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, (61, 17))
    print(f'Example 1: {result}')

    result = get_output(input_data, (0, 1, 2))
    print(f'Example 2: {result}')
