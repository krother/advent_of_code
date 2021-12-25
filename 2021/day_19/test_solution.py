import pytest

from .solution import get_orientations, solve, solve2, SMALL_INPUT
import numpy as np


def test_get_orientations():
    a = np.arange(12).reshape(4,3)
    oris = list(get_orientations(a))
    assert len(oris) == 24
    pos = [ori[1,0] for ori in oris]
    pos.sort()
    for ori in oris:
        print(ori)
    assert pos == [-5, -5, -5, -5,
                   -4, -4, -4, -4,
                   -3, -3, -3, -3,
                    3,  3,  3,  3,
                    4,  4,  4,  4,
                    5,  5,  5,  5]


def test_solve():
    assert solve(SMALL_INPUT) == 79

def test_solve2():
    assert solve2('vectors_small.csv') == 3621
