
data = '''
0: 1 2 3
1: "a"
2: "b"
3: 1 1 4 2
4: 1 | 2

abaabb
baaabb
ababab
abaaab
abaabb
abaabc'''.strip()

data2 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''

def parse(data):
    r, msg = data.strip().split('\n\n')
    msg = msg.split('\n')
    
    rules = {}
    for line in r.split('\n'):
        k, v = line.split(': ')
        v = v.split('|')
        if not v[0][0] == '"':
            v = [x.split() for x in v]
        rules[k] = v
    
    return rules, msg


def is_char(rule):
    if len(rule) == 1 and rule[0][0] == '"':
        return True

  
def solve(rules, message):
    """check whether message matches r"""
    queue = [(0, ['0'])]
    while queue:
        position, (rule, *following) = queue.pop()
        rule = rules[rule]

        # skip too short messages
        if position >= len(message):
            continue
        
        if is_char(rule):
            if message[position] == rule[0][1]:
                if not following and position == len(message) - 1:
                    # match last char with terminal -> success
                    return 1
                if following:
                    queue.append((position + 1, following))

        else:
            # check OR blocks
            for subrule in rule:
                queue.append((position, subrule + following))
                
    return 0

def count(rules, message):
    return sum([solve(rules, message) for message in msg])



rules, msg = parse(data)
assert count(rules, message) == 3

rules, msg = parse(data2)
assert count(rules, message) == 2

rules, msg = parse(open('input_big.txt').read()) # --> 132
print(count(rules, message))
