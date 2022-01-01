import pytest

from .solution import solve

INPUT = """3,4,3,1,2
"""

EXAMPLES = [
    (1, 5),
    (2, 6),
    (3, 7),
    (4, 9),
    (18, 26),
    (80, 5934),
    (256, 26984457539)
]

@pytest.mark.parametrize('days,expected', EXAMPLES)
def test_step(days, expected):
    assert solve(INPUT, days) == expected
