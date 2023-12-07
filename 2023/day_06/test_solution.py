from solution import solve, solve2

INPUT = """
Time:      7  15   30
Distance:  9  40  200
"""


def test_solve():
    assert solve(INPUT) == 288


def test_solve2():
    assert solve2(INPUT) == 71503
