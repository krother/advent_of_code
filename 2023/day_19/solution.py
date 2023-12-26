"""
Aplenty

https://adventofcode.com/2023/day/19
"""
import re
from dataclasses import dataclass
from functools import reduce
from pprint import pprint
from copy import deepcopy


@dataclass
class Condition:
    property: str
    operator: str
    value: int
    result: str


def parse(data):
    rules = {}
    parts = []
    rule_part, val_part = data.strip().split("\n\n")
    for line in rule_part.split("\n"):
        name, conditions = line[:-1].split("{")
        conditions = conditions.split(",")
        rules[name] = [], conditions[-1]
        for c in conditions[:-1]:
            property, operator, value, result = re.findall(r"(\w)(.)(\d+)\:(\w+)", c)[0]
            rules[name][0].append(
                Condition(
                    property=property,
                    operator=operator,
                    value=int(value),
                    result=result,
                )
            )

    for p in val_part.split("\n"):
        p = p.replace("{", "dict(").replace("}", ")")
        parts.append(eval(p))

    return rules, parts


def solve(data):
    rules, parts = parse(data)

    total = 0
    for p in parts:
        wf = "in"
        while wf not in "AR":
            for cond in rules[wf][0]:
                if (cond.operator == ">" and p[cond.property] > cond.value) or (
                    cond.operator == "<" and p[cond.property] < cond.value
                ):
                    wf = cond.result
                    break
            else:
                wf = rules[wf][1]

        if wf == "A":
            total += sum(p.values())

    return total


@dataclass
class Partition:
    wf: str
    min_values: dict[str, int]
    max_values: dict[str, int]

    @property
    def accept(self):
        return self.wf == "A"

    @property
    def reject(self):
        return self.wf == "R"

    def set_min(self, prop, value):
        if value > self.max_values[prop]:
            self.wf = "R"
        else:
            self.min_values[prop] = value

    def set_max(self, prop, value):
        if value < self.min_values[prop]:
            self.wf = "R"
        else:
            self.max_values[prop] = value

    def get_combinations(self):
        combinations = reduce(
            lambda a, b: a * b,
            (self.max_values[char] - self.min_values[char] + 1 for char in "xmas"),
            1,
        )
        assert combinations > 0
        return combinations


def split_partition(part, cond):
    new_part = deepcopy(part)
    new_part.wf = cond.result

    if cond.operator == "<":
        new_part.set_max(cond.property, cond.value - 1)
        part.set_min(cond.property, cond.value)
    else:
        new_part.set_min(cond.property, cond.value + 1)
        part.set_max(cond.property, cond.value)
    return new_part


def place_part(part, stack, accepted):
    if part.accept:
        accepted.append(part)
    elif not part.reject:
        stack.append(part)


def solve2(data):
    rules, _ = parse(data)
    stack = [
        Partition(
            wf="in",
            min_values={"x": 1, "m": 1, "a": 1, "s": 1},
            max_values={"x": 4000, "m": 4000, "a": 4000, "s": 4000},
        )
    ]
    accepted = []
    while stack:
        part = stack.pop()
        for cond in rules[part.wf][0]:
            place_part(part=split_partition(part, cond), stack=stack, accepted=accepted)
        if not part.reject:
            part.wf = rules[part.wf][1]
            place_part(part, stack, accepted)

    return sum([p.get_combinations() for p in accepted])


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 397643

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 132392981697081
