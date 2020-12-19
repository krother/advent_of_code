
import re

def find_par(s):
    """returns first parenthese substring"""
    sub = ""
    par = 0
    start = False
    for c in s:
        if c != '(' and not start:
            continue
        elif c == '(':
            par += 1
            start = True
        elif c == ')':
            par -= 1
        if start:
            sub += c
        if par == 0 and start:
            return sub[1:-1]
        
assert find_par("1 + (1+1) + 1)") == "1+1"

            
def solve(s):
    if "(" in s:
        sub = find_par(s)
        num = str(solve(sub))
        s = s.replace("("+sub+")", num)
        return solve(s)
    else:
        # numbers and operators only
        total = 1
        for add in s.split("*"):
            # no-par additions
            total *= eval(add)
        return total   


assert solve("(1+2) * (3 + 4)") == 21
assert solve("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert solve("2 * 3 + (4 * 5)") == 46
assert solve("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
assert solve("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340

result = 0
for line in open('input_big.txt'):
    result += solve(line.strip())

print(result)  # 351175492232654