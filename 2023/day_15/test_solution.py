import pytest

from solution import solve, solve2, get_hash

EXAMPLES = [
    ("rn=1", 30),
    ("cm-", 253),
    ("qp=3", 97),
    ("cm=2", 47),
    ("qp-", 14),
    ("pc=4", 180),
    ("ot=9", 9),
    ("ab=5", 197),
    ("pc-", 48),
    ("pc=6", 214),
    ("ot=7", 231),
]
INPUT = ",".join([s for s, _ in EXAMPLES])


@pytest.mark.parametrize("data,expected", EXAMPLES)
def test_hash(data, expected):
    assert get_hash(data) == expected


def test_solve():
    assert solve(INPUT) == 1320


def test_solve2():
    assert solve2(INPUT) == 145
