import pytest

from solution import solve, solve2

INPUT = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
54-72,2-42
74-94,51-93
"""

def test_solve():
    assert solve(INPUT) == 2

def test_solve2():
    assert solve2(INPUT) == 5
