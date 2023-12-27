from solution_part1 import solve

INPUT = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""
# 24, 13, 10 @ -3, 1, 2


def test_solve():
    assert solve(INPUT, 7, 27) == 2
