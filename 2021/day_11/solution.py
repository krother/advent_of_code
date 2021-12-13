"""Dumbo Octopus 11

https://adventofcode.com/2021/day/11

"""
import numpy as np


VECTORS = [(-1, -1), (-1, 0), (-1, +1), 
           ( 0, -1),          ( 0, +1),
           (+1, -1), (+1, 0), (+1, +1) ]


class Octopus:

    def __init__(self, data):
        self.data = self.parse(data)
        self.flashes = set()
        self.total_flashes = 0

    @property
    def number_of_flashes(self):
        return len(self.flashes)

    def parse(self, data):
        data = [list(map(int, row)) for row in data.strip().split('\n')]
        return np.array(data)

    def adjacent(self, pos):
        y, x = pos
        for dy, dx in VECTORS:
            xx = x + dx
            yy = y + dy
            if (
                xx >= 0 and yy >= 0 
                and yy < self.data.shape[0]
                and xx < self.data.shape[1]
            ):
                yield yy, xx

    def set_flashes_to_zero(self):
        for pos in self.flashes:
            self.data[pos] = 0
        self.flashes = set()

    def get_all_positions(self):
        return list(np.ndindex(self.data.shape))

    def is_new_flash(self, pos):
        return self.data[pos] > 9 and pos not in self.flashes        

    def all_flashed(self):
        return self.number_of_flashes == 100

    def increase_adjacent(self, center):
        result = []
        for pos in self.adjacent(center):
            self.data[pos] += 1
            result.append(pos)
        return result

    def step(self):
        self.data += 1
        stack = self.get_all_positions()
        while stack:
            pos = stack.pop()
            if self.is_new_flash(pos):
                self.flashes.add(pos)
                self.total_flashes += 1
                stack += self.increase_adjacent(pos)


def solve(data, iter=100):
    octo = Octopus(data)
    for i in range(iter):
        octo.step()
        if octo.all_flashed():
            return i + 1
        octo.set_flashes_to_zero()

    return octo.total_flashes


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 1627

    result = solve(input_data, 9999999999999)
    print(f'Example 2: {result}')
    # 329