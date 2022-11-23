"""title

https://adventofcode.com/2021/day/1

"""


def solve(data):
    cycles = 0
    steps = [int(line) for line in data.strip().split('\n')]
    i = 0
    while 0 <= i < len(steps):
        target = i + steps[i]
        steps[i] += 1
        cycles += 1
        i = target
    return cycles


def solve2(data):
    cycles = 0
    steps = [int(line) for line in data.strip().split('\n')]
    i = 0
    while 0 <= i < len(steps):
        target = i + steps[i]
        if steps[i] >= 3:
            steps[i] -= 1
        else:
            steps[i] += 1
        cycles += 1
        i = target
    return cycles



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
