import pytest

from .solution import (
    Character,
    Item,
    get_item_combinations,
    go_shopping,
    parse,
    parse_shop,
    solve,
    solve2
)

INPUT = """Hit Points: 12
Damage: 17
Armor: 2
"""

TINYSHOP = """
Weapons:    Cost  Damage  Armor
Dagger       10    999      0
Sword        11    999      0
Rubberduck  999      0      0

Armor:      Cost  Damage  Armor
dummy1      999     0       0

Rings:      Cost  Damage  Armor
dummy2      999     0       0
"""

MINISHOP = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Defense +1   20     0       1
"""

def test_parse():
    boss = parse(INPUT)
    assert boss.hp == 12
    assert boss.damage == 17
    assert boss.armor == 2

def test_shop():
    weapons, armor, rings = parse_shop(MINISHOP)
    assert len(weapons) == 2
    assert len(armor) == 2
    assert len(rings) == 3
    assert rings[0].cost == 25

def test_combine_items():
    item1 = Item(10, 2, 3)
    item2 = Item(20, 4, 5)
    item3 = item1 + item2
    assert item3 == Item(30, 6, 8)

def test_get_item_combinations():
    weapon = Item(10, 2, 0)
    armor = Item(20, 0, 3)
    ring1 = Item(30, 4, 5)
    ring2 = Item(40, 6, 7)
    result = list(get_item_combinations([weapon], [armor], [ring1, ring2]))
    assert len(result) == 1
    assert result[0] == Item(100, 12, 15)

def test_get_item_combinations_empty():
    weapon = Item(10, 2, 0)
    result = list(get_item_combinations([weapon], [], []))
    assert len(result) == 0

def test_go_shopping():
     shop = parse_shop(MINISHOP)
     result = list(go_shopping(*shop))
     assert len(result) == 60 # BUG: contains duplicates because of rings!!!
     assert Item(8, 4, 0) in result
     assert Item(46, 5, 1) in result
     assert Item(111, 7, 3) in result

def test_item_equal():
    item1 = Item(1, 2, 3)
    assert item1 == item1
    assert item1 == Item(1, 2, 3)
    assert item1 != Item(0, 2, 3)
    assert item1 != Item(1, 1, 3)
    assert item1 != Item(1, 2, 2)
    assert item1 != Item(3, 2, 1)

FIGHTS = [
    (Character(hp=1, damage=1, armor=0), Character(hp=10, damage=1, armor=0), False),
    (Character(hp=10, damage=1, armor=0), Character(hp=1, damage=1, armor=0), True),
    (Character(hp=10, damage=1, armor=0), Character(hp=5, damage=100, armor=0), False),
    (Character(hp=10, damage=1, armor=0), Character(hp=1, damage=100, armor=0), True),
    (Character(hp=2, damage=1, armor=0), Character(hp=2, damage=1, armor=0), True),
    (Character(hp=2, damage=1, armor=0), Character(hp=3, damage=1, armor=0), False),
    (Character(hp=2, damage=2, armor=0), Character(hp=3, damage=1, armor=0), True),
    # armor examples
    (Character(hp=1, damage=0, armor=0), Character(hp=1, damage=1, armor=0), True),
    (Character(hp=1, damage=0, armor=0), Character(hp=1, damage=1, armor=1), True),
    (Character(hp=1, damage=5, armor=0), Character(hp=5, damage=1, armor=5), False),
    (Character(hp=10, damage=1, armor=100), Character(hp=5, damage=100, armor=0), True),
    (Character(hp=2, damage=1, armor=0), Character(hp=2, damage=1, armor=10), True),
    (Character(hp=2, damage=1, armor=10), Character(hp=3, damage=1, armor=0), False),
]
@pytest.mark.parametrize('char1,char2,expected', FIGHTS)
def test_fight(char1, char2, expected):
    assert char1.fight(char2) is expected

def test_solve():
    assert solve(INPUT, TINYSHOP) == 10

def test_solve2():
    assert solve2(INPUT, TINYSHOP) == 2997
