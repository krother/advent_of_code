import pytest

from solution import solve, solve2

INPUT = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


INPUT2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

def test_solve():
    assert solve(INPUT) == 13

def test_solve2():
    assert solve2(INPUT) == 1

def test_solve2_large():
    assert solve2(INPUT2) == 36
