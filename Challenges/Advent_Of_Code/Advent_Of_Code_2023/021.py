import json
import logging
import os

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)


class Game:
    def __init__(self, line: str, game_split=":", turn_split=";", color_split=",", data_split=" "):
        self.line = line
        self.id = None
        self.counts = {}
        self.game_split = game_split
        self.turn_split = turn_split
        self.color_split = color_split
        self.data_split = data_split

    def update_data(self, color: str, count: int):
        logging.info(f"Updating {color} with {count}")
        color = color.strip()
        mx = self.counts.get(color.strip(), 0)
        self.counts[color] = max(mx, count)

    def parse(self):
        # Divide gameid and game data
        logging.info(f"Parsing game : {self.line}")
        game, game_data = self.line.split(self.game_split)
        game = game.strip()
        game_data = game_data.strip()

        # Extract game id
        _, self.id = game.split()
        self.id = int(self.id)
        logging.info(f"Game id extracted : {self.id}")

        # Divide into turn
        turns = game_data.split(self.turn_split)
        logging.info(f"Parsing game data {turns}")
        for turn in turns:
            turn = turn.strip()
            logging.info(f"Parsing turn {turn}")
            color_datas = turn.split(self.color_split)
            for color_data in color_datas:
                color_data = color_data.strip()
                logging.info(f"Parsing color data {color_data}")
                count, color = color_data.split(self.data_split)
                self.update_data(color, int(count))
        logging.info(
            f"Final status of game : {json.dumps(self.counts, indent=4)}")

    def comparison(self, d: dict) -> bool:
        for k in d.keys():
            if k in self.counts and self.counts[k] > d[k]:
                return False
            else:
                continue
        return True


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '021.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()

        games: list[Game] = []
        s = 0
        d = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        for data in datas[:]:
            g = Game(data)
            g.parse()
            games.append(g)

        for game in games:
            if not game.comparison(d):
                print(
                    f"Found impossible matching game {game.id} : {json.dumps(game.counts, indent=4)}")
            else:
                s += game.id

        print(f"Result : {s}")


if __name__ == "__main__":
    main()
