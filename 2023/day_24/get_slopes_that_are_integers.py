"""
Never Tell Me The Odds

https://adventofcode.com/2023/day/24
"""
from collections import defaultdict
from pprint import pprint
from util import parse
from itertools import product
import math

MR = -110  # estimated value


def create_lookup_dict(m_stone, b_stone):
    """
    we want to look up intercepts of hail stones
    grouped by their slopes
    """
    bs_groups = defaultdict(list)
    for ms, bs in zip(m_stone, b_stone):
        bs_groups[ms].append(bs)
    return bs_groups


def search_axis(m_stone, b_stone):
    # b_stone: the velocity of a hail stone
    # ms: the velocity of two hails moving at same speed
    bs_groups = create_lookup_dict(m_stone, b_stone)

    # examine each group
    for ms in bs_groups:
        diffs = set()
        for bs1, bs2 in product(bs_groups[ms], bs_groups[ms]):
            if bs1 == bs2:
                continue
            diffs.add(abs(bs1 - bs2))
            # print("bs1-bs2 : ", (bs1 - bs2))
            print("div     : ", (bs1 - bs2) / (MR - ms))  # double check divisions

        if len(diffs) > 1:
            denoms = set()
            for diff1, diff2 in product(diffs, diffs):
                if diff1 != diff2:
                    v = math.gcd(diff1, diff2)
                    denoms.add(v)

            print(f"\ndeltat = (bs1 - bs2) / (mr - {ms})")
            print(f"valid max denominators for ms = {ms}")
            print(denoms)
            print("possible mr values")
            mr = [d + ms for d in denoms] + [-d + ms for d in denoms]
            print(mr)
            # diff: the difference of starting positions of hails


def solve2(data):
    stones = parse(data)
    print("\n\n")
    for axis in [0]:  # xyz
        print("\n\naxis: ", "xyz"[axis])
        b_stone = [s[axis] for s in stones]
        m_stone = [s[axis + 3] for s in stones]
        search_axis(m_stone, b_stone)

    return 0


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve2(input_data)
    print(f"Example 2: {result}")
