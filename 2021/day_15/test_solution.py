import pytest

from .solution import solve, solve2, parse, make_big_map

INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def test_solve():
    assert solve(INPUT) == 40

def test_solve2():
    assert solve2(INPUT) == 315

def test_big_map():
    data = """33
33
"""
    a = parse(data)
    b = make_big_map(a)
    assert b.sum() == 592