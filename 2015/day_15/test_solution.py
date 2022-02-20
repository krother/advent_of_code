import pytest

from .solution import solve, solve2, parse, calc_value, find_best_spoons

INPUT = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

def test_calc_value():
    m = parse(INPUT)
    spoons = [1, 1]   # 10 butterscotch, 2 cinnamon
    assert calc_value(m, spoons) == 1 * 1 * 4 * 2

def test_find_best_spoons():
    m = parse(INPUT)
    spoons = find_best_spoons(m, 2)
    assert sum(spoons) == 2
    assert list(spoons) == [1, 1]

def test_solve():
    assert solve(INPUT) == 62842880

#def test_solve2():
#    assert solve2(INPUT) == INPUT
