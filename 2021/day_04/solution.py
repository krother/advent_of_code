"""Bingo

https://adventofcode.com/2021/day/4

"""

class Board:

    def __init__(self, board):
        self.board = []
        for line in board.strip().split('\n'):
            row = [int(x) for x in line.strip().split()]
            assert len(row) == 5
            self.board.append(row)
        assert len(self.board) == 5

    def mark(self, number):
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == number:
                    self.board[y][x] = -1

    def check(self):
        # rows
        for y in range(5):
            if sum(self.board[y]) == -5:
                return True
        # cols
        for x in range(5):
            if sum([self.board[y][x] for y in range(5)]) == -5:
                return True
    
    def calc_value(self):
        total = 0
        for y in range(5):
            for x in range(5):
                if self.board[y][x] > -1:
                    total += self.board[y][x]
        return total

    def __repr__(self):
        return str(self.board)


def parse(data):
    lines = data.split('\n\n')
    numbers = list(map(int, lines[0].split(',')))
    boards = [Board(bb) for bb in lines[1:]]
    return numbers, boards


def solve(data):
    numbers, boards = parse(data)
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.check():
                return b.calc_value() * n
    
    return data


def solve2(data):
    numbers, boards = parse(data)
    for n in numbers:
        new = []
        for b in boards:
            b.mark(n)
            if b.check():
                if len(boards) == 1:
                    return b.calc_value() * n
            else:
                new.append(b)
        boards = new
            


if __name__ == '__main__':
    solve2("""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""")

    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
    # 39902

    result = solve2(input_data)
    print(f'Example 2: {result}')
    # 26936
