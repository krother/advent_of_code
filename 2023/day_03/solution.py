"""
Gear Ratios

https://adventofcode.com/2023/day/3
"""
from dataclasses import dataclass

SYMBOLS = "+-*/#@$%=&"


@dataclass
class Position:
    x: int
    y: int

    def __repr__(self):
        return f"({self.x},{self.y})"


@dataclass
class Symbol:
    pos: Position
    type: str

    def get_neighbors(self, numbers):
        return [n for n in numbers if n.is_adjacent(self.pos)]

    def __repr__(self):
        return f"<{self.pos}:{self.type}>"


@dataclass
class Number:
    start: Position
    end: Position
    value: int

    def __repr__(self):
        return f"<{self.start},{self.end}:{self.value}>"

    def is_adjacent(self, pos):
        return (
            abs(pos.y - self.start.y) <= 1
            and pos.x >= self.start.x - 1
            and pos.x <= self.end.x + 1
        )


def parse(data):
    grid = [list(row) for row in data.strip().split("\n")]
    numbers = []
    symbols = []
    for y, row in enumerate(grid):
        num, start = "", None
        for x, char in enumerate(row):
            if char in SYMBOLS:
                symbols.append(Symbol(pos=Position(x=x, y=y), type=char))
            if char.isdigit():
                num += char
                if start is None:
                    start = Position(x=x, y=y)
            elif num:
                end = Position(x=x - 1, y=y)
                numbers.append(Number(start=start, end=end, value=int(num)))
                num, start = "", None
        if num:
            end = Position(x=x - 1, y=y)
            numbers.append(Number(start=start, end=end, value=int(num)))
    return numbers, symbols


def solve(data):
    numbers, symbols = parse(data)
    return sum(
        n.value for n in numbers if any(s for s in symbols if n.is_adjacent(s.pos))
    )


def find_gears(numbers, symbols):
    for s in symbols:
        if s.type == "*":
            nb = s.get_neighbors(numbers)
            if len(nb) == 2:
                yield nb[0], nb[1]


def solve2(data):
    numbers, symbols = parse(data)
    return sum(num1.value * num2.value for num1, num2 in find_gears(numbers, symbols))


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 556057

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 82824352
