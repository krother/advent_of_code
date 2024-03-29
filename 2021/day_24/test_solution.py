import pytest

from .solution import solve, solve2, run

INPUT = """inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
"""

def test_run():
    assert run(INPUT, '1') == 7
    

def test_solve():
    assert solve(INPUT) == ...
