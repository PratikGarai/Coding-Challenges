import logging
import os
from collections import namedtuple
from enum import Enum

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


PipeSchema = namedtuple("PipeSchema", ["symbol", "allowed_directions"])


class Pipes(Enum):
    VERTICAL_PIPE = PipeSchema(symbol="|", allowed_directions=(
        Direction.NORTH, Direction.SOUTH))
    HORIZONTAL_PIPE = PipeSchema(
        symbol="-", allowed_directions=(Direction.EAST, Direction.WEST))
    BEND_NE = PipeSchema(symbol="L", allowed_directions=(
        Direction.NORTH, Direction.SOUTH))
    BEND_NW = PipeSchema(symbol="J", allowed_directions=(
        Direction.NORTH, Direction.WEST))
    BEND_SE = PipeSchema(symbol="F", allowed_directions=(
        Direction.SOUTH, Direction.EAST))
    BEND_SW = PipeSchema(symbol="7", allowed_directions=(
        Direction.SOUTH, Direction.SOUTH))

    @classmethod
    def get(cls, symbol: str):
        for pipe in cls:
            if pipe.symbol == symbol:
                return pipe
        raise ValueError(f"Symbol {symbol} not found in {cls}")


class Graph:
    def __init__(self):
        self.data: list[list[str]] = []
        self.rows = 0
        self.cols = 0

        self.start = ()

    def parse(self, data: list[str]):
        for d in data:
            self.data.append([i for i in d])

        self.rows = len(self.data)
        self.cols = len(self.cols)

    def bfs(self, start_row: int, start_col: int):
        visited = set()
        queue = [(start_row, start_col)]
        while queue:
            row, col = queue.pop(0)
            if (row, col) in visited:
                continue
            visited.add((row, col))

            symbol = self.data[row][col]
            if symbol != "." and symbol != "S":
                pipe = Pipes.get(symbol)

    def explore(self, row: int, col: int) -> list[tuple[tuple[int, int], Direction]]:
        row1 = max(0, row-1)
        row2 = min(self.rows, row+1)
        col1 = max(0, col-1)
        col2 = min(self.cols, col+1)

        neighbors = []
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                if r == row and c == col:
                    continue
                neighbors.append((r, c))

    @staticmethod
    def get_change(symbol: Pipes, direction: Direction):
        if symbol == None:
            return


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '*.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()


if __name__ == "__main__":
    main()
