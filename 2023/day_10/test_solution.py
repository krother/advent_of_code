from solution import solve, solve2

INPUT = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

INPUT2 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


def test_solve():
    assert solve(INPUT) == 8


def test_solve2():
    assert solve2(INPUT2, "D") == 10
