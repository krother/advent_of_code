"""
Cathode-Ray Tube

https://adventofcode.com/2022/day/10
"""
import re
from pydantic import BaseModel


CYCLES = [20, 60, 100, 140, 180, 220]


class Tube(BaseModel):

    cycles: int = 0
    x: int = 1
    result: int = 0

    def tick(self):
        self.cycles += 1
        if self.cycles in CYCLES:
            self.result += self.cycles * self.x
            print(self)


class SpriteTube(BaseModel):

    cycles: int = 0
    x: int = 1
    result: str = ""

    def tick(self):
        col = self.cycles % 40
        if col - 1 <= self.x <= col + 1:
            self.result += '#'
        else:
            self.result += '.'
        self.cycles += 1
        if col == 39:
            self.result += "\n"



def calculate(data, tube_cls):
    tube = tube_cls()
    for line in data.strip().split('\n'):
        tube.tick()
        if line.startswith('addx'):
            tube.tick()
            tube.x += int(re.findall(r'-?\d+', line)[0])
    return tube.result


def solve(data):
    return calculate(data, Tube)


def solve2(data):
    return calculate(data, SpriteTube)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    input_data = open('input_mr.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: \n{result}')
