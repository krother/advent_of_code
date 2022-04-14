"""
Day 20: Infinite Elves and Infinite Houses

https://adventofcode.com/2015/day/20
"""
from collections import defaultdict


def count_presents(house):
    presents = 0
    for elf in range(1, house + 1):
        if house % elf == 0:
            presents += elf * 10
    return presents


def solve(presents):
    house = 1
    while True:
        if count_presents(house) == presents:
            return house
        house += 1
        if house % 10_000 == 0:
            print(house, count_presents(house))


def solve(target):
    house = 1
    bookings = defaultdict(set)
    while True:
        elves = bookings[house]
        elves.add(house)
        presents = sum(elves) * 10
        if presents >= target:
            return house
        for e in elves:
            bookings[house + e].add(e)
        if house % 10_000 == 0:
            print(house, count_presents(house))
        house += 1


def solve2(data):
    return data


if __name__ == '__main__':
    result = solve(29_000_000)
    print(f'Example 1: {result}')

    #result = solve2(input_data)
    #print(f'Example 2: {result}')
