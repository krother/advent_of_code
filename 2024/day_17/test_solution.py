import pytest

from solution import solve, solve2, calc

INPUT = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

INPUT2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


def test_solve():
    assert solve(INPUT) == "4,6,3,5,6,3,5,2,1,0"


def test_reproduce():
    assert solve(INPUT2.replace("2024", "117440")) == "0,3,5,4,3,0"


def _test_solve2():
    assert solve2(INPUT2) == 117440
