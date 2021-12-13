import pytest

from .solution import solve

INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def test_solve():
    assert solve(INPUT) == 1656

def test_solve2():
    assert solve(INPUT, 999999999999) == 195
