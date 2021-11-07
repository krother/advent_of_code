
from collections import Counter


def get_most_frequent_char(column, index):
    return Counter(column).most_common()[index][0]


def get_consensus(signal, index=0):
    return ''.join([
        get_most_frequent_char(col, index) 
        for col in zip(*signal.split('\n'))
        ])


if __name__ == '__main__':
    print(get_consensus(open('input.txt').read()))
    print(get_consensus(open('input.txt').read(), -1))