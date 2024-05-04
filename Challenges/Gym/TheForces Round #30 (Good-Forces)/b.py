def make_all_ones(c0: int, c1: int, a: int, b: int) -> int:
    c = c0 * a
    c = min(c, c0 * b)
    return c


def make_all_zeros(c0: int, c1: int, a: int, b: int):
    c = c1 * a
    if c1 % 2 == 0:
        c = min(c, (c1 // 2) * b)
    else:
        cst = (c1 // 2) * b + min(a, 2 * b)
        c = min(c, cst)
    return c


def process(st: str, n: int, a: int, b: int) -> int:
    c0 = 0
    c1 = 0
    for i in st:
        if i == "0":
            c0 += 1
        elif i == "1":
            c1 += 1
    if c0 == 0 or c1 == 0:
        return 0
    return min(make_all_zeros(c0, c1, a, b), make_all_ones(c0, c1, a, b))


def main():
    tc = int(input())
    for i in range(tc):
        l, a, b = map(int, input().split())
        st = input()
        print(process(st, l, a, b))


if __name__ == "__main__":
    main()
