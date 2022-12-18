import pytest

from solution import solve, solve2

INPUT = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""


def test_solve():
    assert solve(INPUT, 2022) == 3068

def test_solve2():
    assert solve2(INPUT, 1_000_000_000_000) == 1514285714288
