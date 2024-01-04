import logging
import os
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Sequence:
    def __init__(self):
        self.sequence = []
        self.matrix: list[list[int]] = []
        self.matrix_l = 0
        self.row_l = 0
        self.solved = False

    def parse(self, data: str):
        self.sequence = list(map(int, data.split()))
        self.matrix.append(self.sequence.copy())
        self.matrix_l += 1
        self.row_l = len(self.sequence)

    def parse_next_level(self):
        if self.solved:
            return

        prev = self.matrix[self.matrix_l-1]
        res = []
        for i in range(self.row_l-self.matrix_l):
            res.append(prev[i+1]-prev[i])

        if Sequence.check_zeroes(res):
            self.solved = True

        self.matrix.append(res)
        self.matrix_l += 1

    def bottom_up(self):
        self.matrix[self.matrix_l-1].append(0)
        for i in range(self.matrix_l-2, -1, -1):
            self.matrix[i].append(self.matrix[i][-1] + self.matrix[i+1][-1])

    @staticmethod
    def check_zeroes(data: list[int]) -> list[int]:
        for i in data:
            if i != 0:
                return False
        return True


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '091.txt')
    with open(fname, "r") as f:
        datas = list(f.read().splitlines())
        res = 0
        for data in tqdm(datas):
            seq = Sequence()
            seq.parse(data)

            while not seq.solved:
                seq.parse_next_level()
            # print(seq.matrix)

            seq.bottom_up()
            # print(seq.matrix)

            res += seq.matrix[0][-1]

        print(res)


if __name__ == "__main__":
    main()
