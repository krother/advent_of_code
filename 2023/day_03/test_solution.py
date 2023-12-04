from solution import solve, solve2

INPUT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip()


def test_solve():
    assert solve(INPUT) == 4361


def test_solve2():
    assert solve2(INPUT) == 467835
