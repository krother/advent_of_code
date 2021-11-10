
import pytest
from rep import get_consensus


EXAMPLES = [
    ('a', 'a'),
    ('b', 'b'),
    ('b\na\na', 'a'),
    ('ab\nab', 'ab'),
    ("""eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""", 'easter')
]

@pytest.mark.parametrize('signal, code', EXAMPLES)
def test_get_consensus(signal, code):
    assert get_consensus(signal) == code


def test_get_consensus_least():
    assert get_consensus(EXAMPLES[-1][0], -1) == 'advent'

