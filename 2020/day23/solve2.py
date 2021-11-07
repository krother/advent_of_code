
import re

cups = [3,8,9,1,2,5,4,6,7]

cups = [1,5,6,7,9,4,8,2,3]

lookup = {}


class Chain:
    
    def __init__(self, num, anext=None):
        self.num = num
        self.next = anext
        lookup[num] = self
    
    def __bool__(self):
        return True
    
    def pick(self):
        picked = self.next
        self.next = picked.next.next.next
        picked.next.next.next = None
        return picked
    
    def find_chain(self, a):
        cup = self
        while cup.num != a and cup.next is not None:
            cup = cup.next
        
        if cup.num == a:
            return cup
        else:
            return None
    
    def find_dest(self, picked, highest):
        dest = self.num - 1
        while picked.find_chain(dest) or dest == 0:
            dest -= 1
            if dest <= 0:
                dest = highest
        return lookup[dest]
    
    def insert(self, picked):
        a = self.next
        self.next = picked
        picked.next.next.next = a
        
    def concat(self):
        """concat cup values until a one is found again"""
        result = ""
        cup = self.next
        while cup.num != 1:
            result += str(cup.num)
            cup = cup.next
        return result


def make_chain(cups):
    global lookup
    lookup = {}
    
    last = Chain(cups[-1])
    first = last
    for num in reversed(cups[:-1]):
        first = Chain(num, first)
    last.next = first
    return first


def play(cups, rounds):
    highest = max(cups)
    current = make_chain(cups)

    for i in range(rounds):
        if i % 100000 == 0:
            print(i)
        picked = current.pick()
        dest = current.find_dest(picked, highest)
        dest.insert(picked)
        current = current.next

    return current

def join(current):
    one = current.find_chain(1)
    result = one.concat()
    return result

assert join(play([3,8,9,1,2,5,4,6,7], 10)) == "92658374"
assert join(play([3,8,9,1,2,5,4,6,7], 100)) == "67384529"
assert join(play([1,5,6,7,9,4,8,2,3], 100)) == "82573496"

"""
big = [3,8,9,1,2,5,4,6,7] + list(range(10, 1_000_001))
cup = play(big, 10_000_000)
one = lookup[1]
assert one.next.num == 934001
assert one.next.next.num == 159792
print(one.next.num * one.next.next.num)
"""

big = [1,5,6,7,9,4,8,2,3] + list(range(10, 1_000_001))
cup = play(big, 10_000_000)
one = lookup[1]
print(one.next.num * one.next.next.num)
