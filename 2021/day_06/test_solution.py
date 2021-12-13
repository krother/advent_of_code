import pytest

from .solution import solve

INPUT = """3,4,3,1,2
"""

def test_18():
    assert solve(INPUT, 18) == 26

def test_solve():
    assert solve(INPUT) == 5934

def test_solve2():
    assert solve(INPUT, 256) == 26984457539
