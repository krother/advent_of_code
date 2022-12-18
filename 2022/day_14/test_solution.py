import pytest

from solution import solve, solve2

INPUT = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

def test_solve():
    assert solve(INPUT) == 24

def test_solve2():
    assert solve2(INPUT) == 93
