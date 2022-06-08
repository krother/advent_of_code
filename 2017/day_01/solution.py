"""title

https://adventofcode.com/2021/day/1

"""


def solve(data):
    i = 0
    total = 0
    for i, digit in enumerate(data):
        if digit == data[i - 1]:
            total += int(digit)
        i += 1
    return total

def solve2(data):
    total = 0
    for i, digit in enumerate(data):
        match = (i + len(data) // 2) % len(data)
        if digit == data[match]:
            total += int(digit)
    return total


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data.strip())
    print(f'Example 2: {result}')
