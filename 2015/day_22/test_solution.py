import pytest

from .solution import (
    Wizard,
    Boss,
    parse_boss,
    find_best_spells,
    solve,
    solve2
)

INPUT = """Hit Points: 12
Damage: 17
"""


def test_parse_boss():
    boss = parse_boss(INPUT)
    assert boss.hp == 12
    assert boss.damage == 17

FIGHTS = [
    (Wizard(100, 500), Boss(4, 1), 53),   # missile
    (Wizard(100, 500), Boss(5, 1), 106),  # missile, missile
    (Wizard(100, 500), Boss(9, 1), 159),  # missile, missile, missile
    (Wizard(5, 500), Boss(5, 5), 219),    # shield, missile, missile
    (Wizard(100, 500), Boss(30, 1), 332), # poison, missile, missile, missile
    (Wizard(100, 229), Boss(20, 1), 494), # recharge, missile, missile, missile, missile, missile
    (Wizard(1, 500), Boss(5, 1), 126),    # drain, missile
    (Wizard(10, 250), Boss(14, 8), 229 + 113 + 73 + 173 + 53),   # recharge, shield, drain, poison, missile
    (Wizard(100, 173), Boss(18, 1), -1),  # can't afford enough spells
    (Wizard(100, 1), Boss(1, 1), -1),     # can't afford any spells
]

@pytest.mark.parametrize('wizard,boss,expected', FIGHTS)
def test_find_best_spells(wizard, boss, expected):
    assert find_best_spells(wizard, boss) == expected


@pytest.mark.parametrize('wizard,boss,expected_hp', [
    (Wizard(200, 500), Boss(100, 1), 199),
    (Wizard(100, 500), Boss(100, 7), 93),
])
def test_boss_hits(wizard, boss, expected_hp):
    boss.hit(wizard)
    assert wizard.hp == expected_hp


def test_boss_hits_shield():
    wizard = Wizard(100, 500)
    wizard.shield()
    boss = Boss(100, 7)
    boss.hit(wizard)
    assert wizard.hp == 99
