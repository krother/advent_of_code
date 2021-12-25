"""Reactor Reboot

https://adventofcode.com/2021/day/22

"""
import re


class Cube:

    def __init__(self, state, xmin, xmax, ymin, ymax, zmin, zmax):
        self.state = state
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.overlaps = []

    def __repr__(self):
        return str((self.state, self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax))
        
    def initial_region(self):
        if (
            self.xmin >= -50 and self.xmax <= 50 and
            self.ymin >= -50 and self.ymax <= 50 and
            self.zmin >= -50 and self.zmax <= 50
        ):
            return True

    def volume(self):
        if (
            self.xmin > self.xmax or
            self.ymin > self.ymax or
            self.zmin > self.zmax
        ): 
            return 0
        size = (self.xmax - self.xmin + 1) * (self.ymax - self.ymin + 1) * (self.zmax - self.zmin + 1)
        for ov in self.overlaps:
            size -= ov.volume()
        return size

    def add_overlap(self, other):
        ovcube = Cube(
            other.state,
            xmin = max(self.xmin, other.xmin),
            xmax = min(self.xmax, other.xmax),
            ymin = max(self.ymin, other.ymin),
            ymax = min(self.ymax, other.ymax),
            zmin = max(self.zmin, other.zmin),
            zmax = min(self.zmax, other.zmax)
        )
        if ovcube.volume() > 0:
            for ov in self.overlaps:
                ovcube.add_overlap(ov)
            self.overlaps.append(ovcube)
        
    def calculate_overlaps(self, cubes):
        for other in cubes:
            self.add_overlap(other)


def parse(data):
    steps = []
    for state, *boundaries in re.findall(r'(\w+).x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)', data):
        boundaries = list(map(int, boundaries))
        steps.append(Cube(state, *boundaries))
    return steps


def add_overlaps(cubes):
    for i in range(len(cubes)-1, -1, -1):
        cubes[i].calculate_overlaps(cubes[i+1:])


def get_volume(cubes):
    return sum([c.volume() for c in cubes if c.state == 'on'])


def solve(data, initialize=True):
    cubes = [c for c in parse(data) if (not initialize or c.initial_region())]
    add_overlaps(cubes)
    return get_volume(cubes)



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve(input_data, False)
    print(f'Example 2: {result}')
