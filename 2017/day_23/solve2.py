
def is_prime(b):
    d = 2
    while d < b:
        if b % d == 0:
            return False
        d += 1
    return True


b = 105700
c = b + 17000

h = 0
while b <= c:
    if not is_prime(b):
        h += 1
    b += 17

print(h)
