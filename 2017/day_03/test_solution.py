import pytest

from .solution import solve, solve2

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

#def test_solve2():
#    assert solve2(INPUT) == INPUT
