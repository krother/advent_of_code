"""
Day 19: An Elephant Named Joseph

https://adventofcode.com/2016/day/19

"""

def solve(n):
    elves = list(range(1, n+1))
    stay = 0

    while len(elves) > 1:
        last = elves[-1]
        elves = elves[stay::2]
        stay = 1 if elves[-1] == last else 0
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
    result = solve(3012210)
    print(f'Example 1: {result}')

    result = solve_across(3012210)
    print(f'Example 2: {result}')
