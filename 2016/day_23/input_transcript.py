a, b, c, d = 12, 0, 0, 0

b = a - 1

# -16 jumps here
for i in range(11):
    #print('start', a, b, c, d)
    d = a

    assert d > 0 and b > 0
    a = (b * d)
    c, d = 0, 0

    b -= 1
    c = b
    d = c

    c += d
    d = 0
    
    # tgl c --> inc c
    print('end  ', a, b, c, d) # 20
    c = -16

c = 1
c = 97
d = 79

a += (97 * 79)
print(a)

# cpy -16 c 
# jnz 1 c   --> cpy 1 c
# cpy 97 c
# jnz 79 d  --> cpy 79 d
# inc a
# inc d     --> dec d
# jnz d -2
# inc c     --> dec c
# jnz c -5
