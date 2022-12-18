"""


https://adventofcode.com/2022/day/11
"""
from functools import reduce
from operator import mul
import re
from pydantic import BaseModel


PATTERN = (
    r"Monkey (\d+).+"
    r"Starting items: (.+) "
    r"Operation: new = (.+) "
    r"Test: divisible by (\d+).+ "
    r"If true: throw to monkey (\d+).+"
    r"to monkey (\d+)"
)


class Item(BaseModel):

    value: int
    monkey: int

    def shrink(self, common_denominator):
        self.value %= common_denominator


class Monkey(BaseModel):

    id: int
    items: list
    operation: str
    test: int
    throw_true: int
    throw_false: int
    divide: bool = False
    inspections: int = 0

    def __repr__(self):
        items = [it.value for it in self.items if it.monkey == self.id]
        return f"{self.id} {items}"

    def play(self, monkeys):
        [self.examine(item) for item in self.items if item.monkey == self.id]
    
    def examine(self, item):
        item.value = eval(self.operation)
        if self.divide:
            item.value = item.value // 3
        item.monkey = self.throw_true if item.value % self.test == 0 else self.throw_false
        self.inspections += 1


def parse(data, divide):
    monkeys = []
    item_list = []
    for par in data.strip().split('\n\n'):
        monkey, items, op, test, ttrue, tfalse = re.findall(PATTERN, par, re.DOTALL)[0]
        monkeys.append(Monkey(
            id=int(monkey),
            items=item_list,
            operation=op.strip().replace("old", "item.value"),
            test=int(test),
            throw_true=int(ttrue),
            throw_false=int(tfalse),
            divide=divide
        ))
        for item_value in re.findall(r'\d+', items):
            item_list.append(Item(
                value=int(item_value),
                monkey=int(monkey)
            ))
    return monkeys, item_list


def solve(data, rounds=20, divide=True):
    monkeys, items = parse(data, divide)
    common_denominator = reduce(mul, (m.test for m in monkeys))
    for i in range(rounds):
        for m in monkeys:
            m.play(monkeys)
        for it in items:
            it.shrink(common_denominator)
            
    inspections = [m.inspections for m in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def solve2(data):
    return solve(data, rounds=10000, divide=False)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 62491

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 17408399184