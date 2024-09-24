import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Card:
    def __init__(self) -> None:
        self.win_nums = None
        self.card_nums = None
        self.score = 0

    def ingest_card(self, data: str) -> None:
        _, card_data = data.split(":")
        win_nums, card_nums = card_data.split("|")
        self.win_nums = set(map(int, win_nums.strip().split()))
        self.card_nums = list(map(int, card_nums.strip().split()))

    def success(self) -> None:
        if self.score == 0:
            self.score += 1
        else:
            self.score *= 2

    def play(self) -> int:
        for card_num in self.card_nums:
            if card_num in self.win_nums:
                self.success()


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '041.txt')
    with open(fname, "r") as f:
        s = 0
        datas = f.read().splitlines()
        for data in datas:
            g = Card()
            g.ingest_card(data)
            g.play()
            s += g.score
        print(s)


if __name__ == "__main__":
    main()
