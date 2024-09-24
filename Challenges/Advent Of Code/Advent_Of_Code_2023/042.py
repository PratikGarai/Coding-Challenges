import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Card:
    def __init__(self) -> None:
        self.win_nums = None
        self.card_nums = None
        self.score = 0
        self.card_number = None
        self.matches = 0

    def ingest_card(self, data: str) -> None:
        card_name, card_data = data.split(":")

        _, card_number = card_name.strip().split()
        self.card_number = int(card_number)

        win_nums, card_nums = card_data.split("|")
        self.win_nums = set(map(int, win_nums.strip().split()))
        self.card_nums = list(map(int, card_nums.strip().split()))

    def success(self) -> None:
        if self.score == 0:
            self.score += 1
        else:
            self.score *= 2
        self.matches += 1

    def play(self) -> int:
        for card_num in self.card_nums:
            if card_num in self.win_nums:
                self.success()

class Game : 
    def __init__(self) -> None:
        self.cards : list[Card] = []
        self.card_counts : dict[int, int] = {}

    def ingest_games(self, datas : list[str]) : 
        for data in datas : 
            c = Card()
            c.ingest_card(data)
            self.cards.append(c)
            self.card_counts[c.card_number] = 1
    
    def play(self) -> int:
        l = len(self.cards)
        for card in self.cards:
            card.play()
            matches = card.matches
            logging.info(f"{matches} matches found in Card : {card.card_number}. Score : {card.score}")
            for i in range(card.card_number, min(card.card_number+matches, l)) :
                logging.info(f"Increasing count of {self.cards[i].card_number} by {self.card_counts[card.card_number]}")
                self.card_counts[self.cards[i].card_number] += self.card_counts[card.card_number]

        res = 0
        for _,v in self.card_counts.items() : 
            res += v
        return res
        
def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '041.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        g = Game()
        g.ingest_games(list(datas)[:])
        res = g.play()
        print(res)

if __name__ == "__main__":
    main()
