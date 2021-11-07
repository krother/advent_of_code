
import re

data = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".strip().split('\n')

data = """Player 1:
44
24
36
6
27
46
33
45
47
41
15
23
40
38
43
42
25
5
30
35
34
13
29
1
50

Player 2:
32
28
4
12
9
21
48
18
31
39
20
16
3
37
49
7
17
22
8
26
2
14
11
19
10""".strip().split('\n')


def parse(data):
    d1, d2 = [], []
    p2 = False
    for line in data:
        line = line.strip()
        if line.startswith('Player 2:'):
            p2 = True
        elif line.startswith('Player 1:'):
            continue
        elif p2:
            d2.append(int(line))
        elif line.strip():
            d1.append(int(line))
    return d1, d2

d1, d2 = parse(data)

def play(d1, d2):
    memory = []
    memory.append(tuple(d1 + [0] + d2 ))
    while d1 and d2:
        #print(d1)
        #print(d2)
        #print()
        c1, c2 = d1.pop(0), d2.pop(0)
        # check stack size
        if len(d1) >= c1 and len(d2) >= c2:
            print('subgame', len(d1), len(d2))
            p1, p2 = play(d1[:c1], d2[:c2])
            if p1:
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)
                            
        elif c1 > c2: #p1 wins
            d1.append(c1)
            d1.append(c2)
        else: #p2 wins
            d2.append(c2)
            d2.append(c1)
            
        # avoid recurring configurations
        h = tuple(d1 + [0] + d2)
        if h in memory:
            return d1 + d2, [] # p1 wins subgame
        else:
            memory.append(h)
    return d1, d2


d1, d2 = play(d1, d2)
result = d1
if d2:
    result = d2
    
total = 0
for i, card in enumerate(reversed(result), start=1):
    total += i * card
print(total)
    
"""
bottom card in their deck is worth the value of the 
card multiplied by 1, 
the second-from-the-bottom card is worth the 
value of the card multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10. In this example, the winning player's score is:
"""


#def solve(fn):




#assert solve('input.txt')  ==

#print(solve('input_big.txt'))
