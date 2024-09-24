import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


class Matrix:
    def __init__(self) -> None:
        self.raw_data = None
        self.matrix = None
        self.rows = 0
        self.cols = 0

    def parse(self, datas: list[str]) -> None:
        self.raw_data = datas
        self.matrix = []
        for data in datas:
            self.matrix.append([i for i in data])
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def is_special(self, char: str) -> bool:
        if char.isdigit():
            return False
        if char == ".":
            return False
        return True

    def check_proximity(self, row: int, col_start: int, col_end: int) -> bool:

        c_1 = max(col_start-1, 0)
        c_2 = min(self.cols-1, col_end+1)
        r_1 = max(row-1, 0)
        r_2 = min(self.rows-1, row+1)

        for r in range(r_1, r_2+1):
            for c in range(c_1, c_2+1):
                if self.is_special(self.matrix[r][c]):
                    return True
        return False

    def iter_and_sum(self):
        s = 0

        for r in range(self.rows):
            num = ""
            start_col = -1
            end_col = -1
            for c in range(self.cols):
                char = str(self.matrix[r][c])
                if char.isdigit():
                    if num == "":
                        start_col = c
                        end_col = c
                    else:
                        end_col = c
                    num += char
                else:
                    if num != "":
                        if self.check_proximity(r, start_col, end_col):
                            logging.info(f"Successfully proximity test at [{r}][{c}] => {num}")
                            s += int(num)
                        else : 
                            logging.info(f"Failing proximity test at [{r}][{c}] => {num}")
                        num = ""
                        start_col = -1
                        end_col = -1
            if num != "":
                if self.check_proximity(r, start_col, end_col):
                    s += int(num)

        return s


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '031.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()
        mat = Matrix()
        mat.parse(list(datas))

        res = mat.iter_and_sum()
        print(res)


if __name__ == "__main__":
    main()
