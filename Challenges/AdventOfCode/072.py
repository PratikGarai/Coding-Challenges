import logging
import os
from functools import cmp_to_key

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)

symbol_strength = {
    'J': -1,
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'Q': 10,
    'K': 11,
    'A': 12
}


class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.strength = 0

    def set_strength(self):
        counts = {}
        count_j = 0
        for i in self.hand:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
            if i == 'J':
                count_j += 1

        counts = list(sorted(counts.values(), reverse=True))
        if counts == [5]:
            self.strength = 7
        elif counts == [4, 1]:
            self.strength = 6
            if count_j > 0:
                self.strength = 7
        elif counts == [3, 2]:
            self.strength = 5
            if count_j > 0:
                self.strength = 7
        elif counts == [3, 1, 1]:
            self.strength = 4
            if count_j > 0:
                self.strength = 6
        elif counts == [2, 2, 1]:
            self.strength = 3
            if count_j == 2:
                self.strength = 6
            elif count_j == 1:
                self.strength = 5
        elif counts == [2, 1, 1, 1]:
            self.strength = 2
            if count_j > 0:
                self.strength = 4
        elif counts == [1, 1, 1, 1, 1]:
            self.strength = 1
            if count_j > 0:
                self.strength = 2
        else:
            self.strength = 0


def compare(hand1: Hand, hand2: Hand):
    logging.info(f"hand1: {hand1.hand}, hand2: {hand2.hand}")

    if hand1.strength != hand2.strength:
        logging.info(
            f"hand1.strength: {hand1.strength}, hand2.strength: {hand2.strength}")
        return hand1.strength - hand2.strength

    for i in range(5):
        if symbol_strength[hand1.hand[i]] != symbol_strength[hand2.hand[i]]:
            return symbol_strength[hand1.hand[i]] - symbol_strength[hand2.hand[i]]

    return 0


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '071.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()

        hands = []
        for data in datas:
            hand, bid = data.split()
            bid = int(bid)
            h = Hand(hand, bid)
            h.set_strength()
            hands.append(h)

        hands = sorted(hands, key=cmp_to_key(compare))
        s = 0
        for idx, hand in enumerate(hands):
            print(hand.hand, hand.bid, hand.strength, idx+1)
            s += hand.bid * (idx+1)

        print(s)


if __name__ == "__main__":
    main()
