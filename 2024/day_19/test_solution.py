from solution import solve, solve2

INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


def test_solve():
    assert solve(INPUT) == 6


def test_solve2():
    assert solve2(INPUT) == 16
