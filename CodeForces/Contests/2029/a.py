def solve() :
    l, r, k = map(int, input().split())
    print(max(0, r//k - l + 1))


def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()