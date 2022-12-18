"""


https://adventofcode.com/2022/day/13
"""
WRONG, CORRECT, UNKNOWN = 0, 1, 2


def check_order(pak1, pak2):
    for a, b in zip(pak1, pak2):
        if type(a) == int and type(b) == int:
            if a > b:
                return WRONG
            elif a < b:
                return CORRECT
        else:
            if type(a) == int:
                a = [a]
            if type(b) == int:
                b = [b]
            result = check_order(a, b)
            if result in [CORRECT, WRONG]:
                return result
    if len(pak1) > len(pak2):
        return WRONG
    if len(pak1) < len(pak2):
        return CORRECT
    return UNKNOWN


class Packet:

    def __init__(self, data: str):
        self.p = eval(data)

    def __lt__(self, other):
        c = check_order(self.p, other.p)
        return c == CORRECT

    def __repr__(self):
        return str(self.p)



def solve(data):
    total = 0
    packets = data.strip().split('\n\n')
    for i, p in enumerate(packets, 1):
        pak1, pak2 = p.split('\n')
        pak1 = Packet(pak1)
        pak2 = Packet(pak2)
        if check_order(pak1.p, pak2.p):
            total += i
    return total


def solve2(data):
    data = data + "[[2]]\n[[6]]"
    data = data.replace('\n\n', '\n')
    packets = [Packet(p) for p in data.strip().split('\n')]
    packets.sort()
    result = 1
    for i, p in enumerate(packets, 1):
        if str(p) == "[[2]]":
            result *= i
        if str(p) == "[[6]]":
            result *= i
    return result


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    assert result == 5682

    result = solve2(input_data)
    print(f'Example 2: {result}')
    assert result == 20304
