import pytest

from .solution import solve, solve2

EXAMPLES = [
    ("""
5 1 9 5
7 5 3
2 4 6 8""", 18),
    ("""
1 1 2 2
3 4 5
6 7 8 9""", 6)
    ]

EXAMPLES2 = [
    ("""5 9 2 8
9 4 7 3
3 8 6 5""", 4+3+2)
]


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected

@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve2(data) == expected
