"""Day 21: Scrambled Letters and Hash

https://adventofcode.com/2016/day/21
"""
import re


COMMANDS = [
    'swap position',
    'swap letter',
    'reverse',
    'rotate left',
    'rotate right',
    'rotate based',
    'move'
]

# DIRTY HACK FOR 8 CHARS ONLY
UNROTATE_STEPS = {
    1: 1,
    3: 2,
    5: 3,
    7: 4,
    2: 6,
    4: 7,
    6: 8,
    0: 9,
}


class CommandParser:

    def __init__(self, psw):
        self.psw = list(psw)

    def swap_position(self, cmd):
        p1, p2 = sorted(map(int, 
                        re.findall(r'(\d+).+(\d+)', cmd)[0]))        
        self.psw[p1], self.psw[p2] = self.psw[p2], self.psw[p1]

    def swap_letter(self, cmd):
        char1, char2 = re.findall(r'letter (\w)', cmd)
        i1 = self.psw.index(char1)
        i2 = self.psw.index(char2)
        self.psw[i1] = char2
        self.psw[i2] = char1

    def reverse(self, cmd):
        i1, i2 = map(int, re.findall(r'(\d+)', cmd))
        part = self.psw[i1:i2+1][::-1]
        for i, char in zip(range(i1, i2 + 1), part):
            self.psw[i] = char

    def rotate_left(self, cmd):
        steps = int(re.findall(r'(\d+)', cmd)[0])
        for i in range(steps):
            char = self.psw.pop(0)
            self.psw.append(char)

    def rotate_right(self, cmd):
        steps = int(re.findall(r'(\d+)', cmd)[0])
        for i in range(steps):
            char = self.psw.pop()
            self.psw.insert(0, char)

    def rotate_based(self, cmd):
        char = re.findall(r'letter (\w)', cmd)[0]
        i = self.psw.index(char)
        if i >= 4:
            i += 1
        self.rotate_right(f'{i+1} steps')

    def unrotate_based(self, cmd):
        # ONLY WORKS FOR LENGTH 8. UNDECIDEABLE FOR 5 IN SOME CASES
        assert len(self.psw) == 8

        char = re.findall(r'letter (\w)', cmd)[0]
        i = self.psw.index(char)
        steps = UNROTATE_STEPS[i]
        self.rotate_left(f'{steps} steps')

    def move(self, cmd):
        i1, i2 = map(int, re.findall(r'(\d+)', cmd))
        char = self.psw.pop(i1)
        self.psw.insert(i2, char)

    def execute(self, cmd):
        for prefix in COMMANDS:
            if cmd.startswith(prefix):
                prefix = prefix.replace(' ', '_') 
                f = getattr(self, prefix)
                f(cmd)

    def unexecute(self, cmd):
        if cmd.startswith('rotate based'):
            self.unrotate_based(cmd)
        else:
            cmd = cmd.replace('left', 'xxx')
            cmd = cmd.replace('right', 'left')
            cmd = cmd.replace('xxx', 'right')
            if cmd.startswith('move'):
                i1, i2 = map(int, re.findall(r'(\d+)', cmd))
                cmd = f'move position {i2} to position {i1}'

            self.execute(cmd)



def solve(psw, cmds):
    cp = CommandParser(psw)
    for line in cmds.strip().split('\n'):
        cp.execute(line)

    return ''.join(cp.psw)

def unscramble(psw, cmds):
    cp = CommandParser(psw)
    for line in reversed(cmds.strip().split('\n')):
        cp.unexecute(line)

    return ''.join(cp.psw)




if __name__ == '__main__':
    psw = 'abcdefgh'
    cmds = open('input_data.txt').read()
    result = solve(psw, cmds)
    print(f'Example 1: {result}')

    psw = 'fbgdceah'
    result = unscramble(psw, cmds)
    print(f'Example 2: {result}')
