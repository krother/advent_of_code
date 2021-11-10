import pytest

from .solution import solve, solve_across

EXAMPLES = (
    (1, 1),
    (2, 1),
    (3, 3),
    (4, 1),
    (5, 3),
    (6, 5),
    (7, 7),
)

ACROSS_EXAMPLES = (
    (1, 1),
    (2, 1),
    (3, 3),
    (4, 1),
    (5, 2),
    (6, 3),
    (7, 5),
    (8, 7),
    (9, 9),
    (10, 1),
    (11, 2),
    (12, 3),
    (1000, 271),
)

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected

@pytest.mark.parametrize('data,expected', ACROSS_EXAMPLES)
def test_solve_across(data, expected):
    assert solve_across(data) == expected
