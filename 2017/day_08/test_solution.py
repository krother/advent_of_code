import pytest

from solution import solve, solve2


INPUT = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

def test_solve():
    assert solve(INPUT) == 1

def test_solve2():
    assert solve2(INPUT) == 10
