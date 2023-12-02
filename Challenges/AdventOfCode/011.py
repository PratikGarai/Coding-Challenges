import os

fname = os.path.join(os.path.dirname(__file__), 'inputs', '011.txt')


def get_number(st : str) -> int :
    first = -1
    last = -1

    for char in st :
        char = str(char)
        if char.isdigit():
            if first == -1 : 
                first = int(char)
                last = int(char)
            else :
                last = int(char)

    res = first*10 + last
    return res


with open(fname, 'r') as f:
    data = f.read().splitlines()
    s = 0
    for line in data: 
        s += get_number(line)
    print(s)