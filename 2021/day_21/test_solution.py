import pytest

from .solution import solve, solve2

INPUT = """
"""


def test_solve():
    assert solve(4, 8) == 739785

def test_solve2():
    assert solve2(4, 8) == 444356092776315

