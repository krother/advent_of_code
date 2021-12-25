"""Dirac Dice

https://adventofcode.com/2021/day/21

"""
from collections import defaultdict


def deterministic_dice():
    die = 1
    while True:
        roll = die * 3 + 3
        yield roll
        die += 3

def move(pos, score, roll):
    pos = (pos + roll) % 10
    score += pos + 1
    return pos, score


def solve(p1, p2):
    p1, p2 = p1 - 1, p2 - 1
    s1, s2 = 0, 0
    die = deterministic_dice()
    rolls = 0
    while True:
        p1, s1 = move(p1, s1, next(die))
        rolls += 3
        if s1 >= 1000:
            return rolls * s2
        p1, p2, s1, s2 = p2, p1, s2, s1

def dirac():
    result = defaultdict(int)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                roll = d1 + d2 + d3
                result[roll] += 1
    print(result)
    return result

DIRAC = dirac()


def dirac_steps(position, score):
    for roll in DIRAC:
        p, s = move(position, score, roll)
        yield p, s, DIRAC[roll]


def solve2(p1, p2, end=21):
    p1, p2 = p1 - 1, p2 - 1
    universes = {(p1, p2, 0, 0): 1}
    p1win, p2win = 0, 0

    while universes:
        k = next(iter(universes))
        p1start, p2start, s1start, s2start = k
        occurences = universes[k]
        del universes[k]

        for p1, s1, occ1 in dirac_steps(p1start, s1start):
            if s1 >= end:
                p1win += occurences * occ1
            else:
                for p2, s2, occ2 in dirac_steps(p2start, s2start):
                    if s2 >= end:
                        p2win += occurences * occ1 * occ2
                    else:
                        occ = occurences * occ1 * occ2
                        k = (p1, p2, s1, s2)
                        if k not in universes:
                            universes[k] = 0
                        universes[k] += occ
    
    return max(p1win, p2win)


if __name__ == '__main__':
    result = solve(6, 2)
    print(f'Example 1: {result}')
    # 926610

    result = solve2(6, 2)
    print(f'Example 2: {result}')
    # 146854918035875
