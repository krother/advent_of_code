
import re


def solve(target, buses):
    buses = [int(x) for x in buses.split(',') if x != 'x']
    wait = []
    for b in buses:
        arr = target % b
        wait.append((b - arr, b))
    print(wait)
    x,y = min(wait)
    return x*y


assert solve(939, "7,13,x,x,59,x,31,19")  == 295

big = "37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,587,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,29,x,733,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"
print(solve(1005526, big))

