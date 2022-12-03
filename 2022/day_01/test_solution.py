
from solution import solve, solve2

INPUT = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def test_solve():
    assert solve(INPUT) == 24000

def test_solve2():
    assert solve2(INPUT) == 45000
