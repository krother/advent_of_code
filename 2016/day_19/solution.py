"""Day 19: An Elephant Named Joseph

https://adventofcode.com/2016/day/19

"""
from collections import deque
import pandas as pd


class Chain:

    def __init__(self, n):
        self.n = n
        self.next = None


def solve(n):
    elves = list(range(1, n+1))
    stay = 0

    while len(elves) > 1:
        last = elves[-1]
        elves = elves[stay::2]
        stay = 1 if elves[-1] == last else 0
    return elves[0]

def solve_across(n):
    elim = []
    elves = list(range(1, n+1))
    while len(elves) > 1:
        i = len(elves) // 2
        #elim.append(elves[i])
        elves = elves[1:i] + elves[i+1:] + elves[:1]

    # print(elim)
    # print()

    # a = pd.Series(elim)
    # d = a.diff()
    # d[d<0] += n
    # d = d.fillna(0).astype(int)
    # print(list(d))
    
    return elves[0]



def solve_across(n):
    """DP algorithm"""
    winner = 1
    for elves in range(2, n + 1):
        elim = elves // 2 + 1
        winner = 1 + winner
        if winner >= elim:
            winner += 1 
        if winner > elves:
            winner %= elves
    
    return winner


if __name__ == '__main__':
    result = solve(3012210) # 2/3 -> 1_000_000 -> 333_333 ~> 100_000
    print(f'Example 1: {result}')

    result = solve_across(3012210)
    print(f'Example 2: {result}')
