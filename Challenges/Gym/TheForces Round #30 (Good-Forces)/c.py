def process(n: int, ans: list[str]):
    hnum = n
    hind = n
    lsum = n
    for i in range(n, 0, -1):
        csum = i - 1 + hnum // i
        if csum < lsum:
            lsum = csum
            hind = i
    if hind == n:
        return
    for i in range(n - 1, hind - 1, -1):
        ans[i] = ans[i - 1]
    ans[hind - 1] = str(hnum)
    process(hind - 1, ans)


def main():
    tc = int(input())
    for i in range(tc):
        n = int(input())
        ans = [str(i + 1) for i in range(n)]
        process(n, ans)
        print(" ".join(ans))


if __name__ == "__main__":
    main()
