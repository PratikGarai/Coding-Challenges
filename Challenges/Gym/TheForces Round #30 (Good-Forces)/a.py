def process(target: int):
    mi, ma = target // 4, target // 6
    if target % 4 != 0:
        mi += 1
    if target % 6 != 0:
        ma += 1
    print(ma, mi)


def main():
    tc = int(input())
    for i in range(tc):
        target = int(input())
        process(target)


if __name__ == "__main__":
    main()
