"""
https://adventofcode.com/2019/day/1
"""
def get_fuel(mass):
    return mass // 3 - 2

def get_more_fuel(mass):
    fuel = get_fuel(mass)
    if fuel > 0:
        fuel += max(0, get_more_fuel(fuel))
    return fuel

def solve(data):
    return sum(map(get_fuel, map(int, data.split('\n'))))


def solve2(data):
    return sum(map(get_more_fuel, map(int, data.split('\n'))))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')

    result = solve2(input_data)
    print(f'Example 2: {result}')
