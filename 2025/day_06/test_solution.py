
from solution import solve, solve2

INPUT = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

def test_solve():
    assert solve(INPUT) == 4277556

def test_solve2():
    assert solve2(INPUT) == 3263827
