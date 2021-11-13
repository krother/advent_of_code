import pytest

from .solution import CommandParser, solve, unscramble

EXAMPLES = (
    ('abcde', """swap position 4 with position 0""", 'ebcda'),
    ('abcde', """swap position 1 with position 2""", 'acbde'),
    ('abcde', """swap position 1 with position 4""", 'aecdb'),

    ('abcde', """swap letter a with letter b""", 'bacde'),
    ('abcde', """swap letter d with letter b""", 'adcbe'),

    ('abcde', """reverse positions 0 through 4""", 'edcba'),
    ('abcde', """reverse positions 0 through 2""", 'cbade'),

    ('abcde', """rotate left 1 step""", 'bcdea'),
    ('abcde', """rotate left 2 steps""", 'cdeab'),
    ('abcde', """rotate left 10 steps""", 'abcde'),

    ('abcde', """rotate right 1 step""", 'eabcd'),
    ('abcde', """rotate right 3 steps""", 'cdeab'),
    ('abcde', """rotate right 10 steps""", 'abcde'),

    ('abcde', """move position 1 to position 4""", 'acdeb'),
    ('abcde', """move position 3 to position 0""", 'dabce'),
    ('abcde', """move position 0 to position 3""", 'bcdae'),

)

LONG_EXAMPLE = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d 
"""

EXAMPLES_IRREVERSIBLE = (
    ('abcde', """rotate based on position of letter b""", 'deabc'),
    ('abcde', """rotate based on position of letter d""", 'bcdea'),
    ('abcde', """rotate based on position of letter e""", 'eabcd'),

    ('abcde', LONG_EXAMPLE, 'decab',)

)

SANITY_EXAMPLES = []

instructions = LONG_EXAMPLE.strip().split('\n')
for i in range(1, len(instructions)-2): # last two commands irreversible!! 
    cmds = '\n'.join(instructions[:i])
    SANITY_EXAMPLES.append(('abcde', cmds))

instructions = open('input_data.txt').read().strip().split('\n')
for i in range(len(instructions) - 1):
    for j in range(i+1, len(instructions)): 
        cmds = '\n'.join(instructions[i:j])
        SANITY_EXAMPLES.append(('fbgdceah', cmds))


@pytest.mark.parametrize('psw,instructions,expected', EXAMPLES + EXAMPLES_IRREVERSIBLE)
def test_solve(psw, instructions, expected):
    assert solve(psw, instructions) == expected


def test_unrotate_based():
    expected = 'abcdefgh'
    assert unscramble('cdefghab', 'rotate based on position of letter e') == expected

@pytest.mark.parametrize('expected,instructions,psw', EXAMPLES)
def test_unscramble(psw, instructions, expected):
    assert unscramble(psw, instructions) == expected


@pytest.mark.parametrize('psw,instructions', SANITY_EXAMPLES)
def test_sanity(psw, instructions):
    unscrambled = unscramble(psw, instructions)
    rescrambled = solve(unscrambled, instructions)
    assert rescrambled == psw
