import pytest

from solution import solve, solve2

INPUT = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

# nasty border cases
INPUT2 = """
R 10
D 10
L 10
U 3
R 8
U 4
L 8
U 3
"""

INPUT3 = """
R 2
D 1
R 1
D 1
L 2
U 1
L 1
U 1
"""
EXAMPLES = [
    (INPUT, 62),
    (INPUT2, 97),
    (INPUT3, 10),
]


@pytest.mark.parametrize("data, expected", EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


def test_solve2():
    assert solve2(INPUT) == 952408144115
