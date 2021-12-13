import pytest

from .solution import solve, get_cost, cost_func2

INPUT = """16,1,2,0,4,2,7,1,2,14"""


def test_cost():
    assert get_cost(1) == 1
    assert get_cost(4) == 10
    assert get_cost(3) == 6

def test_solve():
    assert solve(INPUT) == 37

def test_solve2():
    assert solve(INPUT, cost_func2) == 168
