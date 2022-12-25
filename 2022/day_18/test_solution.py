import pytest

from solution import solve, solve2

INPUT = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

def test_solve():
    assert solve(INPUT) == 64

def test_solve2():
    assert solve2(INPUT) == 58
