"""
Bingo

https://adventofcode.com/2021/day/4

"""
import numpy as np
from aoc import parse_numbers


class Board:

    def __init__(self, board):
        self.board = np.array(parse_numbers(board), int).reshape(5, 5)

    def mark(self, number):
        mask = self.board == number
        self.board[mask] = -1

    def check(self):
        if -5 in self.board.sum(axis=0) or -5 in self.board.sum(axis=1):
            return True

    def calc_value(self):
        return self.board[self.board > -1].sum()

    def __repr__(self):
        return str(self.board)


def parse(data):
    lines = data.split('\n\n')
    numbers = list(map(int, lines[0].split(',')))
    boards = [Board(bb) for bb in lines[1:]]
    return numbers, boards


def get_winners(boards, numbers):
    for n in numbers:
        new = []
        for b in boards:
            b.mark(n)
            if b.check():
                yield b.calc_value() * n
            else:
                new.append(b)
        boards = new


def solve(data):
    numbers, boards = parse(data)
    winners = get_winners(boards, numbers)
    return next(winners)


def solve2(data):
    numbers, boards = parse(data)
    winners = list(get_winners(boards, numbers))
    return winners[-1]            


if __name__ == '__main__':

    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    # 39902

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 26936
