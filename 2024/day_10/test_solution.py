from solution import solve, solve2

INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def test_solve():
    assert solve(INPUT) == 36


def test_solve2():
    assert solve2(INPUT) == 81
