import pytest

from solution import solve, solve2

INPUT = """
0
3
0
1
-3
"""

def test_solve():
    assert solve(INPUT) == 5

def test_solve2():
    assert solve2(INPUT) == 10
