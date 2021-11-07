import pytest

from .solution import solve, Building

EXAMPLES = (
    ("""
F4 .  HG .  .  .  
F3 E  .  HM .  . 
F2 .  .  .  .  .  
F1 .  .  .  .  .""", 1),
    ("""
F4 .  HG .  .  .  
F3 .  .  .  .  . 
F2 .  .  .  .  .  
F1 E  .  HM .  .""", 3),

    ("""
F4 .  HG .  .  .  
F3 .  .  .  .  . 
F2 E  .  HM .  .  
F1 .  .  .  .  .""", 2),

    ("""
F4 .  .  .  .  .  
F3 .  .  .  .  . 
F2 E  .  HM .  .  
F1 .  HG .  .  .""", 4),

    ("""
F4 E  .  HM .  .  
F3 .  .  .  .  . 
F2 .  .  .  .  .  
F1 .  HG .  .  .""", 6),

    ("""
F4 .  .  .  .  .
F3 E  HG .  .  . 
F2 .  .  .  .  .  
F1 .  .  HM .  .""", 5),

    ("""
F4 .  .  .  .  LM
F3 E  HG .  .  . 
F2 .  .  .  LG .  
F1 .  .  HM .  .""", 9),

    ("""
F4 .  .  .  .  .
F3 .  .  .  LG . 
F2 .  HG  . .  .  
F1 E  .  HM .  LM""", 11),

)

PARSE_EXAMPLES = (
    ('F4 E  .  .  .  LM', 4, 1, (0, 2)),
    ('F1 E  .  HM .  LM', 1, 2, (0, 2)),
)

CHECK_EXAMPLES = (
    ("F4 .  .  .  .  LM", True),
    ("F3 E  HG .  .  . ", True),
    ("F2 .  .  .  LG . ", True),
    ("F1 .  .  HM .  . ", True),
    ("F3 E  HG .  .  . ", True),
    ("F2 .  .  HM LG . ", False),
    ("F4 E  HG HM LG LM", True),
    ("F2 .  .  .  .  . ", True),
    ("F1 .  .  .  .  . ", True),
    ("F4 .  HG .  .  LM", False),
    ("F2 E  .  HM .  . ", True),
    ("F1 .  .  .  LG . ", True),

)

# @pytest.mark.parametrize('data,expected', CHECK_EXAMPLES)
# def test_check_floor(data,expected):
#     n, f = Building.parse_floor(data)
#     assert f.is_valid() == expected

# @pytest.mark.parametrize('data,floor,num,firstitem', PARSE_EXAMPLES)
# def test_parse_floor(data, floor, num, firstitem):
#     n, f = Building.parse_floor(data)
#     assert n == floor
#     assert len(list(f.items)) == num
#     assert next(f.items) == firstitem

@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected

# def test_building_repr():
#     b = Building("""
# F4 .  .  .  .  .
# F3 .  .  .  .  . 
# F2 .  HG  . LG .  
# F1 E  .  HM .  LM""")
#     assert str(b) == '<E1 (0, 3)(3, 0)(0, 0)(0, 0)>'

