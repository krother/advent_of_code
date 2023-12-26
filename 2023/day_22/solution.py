"""
Sand Slabs

https://adventofcode.com/2023/day/22
"""
import re
from dataclasses import dataclass
from copy import deepcopy


def has_overlap(start1, end1, start2, end2):
    assert start1 <= end1 and start2 <= end2
    if start1 > end2 or start2 > end1:
        return False
    return True


@dataclass
class Position:
    x: int
    y: int
    z: int


@dataclass
class Brick:
    label: str
    start: Position
    end: Position
    resting: bool
    supporters: int
    supported_bricks: list
    xy_overlaps: list

    def __repr__(self):
        return f"{self.start}-{self.end}"

    def supports(self, other):
        return has_overlap(self.start.z + 1, self.end.z + 1, other.start.z, other.end.z)

    def drop(self):
        if self.resting:
            return
        if self.start.z == 1 or self.end.z == 1:
            self.resting = True
            return
        for b in self.xy_overlaps:
            if b.supports(self):
                if b.resting:
                    self.resting = True
                return
        self.start.z -= 1
        self.end.z -= 1


def parse(data):
    chars = "ABCDEFG"
    for i, line in enumerate(data.strip().split("\n")):
        n = list(map(int, re.findall(r"\d+", line)))
        yield Brick(
            label=chars[i % len(chars)],
            start=Position(*n[:3]),
            end=Position(*n[3:]),
            resting=False,
            supporters=0,
            supported_bricks=[],
            xy_overlaps=[],
        )


def cache_overlaps(bricks):
    # speedup: cache overlaps
    for b1 in bricks:
        b1.xy_overlaps = []
        for b2 in bricks:
            if b1 == b2:
                continue
            if has_overlap(b1.start.x, b1.end.x, b2.start.x, b2.end.x) and has_overlap(
                b1.start.y, b1.end.y, b2.start.y, b2.end.y
            ):
                b1.xy_overlaps.append(b2)


def drop_step(falling):
    new_falling = []
    for b in falling:
        b.drop()
        if not b.resting:
            new_falling.append(b)
    return new_falling


def drop(bricks):
    falling = bricks[:]
    while falling:
        print("bricks falling:", len(falling))
        falling = drop_step(falling)


def count(bricks):
    result = 0
    for b in bricks:
        b.supported_bricks = []
        b.supporters = 0

    for b in bricks:
        for c in b.xy_overlaps:
            if b.supports(c):
                b.supported_bricks.append(c)
                c.supporters += 1
    for b in bricks:
        if len(b.supported_bricks) == 0 or all(
            [c.supporters >= 2 for c in b.supported_bricks]
        ):
            result += 1
    return result


def solve(data):
    bricks = list(parse(data))
    cache_overlaps(bricks)
    drop(bricks)
    return count(bricks)


def solve2(data):
    bricks = list(parse(data))
    cache_overlaps(bricks)
    drop(bricks)

    # unlock bricks so they fall again
    for b in bricks:
        b.resting = False
        b.xy_overlaps = []

    result = 0
    for i in range(len(bricks)):
        oneless = deepcopy(bricks[:i] + bricks[i + 1 :])
        cache_overlaps(oneless)
        for b in oneless:
            b.zstart = b.start.z
        drop(oneless)
        ndropped = len([b for b in oneless if b.zstart > b.start.z])
        result += ndropped
        print("eliminating brick", bricks[i].label, "results in", ndropped)
    return result


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example 1: {result}")  # 475

    result = solve2(input_data)
    print(f"Example 2: {result}")  # 79144
