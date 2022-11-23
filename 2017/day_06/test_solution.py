import pytest

from solution import solve, solve2, redistribute

INPUT = """0 2 7 0"""

EXAMPLES = [
    ((0, 2, 7, 0), (2, 4, 1, 2)),
    ((2, 4, 1, 2), (3, 1, 2, 3)),
    ((3, 1, 2, 3), (0, 2, 3, 4)),
    ((0, 2, 3, 4), (1, 3, 4, 1)),
    ((1, 3, 4, 1), (2, 4, 1, 2))
]

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_redistribute(data, expected):
    assert redistribute(data) == expected

def test_solve():
    assert solve(INPUT) == 5

def test_solve2():
    assert solve2(INPUT) == 4
