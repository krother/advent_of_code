import pytest

from solution import solve, solve2

EXAMPLES = [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 1),
    (9, 2),
    (10, 3),
    (12, 3),
    (25, 4),
    (24, 3),
    (23, 2),
    (1024, 31),
]

@pytest.mark.parametrize('number,expected', EXAMPLES)
def test_solve(number, expected):
    assert solve(number) == expected

EXAMPLES2 = [
    (1, 2),
    (2, 4),
    (3, 4),
    (4, 5),
    (5, 10),
    (6, 10),
    (7, 10),
    (8, 10),
    (9, 10),
    (10, 11),
    (11, 23),
]

@pytest.mark.parametrize('number,expected', EXAMPLES2)
def test_solve2(number, expected):
    assert solve2(number) == expected
