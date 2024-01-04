import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Tile:
    def __init__(self):
        self.name = None
        self.left = None
        self.right = None


class Map:
    def __init__(self):
        self.data: dict[str, Tile] = {}

    def add_tile(self, data: str):
        name, paths = data.split(' = ')
        left, right = paths[1:-1].split(",")
        left = left.strip()
        right = right.strip()

        logging.info(f"{name} {left} {right}")
        name_tile = self.data.get(name)
        if not name_tile : 
            logging.info(f"Creating new tile for {name}")
            name_tile = Tile()
            self.data[name] = name_tile

        name_tile.name = name
        name_tile.left = left
        name_tile.right = right

    def traverse(self, start: str, end: str, instructions: str) -> int:
        current = start
        steps = 0
        ind = 0
        l = len(instructions)

        while current != end:
            current_tile = self.data.get(current)
            if instructions[ind] == "L":
                logging.info(f"Going left from {current}, step : {steps}")
                current = current_tile.left
            else:
                logging.info(f"Going right from {current}, step : {steps}")
                current = current_tile.right
            steps += 1
            ind += 1
            if ind == l:
                ind = 0

        return steps


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '081.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        datas = list(datas)
        instructions = datas[0]

        map_ = Map()
        datas = datas[2:]
        for data in datas:
            map_.add_tile(data)
        
        logging.info("\n\n Starting Traversal")
        count = map_.traverse("AAA", "ZZZ", instructions)
        print(count)


if __name__ == "__main__":
    main()
