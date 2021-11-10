import pytest

from .solution import solve, get_output

EXAMPLES = (
    ('''value 5 goes to bot 7
value 4 goes to bot 7''', (5, 4), 7),
    ('''value 7 goes to bot 1
value 8 goes to bot 1''', (7, 8), 1),
    ('''value 1 goes to bot 99
value 2 goes to bot 99''', (1, 2), 99),
    ('''value 77 goes to bot 5
value 1 goes to bot 99
value 2 goes to bot 99''', (1, 2), 99),
    ('''value 1 goes to bot 99
value 77 goes to bot 5
value 2 goes to bot 99''', (1, 2), 99),
    ('''value 1 goes to bot 1
value 2 goes to bot 2
value 3 goes to bot 2''', (2, 3), 2),
    ('''value 77 goes to bot 5
value 1 goes to bot 99
value 2 goes to bot 99
value 66 goes to bot 333''', (1, 2), 99),

    ('''value 1 goes to bot 99
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 99''', (1, 2), 99),
    ('''value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 2
bot 1 gives low to bot 2 and high to output 0
''', (1, 3), 2),
 ('''value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 3
value 4 goes to bot 3
bot 1 gives low to bot 2 and high to output 0
bot 3 gives low to output 7 and high to bot 2
''', (1, 4), 2),
 ('''value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 3
value 4 goes to bot 4
bot 1 gives low to bot 3 and high to bot 4
bot 3 gives low to bot 2 and high to output 7
bot 4 gives low to output 8 and high to bot 2
''', (1, 4), 2),

    ("""value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""", (5, 2), 2),
)

EXAMPLES_OUT = (
    ('''
value 1 goes to bot 2
value 2 goes to bot 2
value 3 goes to bot 3
value 4 goes to bot 3
bot 2 gives low to bot 4 and high to output 0
bot 3 gives low to bot 4 and high to output 1
bot 4 gives low to bot 5 and high to output 2
''', (0, 1, 2), 24),
)


@pytest.mark.parametrize('instructions,query,expected', EXAMPLES)
def test_solve(instructions, query, expected):
    assert solve(instructions, query) == expected


@pytest.mark.parametrize('instructions,query,expected', EXAMPLES_OUT)
def test_get_output(instructions, query, expected):
    assert get_output(instructions, query) == expected
