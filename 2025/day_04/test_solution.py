from solution import solve, solve2

INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_solve():
    assert solve(INPUT) == 13


def test_solve2():
    assert solve2(INPUT) == 43
