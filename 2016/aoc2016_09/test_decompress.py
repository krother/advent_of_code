
import pytest
from decompress import decompress, decompress_v2

EXAMPLES = [
    ('A', 1),
    ('ADVENT', 6),
    ('A(1x5)BC', 7),
    ('(3x3)XYZ', 9),
    ('A(2x2)BCD(2x2)EFG', 11),
    ('(6x1)(1x3)A', 6),
    ('X(9x2)A(4x3)ABCY', 20),
    ('X(8x2)(3x3)ABCY', 18)
]


EXAMPLES_V2 = [
    ('A', 1),
    ('ADVENT', 6),
    ('A(1x5)BC', 7),
    ('(3x3)XYZ', 9),
    ('A(2x2)BCD(2x2)EFG', 11),
    ('(6x2)(1x1)A', 2),
    ('(6x2)(1x3)A', 6),
    ('X(8x2)(3x3)ABCY', 20),
    ('X(9x2)A(4x3)ABCY', 24),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
]


@pytest.mark.parametrize('code,result', EXAMPLES)
def test_decompress(code, result):
    assert decompress(code) == result


@pytest.mark.parametrize('code,result', EXAMPLES_V2)
def test_decompress_v2(code, result):
    assert decompress_v2(code) == result

