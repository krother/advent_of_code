import pytest

from .solution import solve, solve2

INPUT = """
20
15
10
5
5
"""


def test_solve():
    assert solve(INPUT, 25) == 4

def test_solve2():
    assert solve2(INPUT, 25) == 3
