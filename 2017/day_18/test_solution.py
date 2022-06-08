import pytest

from .solution import solve, solve2


CODE = [
    (
        'set a 1', {'a': 1, 'b': 0}, 0
    ),
    (
        'set c 2', {'c': 2, 'a': 0}, 0
    ),
    (
        '''
        set a 2
        add a 4
        ''', {'a': 6}, 0
    ),
    (
        '''
        set a 2
        set b 3
        add a b
        ''', {'a': 5, 'b': 3}, 0
    ),
    (
        '''
        set a 6
        set b 7
        mul a b
        ''', {'a': 42, 'b': 7}, 0
    ),
    (
        '''
        set a 11
        set b 3
        mod a b
        ''', {'a': 2, 'b': 3}, 0
    ),
    (
        '''
        snd 42
        ''', {}, 42
    ),
    (
        '''
        set a 7
        snd a
        ''', {}, 7
    ),
    (
        '''
        snd 42
        set a 1
        rcv a
        ''', {'a': 1, 'output': 42}, 42
    ),
    (
        '''
        set a 1
        jgz a 2
        set a 42
        set b 36
        ''', {'a': 1, 'b': 36}, 0
    ),
    (
        """
        set a 1
        add a 2
        mul a a
        mod a 5
        snd a
        set a 0
        rcv a
        jgz a -1
        set a 1
        jgz a -2
        """, {'output': 4}, 0
    )

]

@pytest.mark.parametrize('instructions,expected_regs,last', CODE)
def test_solve(instructions, expected_regs, last):
    reg, stack = solve(instructions)
    for r in expected_regs:
        assert reg[r] == expected_regs[r]
    if last:
        assert last == stack.pop()


#def test_solve2():
#    assert solve2(INPUT) == INPUT
