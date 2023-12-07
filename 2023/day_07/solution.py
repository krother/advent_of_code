"""
Camel Cards

https://adventofcode.com/2023/day/7
"""

from collections import Counter
from pprint import pprint

CARD_RANKS = list("AKQJT98765432")
JOKER_RANKS = list("AKQT98765432J")


class Hand:

    def __init__(self, cards:str, bid: int, jokers: bool):
        self.cards = cards
        self.bid = bid
        if jokers:
            self.njokers = self.cards.count("J")
        self._card_ranks = JOKER_RANKS if jokers else CARD_RANKS

        c = self.cards.replace("J", "") if jokers else self.cards 
        self._counts = set(Counter(c).values())

        if self.five:
            self.quality = 7
        elif self.four:
            self.quality = 6
        elif self.fullhouse:
            self.quality = 5
        elif self.three:
            self.quality = 4
        elif self.twopair:
            self.quality = 3
        elif self.pair:
            self.quality = 2
        else:
            self.quality = 1

    def __repr__(self):
        return f"[{self.cards}  {self.bid}  {self.quality}]"
    
    @property
    def five(self):
        if self.jokers:
            return self.njokers==5 or max(self._counts) + self.njokers == 5
        return self._counts == {5}
        
    @property
    def four(self):
        if self.jokers:
            return max(self._counts) + self.njokers == 4
        return self._counts == {1, 4}

    @property
    def fullhouse(self):
        if self.jokers and self.njokers:
            return max(self._counts) + self.njokers == 3 and min(self._counts) == 2
        return self._counts == {2, 3}
    
    @property
    def three(self):
        if self.jokers:
            return max(self._counts) + self.njokers == 3
        return self._counts == {1, 3}

    @property
    def twopair(self):
        if self.jokers and self.njokers>0:
            return False
        return len(set(self.cards)) == 3

    @property
    def pair(self):
        if self.jokers and self.njokers:
            return self._counts == {1}
        return len(set(self.cards)) == 4
    
    @property
    def high(self):
        if self.jokers:
            return self.njokers == 0
        return len(set(self.cards)) == 5

    def __lt__(self, other):
        if self.quality != other.quality:
            return self.quality < other.quality
        for a, b in zip(self.cards, other.cards):
            if a != b:
                return self._card_ranks.index(a) > self._card_ranks.index(b)


def parse(data, jokers=False):
    hands = []
    for line in data.strip().split("\n"):
        cards, bid = line.split()
        hands.append(Hand(cards=cards, bid=int(bid), jokers=jokers))
    return hands


def solve(data, jokers=False):
    hands = parse(data, jokers)
    hands.sort()
    result = 0
    for rank, hand in enumerate(hands, 1):
        result += rank * hand.bid
    return result


def solve2(data):
    return solve(data, jokers=True)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example 1: {result}')  # 248569531

    result = solve2(input_data)
    print(f'Example 2: {result}')  # 250382098
