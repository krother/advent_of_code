import pytest

from solution import solve, solve2

INPUT = """
A Y
B X
C Z
"""

def test_solve():
    assert solve(INPUT) == 15

def test_solve2():
    assert solve2(INPUT) == 12
