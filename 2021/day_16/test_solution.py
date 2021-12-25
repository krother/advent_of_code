import pytest

from .solution import all_bin, solve, solve2, parse

INPUT = """
"""

def test_parse_literal():
    lit = parse('D2FE28')[0]
    assert lit.version == 6
    assert lit.value == 2021

def test_parse_operator():
    op = parse('38006F45291200')[0]
    assert op.version == 1

def test_parse_operator_sub():
    op = parse('EE00D40C823060')[0]
    assert op.version == 7

def test_hextobin():
    assert all_bin('D2FE28') == '110100101111111000101000'


VERSION_SUM = [
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31)
]
@pytest.mark.parametrize('data,vsum', VERSION_SUM)
def test_solve(data, vsum):
    assert solve(data) == vsum

EQUATION = [
    ('C200B40A82', 3),
    ('04005AC33890', 54),
    ('880086C3E88112', 7),
    ('CE00C43D881120', 9),
    ('D8005AC2A8F0', 1),
    ('F600BC2D8F', 0),
    ('9C005AC2F8F0', 0),
    ('9C0141080250320F1802104A08', 1),
]
@pytest.mark.parametrize('data,expected', EQUATION)
def test_solve2(data, expected):
    assert solve2(data) == expected
