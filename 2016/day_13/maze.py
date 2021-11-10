"""
AOC 2016-13
"""
class MazeException(Exception): pass


class Maze:

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, base) -> None:
        self.base = base

    def is_position_open(self, x, y):
        if x < 0 or y < 0:
            return False
        num = x*x + 3*x + 2*x*y + y + y*y + self.base
        return bin(num).count('1') % 2 == 0

    def find_moves(self, position):
        possible_moves = set()
        x, y = position
        for dx, dy in self.moves:
            xcheck, ycheck = x + dx, y + dy
            if self.is_position_open(xcheck, ycheck):
                possible_moves.add((xcheck, ycheck))
        return possible_moves

    def get_adjacent_positions(self, positions):
        adjacent = set()
        for p in positions:
            moves = self.find_moves(p)
            adjacent = adjacent.union(moves)
        return adjacent

    def find_path_length(self, start, stop, max_iter):
        positions = {start}
        i = 0
        while not stop in positions:
            positions = self.get_adjacent_positions(positions)
            i += 1
            if i == max_iter:
                raise MazeException("maximum iterations exceeded")
        return i

    def count_positions_visited(self, start, steps):
        positions = {start}
        for i in range(steps):
            positions = positions.union(self.get_adjacent_positions(positions))
        return len(positions)


def find_path_length(base, stop, max_iter=100):
    m = Maze(base)
    return m.find_path_length((1, 1), stop, max_iter)


def count_positions_visited(base, steps):
    m = Maze(base)
    return m.count_positions_visited((1, 1), steps)


if __name__ == '__main__':
    first = find_path_length(base=1352, stop=(31, 39), max_iter=10000)
    print(first)

    second = count_positions_visited(base=1352, steps=50)
    print(second)
