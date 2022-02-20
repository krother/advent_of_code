"""
Day 14: Reindeer Olympics

https://adventofcode.com/2015/day/14

"""
import re

REINDEER = r'\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'

class Reindeer:

    def __init__(self, speed, fly_time, rest_time):
        self.speed = int(speed)
        self.fly_time = int(fly_time)
        self.rest_time = int(rest_time)
        self.flying = 0
        self.resting = 0
        self.distance = 0
        self.points = 0

    def next_second(self):
        if self.flying < self.fly_time:
            self.flying += 1
            self.distance += self.speed
        else:
            self.resting += 1
            if self.resting >= self.rest_time:
                self.flying = 0
                self.resting = 0

    def check_lead(self, maxdist):
        if self.distance == maxdist:
            self.points += 1

def parse(data):
    return [Reindeer(*rd) for rd in re.findall(REINDEER, data)]


def solve(data, seconds):
    reindeers = parse(data)
    for i in range(seconds):
        for rd in reindeers:
            rd.next_second()

        maxdist = max([rd.distance for rd in reindeers])
        for rd in reindeers:
            rd.check_lead(maxdist)

    maxdist = max([rd.distance for rd in reindeers])
    maxpoints = max([rd.points for rd in reindeers])
    return maxdist, maxpoints

def solve2(data):
    return data

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result1, result2 = solve(input_data, 2503)
    print(f'Example 1: {result1}')
    print(f'Example 2: {result2}')
