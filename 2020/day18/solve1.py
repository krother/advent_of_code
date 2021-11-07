
import re

def calc(tokens):
    par = []
    parlevel = 0
    result = 0
    op = "+"
    for t in tokens:
        if t == "(":
            parlevel += 1
        elif t == ")":
            parlevel -= 1
            if parlevel == 0:
                t = str(calc(par[1:]))
                par = []
        if parlevel:
            par.append(t)
        else:
           if t in "+*":
               op = t
           else:
               result = eval(str(result) + op + t)
    return result

def solve(s):
    tokens = re.findall("\d+|[()+*]", s)
    return calc(tokens)


assert solve("(1+2) * (3 + 4)") == 21
assert solve("2 * 3 + (4 * 5)") == 26
assert solve("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert solve("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632

result = 0
for line in open('input_big.txt'):
    result += solve(line.strip())

print(result) # 16332191652452