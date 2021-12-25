import pytest

from .solution import solve

INPUT = """target area: x=20..30, y=-10..-5"""


def test_solve():
    assert solve(INPUT) == (45, 112)

# def test_solve2():
#     assert solve2(INPUT) == INPUT
