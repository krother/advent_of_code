"""title

https://adventofcode.com/2021/day/6

"""
from collections import Counter, defaultdict


def parse(data):
    ages = list(map(int, data.strip().split(',')))
    return Counter(ages)


def solve(data, days=80):
    fish = parse(data)
    for _ in range(days):
        new = defaultdict(int)
        for age in fish:
            if age == 0:Zoom is open to discuss Day 6: https://us02web.zoom.us/j/85658719454
                new[8] = fish[age]
                new[6] += fish[age]
            else:
                new[age - 1] += fish[age]
        fish = new
    return sum(fish.values())


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')
    # 352872

    result = solve(input_data, 256)
    print(f'Example 2: {result}')
    # 1604361182149
