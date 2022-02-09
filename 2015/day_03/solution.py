"""title

https://adventofcode.com/2021/day/1

"""

class Santa:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, c):
        if c == '>':
            self.x += 1
        elif c == '<':
            self.x -= 1
        elif c == 'v':
            self.y += 1
        elif c == '^':
            self.y -= 1
        return self.x, self.y


def solve(data):
    visited = {(0, 0)}
    santa = Santa()
    for c in data:
        pos = santa.move(c)
        visited.add(pos)
    return len(visited)


def solve2(data):
    visited = {(0, 0)}
    santas = [Santa(), Santa()]
    s = 0
    for c in data:
        pos = santas[s].move(c)
        visited.add(pos)
        s = 1 - s
    return len(visited)

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
