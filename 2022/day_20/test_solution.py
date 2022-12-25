import pytest

from solution import solve, solve2

INPUT = """
1
2
-3
3
-2
0
4"""

def test_solve():
    assert solve(INPUT) == 3

def test_solve2():
    assert solve2(INPUT) == 1623178306
