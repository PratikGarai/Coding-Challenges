import logging
import os
from typing import Tuple

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)

fname = os.path.join(os.path.dirname(__file__), 'inputs', '012.txt')

numbers = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]


def check_presence(st: str, index: int, target: str) -> bool:
    if len(target) + index > len(st):
        return False

    for i in range(len(target)):
        if st[index + i] != target[i]:
            return False
    logging.info(
        "String matching completed at position {index} found {target}")
    return True


def check_number(st: str, index: int) -> Tuple[int, int]:
    char = str(st[index])
    if char.isdigit():
        logging.info(f"Char at position {index} is digit : {int(char)}")
        return (int(char), 1)
    else:
        for i, number in enumerate(numbers):
            res = check_presence(st, index, number)
            if res:
                logging.info(
                    f"String at position {index} of length {len(number)} is digit : {i}")
                # return i, len(number)
                return i, 1
    return -1, 1


def get_number(st: str) -> int:
    first = -1
    last = -1
    l = len(st)
    ind = 0

    while ind < l:
        number, jump = check_number(st, ind)
        logging.info(
            f"Index : {ind} \nFound : {number}\n Jumping positions : {jump}")

        if number >= 0:
            if first == -1:
                logging.info("Updating first and last")
                first = number
                last = number
            else:
                logging.info("Updating last")
                last = number
        ind += jump

    logging.info(f"First : {first}, Last : {last}")
    res = first*10 + last
    return res


with open(fname, 'r') as f:
    data = f.read().splitlines()
    s = 0
    for line in data[:]:
        res = get_number(line)
        s += res
        print(f"{line} : {res}")
    print(f"Total : {s}")
