
from solution import solve, solve2

INPUT = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""

def test_solve():
    assert solve(INPUT) == 18

def test_solve2():
    assert solve2(INPUT) == 54
