import pytest

from solution_condensed import solve, solve2


CAVE = {
    'AA': (0, [('DD', 1), ('BB', 1), ('JJ', 2)]),
    'BB': (13, [('AA', 1), ('CC', 1)]),
    'CC': (2, [('BB', 1), ('DD', 1)]),
    'DD': (20, [('AA', 1), ('CC', 1), ('EE', 1)]),
    'EE': (3, [('DD', 1), ('HH', 3)]),
    'HH': (22, [('EE', 3)]),
    'JJ': (21, [('AA', 2)]),
}

def test_solve():
    assert solve(CAVE) == 1651

def test_solve2():
    assert solve2(CAVE) == 1707
