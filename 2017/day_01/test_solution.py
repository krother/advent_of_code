import pytest

from .solution import solve, solve2

EXAMPLES = [
    ('1111', 4),
    ('1122', 3),
    ('1234', 0),
    ('91212129', 9),
    ('5334412345', 12)
]

EXAMPLES2 = [
    ('1111', 4),
    ('1122', 0),
    ('1212', 6),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4)
]

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected

@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve2(data) == expected
