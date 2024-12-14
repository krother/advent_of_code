import pytest

from solution import solve, solve2

INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_solve():
    assert solve(INPUT) == 11


def test_solve2():
    assert solve2(INPUT) == 31
