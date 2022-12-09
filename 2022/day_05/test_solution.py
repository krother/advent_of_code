import pytest

from solution import solve, solve2

INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def test_solve():
    assert solve(INPUT) == "CMZ"

def test_solve2():
    assert solve2(INPUT) == "MCD"
