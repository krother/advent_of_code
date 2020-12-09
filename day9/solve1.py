
import re
from pprint import pprint

def parse(fn):
    return [int(line.strip()) for line in open(fn)]

def search_sum(data, target):
    """finds 2 numbers that add to the target"""
    for i in data:
        for j in data:
            if i != j and i+j == target:
                return True

def solve(fn, pre):
    data = parse(fn)
    check = pre
    while check < len(data):
        start = max([check-pre, 0])
        if not search_sum(data[start:check], data[check]):
            return data[check]
        check += 1

def contig_slow(fn, num):
    """brute force, quadratic"""
    data = parse(fn)
    for i in range(len(data)-2):
        for j in range(i + 2, len(data)-1):
            s = sum(data[i:j])
            if s == num:
                return min(data[i:j]) + max(data[i:j])

def contig(fn, number):
    """single loop, linear time"""
    data = parse(fn)
    tail = 0
    head = 1
    total = data[tail]
    while head < len(data) - 1:
        if total == number:
            part = data[tail:head]
            return min(part) + max(part)
        elif total < number:
            total += data[head]
            head += 1
        else:
            total -= data[tail]
            tail += 1

assert solve('input.txt', 5)  == 127

assert contig('input.txt', 127) == 62

print(solve('input_big.txt', 25))
print(contig('input_big.txt', 167829540))
