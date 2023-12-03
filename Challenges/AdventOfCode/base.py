import logging
import os

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)


def main():
    fname = os.path.join(os.path.dirname(__file__), 'inputs', '*.txt')
    with open(fname, "r") as f:
        datas = f.read().splitlines()


if __name__ == "__main__":
    main()
