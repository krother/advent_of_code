import pytest

from .solution import solve, get_moves


EXAMPLES = (
    ('ihgpwlah', 'DDRRRD'),
    ('kglvqrro', 'DDUDRLRRUDRD'),
    ('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'),
)

LONG_EXAMPLES = (
    ('ihgpwlah', 370),
    ('kglvqrro', 492),
    ('ulqzkmiv', 830),
)

MOVE_EXAMPLES = (
    ('hijkl', (0, 0), '', [((0, 1), 'D')]),
    ('hijkl', (0, 1), 'D', [((0, 0), 'DU'), ((1, 1), 'DR')]),
    ('hijkl', (1, 1), 'DR', []),
    ('hijkl', (0, 0), 'DU', [((1, 0), 'DUR')]),
    ('hijkl', (1, 0), 'DUR', []),

)

@pytest.mark.parametrize('passcode,path,pos,expected', MOVE_EXAMPLES)
def test_get_moves(passcode, path, pos, expected):
    assert get_moves(passcode, path, pos) == expected


@pytest.mark.parametrize('passcode,path', EXAMPLES)
def test_solve(passcode, path):
    assert solve(passcode) == path


@pytest.mark.parametrize('passcode,length', LONG_EXAMPLES)
def test_solve_longest(passcode, length):
    assert len(solve(passcode, shortest=False)) == length
