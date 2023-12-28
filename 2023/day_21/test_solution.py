import pytest

from solution import solve, solve2

INPUT = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

EXAMPLES = [
    # (6, 16),
    # (10, 50),
    # (50, 1594),
    # (100, 6536),
    # (500, 167004),
    # (1000, 668697),
    # (5000, 16733044),
]

EMPTY = """
.....
.....
..S..
.....
.....
"""
EMPTY_EXAMPLES = [
    (1, 4),
    (2, 9),
    (3, 16),
    (4, 25),
    (5, 36),
    (6, 49),
    (7, 64),
    (8, 81),
    (9, 100),
    (10, 121),
    (11, 144),
    (999, 1_000_000),
]


def test_solve():
    assert solve(INPUT, 6) == 16


@pytest.mark.parametrize("steps,expected", EMPTY_EXAMPLES)
def test_solve2(steps, expected):
    assert solve2(EMPTY, steps) == expected
