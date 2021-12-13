import pytest

from .solution import solve, solve2

INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_solve():
    assert solve(INPUT) == 15

def test_solve2():
    assert solve2(INPUT) == 1134
