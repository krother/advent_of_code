
import re

def memory(start, n):
    mem = dict(zip(start, range(1, len(start)+1)))
    mem2 = {}
    last = start[-1]
    turn = len(start) + 1
    while turn <= n:
        prev = mem2.get(last, None)
        if prev is None:
            new = 0
        else:
            new = turn - 1 - prev
        if new in mem:
            mem2[new] = mem[new]
        mem[new] = turn
        last = new
        turn += 1
    return last
            

assert memory([0,3,6], 4) == 0 
assert memory([0,3,6], 5) == 3 
assert memory([0,3,6], 6) == 3 
assert memory([0,3,6], 7) == 1
assert memory([0,3,6], 2020) == 436
assert memory([3,1,2], 2020) == 1836
assert memory([3,1,2], 30000000) == 362

print(memory([1,17,0,10,18,11,6], 2020))
print(memory([1,17,0,10,18,11,6], 30000000))

#print(solve('input_big.txt'))
