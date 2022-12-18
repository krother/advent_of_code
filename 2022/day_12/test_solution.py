import pytest

from solution import solve, solve2

INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

def test_solve():
    assert solve(INPUT) == 31

def test_solve2():
    assert solve2(INPUT) == 29
