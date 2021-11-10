    
from collections import Counter
import pandas as pd

def parse(code):
    prefix, suffix = code.strip()[:-1].split("[")
    *seq, num = prefix.split('-')
    num = int(num)
    return seq, num, suffix


def check(code):
    seq, num, suffix = parse(code)
    counts = Counter(''.join(seq))
    top = counts.most_common(len(counts))
    top = pd.DataFrame(top, columns=["initial", "count"])
    top.sort_values(by=['count', 'initial'], ascending=[False, True], inplace=True)

    initials = ''.join(top['initial'].values[:len(suffix)])
    if initials == suffix:
        return num
    return 0

def decrypt(code):
    result = ''
    seq, num, _ = parse(code)
    for char in ' '.join(seq):
        if char == ' ':
            result += char
        else:
            i = ord(char) + num
            while i > ord('z'):
                i -= 26
            result += chr(i)
    return result


if __name__ == '__main__':
    for line in open('input.txt'):
        print(decrypt(line.strip()), line)

    print(sum(map(check, open('input.txt'))))
