import pytest

from .solution import execute, solve, solve2

INPUT = """
inc a
jio a, +2
tpl a
inc a
"""

FAILS = [
    ({'a': 3, 'b': 0}, 'hlf a'),
]

EXAMPLES = [
    ({'a': 0, 'b': 0}, 'inc a', {'a': 1, 'b': 0}),
    ({'a': 0, 'b': 0}, 'inc b', {'a': 0, 'b': 1}),

    ({'a': 0, 'b': 2}, 'hlf a', {'a': 0, 'b': 2}),
    ({'a': 2, 'b': 0}, 'hlf a', {'a': 1, 'b': 0}),
    ({'a': 4, 'b': 0}, 'hlf a', {'a': 2, 'b': 0}),
    ({'a': 7, 'b': 6}, 'hlf b', {'a': 7, 'b': 3}),

    ({'a': 1, 'b': 1}, 'tpl a', {'a': 3, 'b': 1}),
    ({'a': 2, 'b': 3}, 'tpl b', {'a': 2, 'b': 9}),

    ({'a': 0, 'b': 0}, 'inc a\ninc a', {'a': 2, 'b': 0}),
    ({'a': 0, 'b': 0}, 'inc a\ninc b', {'a': 1, 'b': 1}),
    ({'a': 0, 'b': 0}, 'inc b\ntpl b', {'a': 0, 'b': 3}),

    ({'a': 0, 'b': 0}, 'jmp +1', {'a': 0, 'b': 0}),
    ({'a': 0, 'b': 0}, 'inc a\njmp +1\ninc a', {'a': 2, 'b': 0}),
    ({'a': 0, 'b': 0}, 'inc a\njmp +2\ninc a\ninc a', {'a': 2, 'b': 0}),

    ({'a': 2, 'b': 0}, 'jie a, +2\ninc a\ninc a', {'a': 3, 'b': 0}),
    ({'a': 3, 'b': 0}, 'jie a, +2\ninc a\ninc a', {'a': 5, 'b': 0}),

    ({'a': 0, 'b': 0}, 'inc a\njio a, +2\ninc a', {'a': 1, 'b': 0}),
]


@pytest.mark.parametrize('reg_in, code, reg_out', EXAMPLES)
def test_execute(reg_in, code, reg_out):
    assert execute(reg_in, code) == reg_out


@pytest.mark.parametrize('reg_in, code', FAILS)
def test_execute_fails(reg_in, code):
    with pytest.raises(Exception):
        execute(reg_in, code)


def test_solve():
    assert solve(INPUT) == {'a': 2, 'b': 0}


def test_solve2():
    assert solve2(INPUT) == {'a': 7, 'b': 0}
