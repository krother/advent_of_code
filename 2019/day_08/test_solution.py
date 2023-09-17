import pytest

from solution import solve, solve2

EXAMPLES = [
    ("123456789012", 3, 2, 1),
    ("122456789012", 3, 2, 2),
    ("122156789012", 3, 2, 4),
    ("789012122156", 3, 2, 4),
    ("000012122100", 3, 2, 4),
    ("0000000012122100", 5, 2, 4),
]

@pytest.mark.parametrize('data,x,y,expected', EXAMPLES)
def test_solve(data, x, y, expected):
    assert solve(data, x, y) == expected


EXAMPLES2 = [
    ("0000000000000000", 2, 2, "00\n00"),
    ("0222112222120000", 2, 2, "01\n10"),
]

@pytest.mark.parametrize('data,x,y,expected', EXAMPLES2)
def test_solve2(data, x, y, expected):
    assert solve2(data, x, y) == expected
