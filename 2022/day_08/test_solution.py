import pytest

from solution import solve, solve2

INPUT = """
30373
25512
65332
33549
35390
"""


def test_solve():
    assert solve(INPUT) == 21

def test_solve2():
    assert solve2(INPUT) == 8
