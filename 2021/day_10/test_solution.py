import pytest

from .solution import solve, solve2

INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

SHORT = "[({(<(())[]>[[{[]{<()<>>"

def test_solve():
    assert solve(INPUT) == 26397

def test_solve2():
    assert solve2(INPUT) == 288957

def test_solve_short():
    assert solve2(SHORT) == 288957

