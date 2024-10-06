def solve() :
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    presented = set({})

    ai = 0
    bi = 0
    while bi < m :
        # print(b[bi], presented)
        if b[bi] in presented :
            bi += 1
        elif ai<n and a[ai] == b[bi] :
            presented.add(a[ai])
            ai += 1
            bi += 1
        else :
            print("TIDAK")
            return 
    
    print("YA")

def main() :
    t = int(input())
    for _ in range(t) :
        solve()

if __name__=="__main__" :
    main()