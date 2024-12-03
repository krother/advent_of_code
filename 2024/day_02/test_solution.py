import pytest

from solution import solve, solve2

INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
9 1 2 3 4
1 9 2 3 4
1 9 9 2 3
"""

EXAMPLES = [
    ("7 6 4 2 1", 1, 1),
    ("1 2 7 8 9", 0, 0),
    ("9 7 6 2 1", 0, 0),
    ("1 3 2 4 5", 0, 1),
    ("8 6 4 4 1", 0, 1),
    ("1 3 6 7 9", 1, 1),
    ("9 1 2 3 4", 0, 1),
    ("1 9 2 3 4", 0, 1),
    ("1 9 9 2 3", 0, 0),
    ("1 2 3 4 9", 0, 1),
    ("1 2 9 4 5", 0, 1),
    ("1 2 9 9 5", 0, 0),
    ("2 1 3 4 5", 0, 1),
    ("1 3 2 3 4", 0, 1),
]

@pytest.mark.parametrize('data,exp1,exp2', EXAMPLES)
def test_single(data,exp1, exp2):
    assert solve(data) == exp1
    assert solve2(data) == exp2

def test_solve():
    assert solve(INPUT) == 2

def test_solve2():
    assert solve2(INPUT) == 6
