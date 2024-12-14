import pytest

from solution import solve, solve2

INPUT = """
AAAA
BBCD
BBCC
EEEC
"""

EXAMPLES = [
    (INPUT, 140, 80),
    (
        """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""",
        772,
        436,
    ),
    (
        """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""",
        1930,
        1206,
    ),
]


@pytest.mark.parametrize("data,expected, exp2", EXAMPLES)
def test_solve(data, expected, exp2):
    assert solve(data) == expected
    assert solve2(data) == exp2
