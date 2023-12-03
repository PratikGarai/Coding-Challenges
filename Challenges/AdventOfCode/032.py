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
        self.buffer = {}

    def parse(self, datas: list[str]) -> None:
        self.raw_data = datas
        self.matrix = []
        for data in datas:
            self.matrix.append([i for i in data])
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def is_special(self, char: str) -> bool:
        if char == "*":
            return True
        return False

    def check_proximity(self, row: int, col_start: int, col_end: int) -> tuple[bool, tuple[int, int]]:

        c_1 = max(col_start-1, 0)
        c_2 = min(self.cols-1, col_end+1)
        r_1 = max(row-1, 0)
        r_2 = min(self.rows-1, row+1)

        for r in range(r_1, r_2+1):
            for c in range(c_1, c_2+1):
                if self.is_special(self.matrix[r][c]):
                    return True, (r, c)
        return False, (-1, -1)

    def iter_and_sum(self):
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
                        res, (r_x, c_x) = self.check_proximity(
                            r, start_col, end_col)
                        if res:
                            logging.info(
                                f"Successfully proximity test at [{r}][{c}] => {num}")
                            data: list = self.buffer.get((r_x, c_x), [])
                            data.append(int(num))
                            self.buffer[(r_x, c_x)] = data
                        else:
                            logging.info(
                                f"Failing proximity test at [{r}][{c}] => {num}")
                        num = ""
                        start_col = -1
                        end_col = -1
            if num != "":
                res, (r_x, c_x) = self.check_proximity(r, start_col, end_col)
                if res:
                    logging.info(
                        f"Successfully proximity test at [{r}][{c}] => {num}")
                    data: list = self.buffer.get((r_x, c_x), [])
                    data.append(int(num))
                    self.buffer[(r_x, c_x)] = data

        s = 0
        for k, v in self.buffer.items():
            if len(v) == 2:
                logging.info(f"Gear found at [{k[0]}][{k[1]}] : {v}")
                s += v[0] * v[1]
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
