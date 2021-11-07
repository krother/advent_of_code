
import re

cups = [3,8,9,1,2,5,4,6,7]

cups = [1,5,6,7,9,4,8,2,3]

def pick(cups):
    picked = cups[1:4]
    cups = [cups[0]] + cups[4:]
    return cups, picked

def find_dest(cups, picked, highest):
    dest = cups[0] - 1
    while dest in picked or dest == 0:
        dest -= 1
        if dest <= 0:
            dest = highest
    pos = cups.index(dest)
    return pos

def arrange(cups, picked, pos):
    cups = cups[:pos+1] + list(picked) + cups[pos+1:]
    cups = cups[1:] + [cups[0]]
    return cups

def play(cups, rounds):
    highest = max(cups)
    for i in range(rounds):
        #if i % 1000 == 0:
        #print(i)
        cups, picked = pick(cups)
        pos = find_dest(cups, picked, highest)
        cups = arrange(cups, picked, pos)

    return cups

def join(cups):
    one = cups.index(1)
    result = cups[one+1:] + cups[:one]
    s = ''.join(map(str, result))
    return s

assert join(play([3,8,9,1,2,5,4,6,7], 10)) == "92658374"
assert join(play([3,8,9,1,2,5,4,6,7], 100)) == "67384529"
assert join(play([1,5,6,7,9,4,8,2,3], 100)) == "82573496"

big = [3,8,9,1,2,5,4,6,7] + list(range(10, 1_000_001))
play(big, 100)
#play(big, 10_000_000)

#def solve(fn):

#assert solve('input.txt')  ==

#print(solve('input_big.txt'))
