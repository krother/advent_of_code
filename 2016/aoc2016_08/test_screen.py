
import pytest
from screen import display

EXAMPLES = [
    ('rect 3x2', """
###....
###....
......."""),

    ('rect 2x2', """
##.....
##.....
......."""),

    ('rect 3x2\nrotate column x=1 by 1', """
#.#....
###....
.#....."""),

    ('rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4', """
....#.#
###....
.#....."""),

    ('rect 3x2\nrotate column x=1 by 1\nrotate row y=0 by 4\nrotate column x=1 by 1', """
.#..#.#
#.#....
.#....."""),



]

@pytest.mark.parametrize('instructions, result', EXAMPLES)
def test_display(instructions, result):
    assert display(instructions).strip() == result.strip()
