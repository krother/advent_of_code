import pytest

from .solution import solve, solve2

INPUT = """[{"a":{"b":4},"c":-1}, 5, {"c":"red","b":2}]"""

def test_solve():
    assert solve(INPUT) == 10

def test_solve2():
    assert solve2(INPUT) == 8
