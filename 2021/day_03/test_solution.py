import pytest

from .solution import solve, solve2

EXAMPLES = (
    ("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""", 198),
)

EXAMPLES2 = (
    ("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""", 230),
)



@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES2)
def test_solve2(data, expected):
    assert solve2(data) == expected
