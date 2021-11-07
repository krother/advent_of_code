import pytest

from .solution import solve, is_open

EXAMPLES = (
    ("""
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""", 5),

    ("""
Disc #1 has 2 positions; at time=0, it is at position 0.
Disc #2 has 2 positions; at time=0, it is at position 1.
""", 1),

    ("""
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 3 positions; at time=0, it is at position 1.
""", 0),

)

BOUNCE_EXAMPLES = (
    (1, 5, 4, 0, True),
    (2, 2, 1, 0, False),
    (1, 5, 4, 5, True),
    (2, 2, 1, 5, True),
)

@pytest.mark.parametrize('disc_no,positions,startpos,time,bounces', BOUNCE_EXAMPLES)
def test_is_open(disc_no,positions,startpos,time,bounces):
    assert is_open(disc_no, positions, startpos, time) == bounces

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
     assert solve(data) == expected
