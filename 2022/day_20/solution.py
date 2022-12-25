"""
Grove Positioning System

https://adventofcode.com/2022/day/1
"""

class Number:

    def __init__(self, num):
        self.number = num
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.number}'

    def move(self, chain_size):
        if self.number > 0:
            steps = self.number % (chain_size - 1)
        elif self.number < 0:
            steps = abs(self.number) % (chain_size - 1) + 1
        elif self.number == 0:
            steps = 0
        if steps == 0:
            return

        # remove
        self.prev.next = self.next
        self.next.prev = self.prev

        elem = self
        if self.number > 0:
            for i in range(steps):
                elem = elem.next
        elif self.number < 0:
            for i in range(steps):
                elem = elem.prev

        # insert after elem
        self.next = elem.next
        self.prev = elem
        elem.next.prev = self
        elem.next = self


    def to_list(self):
        result = [self.number]
        elem = self.next
        while elem is not self:
            result.append(elem)
            elem = elem.next
        return result


def parse(data, key):
    numbers = list(map(int, data.strip().split('\n')))
    chain = []
    for n in numbers:
        chain.append(Number(n * key))

    for i, num in enumerate(chain[:-1]):
        num.next = chain[i+1]
    for i, num in enumerate(chain[1:], 1):
        num.prev = chain[i-1]

    chain[-1].next = chain[0]
    chain[0].prev = chain[-1]
    return chain


def mix(chain):
    for num in chain:
        num.move(len(chain))
        #print(num.to_list())


def check(chain):
    # consistency check
    for c in chain:
        assert c.prev.next is c
        assert c.next.prev is c
    assert len(chain[0].to_list()) == len(chain)


def find_target(chain):
    # find target numbers
    zero = [c for c in chain if c.number == 0][0]
    print(len(zero.to_list()))
    total = 0
    for i in (1000, 2000, 3000):
        elem = zero
        for j in range(i):
            elem = elem.next
        print(elem.number, end=';')
        total += elem.number
    return total


def solve(data, key=1):
    chain = parse(data, key)
    mix(chain)
    check(chain)
    return find_target(chain)


def solve2(data, key=811589153):
    chain = parse(data, key)
    for _ in range(10):
        mix(chain)
        check(chain)
    return find_target(chain)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
