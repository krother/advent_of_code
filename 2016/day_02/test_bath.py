
import pytest
from bath import find_code, DIAMOND_KEYPAD

EXAMPLES = [
    ('', 5)
]

SQUARE_PAD_INSTRUCTIONS = [
    ('U', '2'),
    ('UL', '1'),
    ('L', '4'),
    ('R', '6'),
    ('D', '8'),
    ('ULL', '1'),
    ('RDDD', '9'),
    ('LURDL', '4'),
    ('UUUUD', '5'), 
    ('U\nU', '22'),
    ('U\nD', '25'),
    ('LLULURURURDRDRDLDLDLULR', '5'), # round trip
    ("""ULL
RRDDD
LURDL
UUUUD""", '1985'),
]

DIAMOND_PAD_INSTRUCTIONS = [
    ('U', '5'),
    ('DLURURULURDRDRUDRLDLDDLRULUL', '5'), # round trip
    ("""ULL
RRDDD
LURDL
UUUUD""", '5DB3'),
]

@pytest.mark.parametrize('instructions, code', SQUARE_PAD_INSTRUCTIONS)
def test_find_code(instructions, code):
    assert find_code(instructions) == code


@pytest.mark.parametrize('instructions, code', DIAMOND_PAD_INSTRUCTIONS)
def test_find_code_diamond(instructions, code):
    assert find_code(instructions, DIAMOND_KEYPAD) == code
