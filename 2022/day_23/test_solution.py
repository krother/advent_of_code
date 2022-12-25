
from solution import solve, solve2

INPUT = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

SMALL_INPUT = """
.....
..##.
..#..
.....
..##.
....."""

def test_solve():
    assert solve(SMALL_INPUT, rounds=3) == 25

def test_solve():
    assert solve(INPUT, rounds=10) == 110

def test_solve2():
    assert solve2(INPUT) == 20
