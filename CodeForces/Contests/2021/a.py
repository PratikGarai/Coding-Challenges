def solve() :
    n = int(input())
    a = list(map(int, input().split()))
    while n > 1 :
        a = sorted(a)
        x = (a[0]+a[1]) // 2
        a = a[2:] + [x]
        n -= 1
    print(a[0])
    return
        


def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()