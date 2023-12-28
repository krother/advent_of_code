from solution_part_one import solve
from solution_part_two import eval_blueprint, Candidate
from util import Blueprint, parse

INPUT = """
Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
"""


def _test_solve():
    assert solve(INPUT, 24) == 33


def test_eval2():
    """super ugly non-interface test"""
    bps = parse(INPUT)

    # blueprint #1: first actions: ----R-
    start = Candidate(
        bps[0],
        ore_bots=2,
        ore=3,
    )
    assert eval_blueprint(32, start, start_time=7) == 56

    # blueprint #2: first actions: --R-R
    start = Candidate(
        bps[1],
        ore_bots=3,
        ore=3,
    )
    assert eval_blueprint(32, start, start_time=6) == 62
